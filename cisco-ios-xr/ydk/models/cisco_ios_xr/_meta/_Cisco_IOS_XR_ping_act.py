


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PingRpc.Input.Destination' : {
        'meta_info' : _MetaInfoClass('PingRpc.Input.Destination',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ping destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('repeat-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Number of ping packets to be sent out
                ''',
                'repeat_count',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('data-size', ATTRIBUTE, 'int' , None, None, 
                [('36', '18024')], [], 
                '''                Size of ping packet
                ''',
                'data_size',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Ping interval in milli seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Pattern of payload data
                ''',
                'pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sweep is enabled
                ''',
                'sweep',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address or interface
                ''',
                'source',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validate return packet
                ''',
                'verbose',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('type-of-service', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Type of Service
                ''',
                'type_of_service',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('do-not-frag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do Not Fragment
                ''',
                'do_not_frag',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('validate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validate return packet
                ''',
                'validate',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Priority of the packet
                ''',
                'priority',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing interface, needed in case of ping to link local address
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Input.Ipv4' : {
        'meta_info' : _MetaInfoClass('PingRpc.Input.Ipv4',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ping destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-ping-act', True),
            _MetaInfoClassMember('repeat-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Number of ping packets to be sent out
                ''',
                'repeat_count',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('data-size', ATTRIBUTE, 'int' , None, None, 
                [('36', '18024')], [], 
                '''                Size of ping packet
                ''',
                'data_size',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Ping interval in milli seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Pattern of payload data
                ''',
                'pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sweep is enabled
                ''',
                'sweep',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address or interface
                ''',
                'source',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validate return packet
                ''',
                'verbose',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('type-of-service', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Type of Service
                ''',
                'type_of_service',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('do-not-frag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do Not Fragment
                ''',
                'do_not_frag',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('validate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validate return packet
                ''',
                'validate',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Input.Ipv6' : {
        'meta_info' : _MetaInfoClass('PingRpc.Input.Ipv6',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ping destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('repeat-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Number of ping packets to be sent out
                ''',
                'repeat_count',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('data-size', ATTRIBUTE, 'int' , None, None, 
                [('36', '18024')], [], 
                '''                Size of ping packet
                ''',
                'data_size',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Ping interval in milli seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Pattern of payload data
                ''',
                'pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sweep is enabled
                ''',
                'sweep',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address or interface
                ''',
                'source',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validate return packet
                ''',
                'verbose',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Priority of the packet
                ''',
                'priority',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing interface, needed in case of ping to link local address
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Input' : {
        'meta_info' : _MetaInfoClass('PingRpc.Input',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Input.Destination', 
                [], [], 
                '''                ''',
                'destination',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('ipv4', REFERENCE_LIST, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Input.Ipv4', 
                [], [], 
                '''                ''',
                'ipv4',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Input.Ipv6', 
                [], [], 
                '''                ''',
                'ipv6',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress',
            False, 
            [
            _MetaInfoClassMember('reply-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Broadcast reply address
                ''',
                'reply_address',
                'Cisco-IOS-XR-ping-act', True),
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sign for each reply packet
                ''',
                'result',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'broadcast-reply-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses',
            False, 
            [
            _MetaInfoClassMember('broadcast-reply-address', REFERENCE_LIST, 'BroadcastReplyAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress', 
                [], [], 
                '''                ''',
                'broadcast_reply_address',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'broadcast-reply-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv4.Replies.Reply' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv4.Replies.Reply',
            False, 
            [
            _MetaInfoClassMember('reply-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Index of the reply list
                ''',
                'reply_index',
                'Cisco-IOS-XR-ping-act', True),
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Response for each packet
                ''',
                'result',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('broadcast-reply-addresses', REFERENCE_CLASS, 'BroadcastReplyAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses', 
                [], [], 
                '''                ''',
                'broadcast_reply_addresses',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv4.Replies' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv4.Replies',
            False, 
            [
            _MetaInfoClassMember('reply', REFERENCE_LIST, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv4.Replies.Reply', 
                [], [], 
                '''                ''',
                'reply',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'replies',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv4' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv4',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ping destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-ping-act', True),
            _MetaInfoClassMember('repeat-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Number of ping packets to be sent out
                ''',
                'repeat_count',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('data-size', ATTRIBUTE, 'int' , None, None, 
                [('36', '18024')], [], 
                '''                Size of ping packet
                ''',
                'data_size',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Ping interval in milli seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Pattern of payload data
                ''',
                'pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sweep is enabled
                ''',
                'sweep',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('replies', REFERENCE_CLASS, 'Replies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv4.Replies', 
                [], [], 
                '''                ''',
                'replies',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets reach to destination and get reply back
                ''',
                'hits',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent out
                ''',
                'total',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('success-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Successful rate of ping
                ''',
                'success_rate',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rtt-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Minimum value of Round Trip Time
                ''',
                'rtt_min',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rtt-avg', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average value of Round Trip Time
                ''',
                'rtt_avg',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rtt-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum value of Round Trip Time
                ''',
                'rtt_max',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of sweep size
                ''',
                'sweep_min',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum value of sweep size
                ''',
                'sweep_max',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rotate-pattern', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rotate Pattern is enabled
                ''',
                'rotate_pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('ping-error-response', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error response for each ping, in case of bulk ping
                ''',
                'ping_error_response',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv6.Replies.Reply' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv6.Replies.Reply',
            False, 
            [
            _MetaInfoClassMember('reply-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Index of the reply list
                ''',
                'reply_index',
                'Cisco-IOS-XR-ping-act', True),
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Response for each packet
                ''',
                'result',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv6.Replies' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv6.Replies',
            False, 
            [
            _MetaInfoClassMember('reply', REFERENCE_LIST, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv6.Replies.Reply', 
                [], [], 
                '''                ''',
                'reply',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'replies',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse.Ipv6' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse.Ipv6',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ping destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('repeat-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Number of ping packets to be sent out
                ''',
                'repeat_count',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('data-size', ATTRIBUTE, 'int' , None, None, 
                [('36', '18024')], [], 
                '''                Size of ping packet
                ''',
                'data_size',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Ping interval in milli seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Pattern of payload data
                ''',
                'pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sweep is enabled
                ''',
                'sweep',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum value of sweep size
                ''',
                'sweep_min',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('sweep-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum value of sweep size
                ''',
                'sweep_max',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rotate-pattern', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rotate Pattern is enabled
                ''',
                'rotate_pattern',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('replies', REFERENCE_CLASS, 'Replies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv6.Replies', 
                [], [], 
                '''                ''',
                'replies',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets reach to destination and get reply back
                ''',
                'hits',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets sent out
                ''',
                'total',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('success-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Successful rate of ping
                ''',
                'success_rate',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rtt-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Minimum value of Round Trip Time
                ''',
                'rtt_min',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rtt-avg', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average value of Round Trip Time
                ''',
                'rtt_avg',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('rtt-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum value of Round Trip Time
                ''',
                'rtt_max',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output.PingResponse' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output.PingResponse',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_LIST, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv4', 
                [], [], 
                '''                ''',
                'ipv4',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse.Ipv6', 
                [], [], 
                '''                ''',
                'ipv6',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'ping-response',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc.Output' : {
        'meta_info' : _MetaInfoClass('PingRpc.Output',
            False, 
            [
            _MetaInfoClassMember('ping-response', REFERENCE_CLASS, 'PingResponse' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output.PingResponse', 
                [], [], 
                '''                ''',
                'ping_response',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
    'PingRpc' : {
        'meta_info' : _MetaInfoClass('PingRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-ping-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act', 'PingRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XR-ping-act', False),
            ],
            'Cisco-IOS-XR-ping-act',
            'ping',
            _yang_ns._namespaces['Cisco-IOS-XR-ping-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act'
        ),
    },
}
_meta_table['PingRpc.Input.Destination']['meta_info'].parent =_meta_table['PingRpc.Input']['meta_info']
_meta_table['PingRpc.Input.Ipv4']['meta_info'].parent =_meta_table['PingRpc.Input']['meta_info']
_meta_table['PingRpc.Input.Ipv6']['meta_info'].parent =_meta_table['PingRpc.Input']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies.Reply']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv4.Replies']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse.Ipv4']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv6.Replies.Reply']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse.Ipv6.Replies']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv6.Replies']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse.Ipv6']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv4']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse']['meta_info']
_meta_table['PingRpc.Output.PingResponse.Ipv6']['meta_info'].parent =_meta_table['PingRpc.Output.PingResponse']['meta_info']
_meta_table['PingRpc.Output.PingResponse']['meta_info'].parent =_meta_table['PingRpc.Output']['meta_info']
_meta_table['PingRpc.Input']['meta_info'].parent =_meta_table['PingRpc']['meta_info']
_meta_table['PingRpc.Output']['meta_info'].parent =_meta_table['PingRpc']['meta_info']
