


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ClearIsisProcessRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ClearIsisProcessRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IS-IS process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisProcessRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearIsisProcessRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisProcessRpc.Input.Instance', 
                [], [], 
                '''                Clear data from single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('process', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear all IS-IS data structures
                ''',
                'process',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisProcessRpc' : {
        'meta_info' : _MetaInfoClass('ClearIsisProcessRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisProcessRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'clear-isis-process',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisRouteRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ClearIsisRouteRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IS-IS process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisRouteRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearIsisRouteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisRouteRpc.Input.Instance', 
                [], [], 
                '''                Clear data from single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear IS-IS routes
                ''',
                'route',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisRouteRpc' : {
        'meta_info' : _MetaInfoClass('ClearIsisRouteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisRouteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'clear-isis-route',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisStatRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ClearIsisStatRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IS-IS process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisStatRpc.Input.Statistics' : {
        'meta_info' : _MetaInfoClass('ClearIsisStatRpc.Input.Statistics',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisStatRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearIsisStatRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisStatRpc.Input.Instance', 
                [], [], 
                '''                Clear data from single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisStatRpc.Input.Statistics', 
                [], [], 
                '''                Clear IS-IS protocol statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisStatRpc' : {
        'meta_info' : _MetaInfoClass('ClearIsisStatRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisStatRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'clear-isis-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisDistRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ClearIsisDistRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IS-IS process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisDistRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearIsisDistRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisDistRpc.Input.Instance', 
                [], [], 
                '''                Reset BGP-LS topology from single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('distribution', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset BGP-LS topology distribution
                ''',
                'distribution',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisDistRpc' : {
        'meta_info' : _MetaInfoClass('ClearIsisDistRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisDistRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'clear-isis-dist',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisRpc.Input.Instance' : {
        'meta_info' : _MetaInfoClass('ClearIsisRpc.Input.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IS-IS process instance identifier
                ''',
                'instance_identifier',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisRpc.Input.RtTypeEnum' : _MetaInfoEnum('RtTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act',
        {
            'AFI-ALL-MULTICAST':'AFI_ALL_MULTICAST',
            'AFI-ALL-SAFI-ALL':'AFI_ALL_SAFI_ALL',
            'AFI-ALL-UNICAST':'AFI_ALL_UNICAST',
            'IPv4-MULTICAST':'IPv4_MULTICAST',
            'IPv4-SAFI-ALL':'IPv4_SAFI_ALL',
            'IPv4-UNICAST':'IPv4_UNICAST',
            'IPv6-MULTICAST':'IPv6_MULTICAST',
            'IPv6-SAFI-ALL':'IPv6_SAFI_ALL',
            'IPv6-UNICAST':'IPv6_UNICAST',
        }, 'Cisco-IOS-XR-isis-act', _yang_ns._namespaces['Cisco-IOS-XR-isis-act']),
    'ClearIsisRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearIsisRpc.Input',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisRpc.Input.Instance', 
                [], [], 
                '''                Clear data from single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'RtTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisRpc.Input.RtTypeEnum', 
                [], [], 
                '''                Clear data for these route types
                ''',
                'rt_type',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear IS-IS routes
                ''',
                'route',
                'Cisco-IOS-XR-isis-act', False),
            _MetaInfoClassMember('topology', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Topology table information
                ''',
                'topology',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
    'ClearIsisRpc' : {
        'meta_info' : _MetaInfoClass('ClearIsisRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsisRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-isis-act', False),
            ],
            'Cisco-IOS-XR-isis-act',
            'clear-isis',
            _yang_ns._namespaces['Cisco-IOS-XR-isis-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act'
        ),
    },
}
_meta_table['ClearIsisProcessRpc.Input.Instance']['meta_info'].parent =_meta_table['ClearIsisProcessRpc.Input']['meta_info']
_meta_table['ClearIsisProcessRpc.Input']['meta_info'].parent =_meta_table['ClearIsisProcessRpc']['meta_info']
_meta_table['ClearIsisRouteRpc.Input.Instance']['meta_info'].parent =_meta_table['ClearIsisRouteRpc.Input']['meta_info']
_meta_table['ClearIsisRouteRpc.Input']['meta_info'].parent =_meta_table['ClearIsisRouteRpc']['meta_info']
_meta_table['ClearIsisStatRpc.Input.Instance']['meta_info'].parent =_meta_table['ClearIsisStatRpc.Input']['meta_info']
_meta_table['ClearIsisStatRpc.Input.Statistics']['meta_info'].parent =_meta_table['ClearIsisStatRpc.Input']['meta_info']
_meta_table['ClearIsisStatRpc.Input']['meta_info'].parent =_meta_table['ClearIsisStatRpc']['meta_info']
_meta_table['ClearIsisDistRpc.Input.Instance']['meta_info'].parent =_meta_table['ClearIsisDistRpc.Input']['meta_info']
_meta_table['ClearIsisDistRpc.Input']['meta_info'].parent =_meta_table['ClearIsisDistRpc']['meta_info']
_meta_table['ClearIsisRpc.Input.Instance']['meta_info'].parent =_meta_table['ClearIsisRpc.Input']['meta_info']
_meta_table['ClearIsisRpc.Input']['meta_info'].parent =_meta_table['ClearIsisRpc']['meta_info']
