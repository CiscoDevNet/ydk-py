


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MdtInternalPathStatusEnum' : _MetaInfoEnum('MdtInternalPathStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper',
        {
            'active':'active',
            'internal-err':'internal_err',
            'plugin-active':'plugin_active',
            'plugin-not-initialized':'plugin_not_initialized',
            'plugin-invalid-cadence':'plugin_invalid_cadence',
            'plugin-err':'plugin_err',
            'filter-err':'filter_err',
        }, 'Cisco-IOS-XR-telemetry-model-driven-oper', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper']),
    'MdtTransportEnumEnum' : _MetaInfoEnum('MdtTransportEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper',
        {
            'not-set':'not_set',
            'grpc':'grpc',
            'tcp':'tcp',
            'udp':'udp',
            'dialin':'dialin',
        }, 'Cisco-IOS-XR-telemetry-model-driven-oper', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper']),
    'MdtIpEnum' : _MetaInfoEnum('MdtIpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-telemetry-model-driven-oper', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper']),
    'MdtEncodingEnumEnum' : _MetaInfoEnum('MdtEncodingEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper',
        {
            'not-set':'not_set',
            'gpb':'gpb',
            'self-describing-gpb':'self_describing_gpb',
            'json':'json',
        }, 'Cisco-IOS-XR-telemetry-model-driven-oper', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper']),
    'TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress',
            False, 
            [
            _MetaInfoClassMember('ip-type', REFERENCE_ENUM_CLASS, 'MdtIpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtIpEnum', 
                [], [], 
                '''                IPType
                ''',
                'ip_type',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'dest-ip-address',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations.Destination.Destination_.Destination__' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination.Destination_.Destination__',
            False, 
            [
            _MetaInfoClassMember('dest-ip-address', REFERENCE_CLASS, 'DestIpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress', 
                [], [], 
                '''                Destination IP Address
                ''',
                'dest_ip_address',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('dest-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Destination Port number
                ''',
                'dest_port',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MdtEncodingEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnumEnum', 
                [], [], 
                '''                Destination group encoding
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Id
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('last-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of the last collection
                ''',
                'last_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of streaming on this destination
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sub-id', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Sub Id
                ''',
                'sub_id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sub-id-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sub Idstr
                ''',
                'sub_id_str',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('tls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TLS connection to this destination
                ''',
                'tls',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('tls-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TLS Hostname of this destination
                ''',
                'tls_host',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-num-of-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes sent for this destination
                ''',
                'total_num_of_bytes_sent',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-num-of-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent for this
                destination
                ''',
                'total_num_of_packets_sent',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('transport', REFERENCE_ENUM_CLASS, 'MdtTransportEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtTransportEnumEnum', 
                [], [], 
                '''                Destination group transport
                ''',
                'transport',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Path
                ''',
                'path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State, if sensor path is resolved or not
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('status-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error str, if there are any errors resolving the
                sensor path
                ''',
                'status_str',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'collection-path',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup',
            False, 
            [
            _MetaInfoClassMember('avg-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average time for a collection (ms)
                ''',
                'avg_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('cadence', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Period of the collections (ms)
                ''',
                'cadence',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('collection-method', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Collection method in use
                ''',
                'collection_method',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('max-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum time for a collection (ms)
                ''',
                'max_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('min-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Minimum time for a collection (ms)
                ''',
                'min_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sysdb Path
                ''',
                'path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'MdtInternalPathStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtInternalPathStatusEnum', 
                [], [], 
                '''                Status of collection path
                ''',
                'status',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-collections', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Completed collections count
                ''',
                'total_collections',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-collections-missed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of collections missed
                ''',
                'total_collections_missed',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-datalist-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of datalists
                ''',
                'total_datalist_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-datalist-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of datalist errors
                ''',
                'total_datalist_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-encode-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of encode errors
                ''',
                'total_encode_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-encode-notready', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of encode deferred
                ''',
                'total_encode_notready',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-finddata-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of finddata
                ''',
                'total_finddata_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-finddata-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of finddata errors
                ''',
                'total_finddata_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-bulk-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of get bulk
                ''',
                'total_get_bulk_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-bulk-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of get bulk errors
                ''',
                'total_get_bulk_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of gets
                ''',
                'total_get_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of get errors
                ''',
                'total_get_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-item-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of items retrived from sysdb
                ''',
                'total_item_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-list-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of lists
                ''',
                'total_list_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-list-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of list errors
                ''',
                'total_list_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of send bytes dropped
                ''',
                'total_send_bytes_dropped',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of send channel full
                ''',
                'total_send_drops',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of send errors
                ''',
                'total_send_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent
                ''',
                'total_send_packets',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-sent-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes sent
                ''',
                'total_sent_bytes',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'internal-collection-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup',
            False, 
            [
            _MetaInfoClassMember('avg-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average time for all processing (ms)
                ''',
                'avg_total_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('cadence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Period of the collections (ms)
                ''',
                'cadence',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('collection-path', REFERENCE_LIST, 'CollectionPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath', 
                [], [], 
                '''                Array of information for sensor paths within
                collection group
                ''',
                'collection_path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MdtEncodingEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnumEnum', 
                [], [], 
                '''                Destination group encoding
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Collection Group id
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('internal-collection-group', REFERENCE_LIST, 'InternalCollectionGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup', 
                [], [], 
                '''                Array of information for sysdb paths within
                collection group
                ''',
                'internal_collection_group',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('last-collection-end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of the end of last collection
                ''',
                'last_collection_end_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('last-collection-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of the start of last collection
                ''',
                'last_collection_start_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('max-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum time for a collection (ms)
                ''',
                'max_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('max-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum time for all processing (ms)
                ''',
                'max_total_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('min-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum time for a collection (ms)
                ''',
                'min_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('min-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum time for all processing (ms)
                ''',
                'min_total_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-collections', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed collections count
                ''',
                'total_collections',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-not-ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number skipped (not ready)
                ''',
                'total_not_ready',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-other-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of errors
                ''',
                'total_other_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of send drops
                ''',
                'total_send_drops',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of send errors
                ''',
                'total_send_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'collection-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations.Destination.Destination_' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination.Destination_',
            False, 
            [
            _MetaInfoClassMember('collection-group', REFERENCE_LIST, 'CollectionGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup', 
                [], [], 
                '''                List of collection groups for this destination
                group
                ''',
                'collection_group',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination__' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination.Destination_.Destination__', 
                [], [], 
                '''                Destination
                ''',
                'destination',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations.Destination' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations.Destination',
            False, 
            [
            _MetaInfoClassMember('destination-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Id of the destination
                ''',
                'destination_id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', True),
            _MetaInfoClassMember('configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set if this is configured destination group
                ''',
                'configured',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination.Destination_', 
                [], [], 
                '''                list of destinations defined in this group
                ''',
                'destination',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Group name
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Destinations' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Destinations',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations.Destination', 
                [], [], 
                '''                Telemetry Destination
                ''',
                'destination',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'destinations',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Path
                ''',
                'path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State, if sensor path is resolved or not
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('status-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error str, if there are any errors resolving the
                sensor path
                ''',
                'status_str',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'sensor-path',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup',
            False, 
            [
            _MetaInfoClassMember('configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set if this is configured sensor group
                ''',
                'configured',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Group name
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sensor-path', REFERENCE_LIST, 'SensorPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath', 
                [], [], 
                '''                Array of information for sensor paths within
                sensor group
                ''',
                'sensor_path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'sensor-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile',
            False, 
            [
            _MetaInfoClassMember('heartbeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Heartbeat interval for the sensor group (s)
                ''',
                'heartbeat_interval',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sample interval for the sensor group (ms)
                ''',
                'sample_interval',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sensor-group', REFERENCE_CLASS, 'SensorGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup', 
                [], [], 
                '''                sensor group
                ''',
                'sensor_group',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('suppress-redundant', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress Redundant
                ''',
                'suppress_redundant',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'sensor-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress',
            False, 
            [
            _MetaInfoClassMember('ip-type', REFERENCE_ENUM_CLASS, 'MdtIpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtIpEnum', 
                [], [], 
                '''                IPType
                ''',
                'ip_type',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'dest-ip-address',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination',
            False, 
            [
            _MetaInfoClassMember('dest-ip-address', REFERENCE_CLASS, 'DestIpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress', 
                [], [], 
                '''                Destination IP Address
                ''',
                'dest_ip_address',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('dest-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Destination Port number
                ''',
                'dest_port',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MdtEncodingEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnumEnum', 
                [], [], 
                '''                Destination group encoding
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Id
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('last-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of the last collection
                ''',
                'last_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of streaming on this destination
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sub-id', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Sub Id
                ''',
                'sub_id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sub-id-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sub Idstr
                ''',
                'sub_id_str',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('tls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TLS connection to this destination
                ''',
                'tls',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('tls-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TLS Hostname of this destination
                ''',
                'tls_host',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-num-of-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes sent for this destination
                ''',
                'total_num_of_bytes_sent',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-num-of-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent for this
                destination
                ''',
                'total_num_of_packets_sent',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('transport', REFERENCE_ENUM_CLASS, 'MdtTransportEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtTransportEnumEnum', 
                [], [], 
                '''                Destination group transport
                ''',
                'transport',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp',
            False, 
            [
            _MetaInfoClassMember('configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set if this is configured destination group
                ''',
                'configured',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination', 
                [], [], 
                '''                list of destinations defined in this group
                ''',
                'destination',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Group name
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'destination-grp',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.Subscription_' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.Subscription_',
            False, 
            [
            _MetaInfoClassMember('destination-grp', REFERENCE_LIST, 'DestinationGrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp', 
                [], [], 
                '''                Array of destinations within a subscription
                ''',
                'destination_grp',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Collection Subscription name
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sensor-profile', REFERENCE_LIST, 'SensorProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile', 
                [], [], 
                '''                List of sensor groups within a subscription
                ''',
                'sensor_profile',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Subscription state
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'subscription',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Path
                ''',
                'path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State, if sensor path is resolved or not
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('status-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error str, if there are any errors resolving the
                sensor path
                ''',
                'status_str',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'collection-path',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup',
            False, 
            [
            _MetaInfoClassMember('avg-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average time for a collection (ms)
                ''',
                'avg_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('cadence', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Period of the collections (ms)
                ''',
                'cadence',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('collection-method', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Collection method in use
                ''',
                'collection_method',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('max-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum time for a collection (ms)
                ''',
                'max_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('min-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Minimum time for a collection (ms)
                ''',
                'min_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sysdb Path
                ''',
                'path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'MdtInternalPathStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtInternalPathStatusEnum', 
                [], [], 
                '''                Status of collection path
                ''',
                'status',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-collections', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Completed collections count
                ''',
                'total_collections',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-collections-missed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of collections missed
                ''',
                'total_collections_missed',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-datalist-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of datalists
                ''',
                'total_datalist_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-datalist-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of datalist errors
                ''',
                'total_datalist_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-encode-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of encode errors
                ''',
                'total_encode_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-encode-notready', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of encode deferred
                ''',
                'total_encode_notready',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-finddata-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of finddata
                ''',
                'total_finddata_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-finddata-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of finddata errors
                ''',
                'total_finddata_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-bulk-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of get bulk
                ''',
                'total_get_bulk_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-bulk-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of get bulk errors
                ''',
                'total_get_bulk_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of gets
                ''',
                'total_get_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-get-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of get errors
                ''',
                'total_get_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-item-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of items retrived from sysdb
                ''',
                'total_item_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-list-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of lists
                ''',
                'total_list_count',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-list-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of list errors
                ''',
                'total_list_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of send bytes dropped
                ''',
                'total_send_bytes_dropped',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of send channel full
                ''',
                'total_send_drops',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of send errors
                ''',
                'total_send_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent
                ''',
                'total_send_packets',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-sent-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes sent
                ''',
                'total_sent_bytes',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'internal-collection-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup',
            False, 
            [
            _MetaInfoClassMember('avg-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average time for all processing (ms)
                ''',
                'avg_total_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('cadence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Period of the collections (ms)
                ''',
                'cadence',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('collection-path', REFERENCE_LIST, 'CollectionPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath', 
                [], [], 
                '''                Array of information for sensor paths within
                collection group
                ''',
                'collection_path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MdtEncodingEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnumEnum', 
                [], [], 
                '''                Destination group encoding
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Collection Group id
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('internal-collection-group', REFERENCE_LIST, 'InternalCollectionGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup', 
                [], [], 
                '''                Array of information for sysdb paths within
                collection group
                ''',
                'internal_collection_group',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('last-collection-end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of the end of last collection
                ''',
                'last_collection_end_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('last-collection-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of the start of last collection
                ''',
                'last_collection_start_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('max-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum time for a collection (ms)
                ''',
                'max_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('max-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum time for all processing (ms)
                ''',
                'max_total_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('min-collection-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum time for a collection (ms)
                ''',
                'min_collection_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('min-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum time for all processing (ms)
                ''',
                'min_total_time',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-collections', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed collections count
                ''',
                'total_collections',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-not-ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number skipped (not ready)
                ''',
                'total_not_ready',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-other-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of errors
                ''',
                'total_other_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of send drops
                ''',
                'total_send_drops',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-send-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of send errors
                ''',
                'total_send_errors',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'collection-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription',
            False, 
            [
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Id of the subscription
                ''',
                'subscription_id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', True),
            _MetaInfoClassMember('collection-group', REFERENCE_LIST, 'CollectionGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup', 
                [], [], 
                '''                List of collection groups active for this
                subscription
                ''',
                'collection_group',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('subscription', REFERENCE_CLASS, 'Subscription_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription.Subscription_', 
                [], [], 
                '''                Subscription
                ''',
                'subscription',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-num-of-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes sent for this subscription
                ''',
                'total_num_of_bytes_sent',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('total-num-of-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent for this
                subscription
                ''',
                'total_num_of_packets_sent',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'subscription',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.Subscriptions' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions.Subscription', 
                [], [], 
                '''                Telemetry Subscription
                ''',
                'subscription',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'subscriptions',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Path
                ''',
                'path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State, if sensor path is resolved or not
                ''',
                'state',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('status-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error str, if there are any errors resolving the
                sensor path
                ''',
                'status_str',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'sensor-path',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.SensorGroups.SensorGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup',
            False, 
            [
            _MetaInfoClassMember('sensor-group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Id of the sensor group
                ''',
                'sensor_group_id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', True),
            _MetaInfoClassMember('configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set if this is configured sensor group
                ''',
                'configured',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Group name
                ''',
                'id',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sensor-path', REFERENCE_LIST, 'SensorPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath', 
                [], [], 
                '''                Array of information for sensor paths within
                sensor group
                ''',
                'sensor_path',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'sensor-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven.SensorGroups' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups',
            False, 
            [
            _MetaInfoClassMember('sensor-group', REFERENCE_LIST, 'SensorGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.SensorGroups.SensorGroup', 
                [], [], 
                '''                Telemetry Sensor Groups
                ''',
                'sensor_group',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'sensor-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
    'TelemetryModelDriven' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven',
            False, 
            [
            _MetaInfoClassMember('destinations', REFERENCE_CLASS, 'Destinations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Destinations', 
                [], [], 
                '''                Telemetry Destinations
                ''',
                'destinations',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('sensor-groups', REFERENCE_CLASS, 'SensorGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.SensorGroups', 
                [], [], 
                '''                Telemetry Sensor Groups
                ''',
                'sensor_groups',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            _MetaInfoClassMember('subscriptions', REFERENCE_CLASS, 'Subscriptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'TelemetryModelDriven.Subscriptions', 
                [], [], 
                '''                Telemetry Subscriptions
                ''',
                'subscriptions',
                'Cisco-IOS-XR-telemetry-model-driven-oper', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-oper',
            'telemetry-model-driven',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper'
        ),
    },
}
_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.Destination__']['meta_info']
_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup']['meta_info']
_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup']['meta_info']
_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.Destination__']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_']['meta_info']
_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_']['meta_info']
_meta_table['TelemetryModelDriven.Destinations.Destination.Destination_']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations.Destination']['meta_info']
_meta_table['TelemetryModelDriven.Destinations.Destination']['meta_info'].parent =_meta_table['TelemetryModelDriven.Destinations']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups']['meta_info']
_meta_table['TelemetryModelDriven.Destinations']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
