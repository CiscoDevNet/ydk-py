


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'UnitsEnum' : _MetaInfoEnum('UnitsEnum', 'ydk.models.ietf.ietf_lspping',
        {
            'seconds':'seconds',
            'milliseconds':'milliseconds',
            'microseconds':'microseconds',
            'nanoseconds':'nanoseconds',
        }, 'ietf-lspping', _yang_ns._namespaces['ietf-lspping']),
    'TargetFecTypeEnum' : _MetaInfoEnum('TargetFecTypeEnum', 'ydk.models.ietf.ietf_lspping',
        {
            'ip-prefix':'ip_prefix',
            'bgp':'bgp',
            'rsvp':'rsvp',
            'vpn':'vpn',
            'pw':'pw',
            'vpls':'vpls',
        }, 'ietf-lspping', _yang_ns._namespaces['ietf-lspping']),
    'OperationalStatusEnum' : _MetaInfoEnum('OperationalStatusEnum', 'ydk.models.ietf.ietf_lspping',
        {
            'enabled':'enabled',
            'disabled':'disabled',
            'completed':'completed',
        }, 'ietf-lspping', _yang_ns._namespaces['ietf-lspping']),
    'ReplyModeEnum' : _MetaInfoEnum('ReplyModeEnum', 'ydk.models.ietf.ietf_lspping',
        {
            'do-not-reply':'do_not_reply',
            'reply-via-udp':'reply_via_udp',
            'reply-via-udp-router-alert':'reply_via_udp_router_alert',
            'reply-via-control-channel':'reply_via_control_channel',
        }, 'ietf-lspping', _yang_ns._namespaces['ietf-lspping']),
    'ResultTypeEnum' : _MetaInfoEnum('ResultTypeEnum', 'ydk.models.ietf.ietf_lspping',
        {
            'success':'success',
            'fail':'fail',
            'timeout':'timeout',
        }, 'ietf-lspping', _yang_ns._namespaces['ietf-lspping']),
    'LspPings.LspPing.ControlInfo' : {
        'meta_info' : _MetaInfoClass('LspPings.LspPing.ControlInfo',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP IPv4/IPv6 Prefix.
                ''',
                'bgp',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('bgp', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP IPv4/IPv6 Prefix.
                        ''',
                        'bgp',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('bgp', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP IPv4/IPv6 Prefix.
                        ''',
                        'bgp',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('data-fill', ATTRIBUTE, 'str' , None, None, 
                [(0, 1564)], [], 
                '''                Used together with the corresponding
                data-size value to determine how to fill the data
                portion of a probe packet.
                ''',
                'data_fill',
                'ietf-lspping', False),
            _MetaInfoClassMember('data-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the size of the data portion to
                be transmitted in a LSP Ping operation, in octets.
                ''',
                'data_size',
                'ietf-lspping', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                A descriptive name of the LSP Ping test.
                ''',
                'description',
                'ietf-lspping', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Specifies the outgoing interface.
                ''',
                'interface_name',
                'ietf-lspping', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the interval to send a LSP Ping
                echo request packet(probe) as part of one LSP Ping test.
                ''',
                'interval',
                'ietf-lspping', False),
            _MetaInfoClassMember('interval-units', REFERENCE_ENUM_CLASS, 'UnitsEnum' , 'ydk.models.ietf.ietf_lspping', 'UnitsEnum', 
                [], [], 
                '''                Interval units.
                ''',
                'interval_units',
                'ietf-lspping', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4/IPv6 Prefix.
                ''',
                'ip_address',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/IPv6 Prefix.
                        ''',
                        'ip_address',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/IPv6 Prefix.
                        ''',
                        'ip_address',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('nexthop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specifies the nexthop.
                ''',
                'nexthop',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('nexthop', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Specifies the nexthop.
                        ''',
                        'nexthop',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('nexthop', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Specifies the nexthop.
                        ''',
                        'nexthop',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the number of probe sent of one
                LSP Ping test.
                ''',
                'probe_count',
                'ietf-lspping', False),
            _MetaInfoClassMember('reply-mode', REFERENCE_ENUM_CLASS, 'ReplyModeEnum' , 'ydk.models.ietf.ietf_lspping', 'ReplyModeEnum', 
                [], [], 
                '''                Specifies the reply mode.
                ''',
                'reply_mode',
                'ietf-lspping', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specifies the source address.
                ''',
                'source_address',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Specifies the source address.
                        ''',
                        'source_address',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Specifies the source address.
                        ''',
                        'source_address',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('source-address-type', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                Specifies the type of the source address.
                ''',
                'source_address_type',
                'ietf-lspping', False),
            _MetaInfoClassMember('target-fec-type', REFERENCE_ENUM_CLASS, 'TargetFecTypeEnum' , 'ydk.models.ietf.ietf_lspping', 'TargetFecTypeEnum', 
                [], [], 
                '''                Specifies the address type of Target FEC.
                ''',
                'target_fec_type',
                'ietf-lspping', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the time-out value for a
                LSP Ping operation.
                ''',
                'timeout',
                'ietf-lspping', False),
            _MetaInfoClassMember('timeout-units', REFERENCE_ENUM_CLASS, 'UnitsEnum' , 'ydk.models.ietf.ietf_lspping', 'UnitsEnum', 
                [], [], 
                '''                Time-out units.
                ''',
                'timeout_units',
                'ietf-lspping', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specifies the Traffic Class.
                ''',
                'traffic_class',
                'ietf-lspping', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time to live.
                ''',
                'ttl',
                'ietf-lspping', False),
            _MetaInfoClassMember('tunnel-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel interface
                ''',
                'tunnel_interface',
                'ietf-lspping', False),
            _MetaInfoClassMember('vcid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VC ID
                ''',
                'vcid',
                'ietf-lspping', False),
            _MetaInfoClassMember('vpn-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Layer3 VPN IPv4 Prefix.
                ''',
                'vpn_ip_address',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('vpn-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Layer3 VPN IPv4 Prefix.
                        ''',
                        'vpn_ip_address',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('vpn-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Layer3 VPN IPv4 Prefix.
                        ''',
                        'vpn_ip_address',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer3 VPN Name.
                ''',
                'vrf_name',
                'ietf-lspping', False),
            _MetaInfoClassMember('vsi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VPLS VSI
                ''',
                'vsi_name',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'control-info',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
    'LspPings.LspPing.ScheduleParameters' : {
        'meta_info' : _MetaInfoClass('LspPings.LspPing.ScheduleParameters',
            False, 
            [
            _MetaInfoClassMember('end-test-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                End test at a specific time.
                ''',
                'end_test_at',
                'ietf-lspping', False),
            _MetaInfoClassMember('end-test-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                End after a specific delay.
                ''',
                'end_test_delay',
                'ietf-lspping', False),
            _MetaInfoClassMember('end-test-delay-units', REFERENCE_ENUM_CLASS, 'UnitsEnum' , 'ydk.models.ietf.ietf_lspping', 'UnitsEnum', 
                [], [], 
                '''                Delay units.
                ''',
                'end_test_delay_units',
                'ietf-lspping', False),
            _MetaInfoClassMember('end-test-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set the test lifetime.
                ''',
                'end_test_lifetime',
                'ietf-lspping', False),
            _MetaInfoClassMember('lifetime-units', REFERENCE_ENUM_CLASS, 'UnitsEnum' , 'ydk.models.ietf.ietf_lspping', 'UnitsEnum', 
                [], [], 
                '''                Lifetime units.
                ''',
                'lifetime_units',
                'ietf-lspping', False),
            _MetaInfoClassMember('start-test-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Start test at a specific time.
                ''',
                'start_test_at',
                'ietf-lspping', False),
            _MetaInfoClassMember('start-test-daily', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Start test daily.
                ''',
                'start_test_daily',
                'ietf-lspping', False),
            _MetaInfoClassMember('start-test-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Start after a specific delay.
                ''',
                'start_test_delay',
                'ietf-lspping', False),
            _MetaInfoClassMember('start-test-delay-units', REFERENCE_ENUM_CLASS, 'UnitsEnum' , 'ydk.models.ietf.ietf_lspping', 'UnitsEnum', 
                [], [], 
                '''                Delay units.
                ''',
                'start_test_delay_units',
                'ietf-lspping', False),
            _MetaInfoClassMember('start-test-now', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start test now.
                ''',
                'start_test_now',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'schedule-parameters',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
    'LspPings.LspPing.ResultInfo.ProbeResults.ProbeResult' : {
        'meta_info' : _MetaInfoClass('LspPings.LspPing.ResultInfo.ProbeResults.ProbeResult',
            False, 
            [
            _MetaInfoClassMember('probe-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Probe index
                ''',
                'probe_index',
                'ietf-lspping', True),
            _MetaInfoClassMember('result-type', REFERENCE_ENUM_CLASS, 'ResultTypeEnum' , 'ydk.models.ietf.ietf_lspping', 'ResultTypeEnum', 
                [], [], 
                '''                The probe result type.
                ''',
                'result_type',
                'ietf-lspping', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The Return Code set in the echo reply.
                ''',
                'return_code',
                'ietf-lspping', False),
            _MetaInfoClassMember('return-sub-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The Return Sub-code set in the
                echo reply.
                ''',
                'return_sub_code',
                'ietf-lspping', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The round-trip-time (RTT) received.
                ''',
                'rtt',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'probe-result',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
    'LspPings.LspPing.ResultInfo.ProbeResults' : {
        'meta_info' : _MetaInfoClass('LspPings.LspPing.ResultInfo.ProbeResults',
            False, 
            [
            _MetaInfoClassMember('probe-result', REFERENCE_LIST, 'ProbeResult' , 'ydk.models.ietf.ietf_lspping', 'LspPings.LspPing.ResultInfo.ProbeResults.ProbeResult', 
                [], [], 
                '''                Result info of each test probe.
                ''',
                'probe_result',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'probe-results',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
    'LspPings.LspPing.ResultInfo' : {
        'meta_info' : _MetaInfoClass('LspPings.LspPing.ResultInfo',
            False, 
            [
            _MetaInfoClassMember('average-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current average LSP Ping round-trip-time
                (RTT).
                ''',
                'average_rtt',
                'ietf-lspping', False),
            _MetaInfoClassMember('bgp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP IPv4/IPv6 Prefix.
                ''',
                'bgp',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('bgp', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP IPv4/IPv6 Prefix.
                        ''',
                        'bgp',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('bgp', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP IPv4/IPv6 Prefix.
                        ''',
                        'bgp',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4/IPv6 Prefix.
                ''',
                'ip_address',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/IPv6 Prefix.
                        ''',
                        'ip_address',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/IPv6 Prefix.
                        ''',
                        'ip_address',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('last-good-probe', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Date and time when the last response
                was received for a probe.
                ''',
                'last_good_probe',
                'ietf-lspping', False),
            _MetaInfoClassMember('max-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum LSP Ping round-trip-time (RTT)
                received.
                ''',
                'max_rtt',
                'ietf-lspping', False),
            _MetaInfoClassMember('min-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum LSP Ping round-trip-time (RTT)
                received.
                ''',
                'min_rtt',
                'ietf-lspping', False),
            _MetaInfoClassMember('operational-status', REFERENCE_ENUM_CLASS, 'OperationalStatusEnum' , 'ydk.models.ietf.ietf_lspping', 'OperationalStatusEnum', 
                [], [], 
                '''                Operational state of a LSP Ping test
                ''',
                'operational_status',
                'ietf-lspping', False),
            _MetaInfoClassMember('probe-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of responses received for the
                corresponding LSP Ping test.
                ''',
                'probe_responses',
                'ietf-lspping', False),
            _MetaInfoClassMember('probe-results', REFERENCE_CLASS, 'ProbeResults' , 'ydk.models.ietf.ietf_lspping', 'LspPings.LspPing.ResultInfo.ProbeResults', 
                [], [], 
                '''                Result info of test probes.
                ''',
                'probe_results',
                'ietf-lspping', False),
            _MetaInfoClassMember('sent-probes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of probes sent for the
                corresponding LSP Ping test.
                ''',
                'sent_probes',
                'ietf-lspping', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The source address of the test.
                ''',
                'source_address',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The source address of the test.
                        ''',
                        'source_address',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The source address of the test.
                        ''',
                        'source_address',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('source-address-type', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The source address type.
                ''',
                'source_address_type',
                'ietf-lspping', False),
            _MetaInfoClassMember('sum-of-squares', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The sum of the squares for all
                replys received.
                ''',
                'sum_of_squares',
                'ietf-lspping', False),
            _MetaInfoClassMember('target-fec-type', REFERENCE_ENUM_CLASS, 'TargetFecTypeEnum' , 'ydk.models.ietf.ietf_lspping', 'TargetFecTypeEnum', 
                [], [], 
                '''                The Target FEC address type.
                ''',
                'target_fec_type',
                'ietf-lspping', False),
            _MetaInfoClassMember('tunnel-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel interface
                ''',
                'tunnel_interface',
                'ietf-lspping', False),
            _MetaInfoClassMember('vcid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VC ID
                ''',
                'vcid',
                'ietf-lspping', False),
            _MetaInfoClassMember('vpn-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Layer3 VPN IPv4 Prefix.
                ''',
                'vpn_ip_address',
                'ietf-lspping', False, [
                    _MetaInfoClassMember('vpn-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Layer3 VPN IPv4 Prefix.
                        ''',
                        'vpn_ip_address',
                        'ietf-lspping', False),
                    _MetaInfoClassMember('vpn-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Layer3 VPN IPv4 Prefix.
                        ''',
                        'vpn_ip_address',
                        'ietf-lspping', False),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer3 VPN Name.
                ''',
                'vrf_name',
                'ietf-lspping', False),
            _MetaInfoClassMember('vsi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VPLS VSI
                ''',
                'vsi_name',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'result-info',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
    'LspPings.LspPing' : {
        'meta_info' : _MetaInfoClass('LspPings.LspPing',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                LSP Ping test name.
                ''',
                'lsp_ping_name',
                'ietf-lspping', True),
            _MetaInfoClassMember('control-info', REFERENCE_CLASS, 'ControlInfo' , 'ydk.models.ietf.ietf_lspping', 'LspPings.LspPing.ControlInfo', 
                [], [], 
                '''                Control information of the LSP Ping test.
                ''',
                'control_info',
                'ietf-lspping', False),
            _MetaInfoClassMember('result-info', REFERENCE_CLASS, 'ResultInfo' , 'ydk.models.ietf.ietf_lspping', 'LspPings.LspPing.ResultInfo', 
                [], [], 
                '''                LSP Ping test result information.
                ''',
                'result_info',
                'ietf-lspping', False),
            _MetaInfoClassMember('schedule-parameters', REFERENCE_CLASS, 'ScheduleParameters' , 'ydk.models.ietf.ietf_lspping', 'LspPings.LspPing.ScheduleParameters', 
                [], [], 
                '''                LSP Ping test schedule parameter
                ''',
                'schedule_parameters',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'lsp-ping',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
    'LspPings' : {
        'meta_info' : _MetaInfoClass('LspPings',
            False, 
            [
            _MetaInfoClassMember('lsp-ping', REFERENCE_LIST, 'LspPing' , 'ydk.models.ietf.ietf_lspping', 'LspPings.LspPing', 
                [], [], 
                '''                LSP Ping test
                ''',
                'lsp_ping',
                'ietf-lspping', False),
            ],
            'ietf-lspping',
            'lsp-pings',
            _yang_ns._namespaces['ietf-lspping'],
        'ydk.models.ietf.ietf_lspping'
        ),
    },
}
_meta_table['LspPings.LspPing.ResultInfo.ProbeResults.ProbeResult']['meta_info'].parent =_meta_table['LspPings.LspPing.ResultInfo.ProbeResults']['meta_info']
_meta_table['LspPings.LspPing.ResultInfo.ProbeResults']['meta_info'].parent =_meta_table['LspPings.LspPing.ResultInfo']['meta_info']
_meta_table['LspPings.LspPing.ControlInfo']['meta_info'].parent =_meta_table['LspPings.LspPing']['meta_info']
_meta_table['LspPings.LspPing.ScheduleParameters']['meta_info'].parent =_meta_table['LspPings.LspPing']['meta_info']
_meta_table['LspPings.LspPing.ResultInfo']['meta_info'].parent =_meta_table['LspPings.LspPing']['meta_info']
_meta_table['LspPings.LspPing']['meta_info'].parent =_meta_table['LspPings']['meta_info']
