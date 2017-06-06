


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MetricEnum' : _MetaInfoEnum('MetricEnum', 'ydk.models.cisco_ios_xe.policy_types',
        {
            'none':'none',
            'peta':'peta',
            'tera':'tera',
            'giga':'giga',
            'mega':'mega',
            'kilo':'kilo',
            'milli':'milli',
            'nano':'nano',
        }, 'policy-types', _yang_ns._namespaces['policy-types']),
    'RateUnitEnum' : _MetaInfoEnum('RateUnitEnum', 'ydk.models.cisco_ios_xe.policy_types',
        {
            'pps':'pps',
            'cps':'cps',
            'bps':'bps',
            'perc':'perc',
            'ratio':'ratio',
        }, 'policy-types', _yang_ns._namespaces['policy-types']),
    'DirectionEnum' : _MetaInfoEnum('DirectionEnum', 'ydk.models.cisco_ios_xe.policy_types',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'policy-types', _yang_ns._namespaces['policy-types']),
    'MplsExpTopIdentity' : {
        'meta_info' : _MetaInfoClass('MplsExpTopIdentity',
            False, 
            [
            ],
            'policy-types',
            'mpls-exp-top',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'AtmVciIdentity' : {
        'meta_info' : _MetaInfoClass('AtmVciIdentity',
            False, 
            [
            ],
            'policy-types',
            'atm-vci',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'PacketLengthIdentity' : {
        'meta_info' : _MetaInfoClass('PacketLengthIdentity',
            False, 
            [
            ],
            'policy-types',
            'packet-length',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'SecurityGroupNameIdentity' : {
        'meta_info' : _MetaInfoClass('SecurityGroupNameIdentity',
            False, 
            [
            ],
            'policy-types',
            'security-group-name',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'FlowDlciIdentity' : {
        'meta_info' : _MetaInfoClass('FlowDlciIdentity',
            False, 
            [
            ],
            'policy-types',
            'flow-dlci',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'VlanInnerIdentity' : {
        'meta_info' : _MetaInfoClass('VlanInnerIdentity',
            False, 
            [
            ],
            'policy-types',
            'vlan-inner',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'Ipv4AclNameIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4AclNameIdentity',
            False, 
            [
            ],
            'policy-types',
            'ipv4-acl-name',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'CosIdentity' : {
        'meta_info' : _MetaInfoClass('CosIdentity',
            False, 
            [
            ],
            'policy-types',
            'cos',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'SecurityGroupTagIdentity' : {
        'meta_info' : _MetaInfoClass('SecurityGroupTagIdentity',
            False, 
            [
            ],
            'policy-types',
            'security-group-tag',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'ApplicationIdentity' : {
        'meta_info' : _MetaInfoClass('ApplicationIdentity',
            False, 
            [
            ],
            'policy-types',
            'application',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'QosGroupIdentity' : {
        'meta_info' : _MetaInfoClass('QosGroupIdentity',
            False, 
            [
            ],
            'policy-types',
            'qos-group',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'VplsIdentity' : {
        'meta_info' : _MetaInfoClass('VplsIdentity',
            False, 
            [
            ],
            'policy-types',
            'vpls',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'Ipv4AclIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4AclIdentity',
            False, 
            [
            ],
            'policy-types',
            'ipv4-acl',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'FlowRecordIdentity' : {
        'meta_info' : _MetaInfoClass('FlowRecordIdentity',
            False, 
            [
            ],
            'policy-types',
            'flow-record',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'Ipv6AclNameIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6AclNameIdentity',
            False, 
            [
            ],
            'policy-types',
            'ipv6-acl-name',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'VlanIdentity' : {
        'meta_info' : _MetaInfoClass('VlanIdentity',
            False, 
            [
            ],
            'policy-types',
            'vlan',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'FlowDeIdentity' : {
        'meta_info' : _MetaInfoClass('FlowDeIdentity',
            False, 
            [
            ],
            'policy-types',
            'flow-de',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'CosInnerIdentity' : {
        'meta_info' : _MetaInfoClass('CosInnerIdentity',
            False, 
            [
            ],
            'policy-types',
            'cos-inner',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'IpRtpIdentity' : {
        'meta_info' : _MetaInfoClass('IpRtpIdentity',
            False, 
            [
            ],
            'policy-types',
            'ip-rtp',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'DiscardClassIdentity' : {
        'meta_info' : _MetaInfoClass('DiscardClassIdentity',
            False, 
            [
            ],
            'policy-types',
            'discard-class',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'DstMacIdentity' : {
        'meta_info' : _MetaInfoClass('DstMacIdentity',
            False, 
            [
            ],
            'policy-types',
            'dst-mac',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'Ipv6AclIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6AclIdentity',
            False, 
            [
            ],
            'policy-types',
            'ipv6-acl',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'MetadataIdentity' : {
        'meta_info' : _MetaInfoClass('MetadataIdentity',
            False, 
            [
            ],
            'policy-types',
            'metadata',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'InputInterfaceIdentity' : {
        'meta_info' : _MetaInfoClass('InputInterfaceIdentity',
            False, 
            [
            ],
            'policy-types',
            'input-interface',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'FlowIpIdentity' : {
        'meta_info' : _MetaInfoClass('FlowIpIdentity',
            False, 
            [
            ],
            'policy-types',
            'flow-ip',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'WlanUserPriorityIdentity' : {
        'meta_info' : _MetaInfoClass('WlanUserPriorityIdentity',
            False, 
            [
            ],
            'policy-types',
            'wlan-user-priority',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'DeiInnerIdentity' : {
        'meta_info' : _MetaInfoClass('DeiInnerIdentity',
            False, 
            [
            ],
            'policy-types',
            'dei-inner',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'ClassTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ClassTypeIdentity',
            False, 
            [
            ],
            'policy-types',
            'class-type',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'AtmClpIdentity' : {
        'meta_info' : _MetaInfoClass('AtmClpIdentity',
            False, 
            [
            ],
            'policy-types',
            'atm-clp',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'PolicyTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PolicyTypeIdentity',
            False, 
            [
            ],
            'policy-types',
            'policy-type',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'MplsExpImpIdentity' : {
        'meta_info' : _MetaInfoClass('MplsExpImpIdentity',
            False, 
            [
            ],
            'policy-types',
            'mpls-exp-imp',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'SrcMacIdentity' : {
        'meta_info' : _MetaInfoClass('SrcMacIdentity',
            False, 
            [
            ],
            'policy-types',
            'src-mac',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'ClassMapIdentity' : {
        'meta_info' : _MetaInfoClass('ClassMapIdentity',
            False, 
            [
            ],
            'policy-types',
            'class-map',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'PrecIdentity' : {
        'meta_info' : _MetaInfoClass('PrecIdentity',
            False, 
            [
            ],
            'policy-types',
            'prec',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'DeiIdentity' : {
        'meta_info' : _MetaInfoClass('DeiIdentity',
            False, 
            [
            ],
            'policy-types',
            'dei',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'AppnavIdentity' : {
        'meta_info' : _MetaInfoClass('AppnavIdentity',
            False, 
            [
            ],
            'policy-types',
            'appnav',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'PacketServiceIdentity' : {
        'meta_info' : _MetaInfoClass('PacketServiceIdentity',
            False, 
            [
            ],
            'policy-types',
            'packet-service',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'ControlIdentity' : {
        'meta_info' : _MetaInfoClass('ControlIdentity',
            False, 
            [
            ],
            'policy-types',
            'control',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'ControlClassIdentity' : {
        'meta_info' : _MetaInfoClass('ControlClassIdentity',
            False, 
            [
            ],
            'policy-types',
            'control-class',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'AccessControlIdentity' : {
        'meta_info' : _MetaInfoClass('AccessControlIdentity',
            False, 
            [
            ],
            'policy-types',
            'access-control',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'InspectIdentity' : {
        'meta_info' : _MetaInfoClass('InspectIdentity',
            False, 
            [
            ],
            'policy-types',
            'inspect',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'AccessControlClassIdentity' : {
        'meta_info' : _MetaInfoClass('AccessControlClassIdentity',
            False, 
            [
            ],
            'policy-types',
            'access-control-class',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'AppnavClassIdentity' : {
        'meta_info' : _MetaInfoClass('AppnavClassIdentity',
            False, 
            [
            ],
            'policy-types',
            'appnav-class',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'ServiceIdentity' : {
        'meta_info' : _MetaInfoClass('ServiceIdentity',
            False, 
            [
            ],
            'policy-types',
            'service',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'QosIdentity' : {
        'meta_info' : _MetaInfoClass('QosIdentity',
            False, 
            [
            ],
            'policy-types',
            'qos',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'InspectClassIdentity' : {
        'meta_info' : _MetaInfoClass('InspectClassIdentity',
            False, 
            [
            ],
            'policy-types',
            'inspect-class',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'PbrIdentity' : {
        'meta_info' : _MetaInfoClass('PbrIdentity',
            False, 
            [
            ],
            'policy-types',
            'pbr',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'QosClassIdentity' : {
        'meta_info' : _MetaInfoClass('QosClassIdentity',
            False, 
            [
            ],
            'policy-types',
            'qos-class',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
    'PerfMonIdentity' : {
        'meta_info' : _MetaInfoClass('PerfMonIdentity',
            False, 
            [
            ],
            'policy-types',
            'perf-mon',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.cisco_ios_xe.policy_types'
        ),
    },
}
