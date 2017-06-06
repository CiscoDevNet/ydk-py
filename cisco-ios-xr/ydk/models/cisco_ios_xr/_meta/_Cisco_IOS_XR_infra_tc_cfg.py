


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HistoryTimeoutEnum' : _MetaInfoEnum('HistoryTimeoutEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        {
            'max':'max',
        }, 'Cisco-IOS-XR-infra-tc-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg']),
    'CollectIonIntervalEnum' : _MetaInfoEnum('CollectIonIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        {
            '1-minute':'Y_1_minute',
            '2-minutes':'Y_2_minutes',
            '3-minutes':'Y_3_minutes',
            '4-minutes':'Y_4_minutes',
            '5-minutes':'Y_5_minutes',
            '6-minutes':'Y_6_minutes',
            '10-minutes':'Y_10_minutes',
            '12-minutes':'Y_12_minutes',
            '15-minutes':'Y_15_minutes',
            '20-minutes':'Y_20_minutes',
            '30-minutes':'Y_30_minutes',
            '60-minutes':'Y_60_minutes',
        }, 'Cisco-IOS-XR-infra-tc-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg']),
    'HistorySizeEnum' : _MetaInfoEnum('HistorySizeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        {
            'max':'max',
        }, 'Cisco-IOS-XR-infra-tc-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg']),
    'TrafficCollector.ExternalInterfaces.ExternalInterface' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.ExternalInterfaces.ExternalInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-tc-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable traffic collector on this interface
                ''',
                'enable',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'external-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg'
        ),
    },
    'TrafficCollector.ExternalInterfaces' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.ExternalInterfaces',
            False, 
            [
            _MetaInfoClassMember('external-interface', REFERENCE_LIST, 'ExternalInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'TrafficCollector.ExternalInterfaces.ExternalInterface', 
                [], [], 
                '''                Configure an external internface
                ''',
                'external_interface',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'external-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg'
        ),
    },
    'TrafficCollector.Statistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Statistics',
            False, 
            [
            _MetaInfoClassMember('collection-interval', REFERENCE_ENUM_CLASS, 'CollectIonIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'CollectIonIntervalEnum', 
                [], [], 
                '''                Configure statistics collection interval
                ''',
                'collection_interval',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('enable-traffic-collector-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable traffic collector statistics
                ''',
                'enable_traffic_collector_statistics',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('history-size', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure statistics history size
                ''',
                'history_size',
                'Cisco-IOS-XR-infra-tc-cfg', False, [
                    _MetaInfoClassMember('history-size', REFERENCE_ENUM_CLASS, 'HistorySizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistorySizeEnum', 
                        [], [], 
                        '''                        Configure statistics history size
                        ''',
                        'history_size',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                    _MetaInfoClassMember('history-size', ATTRIBUTE, 'int' , None, None, 
                        [('1', '10')], [], 
                        '''                        Configure statistics history size
                        ''',
                        'history_size',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                ]),
            _MetaInfoClassMember('history-timeout', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure statistics history timeout interval
                ''',
                'history_timeout',
                'Cisco-IOS-XR-infra-tc-cfg', False, [
                    _MetaInfoClassMember('history-timeout', REFERENCE_ENUM_CLASS, 'HistoryTimeoutEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistoryTimeoutEnum', 
                        [], [], 
                        '''                        Configure statistics history timeout interval
                        ''',
                        'history_timeout',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                    _MetaInfoClassMember('history-timeout', ATTRIBUTE, 'int' , None, None, 
                        [('0', '720')], [], 
                        '''                        Configure statistics history timeout interval
                        ''',
                        'history_timeout',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg'
        ),
    },
    'TrafficCollector' : {
        'meta_info' : _MetaInfoClass('TrafficCollector',
            False, 
            [
            _MetaInfoClassMember('enable-traffic-collector', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable traffic collector
                ''',
                'enable_traffic_collector',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('external-interfaces', REFERENCE_CLASS, 'ExternalInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'TrafficCollector.ExternalInterfaces', 
                [], [], 
                '''                Configure external interfaces
                ''',
                'external_interfaces',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'TrafficCollector.Statistics', 
                [], [], 
                '''                Configure statistics related parameters
                ''',
                'statistics',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'traffic-collector',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg'
        ),
    },
}
_meta_table['TrafficCollector.ExternalInterfaces.ExternalInterface']['meta_info'].parent =_meta_table['TrafficCollector.ExternalInterfaces']['meta_info']
_meta_table['TrafficCollector.ExternalInterfaces']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
_meta_table['TrafficCollector.Statistics']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
