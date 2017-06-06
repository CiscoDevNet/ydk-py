


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RestconfState.Capabilities' : {
        'meta_info' : _MetaInfoClass('RestconfState.Capabilities',
            False, 
            [
            _MetaInfoClassMember('capability', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                A RESTCONF protocol capability URI.
                ''',
                'capability',
                'ietf-restconf-monitoring', False),
            ],
            'ietf-restconf-monitoring',
            'capabilities',
            _yang_ns._namespaces['ietf-restconf-monitoring'],
        'ydk.models.ietf.ietf_restconf_monitoring'
        ),
    },
    'RestconfState.Streams.Stream.Access' : {
        'meta_info' : _MetaInfoClass('RestconfState.Streams.Stream.Access',
            False, 
            [
            _MetaInfoClassMember('encoding', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is the secondary encoding format within the
                'text/event-stream' encoding used by all streams.
                The type 'xml' is supported for XML encoding.
                The type 'json' is supported for JSON encoding.
                ''',
                'encoding',
                'ietf-restconf-monitoring', True),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Contains a URL that represents the entry point
                for establishing notification delivery via server
                sent events.
                ''',
                'location',
                'ietf-restconf-monitoring', False),
            ],
            'ietf-restconf-monitoring',
            'access',
            _yang_ns._namespaces['ietf-restconf-monitoring'],
        'ydk.models.ietf.ietf_restconf_monitoring'
        ),
    },
    'RestconfState.Streams.Stream' : {
        'meta_info' : _MetaInfoClass('RestconfState.Streams.Stream',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The stream name
                ''',
                'name',
                'ietf-restconf-monitoring', True),
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access' , 'ydk.models.ietf.ietf_restconf_monitoring', 'RestconfState.Streams.Stream.Access', 
                [], [], 
                '''                The server will create an entry in this list for each
                encoding format that is supported for this stream.
                The media type 'text/event-stream' is expected
                for all event streams. This list identifies the
                sub-types supported for this stream.
                ''',
                'access',
                'ietf-restconf-monitoring', False, min_elements=1),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of stream content
                ''',
                'description',
                'ietf-restconf-monitoring', False),
            _MetaInfoClassMember('replay-log-creation-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indicates the time the replay log for this stream
                was created.
                ''',
                'replay_log_creation_time',
                'ietf-restconf-monitoring', False),
            _MetaInfoClassMember('replay-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if replay buffer supported for this stream.
                If 'true', then the server MUST support the 'start-time'
                and 'stop-time' query parameters for this stream.
                ''',
                'replay_support',
                'ietf-restconf-monitoring', False),
            ],
            'ietf-restconf-monitoring',
            'stream',
            _yang_ns._namespaces['ietf-restconf-monitoring'],
        'ydk.models.ietf.ietf_restconf_monitoring'
        ),
    },
    'RestconfState.Streams' : {
        'meta_info' : _MetaInfoClass('RestconfState.Streams',
            False, 
            [
            _MetaInfoClassMember('stream', REFERENCE_LIST, 'Stream' , 'ydk.models.ietf.ietf_restconf_monitoring', 'RestconfState.Streams.Stream', 
                [], [], 
                '''                Each entry describes an event stream supported by
                the server.
                ''',
                'stream',
                'ietf-restconf-monitoring', False),
            ],
            'ietf-restconf-monitoring',
            'streams',
            _yang_ns._namespaces['ietf-restconf-monitoring'],
        'ydk.models.ietf.ietf_restconf_monitoring'
        ),
    },
    'RestconfState' : {
        'meta_info' : _MetaInfoClass('RestconfState',
            False, 
            [
            _MetaInfoClassMember('capabilities', REFERENCE_CLASS, 'Capabilities' , 'ydk.models.ietf.ietf_restconf_monitoring', 'RestconfState.Capabilities', 
                [], [], 
                '''                Contains a list of protocol capability URIs
                ''',
                'capabilities',
                'ietf-restconf-monitoring', False),
            _MetaInfoClassMember('streams', REFERENCE_CLASS, 'Streams' , 'ydk.models.ietf.ietf_restconf_monitoring', 'RestconfState.Streams', 
                [], [], 
                '''                Container representing the notification event streams
                supported by the server.
                ''',
                'streams',
                'ietf-restconf-monitoring', False),
            ],
            'ietf-restconf-monitoring',
            'restconf-state',
            _yang_ns._namespaces['ietf-restconf-monitoring'],
        'ydk.models.ietf.ietf_restconf_monitoring'
        ),
    },
}
_meta_table['RestconfState.Streams.Stream.Access']['meta_info'].parent =_meta_table['RestconfState.Streams.Stream']['meta_info']
_meta_table['RestconfState.Streams.Stream']['meta_info'].parent =_meta_table['RestconfState.Streams']['meta_info']
_meta_table['RestconfState.Capabilities']['meta_info'].parent =_meta_table['RestconfState']['meta_info']
_meta_table['RestconfState.Streams']['meta_info'].parent =_meta_table['RestconfState']['meta_info']
