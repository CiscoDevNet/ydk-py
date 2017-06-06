


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'QosUnitEnum' : _MetaInfoEnum('QosUnitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
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
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'ActionEnum' : _MetaInfoEnum('ActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
        {
            'police-transmit':'police_transmit',
            'police-set-transmit':'police_set_transmit',
            'police-drop':'police_drop',
            'police-unknown':'police_unknown',
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'TbAlgorithmEnum' : _MetaInfoEnum('TbAlgorithmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
        {
            'inactive':'inactive',
            'single':'single',
            'single-rate-tcm':'single_rate_tcm',
            'two-rate-tcm':'two_rate_tcm',
            'mef-tcm':'mef_tcm',
            'dummy':'dummy',
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'ActionOpcodeEnum' : _MetaInfoEnum('ActionOpcodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
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
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'PolicyStateEnum' : _MetaInfoEnum('PolicyStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
        {
            'active':'active',
            'suspended':'suspended',
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'PolicyParamUnitEnum' : _MetaInfoEnum('PolicyParamUnitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
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
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'CacStateEnum' : _MetaInfoEnum('CacStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
        {
            'unknown':'unknown',
            'admit':'admit',
            'redirect':'redirect',
            'ubrl':'ubrl',
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'WredEnum' : _MetaInfoEnum('WredEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper',
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
        }, 'Cisco-IOS-XR-skp-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper']),
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-config-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-program-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('interface-config-rate', REFERENCE_CLASS, 'InterfaceConfigRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate', 
                [], [], 
                '''                Interface Configured Rate
                ''',
                'interface_config_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-program-rate', REFERENCE_CLASS, 'InterfaceProgramRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate', 
                [], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_program_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue',
            False, 
            [
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Queue Type
                ''',
                'queue_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'committed-weight',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'programmed-wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq',
            False, 
            [
            _MetaInfoClassMember('committed-weight', REFERENCE_CLASS, 'CommittedWeight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight', 
                [], [], 
                '''                Committed Weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('programmed-wfq', REFERENCE_CLASS, 'ProgrammedWfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq', 
                [], [], 
                '''                QoS Programmed WFQ parameters
                ''',
                'programmed_wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer ID
                ''',
                'policer_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-only',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking',
            False, 
            [
            _MetaInfoClassMember('mark-only', REFERENCE_CLASS, 'MarkOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly', 
                [], [], 
                '''                Mark Only
                ''',
                'mark_only',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform', 
                [], [], 
                '''                Police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed', 
                [], [], 
                '''                Police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'marking',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('marking', REFERENCE_CLASS, 'Marking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking', 
                [], [], 
                '''                QoS Mark parameters
                ''',
                'marking',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police', 
                [], [], 
                '''                QoS Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue', 
                [], [], 
                '''                QoS Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq', 
                [], [], 
                '''                QoS WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-pclass-st', REFERENCE_LIST, 'QosShowPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt', 
                [], [], 
                '''                qos show pclass st
                ''',
                'qos_show_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters', 
                [], [], 
                '''                QoS Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-input',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-config-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-program-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('interface-config-rate', REFERENCE_CLASS, 'InterfaceConfigRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate', 
                [], [], 
                '''                Interface Configured Rate
                ''',
                'interface_config_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-program-rate', REFERENCE_CLASS, 'InterfaceProgramRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate', 
                [], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_program_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue',
            False, 
            [
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Queue Type
                ''',
                'queue_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'committed-weight',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'programmed-wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq',
            False, 
            [
            _MetaInfoClassMember('committed-weight', REFERENCE_CLASS, 'CommittedWeight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight', 
                [], [], 
                '''                Committed Weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('programmed-wfq', REFERENCE_CLASS, 'ProgrammedWfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq', 
                [], [], 
                '''                QoS Programmed WFQ parameters
                ''',
                'programmed_wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer ID
                ''',
                'policer_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-only',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking',
            False, 
            [
            _MetaInfoClassMember('mark-only', REFERENCE_CLASS, 'MarkOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly', 
                [], [], 
                '''                Mark Only
                ''',
                'mark_only',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform', 
                [], [], 
                '''                Police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed', 
                [], [], 
                '''                Police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'marking',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('marking', REFERENCE_CLASS, 'Marking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking', 
                [], [], 
                '''                QoS Mark parameters
                ''',
                'marking',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police', 
                [], [], 
                '''                QoS Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue', 
                [], [], 
                '''                QoS Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq', 
                [], [], 
                '''                QoS WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-pclass-st', REFERENCE_LIST, 'QosShowPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt', 
                [], [], 
                '''                qos show pclass st
                ''',
                'qos_show_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters', 
                [], [], 
                '''                QoS Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-output',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Memeber interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('bundle-input', REFERENCE_CLASS, 'BundleInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput', 
                [], [], 
                '''                QoS policy direction input
                ''',
                'bundle_input',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('bundle-output', REFERENCE_CLASS, 'BundleOutput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput', 
                [], [], 
                '''                QoS policy direction output
                ''',
                'bundle_output',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'member-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces',
            False, 
            [
            _MetaInfoClassMember('member-interface', REFERENCE_LIST, 'MemberInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface', 
                [], [], 
                '''                QoS interface name
                ''',
                'member_interface',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'member-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
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
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('member-interfaces', REFERENCE_CLASS, 'MemberInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces', 
                [], [], 
                '''                QoS list of member interfaces
                ''',
                'member_interfaces',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces',
            False, 
            [
            _MetaInfoClassMember('bundle-interface', REFERENCE_LIST, 'BundleInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface', 
                [], [], 
                '''                QoS interface name
                ''',
                'bundle_interface',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Capability' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Capability',
            False, 
            [
            _MetaInfoClassMember('max-bundle-members', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum bundle members
                ''',
                'max_bundle_members',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-classes-per-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum classes per policy
                ''',
                'max_classes_per_policy',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-classmap-name-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum classmap name length
                ''',
                'max_classmap_name_length',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-marking-actions-per-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum marking action  per class
                ''',
                'max_marking_actions_per_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-matches-per-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum matches per class
                ''',
                'max_matches_per_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-police-actions-per-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum police actions per class
                ''',
                'max_police_actions_per_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-policy-hierarchy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum policy hierarchy
                ''',
                'max_policy_hierarchy',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-policy-maps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum policy maps per system
                ''',
                'max_policy_maps',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('max-policy-name-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum policy name length
                ''',
                'max_policy_name_length',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'capability',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-config-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-program-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('interface-config-rate', REFERENCE_CLASS, 'InterfaceConfigRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate', 
                [], [], 
                '''                Interface Configured Rate
                ''',
                'interface_config_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-program-rate', REFERENCE_CLASS, 'InterfaceProgramRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate', 
                [], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_program_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue',
            False, 
            [
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Queue Type
                ''',
                'queue_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'committed-weight',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'programmed-wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq',
            False, 
            [
            _MetaInfoClassMember('committed-weight', REFERENCE_CLASS, 'CommittedWeight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight', 
                [], [], 
                '''                Committed Weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('programmed-wfq', REFERENCE_CLASS, 'ProgrammedWfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq', 
                [], [], 
                '''                QoS Programmed WFQ parameters
                ''',
                'programmed_wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer ID
                ''',
                'policer_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-only',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking',
            False, 
            [
            _MetaInfoClassMember('mark-only', REFERENCE_CLASS, 'MarkOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly', 
                [], [], 
                '''                Mark Only
                ''',
                'mark_only',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform', 
                [], [], 
                '''                Police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed', 
                [], [], 
                '''                Police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'marking',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('marking', REFERENCE_CLASS, 'Marking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking', 
                [], [], 
                '''                QoS Mark parameters
                ''',
                'marking',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police', 
                [], [], 
                '''                QoS Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue', 
                [], [], 
                '''                QoS Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq', 
                [], [], 
                '''                QoS WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-pclass-st', REFERENCE_LIST, 'QosShowPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt', 
                [], [], 
                '''                qos show pclass st
                ''',
                'qos_show_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Output' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Output',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters', 
                [], [], 
                '''                QoS Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-config-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-program-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'port-shaper-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('interface-config-rate', REFERENCE_CLASS, 'InterfaceConfigRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate', 
                [], [], 
                '''                Interface Configured Rate
                ''',
                'interface_config_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-program-rate', REFERENCE_CLASS, 'InterfaceProgramRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate', 
                [], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_program_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', REFERENCE_CLASS, 'PortShaperRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate', 
                [], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue',
            False, 
            [
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Queue Type
                ''',
                'queue_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'committed-weight',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'programmed-wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq',
            False, 
            [
            _MetaInfoClassMember('committed-weight', REFERENCE_CLASS, 'CommittedWeight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight', 
                [], [], 
                '''                Committed Weight
                ''',
                'committed_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Weight
                ''',
                'excess_weight',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('programmed-wfq', REFERENCE_CLASS, 'ProgrammedWfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq', 
                [], [], 
                '''                QoS Programmed WFQ parameters
                ''',
                'programmed_wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer ID
                ''',
                'policer_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-only',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-conform',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail',
            False, 
            [
            _MetaInfoClassMember('action-opcode', REFERENCE_ENUM_CLASS, 'ActionOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcodeEnum', 
                [], [], 
                '''                Action opcode
                ''',
                'action_opcode',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'mark-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionEnum', 
                [], [], 
                '''                Action type
                ''',
                'action_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('mark-detail', REFERENCE_LIST, 'MarkDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail', 
                [], [], 
                '''                Mark value
                ''',
                'mark_detail',
                'Cisco-IOS-XR-skp-qos-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police-exceed',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking',
            False, 
            [
            _MetaInfoClassMember('mark-only', REFERENCE_CLASS, 'MarkOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly', 
                [], [], 
                '''                Mark Only
                ''',
                'mark_only',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-conform', REFERENCE_CLASS, 'PoliceConform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform', 
                [], [], 
                '''                Police conform mark
                ''',
                'police_conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police-exceed', REFERENCE_CLASS, 'PoliceExceed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed', 
                [], [], 
                '''                Police exceed mark
                ''',
                'police_exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'marking',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('marking', REFERENCE_CLASS, 'Marking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking', 
                [], [], 
                '''                QoS Mark parameters
                ''',
                'marking',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police', 
                [], [], 
                '''                QoS Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue', 
                [], [], 
                '''                QoS Queue parameters
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq', 
                [], [], 
                '''                QoS WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-pclass-st', REFERENCE_LIST, 'QosShowPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt', 
                [], [], 
                '''                qos show pclass st
                ''',
                'qos_show_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Input' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Input',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters', 
                [], [], 
                '''                QoS Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
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
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Input', 
                [], [], 
                '''                QoS policy direction ingress
                ''',
                'input',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Output', 
                [], [], 
                '''                QoS policy direction egress
                ''',
                'output',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                QoS interface name
                ''',
                'interface',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
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
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('bundle-interfaces', REFERENCE_CLASS, 'BundleInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces', 
                [], [], 
                '''                QoS list of bundle interfaces
                ''',
                'bundle_interfaces',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('capability', REFERENCE_CLASS, 'Capability' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Capability', 
                [], [], 
                '''                QoS system capability
                ''',
                'capability',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node.Interfaces', 
                [], [], 
                '''                QoS list of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos.Nodes' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes.Node', 
                [], [], 
                '''                Node with platform specific QoS configuration
                ''',
                'node',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQos' : {
        'meta_info' : _MetaInfoClass('PlatformQos',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQos.Nodes', 
                [], [], 
                '''                List of nodes with platform specific QoS
                configuration
                ''',
                'nodes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'platform-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('bundle-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Bundle Interface ID
                ''',
                'bundle_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('hierarchical-depth', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Max Hierarchial Depth
                ''',
                'hierarchical_depth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Type
                ''',
                'interface_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-map-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Policy Map ID
                ''',
                'policy_map_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Port
                ''',
                'port',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('qos-interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                QoS Interface handle
                ''',
                'qos_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('uidb-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                UIDB Index
                ''',
                'uidb_index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('under-line-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                UnderLineInterface Handle
                ''',
                'under_line_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('color-aware', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Color Aware
                ''',
                'color_aware',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config',
            False, 
            [
            _MetaInfoClassMember('node-config', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Config
                ''',
                'node_config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police', 
                [], [], 
                '''                QoS EA Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq', 
                [], [], 
                '''                QoS EA WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'config',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue',
            False, 
            [
            _MetaInfoClassMember('commit-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Commit Tx
                ''',
                'commit_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop
                ''',
                'drop',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Tx
                ''',
                'excess_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police',
            False, 
            [
            _MetaInfoClassMember('conform', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conform Rate
                ''',
                'conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Exceed Rate
                ''',
                'exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('token-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Token Bucket ID
                ''',
                'token_bucket_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('violate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Violate Rate
                ''',
                'violate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result',
            False, 
            [
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police', 
                [], [], 
                '''                QoS EA Policer Result
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue', 
                [], [], 
                '''                QoS EA Queue Result
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stats ID
                ''',
                'stats_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'result',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config', 
                [], [], 
                '''                QoS EA Class Configuration
                ''',
                'config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Class Index
                ''',
                'index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('node-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Flags
                ''',
                'node_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('result', REFERENCE_CLASS, 'Result' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result', 
                [], [], 
                '''                QoS EA Class Result
                ''',
                'result',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Statistical Flags
                ''',
                'stats_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-ea-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-pclass-st', REFERENCE_LIST, 'QosShowEaPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt', 
                [], [], 
                '''                qos show ea pclass st
                ''',
                'qos_show_ea_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters', 
                [], [], 
                '''                QoS EA Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS EA policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details', 
                [], [], 
                '''                QoS-EA policy details
                ''',
                'details',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-output',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('bundle-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Bundle Interface ID
                ''',
                'bundle_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('hierarchical-depth', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Max Hierarchial Depth
                ''',
                'hierarchical_depth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Type
                ''',
                'interface_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-map-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Policy Map ID
                ''',
                'policy_map_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Port
                ''',
                'port',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('qos-interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                QoS Interface handle
                ''',
                'qos_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('uidb-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                UIDB Index
                ''',
                'uidb_index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('under-line-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                UnderLineInterface Handle
                ''',
                'under_line_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('color-aware', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Color Aware
                ''',
                'color_aware',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config',
            False, 
            [
            _MetaInfoClassMember('node-config', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Config
                ''',
                'node_config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police', 
                [], [], 
                '''                QoS EA Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq', 
                [], [], 
                '''                QoS EA WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'config',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue',
            False, 
            [
            _MetaInfoClassMember('commit-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Commit Tx
                ''',
                'commit_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop
                ''',
                'drop',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Tx
                ''',
                'excess_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police',
            False, 
            [
            _MetaInfoClassMember('conform', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conform Rate
                ''',
                'conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Exceed Rate
                ''',
                'exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('token-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Token Bucket ID
                ''',
                'token_bucket_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('violate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Violate Rate
                ''',
                'violate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result',
            False, 
            [
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police', 
                [], [], 
                '''                QoS EA Policer Result
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue', 
                [], [], 
                '''                QoS EA Queue Result
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stats ID
                ''',
                'stats_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'result',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config', 
                [], [], 
                '''                QoS EA Class Configuration
                ''',
                'config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Class Index
                ''',
                'index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('node-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Flags
                ''',
                'node_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('result', REFERENCE_CLASS, 'Result' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result', 
                [], [], 
                '''                QoS EA Class Result
                ''',
                'result',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Statistical Flags
                ''',
                'stats_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-ea-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-pclass-st', REFERENCE_LIST, 'QosShowEaPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt', 
                [], [], 
                '''                qos show ea pclass st
                ''',
                'qos_show_ea_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters', 
                [], [], 
                '''                QoS EA Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS EA policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details', 
                [], [], 
                '''                QoS-EA policy details
                ''',
                'details',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-input',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Memeber interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('bundle-input', REFERENCE_CLASS, 'BundleInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput', 
                [], [], 
                '''                QoS-EA policy direction input
                ''',
                'bundle_input',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('bundle-output', REFERENCE_CLASS, 'BundleOutput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput', 
                [], [], 
                '''                QoS-EA policy direction output
                ''',
                'bundle_output',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'member-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces',
            False, 
            [
            _MetaInfoClassMember('member-interface', REFERENCE_LIST, 'MemberInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface', 
                [], [], 
                '''                QoS-EA interface name
                ''',
                'member_interface',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'member-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Bundle interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('member-interfaces', REFERENCE_CLASS, 'MemberInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces', 
                [], [], 
                '''                QoS-EA list of member interfaces
                ''',
                'member_interfaces',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.BundleInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.BundleInterfaces',
            False, 
            [
            _MetaInfoClassMember('bundle-interface', REFERENCE_LIST, 'BundleInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface', 
                [], [], 
                '''                QoS-EA interface name
                ''',
                'bundle_interface',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bundle-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('bundle-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Bundle Interface ID
                ''',
                'bundle_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('hierarchical-depth', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Max Hierarchial Depth
                ''',
                'hierarchical_depth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Type
                ''',
                'interface_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-map-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Policy Map ID
                ''',
                'policy_map_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Port
                ''',
                'port',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('qos-interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                QoS Interface handle
                ''',
                'qos_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('uidb-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                UIDB Index
                ''',
                'uidb_index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('under-line-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                UnderLineInterface Handle
                ''',
                'under_line_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('color-aware', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Color Aware
                ''',
                'color_aware',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config',
            False, 
            [
            _MetaInfoClassMember('node-config', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Config
                ''',
                'node_config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police', 
                [], [], 
                '''                QoS EA Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq', 
                [], [], 
                '''                QoS EA WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'config',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue',
            False, 
            [
            _MetaInfoClassMember('commit-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Commit Tx
                ''',
                'commit_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop
                ''',
                'drop',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Tx
                ''',
                'excess_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police',
            False, 
            [
            _MetaInfoClassMember('conform', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conform Rate
                ''',
                'conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Exceed Rate
                ''',
                'exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('token-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Token Bucket ID
                ''',
                'token_bucket_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('violate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Violate Rate
                ''',
                'violate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result',
            False, 
            [
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police', 
                [], [], 
                '''                QoS EA Policer Result
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue', 
                [], [], 
                '''                QoS EA Queue Result
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stats ID
                ''',
                'stats_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'result',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config', 
                [], [], 
                '''                QoS EA Class Configuration
                ''',
                'config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Class Index
                ''',
                'index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('node-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Flags
                ''',
                'node_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('result', REFERENCE_CLASS, 'Result' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result', 
                [], [], 
                '''                QoS EA Class Result
                ''',
                'result',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Statistical Flags
                ''',
                'stats_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-ea-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-pclass-st', REFERENCE_LIST, 'QosShowEaPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt', 
                [], [], 
                '''                qos show ea pclass st
                ''',
                'qos_show_ea_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters', 
                [], [], 
                '''                QoS EA Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS EA policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Output',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details', 
                [], [], 
                '''                QoS-EA policy details
                ''',
                'details',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header',
            False, 
            [
            _MetaInfoClassMember('classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of classes
                ''',
                'classes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Direction
                ''',
                'direction',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters',
            False, 
            [
            _MetaInfoClassMember('bundle-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Bundle Interface ID
                ''',
                'bundle_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('hierarchical-depth', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Max Hierarchial Depth
                ''',
                'hierarchical_depth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Programmed Rate
                ''',
                'interface_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Interface Type
                ''',
                'interface_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-map-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Policy Map ID
                ''',
                'policy_map_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Port
                ''',
                'port',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('port-shaper-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port Shaper Rate
                ''',
                'port_shaper_rate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('qos-interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                QoS Interface handle
                ''',
                'qos_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('uidb-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                UIDB Index
                ''',
                'uidb_index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('under-line-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                UnderLineInterface Handle
                ''',
                'under_line_interface_handle',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'cbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police',
            False, 
            [
            _MetaInfoClassMember('cbs', REFERENCE_CLASS, 'Cbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs', 
                [], [], 
                '''                CBS
                ''',
                'cbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('cir', REFERENCE_CLASS, 'Cir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir', 
                [], [], 
                '''                CIR
                ''',
                'cir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('color-aware', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Color Aware
                ''',
                'color_aware',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policer-type', REFERENCE_ENUM_CLASS, 'TbAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithmEnum', 
                [], [], 
                '''                Policer type
                ''',
                'policer_type',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pir',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'pbs',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape',
            False, 
            [
            _MetaInfoClassMember('pbs', REFERENCE_CLASS, 'Pbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs', 
                [], [], 
                '''                PBS in bytes
                ''',
                'pbs',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('pir', REFERENCE_CLASS, 'Pir' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir', 
                [], [], 
                '''                PIR in kbps
                ''',
                'pir',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'QosUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnitEnum', 
                [], [], 
                '''                Config unit
                ''',
                'unit',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Config value
                ''',
                'value',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'sum-of-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq',
            False, 
            [
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth', 
                [], [], 
                '''                Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Excess Ratio
                ''',
                'excess_ratio',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('sum-of-bandwidth', REFERENCE_CLASS, 'SumOfBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth', 
                [], [], 
                '''                Sum of Bandwidth
                ''',
                'sum_of_bandwidth',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'wfq',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config',
            False, 
            [
            _MetaInfoClassMember('node-config', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Config
                ''',
                'node_config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police', 
                [], [], 
                '''                QoS EA Policer parameters
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape', 
                [], [], 
                '''                QoS EA Shaper parameters
                ''',
                'shape',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('wfq', REFERENCE_CLASS, 'Wfq' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq', 
                [], [], 
                '''                QoS EA WFQ parameters
                ''',
                'wfq',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'config',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue',
            False, 
            [
            _MetaInfoClassMember('commit-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Commit Tx
                ''',
                'commit_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop
                ''',
                'drop',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('excess-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Tx
                ''',
                'excess_tx',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue ID
                ''',
                'queue_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police',
            False, 
            [
            _MetaInfoClassMember('conform', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conform Rate
                ''',
                'conform',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Exceed Rate
                ''',
                'exceed',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('token-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Token Bucket ID
                ''',
                'token_bucket_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('violate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Violate Rate
                ''',
                'violate',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result',
            False, 
            [
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police', 
                [], [], 
                '''                QoS EA Policer Result
                ''',
                'police',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue', 
                [], [], 
                '''                QoS EA Queue Result
                ''',
                'queue',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stats ID
                ''',
                'stats_id',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'result',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt',
            False, 
            [
            _MetaInfoClassMember('class-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config', 
                [], [], 
                '''                QoS EA Class Configuration
                ''',
                'config',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Class Index
                ''',
                'index',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('node-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Node Flags
                ''',
                'node_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('result', REFERENCE_CLASS, 'Result' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result', 
                [], [], 
                '''                QoS EA Class Result
                ''',
                'result',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('stats-flags', ATTRIBUTE, 'str' , None, None, 
                [(0, 101)], [], 
                '''                Statistical Flags
                ''',
                'stats_flags',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'qos-show-ea-pclass-st',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass',
            False, 
            [
            _MetaInfoClassMember('qos-show-ea-pclass-st', REFERENCE_LIST, 'QosShowEaPclassSt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt', 
                [], [], 
                '''                qos show ea pclass st
                ''',
                'qos_show_ea_pclass_st',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'skywarp-qos-policy-class',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header', 
                [], [], 
                '''                QoS EA policy header
                ''',
                'header',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interface-parameters', REFERENCE_CLASS, 'InterfaceParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters', 
                [], [], 
                '''                QoS EA Interface Parameters
                ''',
                'interface_parameters',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('skywarp-qos-policy-class', REFERENCE_CLASS, 'SkywarpQosPolicyClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass', 
                [], [], 
                '''                Skywarp QoS EA policy class details
                ''',
                'skywarp_qos_policy_class',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface.Input',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details', 
                [], [], 
                '''                QoS-EA policy details
                ''',
                'details',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Input', 
                [], [], 
                '''                QoS-EA policy direction ingress
                ''',
                'input',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface.Output', 
                [], [], 
                '''                QoS-EA policy direction egress
                ''',
                'output',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                QoS-EA interface name
                ''',
                'interface',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-skp-qos-oper', True),
            _MetaInfoClassMember('bundle-interfaces', REFERENCE_CLASS, 'BundleInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.BundleInterfaces', 
                [], [], 
                '''                QoS-EA list of bundle interfaces
                ''',
                'bundle_interfaces',
                'Cisco-IOS-XR-skp-qos-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node.Interfaces', 
                [], [], 
                '''                QoS-EA list of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa.Nodes' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes.Node', 
                [], [], 
                '''                Node with platform specific QoS-EA
                configuration
                ''',
                'node',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
    'PlatformQosEa' : {
        'meta_info' : _MetaInfoClass('PlatformQosEa',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'PlatformQosEa.Nodes', 
                [], [], 
                '''                List of nodes with platform specific QoS-EA
                configuration
                ''',
                'nodes',
                'Cisco-IOS-XR-skp-qos-oper', False),
            ],
            'Cisco-IOS-XR-skp-qos-oper',
            'platform-qos-ea',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper'
        ),
    },
}
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Capability']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node']['meta_info'].parent =_meta_table['PlatformQos.Nodes']['meta_info']
_meta_table['PlatformQos.Nodes']['meta_info'].parent =_meta_table['PlatformQos']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node.Interfaces']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes.Node']['meta_info']
_meta_table['PlatformQosEa.Nodes.Node']['meta_info'].parent =_meta_table['PlatformQosEa.Nodes']['meta_info']
_meta_table['PlatformQosEa.Nodes']['meta_info'].parent =_meta_table['PlatformQosEa']['meta_info']
