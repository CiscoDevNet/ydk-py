


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DirectionIdentity' : {
        'meta_info' : _MetaInfoClass('DirectionIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'direction',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics',
            False, 
            [
            _MetaInfoClassMember('classified-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Number of total bytes which filtered 
                 to the classifier-entry
                ''',
                'classified_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('classified-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Number of total packets which filtered
                 to the classifier-entry
                ''',
                'classified_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('classified-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Rate of average data flow through the 
                 classifier-entry
                ''',
                'classified_rate',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'classifier-entry-statistics',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics',
            False, 
            [
            _MetaInfoClassMember('meter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Meter Identifier
                ''',
                'meter_id',
                'Cisco-IOS-XE-diffserv-target-oper', True),
            _MetaInfoClassMember('meter-failed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets which failed the meter
                ''',
                'meter_failed_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('meter-failed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets which failed the meter
                ''',
                'meter_failed_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('meter-succeed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets which succeed the meter
                ''',
                'meter_succeed_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('meter-succeed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets which succeed the meter
                ''',
                'meter_succeed_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'meter-statistics',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats',
            False, 
            [
            _MetaInfoClassMember('early-drop-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Early drop bytes 
                ''',
                'early_drop_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('early-drop-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Early drop packets 
                ''',
                'early_drop_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'wred-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics',
            False, 
            [
            _MetaInfoClassMember('drop-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes dropped 
                ''',
                'drop_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('drop-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets dropped 
                ''',
                'drop_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('output-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes transmitted from queue 
                ''',
                'output_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('output-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets transmitted from queue 
                ''',
                'output_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('queue-size-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes currently buffered 
                ''',
                'queue_size_bytes',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('queue-size-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets currently buffered 
                ''',
                'queue_size_pkts',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('wred-stats', REFERENCE_CLASS, 'WredStats' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats', 
                [], [], 
                '''                Container for WRED statistics
                ''',
                'wred_stats',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'queuing-statistics',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics',
            False, 
            [
            _MetaInfoClassMember('classifier-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Classifier Entry Name
                ''',
                'classifier_entry_name',
                'Cisco-IOS-XE-diffserv-target-oper', True),
            _MetaInfoClassMember('parent-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path of the Classifier Entry in a hierarchial policy 
                ''',
                'parent_path',
                'Cisco-IOS-XE-diffserv-target-oper', True),
            _MetaInfoClassMember('classifier-entry-statistics', REFERENCE_CLASS, 'ClassifierEntryStatistics' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics', 
                [], [], 
                '''                
                This group defines the classifier filter statistics of 
                each classifier entry
                       
                
                ''',
                'classifier_entry_statistics',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('meter-statistics', REFERENCE_LIST, 'MeterStatistics' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics', 
                [], [], 
                '''                Meter statistics
                ''',
                'meter_statistics',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            _MetaInfoClassMember('queuing-statistics', REFERENCE_CLASS, 'QueuingStatistics' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics', 
                [], [], 
                '''                queue related statistics 
                ''',
                'queuing_statistics',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'diffserv-target-classifier-statistics',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface.DiffservTargetEntry',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_IDENTITY_CLASS, 'DirectionIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DirectionIdentity', 
                [], [], 
                '''                Direction fo the traffic flow either inbound or outbound
                ''',
                'direction',
                'Cisco-IOS-XE-diffserv-target-oper', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy entry name
                ''',
                'policy_name',
                'Cisco-IOS-XE-diffserv-target-oper', True),
            _MetaInfoClassMember('diffserv-target-classifier-statistics', REFERENCE_LIST, 'DiffservTargetClassifierStatistics' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics', 
                [], [], 
                '''                Statistics for each Classifier Entry in a Policy
                ''',
                'diffserv_target_classifier_statistics',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'diffserv-target-entry',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState.DiffservInterface' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState.DiffservInterface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'name',
                'Cisco-IOS-XE-diffserv-target-oper', True),
            _MetaInfoClassMember('diffserv-target-entry', REFERENCE_LIST, 'DiffservTargetEntry' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface.DiffservTargetEntry', 
                [], [], 
                '''                policy target for inbound or outbound direction
                ''',
                'diffserv_target_entry',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'diffserv-interface',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'DiffservInterfacesState' : {
        'meta_info' : _MetaInfoClass('DiffservInterfacesState',
            False, 
            [
            _MetaInfoClassMember('diffserv-interface', REFERENCE_LIST, 'DiffservInterface' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper', 'DiffservInterfacesState.DiffservInterface', 
                [], [], 
                '''                The list of configured interfaces on the device.
                ''',
                'diffserv_interface',
                'Cisco-IOS-XE-diffserv-target-oper', False),
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'diffserv-interfaces-state',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'InboundIdentity' : {
        'meta_info' : _MetaInfoClass('InboundIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
    'OutboundIdentity' : {
        'meta_info' : _MetaInfoClass('OutboundIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-diffserv-target-oper',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XE-diffserv-target-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper'
        ),
    },
}
_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats']['meta_info'].parent =_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics']['meta_info']
_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics']['meta_info'].parent =_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']
_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics']['meta_info'].parent =_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']
_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics']['meta_info'].parent =_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']
_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info'].parent =_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry']['meta_info']
_meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry']['meta_info'].parent =_meta_table['DiffservInterfacesState.DiffservInterface']['meta_info']
_meta_table['DiffservInterfacesState.DiffservInterface']['meta_info'].parent =_meta_table['DiffservInterfacesState']['meta_info']
