


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Wred1Enum' : _MetaInfoEnum('Wred1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'wred-cos-cmd':'wred_cos_cmd',
            'wred-dscp-cmd':'wred_dscp_cmd',
            'wred-precedence-cmd':'wred_precedence_cmd',
            'wred-discard-class-cmd':'wred_discard_class_cmd',
            'wred-mpls-exp-cmd':'wred_mpls_exp_cmd',
            'red-with-user-min-max':'red_with_user_min_max',
            'red-with-default-min-max':'red_with_default_min_max',
            'wred-dei-cmd':'wred_dei_cmd',
            'wred-ecn-cmd':'wred_ecn_cmd',
            'wred-invalid-cmd':'wred_invalid_cmd',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'QueueEnum' : _MetaInfoEnum('QueueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'port-default':'port_default',
            'class-default':'class_default',
            'priority1-queue':'priority1_queue',
            'priority2-queue':'priority2_queue',
            'priority3-queue':'priority3_queue',
            'priority4-queue':'priority4_queue',
            'priority5-queue':'priority5_queue',
            'priority6-queue':'priority6_queue',
            'priority7-queue':'priority7_queue',
            'first-p1-class-name':'first_p1_class_name',
            'first-p2-class-name':'first_p2_class_name',
            'first-p3-class-name':'first_p3_class_name',
            'first-p4-class-name':'first_p4_class_name',
            'first-p5-class-name':'first_p5_class_name',
            'first-p6-class-name':'first_p6_class_name',
            'first-p7-class-name':'first_p7_class_name',
            'port-priority1':'port_priority1',
            'port-priority2':'port_priority2',
            'port-priority3':'port_priority3',
            'port-priority4':'port_priority4',
            'port-priority5':'port_priority5',
            'port-priority6':'port_priority6',
            'port-priority7':'port_priority7',
            'new':'new',
            'parent-class':'parent_class',
            'priority1':'priority1',
            'priority2':'priority2',
            'priority3':'priority3',
            'priority4':'priority4',
            'priority5':'priority5',
            'priority6':'priority6',
            'priority7':'priority7',
            'priority-ignored-normal':'priority_ignored_normal',
            'normal-priority':'normal_priority',
            'class-unknown':'class_unknown',
            'unknown-priority':'unknown_priority',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'QosUnitEnum' : _MetaInfoEnum('QosUnitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'invalid':'invalid',
            'bytes':'bytes',
            'kilobytes':'kilobytes',
            'megabytes':'megabytes',
            'gigabytes':'gigabytes',
            'bps':'bps',
            'kbps':'kbps',
            'mbps':'mbps',
            'gbps':'gbps',
            'cells-per-second':'cells_per_second',
            'packets-per-second':'packets_per_second',
            'microsecond':'microsecond',
            'millisecond':'millisecond',
            'packets':'packets',
            'cells':'cells',
            'percentage':'percentage',
            'ratio':'ratio',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'ActionEnum' : _MetaInfoEnum('ActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'police-transmit':'police_transmit',
            'police-set-transmit':'police_set_transmit',
            'police-drop':'police_drop',
            'police-unknown':'police_unknown',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'PolicyParamUnitEnum' : _MetaInfoEnum('PolicyParamUnitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
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
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'PolicyStateEnum' : _MetaInfoEnum('PolicyStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'active':'active',
            'suspended':'suspended',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'ActionOpcodeEnum' : _MetaInfoEnum('ActionOpcodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'precedence':'precedence',
            'dscp':'dscp',
            'discard-class':'discard_class',
            'qos-group':'qos_group',
            'cos-inner':'cos_inner',
            'cos':'cos',
            'exp-top':'exp_top',
            'exp-imp':'exp_imp',
            'tunnel-precedence':'tunnel_precedence',
            'tunnel-dscp':'tunnel_dscp',
            'itag-dei':'itag_dei',
            'itag-cos':'itag_cos',
            'cos-imposition':'cos_imposition',
            'dei-imposition':'dei_imposition',
            'dei':'dei',
            'no-marking':'no_marking',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'TbAlgorithmEnum' : _MetaInfoEnum('TbAlgorithmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'inactive':'inactive',
            'single':'single',
            'single-rate-tcm':'single_rate_tcm',
            'two-rate-tcm':'two_rate_tcm',
            'mef-tcm':'mef_tcm',
            'dummy':'dummy',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'CacStateEnum' : _MetaInfoEnum('CacStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'unknown':'unknown',
            'admit':'admit',
            'redirect':'redirect',
            'ubrl':'ubrl',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'ShapeProfiletypeV2Enum' : _MetaInfoEnum('ShapeProfiletypeV2Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'invalid':'invalid',
            'always':'always',
            'never':'never',
            'explicit':'explicit',
            'scale':'scale',
            'grid':'grid',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'WredEnum' : _MetaInfoEnum('WredEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper',
        {
            'wred-cos':'wred_cos',
            'wred-dscp':'wred_dscp',
            'wred-precedence':'wred_precedence',
            'wred-discard-class':'wred_discard_class',
            'wred-mpls-exp':'wred_mpls_exp',
            'red-with-user-min-max':'red_with_user_min_max',
            'red-with-default-min-max':'red_with_default_min_max',
            'wred-dei':'wred_dei',
        }, 'Cisco-IOS-XR-asr9k-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper']),
    'PlatformQos.Nodes.Node.Capability' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Capability',
            False, 
            [
            _MetaInfoClassMember('max-bundle-members', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum bundle members
                ''',
                'max_bundle_members',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-classes-per-child-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum classes per child policy
                ''',
                'max_classes_per_child_policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-classes-per-grand-parent-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum classes per parent policy
                ''',
                'max_classes_per_grand_parent_policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-classes-per-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum classes per policy
                ''',
                'max_classes_per_policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-classmap-name-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum classmap name length
                ''',
                'max_classmap_name_length',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-instance-name-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum instance name length
                ''',
                'max_instance_name_length',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-marking-actions-per-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum marking action  per class
                ''',
                'max_marking_actions_per_class',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-matches-per-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum matches per class
                ''',
                'max_matches_per_class',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-police-actions-per-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum police actions per class
                ''',
                'max_police_actions_per_class',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-policy-hierarchy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum policy hierarchy
                ''',
                'max_policy_hierarchy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-policy-maps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum policy maps per system
                ''',
                'max_policy_maps',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-policy-name-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum policy name length
                ''',
                'max_policy_name_length',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'capability',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('ancp-config-bandwidth', REFERENCE_CLASS, 'AncpConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpConfigBandwidth', 
                [], [], 
                '''                Bandwidth obtain from IM
                ''',
                'ancp_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('ancp-programmed-bandwidth', REFERENCE_CLASS, 'AncpProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpProgrammedBandwidth', 
                [], [], 
                '''                ANCP bandwidth that was programmed
                ''',
                'ancp_programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-config-bandwidth', REFERENCE_CLASS, 'PortConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortConfigBandwidth', 
                [], [], 
                '''                Bandwidth due to port speed change
                ''',
                'port_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.ProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.ProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters', 
                [], [], 
                '''                Interface config and programmed parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('programmed-bandwidth', REFERENCE_CLASS, 'ProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.ProgrammedBandwidth', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED precedence match if precedence start value
                equals to end value Format: <start-value> , else
                range Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Table ID
                ''',
                'table_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v1',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v1', REFERENCE_LIST, 'QosShowEaStV1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1', 
                [], [], 
                '''                qos show ea st v1
                ''',
                'qos_show_ea_st_v1',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape',
            False, 
            [
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape',
            False, 
            [
            _MetaInfoClassMember('cir-shape', REFERENCE_CLASS, 'CirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape', 
                [], [], 
                '''                CIR shaper params
                ''',
                'cir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                CIR Shaper type
                ''',
                'cir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape', REFERENCE_CLASS, 'PirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape', 
                [], [], 
                '''                PIR shaper params
                ''',
                'pir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                PIR Shaper type
                ''',
                'pir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exp-match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED exp match if EXP start value equals to end
                value Format: <start-value> , else range Format:
                <start-value> <end-value>
                ''',
                'exp_match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED match if precedence start value equals to
                end value Format: <start-value> , else range
                Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v2', REFERENCE_LIST, 'QosShowEaStV2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2', 
                [], [], 
                '''                qos show ea st v2
                ''',
                'qos_show_ea_st_v2',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy-typhoon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header', 
                [], [], 
                '''                QoS policy header
                ''',
                'header',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy', 
                [], [], 
                '''                Trident QoS policy details
                ''',
                'policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-typhoon', REFERENCE_CLASS, 'PolicyTyphoon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon', 
                [], [], 
                '''                Typhoon QoS policy details
                ''',
                'policy_typhoon',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details', 
                [], [], 
                '''                QoS policy direction egress
                ''',
                'details',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('ancp-config-bandwidth', REFERENCE_CLASS, 'AncpConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpConfigBandwidth', 
                [], [], 
                '''                Bandwidth obtain from IM
                ''',
                'ancp_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('ancp-programmed-bandwidth', REFERENCE_CLASS, 'AncpProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpProgrammedBandwidth', 
                [], [], 
                '''                ANCP bandwidth that was programmed
                ''',
                'ancp_programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-config-bandwidth', REFERENCE_CLASS, 'PortConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortConfigBandwidth', 
                [], [], 
                '''                Bandwidth due to port speed change
                ''',
                'port_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.ProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.ProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters', 
                [], [], 
                '''                Interface config and programmed parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('programmed-bandwidth', REFERENCE_CLASS, 'ProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.ProgrammedBandwidth', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED precedence match if precedence start value
                equals to end value Format: <start-value> , else
                range Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Table ID
                ''',
                'table_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v1',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v1', REFERENCE_LIST, 'QosShowEaStV1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1', 
                [], [], 
                '''                qos show ea st v1
                ''',
                'qos_show_ea_st_v1',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape',
            False, 
            [
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape',
            False, 
            [
            _MetaInfoClassMember('cir-shape', REFERENCE_CLASS, 'CirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape', 
                [], [], 
                '''                CIR shaper params
                ''',
                'cir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                CIR Shaper type
                ''',
                'cir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape', REFERENCE_CLASS, 'PirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape', 
                [], [], 
                '''                PIR shaper params
                ''',
                'pir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                PIR Shaper type
                ''',
                'pir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exp-match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED exp match if EXP start value equals to end
                value Format: <start-value> , else range Format:
                <start-value> <end-value>
                ''',
                'exp_match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED match if precedence start value equals to
                end value Format: <start-value> , else range
                Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v2', REFERENCE_LIST, 'QosShowEaStV2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2', 
                [], [], 
                '''                qos show ea st v2
                ''',
                'qos_show_ea_st_v2',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy-typhoon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header', 
                [], [], 
                '''                QoS policy header
                ''',
                'header',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy', 
                [], [], 
                '''                Trident QoS policy details
                ''',
                'policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-typhoon', REFERENCE_CLASS, 'PolicyTyphoon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon', 
                [], [], 
                '''                Typhoon QoS policy details
                ''',
                'policy_typhoon',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details', 
                [], [], 
                '''                QoS policy direction egress
                ''',
                'details',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-asr9k-qos-oper', True),
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input', 
                [], [], 
                '''                QoS policy direction ingress
                ''',
                'input',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output', 
                [], [], 
                '''                QoS policy direction egress
                ''',
                'output',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                QoS interface name
                ''',
                'interface',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('ancp-config-bandwidth', REFERENCE_CLASS, 'AncpConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth', 
                [], [], 
                '''                Bandwidth obtain from IM
                ''',
                'ancp_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('ancp-programmed-bandwidth', REFERENCE_CLASS, 'AncpProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth', 
                [], [], 
                '''                ANCP bandwidth that was programmed
                ''',
                'ancp_programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-config-bandwidth', REFERENCE_CLASS, 'PortConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth', 
                [], [], 
                '''                Bandwidth due to port speed change
                ''',
                'port_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters', 
                [], [], 
                '''                Interface config and programmed parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('programmed-bandwidth', REFERENCE_CLASS, 'ProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED precedence match if precedence start value
                equals to end value Format: <start-value> , else
                range Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Table ID
                ''',
                'table_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v1',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v1', REFERENCE_LIST, 'QosShowEaStV1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1', 
                [], [], 
                '''                qos show ea st v1
                ''',
                'qos_show_ea_st_v1',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape',
            False, 
            [
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape',
            False, 
            [
            _MetaInfoClassMember('cir-shape', REFERENCE_CLASS, 'CirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape', 
                [], [], 
                '''                CIR shaper params
                ''',
                'cir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                CIR Shaper type
                ''',
                'cir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape', REFERENCE_CLASS, 'PirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape', 
                [], [], 
                '''                PIR shaper params
                ''',
                'pir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                PIR Shaper type
                ''',
                'pir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exp-match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED exp match if EXP start value equals to end
                value Format: <start-value> , else range Format:
                <start-value> <end-value>
                ''',
                'exp_match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED match if precedence start value equals to
                end value Format: <start-value> , else range
                Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v2', REFERENCE_LIST, 'QosShowEaStV2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2', 
                [], [], 
                '''                qos show ea st v2
                ''',
                'qos_show_ea_st_v2',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy-typhoon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header', 
                [], [], 
                '''                QoS policy header
                ''',
                'header',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy', 
                [], [], 
                '''                Trident QoS policy details
                ''',
                'policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-typhoon', REFERENCE_CLASS, 'PolicyTyphoon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon', 
                [], [], 
                '''                Typhoon QoS policy details
                ''',
                'policy_typhoon',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Memeber interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-asr9k-qos-oper', True),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details', 
                [], [], 
                '''                QoS policy direction egress
                ''',
                'details',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'member-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces',
            False, 
            [
            _MetaInfoClassMember('member-interface', REFERENCE_LIST, 'MemberInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface', 
                [], [], 
                '''                QoS interface name
                ''',
                'member_interface',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'member-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput',
            False, 
            [
            _MetaInfoClassMember('member-interfaces', REFERENCE_CLASS, 'MemberInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces', 
                [], [], 
                '''                QoS list of member interfaces
                ''',
                'member_interfaces',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bundle-output',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'ancp-programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('ancp-config-bandwidth', REFERENCE_CLASS, 'AncpConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth', 
                [], [], 
                '''                Bandwidth obtain from IM
                ''',
                'ancp_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('ancp-programmed-bandwidth', REFERENCE_CLASS, 'AncpProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth', 
                [], [], 
                '''                ANCP bandwidth that was programmed
                ''',
                'ancp_programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-config-bandwidth', REFERENCE_CLASS, 'PortConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth', 
                [], [], 
                '''                Bandwidth due to port speed change
                ''',
                'port_config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'programmed-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters', 
                [], [], 
                '''                Interface config and programmed parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('programmed-bandwidth', REFERENCE_CLASS, 'ProgrammedBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth', 
                [], [], 
                '''                Bandwidth that was programmed
                ''',
                'programmed_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED precedence match if precedence start value
                equals to end value Format: <start-value> , else
                range Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scaling-profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Scaling profile ID
                ''',
                'scaling_profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Table ID
                ''',
                'table_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v1',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v1', REFERENCE_LIST, 'QosShowEaStV1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1', 
                [], [], 
                '''                qos show ea st v1
                ''',
                'qos_show_ea_st_v1',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'QueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit', 
                [], [], 
                '''                Config queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit', 
                [], [], 
                '''                Queue limit in kbytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'queue-limit-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'minimum-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth',
            False, 
            [
            _MetaInfoClassMember('minimum-rate', REFERENCE_CLASS, 'MinimumRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate', 
                [], [], 
                '''                Minimum bandwidth rate
                ''',
                'minimum_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'config-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs', 
                [], [], 
                '''                CBS in bytes
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir', 
                [], [], 
                '''                CIR in kbps
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('config-bandwidth', REFERENCE_CLASS, 'ConfigBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth', 
                [], [], 
                '''                Config bandwidth
                ''',
                'config_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape',
            False, 
            [
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Shape profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('scale-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Scale Factor
                ''',
                'scale_factor',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir-shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape',
            False, 
            [
            _MetaInfoClassMember('cir-shape', REFERENCE_CLASS, 'CirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape', 
                [], [], 
                '''                CIR shaper params
                ''',
                'cir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                CIR Shaper type
                ''',
                'cir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape', REFERENCE_CLASS, 'PirShape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape', 
                [], [], 
                '''                PIR shaper params
                ''',
                'pir_shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir-shape-type', REFERENCE_ENUM_CLASS, 'ShapeProfiletypeV2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ShapeProfiletypeV2Enum', 
                [], [], 
                '''                PIR Shaper type
                ''',
                'pir_shape_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'exceed-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters',
            False, 
            [
            _MetaInfoClassMember('average-rate', REFERENCE_CLASS, 'AverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate', 
                [], [], 
                '''                Average rate
                ''',
                'average_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('conform-burst', REFERENCE_CLASS, 'ConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst', 
                [], [], 
                '''                Conform burst
                ''',
                'conform_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exceed-burst', REFERENCE_CLASS, 'ExceedBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst', 
                [], [], 
                '''                Exceed burst
                ''',
                'exceed_burst',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate', 
                [], [], 
                '''                Peak rate
                ''',
                'peak_rate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-config-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs', 
                [], [], 
                '''                PBS
                ''',
                'pbs',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir', 
                [], [], 
                '''                PIR
                ''',
                'pir',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-config-parameters', REFERENCE_CLASS, 'PoliceConfigParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters', 
                [], [], 
                '''                Police config parameters
                ''',
                'police_config_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Police profile ID
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth', 
                [], [], 
                '''                CFG Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('chunk-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Chunk ID
                ''',
                'chunk_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('committed-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parent Excess ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-bandwidth', REFERENCE_CLASS, 'ParentBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth', 
                [], [], 
                '''                Parent bandwidth
                ''',
                'parent_bandwidth',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WFQ profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'min-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'max-threshold-user-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve',
            False, 
            [
            _MetaInfoClassMember('absolute-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Absolute Index
                ''',
                'absolute_index',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('curve-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Curve ID
                ''',
                'curve_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('exp-match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED exp match if EXP start value equals to end
                value Format: <start-value> , else range Format:
                <start-value> <end-value>
                ''',
                'exp_match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('match', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                WRED match if precedence start value equals to
                end value Format: <start-value> , else range
                Format: <start-value> <end-value>
                ''',
                'match',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold', REFERENCE_CLASS, 'MaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold', 
                [], [], 
                '''                Maximum threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('max-threshold-user-config', REFERENCE_CLASS, 'MaxThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig', 
                [], [], 
                '''                Maximum threshold WRED context
                ''',
                'max_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold', REFERENCE_CLASS, 'MinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold', 
                [], [], 
                '''                Minimum threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('min-threshold-user-config', REFERENCE_CLASS, 'MinThresholdUserConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig', 
                [], [], 
                '''                Minimum threshold WRED context
                ''',
                'min_threshold_user_config',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('template-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Template ID
                ''',
                'template_id',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'curve',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred',
            False, 
            [
            _MetaInfoClassMember('curve', REFERENCE_LIST, 'Curve' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve', 
                [], [], 
                '''                Curve details
                ''',
                'curve',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=64),
            _MetaInfoClassMember('curve-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of curves
                ''',
                'curve_xr',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'WredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'WredEnum', 
                [], [], 
                '''                WRED type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'child-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-asr9k-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'parent-police-violate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark',
            False, 
            [
            _MetaInfoClassMember('child-mark', REFERENCE_CLASS, 'ChildMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark', 
                [], [], 
                '''                Child mark only
                ''',
                'child_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-mark', REFERENCE_CLASS, 'ParentMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark', 
                [], [], 
                '''                Parent mark only
                ''',
                'parent_mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-conform', REFERENCE_CLASS, 'ParentPoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform', 
                [], [], 
                '''                Parent police conform mark
                ''',
                'parent_police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-exceed', REFERENCE_CLASS, 'ParentPoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed', 
                [], [], 
                '''                Parent police exceed mark
                ''',
                'parent_police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-police-violate', REFERENCE_CLASS, 'ParentPoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate', 
                [], [], 
                '''                Parent police violate mark
                ''',
                'parent_police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform', 
                [], [], 
                '''                Child police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed', 
                [], [], 
                '''                Child police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police-violate', REFERENCE_CLASS, 'PoliceViolate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate', 
                [], [], 
                '''                Child police violate mark
                ''',
                'police_violate',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_CLASS, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark', 
                [], [], 
                '''                Mark parameters
                ''',
                'mark',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent class name
                ''',
                'parent_class_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('parent-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Parent policy name
                ''',
                'parent_policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police', 
                [], [], 
                '''                Police parameters
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue', 
                [], [], 
                '''                Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('queue-limit-parameters', REFERENCE_CLASS, 'QueueLimitParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters', 
                [], [], 
                '''                Queue limit parameters
                ''',
                'queue_limit_parameters',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape', 
                [], [], 
                '''                Shape parameters
                ''',
                'shape',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq', 
                [], [], 
                '''                WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_CLASS, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'qos-show-ea-st-v2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-st-v2', REFERENCE_LIST, 'QosShowEaStV2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2', 
                [], [], 
                '''                qos show ea st v2
                ''',
                'qos_show_ea_st_v2',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'policy-typhoon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header', 
                [], [], 
                '''                QoS policy header
                ''',
                'header',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy', 
                [], [], 
                '''                Trident QoS policy details
                ''',
                'policy',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('policy-typhoon', REFERENCE_CLASS, 'PolicyTyphoon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon', 
                [], [], 
                '''                Typhoon QoS policy details
                ''',
                'policy_typhoon',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Memeber interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-asr9k-qos-oper', True),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details', 
                [], [], 
                '''                QoS policy direction egress
                ''',
                'details',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'member-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces',
            False, 
            [
            _MetaInfoClassMember('member-interface', REFERENCE_LIST, 'MemberInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface', 
                [], [], 
                '''                QoS interface name
                ''',
                'member_interface',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'member-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput',
            False, 
            [
            _MetaInfoClassMember('member-interfaces', REFERENCE_CLASS, 'MemberInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces', 
                [], [], 
                '''                QoS list of member interfaces
                ''',
                'member_interfaces',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bundle-input',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Bundle interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-asr9k-qos-oper', True),
            _MetaInfoClassMember('bundle-input', REFERENCE_CLASS, 'BundleInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput', 
                [], [], 
                '''                QoS policy direction output
                ''',
                'bundle_input',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('bundle-output', REFERENCE_CLASS, 'BundleOutput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput', 
                [], [], 
                '''                QoS policy direction output
                ''',
                'bundle_output',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bundle-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces',
            False, 
            [
            _MetaInfoClassMember('bundle-interface', REFERENCE_LIST, 'BundleInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface', 
                [], [], 
                '''                QoS interface name
                ''',
                'bundle_interface',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'bundle-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-qos-oper', True),
            _MetaInfoClassMember('bundle-interfaces', REFERENCE_CLASS, 'BundleInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces', 
                [], [], 
                '''                QoS list of bundle interfaces
                ''',
                'bundle_interfaces',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('capability', REFERENCE_CLASS, 'Capability' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Capability', 
                [], [], 
                '''                QoS system capability
                ''',
                'capability',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node.Interfaces', 
                [], [], 
                '''                QoS list of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos.Nodes' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes.Node', 
                [], [], 
                '''                Node with platform specific QoS configuration
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
    'PlatformQos' : {
        'meta_info' : _MetaInfoClass('PlatformQos',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper', 'PlatformQos.Nodes', 
                [], [], 
                '''                List of nodes with platform specific QoS
                configuration
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-qos-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-oper',
            'platform-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_qos_oper'
        ),
    },
}
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.AncpProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header.ProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy.QosShowEaStV1']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon.QosShowEaStV2']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.Policy']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details.PolicyTyphoon']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.AncpProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header.ProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy.QosShowEaStV1']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon.QosShowEaStV2']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.Policy']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details.PolicyTyphoon']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.Policy']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface.Details']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces.MemberInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput.MemberInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.AncpProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header.ProgrammedBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy.QosShowEaStV1']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.QueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth.MinimumRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.ConfigBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.CirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape.PirShape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.AverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.PeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters.ExceedBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police.PoliceConfigParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.ParentBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MinThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve.MaxThresholdUserConfig']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred.Curve']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ChildMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.PoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark.ParentPoliceViolate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.QueueLimitParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon.QosShowEaStV2']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.Policy']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details.PolicyTyphoon']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface.Details']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces.MemberInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput.MemberInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleOutput']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.BundleInput']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Capability']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node']['meta_info'].parent =_meta_table['PlatformQos.Nodes']['meta_info']
_meta_table['PlatformQos.Nodes']['meta_info'].parent =_meta_table['PlatformQos']['meta_info']
