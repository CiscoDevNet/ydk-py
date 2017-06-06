


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ActOspfRoutesRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfRoutesRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfRoutesRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfRoutesRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfRoutesRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPF instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfRoutesRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfRoutesRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfRoutesRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfRedistributionRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfRedistributionRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfRedistributionRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfRedistributionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfRedistributionRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPF instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF Route Redistribution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfRedistributionRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfRedistributionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfRedistributionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPF instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                All OSPF counters and statistics
                ''',
                'all',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('message-queue', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Message-queue statistics
                ''',
                'message_queue',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Neighbor statistics per neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                OSPF interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsNeighborRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsNeighborRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsNeighborRpc.Input.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsNeighborRpc.Input.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsNeighborRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsNeighborRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsNeighborRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPF instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsNeighborRpc.Input.Neighbor', 
                [], [], 
                '''                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsNeighborRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsNeighborRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsNeighborRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-statistics-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsInterfaceRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsInterfaceRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsInterfaceRpc.Input.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsInterfaceRpc.Input.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPF interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsInterfaceRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsInterfaceRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsInterfaceRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPF instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsInterfaceRpc.Input.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfStatisticsInterfaceRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfStatisticsInterfaceRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfStatisticsInterfaceRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-statistics-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfProcessRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfProcessRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfProcessRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfProcessRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfProcessRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPF instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPF process
                ''',
                'process',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfProcessRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfProcessRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfProcessRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-process',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPF interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats',
            False, 
            [
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('message-queue', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Message-queue statistics
                ''',
                'message_queue',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface', 
                [], [], 
                '''                OSPF interface statistics
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor', 
                [], [], 
                '''                Neighbor statistics per interface or neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.Vrf' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPF process
                ''',
                'process',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route redistrbution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats', 
                [], [], 
                '''                OSPF counters and statistics
                ''',
                'stats',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPF interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.All.Stats' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.All.Stats',
            False, 
            [
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('message-queue', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Message-queue statistics
                ''',
                'message_queue',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface', 
                [], [], 
                '''                OSPF interface statistics
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor', 
                [], [], 
                '''                Neighbor statistics per interface or neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.All' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.All',
            False, 
            [
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPF process
                ''',
                'process',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route redistrbution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.All.Stats', 
                [], [], 
                '''                OSPF counters and statistics
                ''',
                'stats',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPF interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats',
            False, 
            [
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('message-queue', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Message-queue statistics
                ''',
                'message_queue',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface', 
                [], [], 
                '''                OSPF interface statistics
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor', 
                [], [], 
                '''                Neighbor statistics per interface or neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance.AllInclusive',
            False, 
            [
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPF process
                ''',
                'process',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route redistrbution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPF route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats', 
                [], [], 
                '''                OSPF counters and statistics
                ''',
                'stats',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'all-inclusive',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('vrf', REFERENCE_CLASS, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.Vrf', 
                [], [], 
                '''                Clear one or more non-default OSPF VRFs in process
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.All', 
                [], [], 
                '''                Clear all non-default OSPF VRFs
                ''',
                'all',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            _MetaInfoClassMember('all-inclusive', REFERENCE_CLASS, 'AllInclusive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance.AllInclusive', 
                [], [], 
                '''                Clear all non-default and default OSPF VRFs
                ''',
                'all_inclusive',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input.Instance', 
                [], [], 
                '''                OSPF instance name
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
    'ActOspfInstanceVrfRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfInstanceVrfRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act', 'ActOspfInstanceVrfRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ospf-act', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-act',
            'act-ospf-instance-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act'
        ),
    },
}
_meta_table['ActOspfRoutesRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfRoutesRpc.Input']['meta_info']
_meta_table['ActOspfRoutesRpc.Input']['meta_info'].parent =_meta_table['ActOspfRoutesRpc']['meta_info']
_meta_table['ActOspfRedistributionRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfRedistributionRpc.Input']['meta_info']
_meta_table['ActOspfRedistributionRpc.Input']['meta_info'].parent =_meta_table['ActOspfRedistributionRpc']['meta_info']
_meta_table['ActOspfStatisticsRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfStatisticsRpc.Input']['meta_info']
_meta_table['ActOspfStatisticsRpc.Input']['meta_info'].parent =_meta_table['ActOspfStatisticsRpc']['meta_info']
_meta_table['ActOspfStatisticsNeighborRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfStatisticsNeighborRpc.Input']['meta_info']
_meta_table['ActOspfStatisticsNeighborRpc.Input.Neighbor']['meta_info'].parent =_meta_table['ActOspfStatisticsNeighborRpc.Input']['meta_info']
_meta_table['ActOspfStatisticsNeighborRpc.Input']['meta_info'].parent =_meta_table['ActOspfStatisticsNeighborRpc']['meta_info']
_meta_table['ActOspfStatisticsInterfaceRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfStatisticsInterfaceRpc.Input']['meta_info']
_meta_table['ActOspfStatisticsInterfaceRpc.Input.Interface']['meta_info'].parent =_meta_table['ActOspfStatisticsInterfaceRpc.Input']['meta_info']
_meta_table['ActOspfStatisticsInterfaceRpc.Input']['meta_info'].parent =_meta_table['ActOspfStatisticsInterfaceRpc']['meta_info']
_meta_table['ActOspfProcessRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfProcessRpc.Input']['meta_info']
_meta_table['ActOspfProcessRpc.Input']['meta_info'].parent =_meta_table['ActOspfProcessRpc']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.All']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input.Instance']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc.Input']['meta_info']
_meta_table['ActOspfInstanceVrfRpc.Input']['meta_info'].parent =_meta_table['ActOspfInstanceVrfRpc']['meta_info']
