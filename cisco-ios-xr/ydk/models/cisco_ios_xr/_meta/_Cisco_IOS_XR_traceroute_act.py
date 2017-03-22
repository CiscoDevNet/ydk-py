


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TracerouteRpc.Input.Destination' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Input.Destination',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address or interface
                ''',
                'source',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('probe', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Probe count
                ''',
                'probe',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('numeric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Numeric display only
                ''',
                'numeric',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('min-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                minimum time to live
                ''',
                'min_ttl',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('max-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                maximum time to live
                ''',
                'max_ttl',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port numbe
                ''',
                'port',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                verbose output
                ''',
                'verbose',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Priority of hte packet
                ''',
                'priority',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing interface, needed in case of traceroute to link local address
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Input.Ipv4' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Input.Ipv4',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address or interface
                ''',
                'source',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('probe', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Probe count
                ''',
                'probe',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('numeric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Numeric display only
                ''',
                'numeric',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('min-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                minimum time to live
                ''',
                'min_ttl',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('max-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                maximum time to live
                ''',
                'max_ttl',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port numbe
                ''',
                'port',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                verbose output
                ''',
                'verbose',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Input.Ipv6' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Input.Ipv6',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address or interface
                ''',
                'source',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '36')], [], 
                '''                Timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('probe', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Probe count
                ''',
                'probe',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('numeric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Numeric display only
                ''',
                'numeric',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('min-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                minimum time to live
                ''',
                'min_ttl',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('max-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                maximum time to live
                ''',
                'max_ttl',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port numbe
                ''',
                'port',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                verbose output
                ''',
                'verbose',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Priority of hte packet
                ''',
                'priority',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing interface, needed in case of traceroute to link local address
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Input' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Input.Destination', 
                [], [], 
                '''                ''',
                'destination',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Input.Ipv4', 
                [], [], 
                '''                ''',
                'ipv4',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Input.Ipv6', 
                [], [], 
                '''                ''',
                'ipv6',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops.Probes' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops.Probes',
            False, 
            [
            _MetaInfoClassMember('probe-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the probe
                ''',
                'probe_index',
                'Cisco-IOS-XR-traceroute-act', True),
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Response for each probe
                ''',
                'result',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('delta-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delta time in seconds
                ''',
                'delta_time',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address of the hop
                ''',
                'hop_address',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hop-hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname of the hop
                ''',
                'hop_hostname',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'probes',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops',
            False, 
            [
            _MetaInfoClassMember('hop-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the hop
                ''',
                'hop_index',
                'Cisco-IOS-XR-traceroute-act', True),
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address of the hop
                ''',
                'hop_address',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hop-hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname of the hop
                ''',
                'hop_hostname',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('probes', REFERENCE_LIST, 'Probes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops.Probes', 
                [], [], 
                '''                ''',
                'probes',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'hops',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse.Ipv4' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse.Ipv4',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hops', REFERENCE_LIST, 'Hops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops', 
                [], [], 
                '''                ''',
                'hops',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('verbose-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Verbose output
                ''',
                'verbose_output',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops.Probes' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops.Probes',
            False, 
            [
            _MetaInfoClassMember('probe-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the probe
                ''',
                'probe_index',
                'Cisco-IOS-XR-traceroute-act', True),
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Response for each probe
                ''',
                'result',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('delta-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delta time in seconds
                ''',
                'delta_time',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address of the hop
                ''',
                'hop_address',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hop-hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname of the hop
                ''',
                'hop_hostname',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'probes',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops',
            False, 
            [
            _MetaInfoClassMember('hop-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the hop
                ''',
                'hop_index',
                'Cisco-IOS-XR-traceroute-act', True),
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address of the hop
                ''',
                'hop_address',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hop-hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname of the hop
                ''',
                'hop_hostname',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('probes', REFERENCE_LIST, 'Probes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops.Probes', 
                [], [], 
                '''                ''',
                'probes',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'hops',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse.Ipv6' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse.Ipv6',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination address or hostname
                ''',
                'destination',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('hops', REFERENCE_LIST, 'Hops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops', 
                [], [], 
                '''                ''',
                'hops',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('verbose-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Verbose output
                ''',
                'verbose_output',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output.TracerouteResponse' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.TracerouteResponse',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse.Ipv4', 
                [], [], 
                '''                ''',
                'ipv4',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse.Ipv6', 
                [], [], 
                '''                ''',
                'ipv6',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'traceroute-response',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc.Output' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output',
            False, 
            [
            _MetaInfoClassMember('traceroute-response', REFERENCE_CLASS, 'TracerouteResponse' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output.TracerouteResponse', 
                [], [], 
                '''                ''',
                'traceroute_response',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
    'TracerouteRpc' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-traceroute-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act', 'TracerouteRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XR-traceroute-act', False),
            ],
            'Cisco-IOS-XR-traceroute-act',
            'traceroute',
            _yang_ns._namespaces['Cisco-IOS-XR-traceroute-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act'
        ),
    },
}
_meta_table['TracerouteRpc.Input.Destination']['meta_info'].parent =_meta_table['TracerouteRpc.Input']['meta_info']
_meta_table['TracerouteRpc.Input.Ipv4']['meta_info'].parent =_meta_table['TracerouteRpc.Input']['meta_info']
_meta_table['TracerouteRpc.Input.Ipv6']['meta_info'].parent =_meta_table['TracerouteRpc.Input']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops.Probes']['meta_info'].parent =_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops']['meta_info'].parent =_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops.Probes']['meta_info'].parent =_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops']['meta_info'].parent =_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4']['meta_info'].parent =_meta_table['TracerouteRpc.Output.TracerouteResponse']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6']['meta_info'].parent =_meta_table['TracerouteRpc.Output.TracerouteResponse']['meta_info']
_meta_table['TracerouteRpc.Output.TracerouteResponse']['meta_info'].parent =_meta_table['TracerouteRpc.Output']['meta_info']
_meta_table['TracerouteRpc.Input']['meta_info'].parent =_meta_table['TracerouteRpc']['meta_info']
_meta_table['TracerouteRpc.Output']['meta_info'].parent =_meta_table['TracerouteRpc']['meta_info']
