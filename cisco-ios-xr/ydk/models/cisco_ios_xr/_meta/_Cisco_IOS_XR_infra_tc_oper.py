


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TcOperAfNameEnum' : _MetaInfoEnum('TcOperAfNameEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-infra-tc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper']),
    'TrafficCollector.ExternalInterfaces.ExternalInterface' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.ExternalInterfaces.ExternalInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-tc-oper', True),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name in Display format
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-interface-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate interface enabled or not
                ''',
                'is_interface_enabled',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('vrfid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface VRF ID
                ''',
                'vrfid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'external-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.ExternalInterfaces' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.ExternalInterfaces',
            False, 
            [
            _MetaInfoClassMember('external-interface', REFERENCE_LIST, 'ExternalInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.ExternalInterfaces.ExternalInterface', 
                [], [], 
                '''                External Interface 
                ''',
                'external_interface',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'external-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary.DatabaseStatisticsExternalInterface' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary.DatabaseStatisticsExternalInterface',
            False, 
            [
            _MetaInfoClassMember('number-of-add-o-perations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of add operations
                ''',
                'number_of_add_o_perations',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-delete-o-perations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of delete operations
                ''',
                'number_of_delete_o_perations',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DB entries
                ''',
                'number_of_entries',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of stale  entries
                ''',
                'number_of_stale_entries',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'database-statistics-external-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4',
            False, 
            [
            _MetaInfoClassMember('number-of-add-o-perations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of add operations
                ''',
                'number_of_add_o_perations',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-delete-o-perations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of delete operations
                ''',
                'number_of_delete_o_perations',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DB entries
                ''',
                'number_of_entries',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of stale  entries
                ''',
                'number_of_stale_entries',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'database-statistics-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel',
            False, 
            [
            _MetaInfoClassMember('number-of-add-o-perations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of add operations
                ''',
                'number_of_add_o_perations',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-delete-o-perations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of delete operations
                ''',
                'number_of_delete_o_perations',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DB entries
                ''',
                'number_of_entries',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('number-of-stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of stale  entries
                ''',
                'number_of_stale_entries',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'database-statistics-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary.VrfStatistic' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary.VrfStatistic',
            False, 
            [
            _MetaInfoClassMember('database-statistics-ipv4', REFERENCE_CLASS, 'DatabaseStatisticsIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4', 
                [], [], 
                '''                Database statistics for IPv4 table
                ''',
                'database_statistics_ipv4',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('database-statistics-tunnel', REFERENCE_CLASS, 'DatabaseStatisticsTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel', 
                [], [], 
                '''                Database statistics for Tunnel table
                ''',
                'database_statistics_tunnel',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'vrf-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary.CollectionMessageStatistic' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary.CollectionMessageStatistic',
            False, 
            [
            _MetaInfoClassMember('byte-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes received
                ''',
                'byte_received',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('byte-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes sent
                ''',
                'byte_sent',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('maimum-latency-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of maximum latency
                ''',
                'maimum_latency_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('maximum-roundtrip-latency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum roundtrip latency in msec
                ''',
                'maximum_roundtrip_latency',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('packet-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets received
                ''',
                'packet_received',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('packet-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets sent
                ''',
                'packet_sent',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'collection-message-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary.CheckpointMessageStatistic' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary.CheckpointMessageStatistic',
            False, 
            [
            _MetaInfoClassMember('byte-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes received
                ''',
                'byte_received',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('byte-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes sent
                ''',
                'byte_sent',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('maimum-latency-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of maximum latency
                ''',
                'maimum_latency_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('maximum-roundtrip-latency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum roundtrip latency in msec
                ''',
                'maximum_roundtrip_latency',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('packet-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets received
                ''',
                'packet_received',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('packet-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets sent
                ''',
                'packet_sent',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'checkpoint-message-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Summary' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Summary',
            False, 
            [
            _MetaInfoClassMember('checkpoint-message-statistic', REFERENCE_LIST, 'CheckpointMessageStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary.CheckpointMessageStatistic', 
                [], [], 
                '''                Statistics per message type for Chkpt
                ''',
                'checkpoint_message_statistic',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('collection-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Statistic collection interval in minutes
                ''',
                'collection_interval',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('collection-message-statistic', REFERENCE_LIST, 'CollectionMessageStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary.CollectionMessageStatistic', 
                [], [], 
                '''                Statistics per message type for STAT collector
                ''',
                'collection_message_statistic',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('collection-timer-is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if collection timer is running
                ''',
                'collection_timer_is_running',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('database-statistics-external-interface', REFERENCE_CLASS, 'DatabaseStatisticsExternalInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary.DatabaseStatisticsExternalInterface', 
                [], [], 
                '''                Database statistics for External Interface
                ''',
                'database_statistics_external_interface',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('history-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Statistics history size
                ''',
                'history_size',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('timeout-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Statistic history timeout interval in hours
                ''',
                'timeout_interval',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('timeout-timer-is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if history timeout timer is running
                ''',
                'timeout_timer_is_running',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('vrf-statistic', REFERENCE_LIST, 'VrfStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary.VrfStatistic', 
                [], [], 
                '''                VRF table statistics
                ''',
                'vrf_statistic',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory',
            False, 
            [
            _MetaInfoClassMember('event-end-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event End timestamp
                ''',
                'event_end_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('event-start-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event Start timestamp
                ''',
                'event_start_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate if this history entry is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched in this interval
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched in this interval
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'count-history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics',
            False, 
            [
            _MetaInfoClassMember('count-history', REFERENCE_LIST, 'CountHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory', 
                [], [], 
                '''                Counter History
                ''',
                'count_history',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-bytes-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Bytes/second switched
                ''',
                'transmit_bytes_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-packets-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Packets/second switched
                ''',
                'transmit_packets_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'base-counter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory',
            False, 
            [
            _MetaInfoClassMember('event-end-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event End timestamp
                ''',
                'event_end_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('event-start-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event Start timestamp
                ''',
                'event_start_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate if this history entry is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched in this interval
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched in this interval
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'count-history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics',
            False, 
            [
            _MetaInfoClassMember('count-history', REFERENCE_LIST, 'CountHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory', 
                [], [], 
                '''                Counter History
                ''',
                'count_history',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-bytes-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Bytes/second switched
                ''',
                'transmit_bytes_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-packets-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Packets/second switched
                ''',
                'transmit_packets_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'traffic-matrix-counter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('base-counter-statistics', REFERENCE_CLASS, 'BaseCounterStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics', 
                [], [], 
                '''                Base counter statistics
                ''',
                'base_counter_statistics',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('ipaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP Address
                ''',
                'ipaddr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is Active and collecting new Statistics
                ''',
                'is_active',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'label',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'label_xr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Prefix Mask
                ''',
                'mask',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix Address (V4 or V6 Format)
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('traffic-matrix-counter-statistics', REFERENCE_CLASS, 'TrafficMatrixCounterStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics', 
                [], [], 
                '''                Traffic Matrix (TM) counter statistics
                ''',
                'traffic_matrix_counter_statistics',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix', 
                [], [], 
                '''                Show Prefix Counter
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory',
            False, 
            [
            _MetaInfoClassMember('event-end-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event End timestamp
                ''',
                'event_end_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('event-start-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event Start timestamp
                ''',
                'event_start_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate if this history entry is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched in this interval
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched in this interval
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'count-history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics',
            False, 
            [
            _MetaInfoClassMember('count-history', REFERENCE_LIST, 'CountHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory', 
                [], [], 
                '''                Counter History
                ''',
                'count_history',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-bytes-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Bytes/second switched
                ''',
                'transmit_bytes_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-packets-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Packets/second switched
                ''',
                'transmit_packets_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'base-counter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-tc-oper', True),
            _MetaInfoClassMember('base-counter-statistics', REFERENCE_CLASS, 'BaseCounterStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics', 
                [], [], 
                '''                Base counter statistics
                ''',
                'base_counter_statistics',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name in Display format
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface is Active and collecting new
                Statistics
                ''',
                'is_active',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('vrfid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface VRF ID
                ''',
                'vrfid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels',
            False, 
            [
            _MetaInfoClassMember('tunnel', REFERENCE_LIST, 'Tunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel', 
                [], [], 
                '''                Tunnel information
                ''',
                'tunnel',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters',
            False, 
            [
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes', 
                [], [], 
                '''                Prefix Database
                ''',
                'prefixes',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('tunnels', REFERENCE_CLASS, 'Tunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels', 
                [], [], 
                '''                Tunnels
                ''',
                'tunnels',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'counters',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcOperAfNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TcOperAfNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-tc-oper', True),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters', 
                [], [], 
                '''                Show Counters
                ''',
                'counters',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf.Afs' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs.Af', 
                [], [], 
                '''                Operational data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf.Afs', 
                [], [], 
                '''                Address Family specific operational data
                ''',
                'afs',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.VrfTable' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.VrfTable',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable.DefaultVrf', 
                [], [], 
                '''                DefaultVRF specific operational data
                ''',
                'default_vrf',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'vrf-table',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory',
            False, 
            [
            _MetaInfoClassMember('event-end-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event End timestamp
                ''',
                'event_end_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('event-start-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event Start timestamp
                ''',
                'event_start_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate if this history entry is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched in this interval
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched in this interval
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'count-history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics',
            False, 
            [
            _MetaInfoClassMember('count-history', REFERENCE_LIST, 'CountHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory', 
                [], [], 
                '''                Counter History
                ''',
                'count_history',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-bytes-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Bytes/second switched
                ''',
                'transmit_bytes_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-packets-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Packets/second switched
                ''',
                'transmit_packets_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'base-counter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory',
            False, 
            [
            _MetaInfoClassMember('event-end-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event End timestamp
                ''',
                'event_end_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('event-start-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event Start timestamp
                ''',
                'event_start_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate if this history entry is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched in this interval
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched in this interval
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'count-history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics',
            False, 
            [
            _MetaInfoClassMember('count-history', REFERENCE_LIST, 'CountHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory', 
                [], [], 
                '''                Counter History
                ''',
                'count_history',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-bytes-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Bytes/second switched
                ''',
                'transmit_bytes_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-packets-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Packets/second switched
                ''',
                'transmit_packets_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'traffic-matrix-counter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Prefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('base-counter-statistics', REFERENCE_CLASS, 'BaseCounterStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics', 
                [], [], 
                '''                Base counter statistics
                ''',
                'base_counter_statistics',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('ipaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP Address
                ''',
                'ipaddr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is Active and collecting new Statistics
                ''',
                'is_active',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'label',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('label-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'label_xr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Prefix Mask
                ''',
                'mask',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix Address (V4 or V6 Format)
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('traffic-matrix-counter-statistics', REFERENCE_CLASS, 'TrafficMatrixCounterStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics', 
                [], [], 
                '''                Traffic Matrix (TM) counter statistics
                ''',
                'traffic_matrix_counter_statistics',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Prefixes' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Prefixes',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Prefixes.Prefix', 
                [], [], 
                '''                Show Prefix Counter
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory',
            False, 
            [
            _MetaInfoClassMember('event-end-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event End timestamp
                ''',
                'event_end_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('event-start-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Event Start timestamp
                ''',
                'event_start_timestamp',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate if this history entry is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched in this interval
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched in this interval
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'count-history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics',
            False, 
            [
            _MetaInfoClassMember('count-history', REFERENCE_LIST, 'CountHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory', 
                [], [], 
                '''                Counter History
                ''',
                'count_history',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-bytes-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Bytes/second switched
                ''',
                'transmit_bytes_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('transmit-packets-per-second-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Rate of Packets/second switched
                ''',
                'transmit_packets_per_second_switched',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'base-counter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-tc-oper', True),
            _MetaInfoClassMember('base-counter-statistics', REFERENCE_CLASS, 'BaseCounterStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics', 
                [], [], 
                '''                Base counter statistics
                ''',
                'base_counter_statistics',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name in Display format
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('is-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface is Active and collecting new
                Statistics
                ''',
                'is_active',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('vrfid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface VRF ID
                ''',
                'vrfid',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters.Tunnels' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters.Tunnels',
            False, 
            [
            _MetaInfoClassMember('tunnel', REFERENCE_LIST, 'Tunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel', 
                [], [], 
                '''                Tunnel information
                ''',
                'tunnel',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af.Counters' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af.Counters',
            False, 
            [
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Prefixes', 
                [], [], 
                '''                Prefix Database
                ''',
                'prefixes',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('tunnels', REFERENCE_CLASS, 'Tunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters.Tunnels', 
                [], [], 
                '''                Tunnels
                ''',
                'tunnels',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'counters',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs.Af' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcOperAfNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TcOperAfNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-tc-oper', True),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af.Counters', 
                [], [], 
                '''                Show Counters
                ''',
                'counters',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector.Afs' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs.Af', 
                [], [], 
                '''                Operational data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
    'TrafficCollector' : {
        'meta_info' : _MetaInfoClass('TrafficCollector',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Afs', 
                [], [], 
                '''                Address Family specific operational data
                ''',
                'afs',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('external-interfaces', REFERENCE_CLASS, 'ExternalInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.ExternalInterfaces', 
                [], [], 
                '''                External Interface
                ''',
                'external_interfaces',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.Summary', 
                [], [], 
                '''                Traffic Collector summary
                ''',
                'summary',
                'Cisco-IOS-XR-infra-tc-oper', False),
            _MetaInfoClassMember('vrf-table', REFERENCE_CLASS, 'VrfTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TrafficCollector.VrfTable', 
                [], [], 
                '''                VRF specific operational data
                ''',
                'vrf_table',
                'Cisco-IOS-XR-infra-tc-oper', False),
            ],
            'Cisco-IOS-XR-infra-tc-oper',
            'traffic-collector',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-tc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper'
        ),
    },
}
_meta_table['TrafficCollector.ExternalInterfaces.ExternalInterface']['meta_info'].parent =_meta_table['TrafficCollector.ExternalInterfaces']['meta_info']
_meta_table['TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4']['meta_info'].parent =_meta_table['TrafficCollector.Summary.VrfStatistic']['meta_info']
_meta_table['TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel']['meta_info'].parent =_meta_table['TrafficCollector.Summary.VrfStatistic']['meta_info']
_meta_table['TrafficCollector.Summary.DatabaseStatisticsExternalInterface']['meta_info'].parent =_meta_table['TrafficCollector.Summary']['meta_info']
_meta_table['TrafficCollector.Summary.VrfStatistic']['meta_info'].parent =_meta_table['TrafficCollector.Summary']['meta_info']
_meta_table['TrafficCollector.Summary.CollectionMessageStatistic']['meta_info'].parent =_meta_table['TrafficCollector.Summary']['meta_info']
_meta_table['TrafficCollector.Summary.CheckpointMessageStatistic']['meta_info'].parent =_meta_table['TrafficCollector.Summary']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable.DefaultVrf']['meta_info']
_meta_table['TrafficCollector.VrfTable.DefaultVrf']['meta_info'].parent =_meta_table['TrafficCollector.VrfTable']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Prefixes']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters.Tunnels']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af.Counters']['meta_info']
_meta_table['TrafficCollector.Afs.Af.Counters']['meta_info'].parent =_meta_table['TrafficCollector.Afs.Af']['meta_info']
_meta_table['TrafficCollector.Afs.Af']['meta_info'].parent =_meta_table['TrafficCollector.Afs']['meta_info']
_meta_table['TrafficCollector.ExternalInterfaces']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
_meta_table['TrafficCollector.Summary']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
_meta_table['TrafficCollector.VrfTable']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
_meta_table['TrafficCollector.Afs']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
