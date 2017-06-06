


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ActOspfv3RoutesRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfv3RoutesRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3RoutesRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfv3RoutesRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3RoutesRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPFv3 instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3RoutesRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfv3RoutesRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3RoutesRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'act-ospfv3-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3RedistributionRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfv3RedistributionRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3RedistributionRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfv3RedistributionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3RedistributionRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPFv3 instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 Route Redistribution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3RedistributionRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfv3RedistributionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3RedistributionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'act-ospfv3-redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3ProcessRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfv3ProcessRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3ProcessRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfv3ProcessRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3ProcessRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPFv3 instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPFv3 process
                ''',
                'process',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3ProcessRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfv3ProcessRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3ProcessRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'act-ospfv3-process',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsNeighborRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsNeighborRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsNeighborRpc.Input.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsNeighborRpc.Input.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsNeighborRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsNeighborRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3StatisticsNeighborRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPFv3 instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3StatisticsNeighborRpc.Input.Neighbor', 
                [], [], 
                '''                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsNeighborRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsNeighborRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3StatisticsNeighborRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'act-ospfv3-statistics-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3StatisticsRpc.Input.Instance', 
                [], [], 
                '''                Clear data from OSPFv3 instance
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('prefix-priority', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                All OSPFv3 counters and statistics
                ''',
                'prefix_priority',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Neighbor statistics per neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3StatisticsRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfv3StatisticsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3StatisticsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'act-ospfv3-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPFv3 interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats',
            False, 
            [
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('prefix-priority', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF Prefix Priority statistics
                ''',
                'prefix_priority',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor', 
                [], [], 
                '''                Neighbor statistics per interface or neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPFv3 process
                ''',
                'process',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route redistrbution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats', 
                [], [], 
                '''                OSPFv3 counters and statistics
                ''',
                'stats',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPFv3 interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats',
            False, 
            [
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('prefix-priority', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF Prefix Priority statistics
                ''',
                'prefix_priority',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor', 
                [], [], 
                '''                Neighbor statistics per interface or neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.All' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.All',
            False, 
            [
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPFv3 process
                ''',
                'process',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route redistrbution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats', 
                [], [], 
                '''                OSPFv3 counters and statistics
                ''',
                'stats',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OSPFv3 interface statistics
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID
                ''',
                'neighbor_id',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface', 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats',
            False, 
            [
            _MetaInfoClassMember('spf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF statistics
                ''',
                'spf',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('prefix-priority', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF Prefix Priority statistics
                ''',
                'prefix_priority',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor', 
                [], [], 
                '''                Neighbor statistics per interface or neighbor id
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive',
            False, 
            [
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset OSPFv3 process
                ''',
                'process',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('redistribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route redistrbution
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear OSPFv3 route table
                ''',
                'route',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats', 
                [], [], 
                '''                OSPFv3 counters and statistics
                ''',
                'stats',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'all-inclusive',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPFv3 process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('vrf', REFERENCE_CLASS, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.Vrf', 
                [], [], 
                '''                Clear one or more non-default OSPFv3 VRFs in process
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.All', 
                [], [], 
                '''                Clear all non-default OSPFv3 VRFs
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            _MetaInfoClassMember('all-inclusive', REFERENCE_CLASS, 'AllInclusive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive', 
                [], [], 
                '''                Clear all non-default and default OSPFv3 VRFs
                ''',
                'all_inclusive',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc.Input' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input.Instance', 
                [], [], 
                '''                OSPFv3 instance name
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
    'ActOspfv3InstanceVrfRpc' : {
        'meta_info' : _MetaInfoClass('ActOspfv3InstanceVrfRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act', 'ActOspfv3InstanceVrfRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ospfv3-act', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-act',
            'act-ospfv3-instance-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act'
        ),
    },
}
_meta_table['ActOspfv3RoutesRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfv3RoutesRpc.Input']['meta_info']
_meta_table['ActOspfv3RoutesRpc.Input']['meta_info'].parent =_meta_table['ActOspfv3RoutesRpc']['meta_info']
_meta_table['ActOspfv3RedistributionRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfv3RedistributionRpc.Input']['meta_info']
_meta_table['ActOspfv3RedistributionRpc.Input']['meta_info'].parent =_meta_table['ActOspfv3RedistributionRpc']['meta_info']
_meta_table['ActOspfv3ProcessRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfv3ProcessRpc.Input']['meta_info']
_meta_table['ActOspfv3ProcessRpc.Input']['meta_info'].parent =_meta_table['ActOspfv3ProcessRpc']['meta_info']
_meta_table['ActOspfv3StatisticsNeighborRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfv3StatisticsNeighborRpc.Input']['meta_info']
_meta_table['ActOspfv3StatisticsNeighborRpc.Input.Neighbor']['meta_info'].parent =_meta_table['ActOspfv3StatisticsNeighborRpc.Input']['meta_info']
_meta_table['ActOspfv3StatisticsNeighborRpc.Input']['meta_info'].parent =_meta_table['ActOspfv3StatisticsNeighborRpc']['meta_info']
_meta_table['ActOspfv3StatisticsRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfv3StatisticsRpc.Input']['meta_info']
_meta_table['ActOspfv3StatisticsRpc.Input']['meta_info'].parent =_meta_table['ActOspfv3StatisticsRpc']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input.Instance']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc.Input']['meta_info']
_meta_table['ActOspfv3InstanceVrfRpc.Input']['meta_info'].parent =_meta_table['ActOspfv3InstanceVrfRpc']['meta_info']
