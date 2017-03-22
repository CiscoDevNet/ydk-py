


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'XrXml.Agent.Default.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Session',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Timeout in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Default.Throttle' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Throttle',
            False, 
            [
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int' , None, None, 
                [('100', '600')], [], 
                '''                Size of memory usage, in MBytes, per session.
                ''',
                'memory',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('process-rate', ATTRIBUTE, 'int' , None, None, 
                [('1000', '30000')], [], 
                '''                Process rate in number of XML tags per second
                ''',
                'process_rate',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Default.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', True),
            _MetaInfoClassMember('access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Access list for XML agent
                ''',
                'access_list',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ipv4-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                IPv4 Transport Access list for VRF
                ''',
                'ipv4_access_list',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ipv6-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                IPv6 Transport Access list for VRF
                ''',
                'ipv6_access_list',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Shutdown default VRF. This is applicable only
                for VRF default.
                ''',
                'shutdown',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Default.Vrfs' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Default.Vrfs.Vrf', 
                [], [], 
                '''                A specific VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Default' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable specified XML agent
                ''',
                'enable',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ipv4-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable IPV4
                ''',
                'ipv4_disable',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ipv6-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IPv6 Transport State
                ''',
                'ipv6_enable',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('iteration-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000')], [], 
                '''                Iterator size, in KBytes, of the XML response.
                Specify 0 to turn off the XML response iterator.
                ''',
                'iteration_size',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Default.Session', 
                [], [], 
                '''                Session attributes
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('streaming-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '100000')], [], 
                '''                Streaming size, in KBytes, of the XML response.
                ''',
                'streaming_size',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Default.Throttle', 
                [], [], 
                '''                XML agent throttling
                ''',
                'throttle',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Default.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'default',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Tty.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty.Session',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Timeout in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Tty.Throttle' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty.Throttle',
            False, 
            [
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int' , None, None, 
                [('100', '600')], [], 
                '''                Size of memory usage, in MBytes, per session.
                ''',
                'memory',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('process-rate', ATTRIBUTE, 'int' , None, None, 
                [('1000', '30000')], [], 
                '''                Process rate in number of XML tags per second
                ''',
                'process_rate',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Tty' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable specified XML agent
                ''',
                'enable',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('iteration-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000')], [], 
                '''                Iterator size, in KBytes, of the XML response.
                Specify 0 to turn off the XML response iterator.
                ''',
                'iteration_size',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Tty.Session', 
                [], [], 
                '''                Session attributes
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('streaming-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '100000')], [], 
                '''                Streaming size, in KBytes, of the XML response.
                ''',
                'streaming_size',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Tty.Throttle', 
                [], [], 
                '''                XML agent throttling
                ''',
                'throttle',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Ssl.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Session',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Timeout in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Ssl.Throttle' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Throttle',
            False, 
            [
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int' , None, None, 
                [('100', '600')], [], 
                '''                Size of memory usage, in MBytes, per session.
                ''',
                'memory',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('process-rate', ATTRIBUTE, 'int' , None, None, 
                [('1000', '30000')], [], 
                '''                Process rate in number of XML tags per second
                ''',
                'process_rate',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Ssl.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', True),
            _MetaInfoClassMember('access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Access list for XML agent
                ''',
                'access_list',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ipv4-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                IPv4 Transport Access list for VRF
                ''',
                'ipv4_access_list',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ipv6-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                IPv6 Transport Access list for VRF
                ''',
                'ipv6_access_list',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Shutdown default VRF. This is applicable only
                for VRF default.
                ''',
                'shutdown',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Ssl.Vrfs' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Ssl.Vrfs.Vrf', 
                [], [], 
                '''                A specific VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent.Ssl' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable specified XML agent
                ''',
                'enable',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('iteration-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000')], [], 
                '''                Iterator size, in KBytes, of the XML response.
                Specify 0 to turn off the XML response iterator.
                ''',
                'iteration_size',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Ssl.Session', 
                [], [], 
                '''                Session attributes
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('streaming-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '100000')], [], 
                '''                Streaming size, in KBytes, of the XML response.
                ''',
                'streaming_size',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Ssl.Throttle', 
                [], [], 
                '''                XML agent throttling
                ''',
                'throttle',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Ssl.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'ssl',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml.Agent' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent',
            False, 
            [
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Default', 
                [], [], 
                '''                XML default dedicated agent
                ''',
                'default',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('ssl', REFERENCE_CLASS, 'Ssl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Ssl', 
                [], [], 
                '''                XML SSL agent
                ''',
                'ssl',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('tty', REFERENCE_CLASS, 'Tty' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent.Tty', 
                [], [], 
                '''                XML TTY agent
                ''',
                'tty',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'XrXml' : {
        'meta_info' : _MetaInfoClass('XrXml',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'XrXml.Agent', 
                [], [], 
                '''                XML agent
                ''',
                'agent',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'Netconf.Agent.Tty.Throttle' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent.Tty.Throttle',
            False, 
            [
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int' , None, None, 
                [('100', '600')], [], 
                '''                Size of memory usage, in MBytes, per session.
                ''',
                'memory',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('offload-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '12000')], [], 
                '''                Size of memory usage, in MBytes, per session.
                ''',
                'offload_memory',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('process-rate', ATTRIBUTE, 'int' , None, None, 
                [('1000', '30000')], [], 
                '''                Process rate in number of XML tags per second
                ''',
                'process_rate',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'Netconf.Agent.Tty.Session' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent.Tty.Session',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Timeout in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'Netconf.Agent.Tty' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent.Tty',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable specified NETCONF agent
                ''',
                'enable',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'Netconf.Agent.Tty.Session', 
                [], [], 
                '''                Session attributes
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'Netconf.Agent.Tty.Throttle', 
                [], [], 
                '''                NETCONF agent throttling
                ''',
                'throttle',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'Netconf.Agent' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent',
            False, 
            [
            _MetaInfoClassMember('tty', REFERENCE_CLASS, 'Tty' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'Netconf.Agent.Tty', 
                [], [], 
                '''                NETCONF agent over TTY
                ''',
                'tty',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
    'Netconf' : {
        'meta_info' : _MetaInfoClass('Netconf',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg', 'Netconf.Agent', 
                [], [], 
                '''                XML agent
                ''',
                'agent',
                'Cisco-IOS-XR-man-xml-ttyagent-cfg', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-cfg',
            'netconf',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg'
        ),
    },
}
_meta_table['XrXml.Agent.Default.Vrfs.Vrf']['meta_info'].parent =_meta_table['XrXml.Agent.Default.Vrfs']['meta_info']
_meta_table['XrXml.Agent.Default.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Default']['meta_info']
_meta_table['XrXml.Agent.Default.Throttle']['meta_info'].parent =_meta_table['XrXml.Agent.Default']['meta_info']
_meta_table['XrXml.Agent.Default.Vrfs']['meta_info'].parent =_meta_table['XrXml.Agent.Default']['meta_info']
_meta_table['XrXml.Agent.Tty.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Tty']['meta_info']
_meta_table['XrXml.Agent.Tty.Throttle']['meta_info'].parent =_meta_table['XrXml.Agent.Tty']['meta_info']
_meta_table['XrXml.Agent.Ssl.Vrfs.Vrf']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl.Vrfs']['meta_info']
_meta_table['XrXml.Agent.Ssl.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl']['meta_info']
_meta_table['XrXml.Agent.Ssl.Throttle']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl']['meta_info']
_meta_table['XrXml.Agent.Ssl.Vrfs']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl']['meta_info']
_meta_table['XrXml.Agent.Default']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent.Tty']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent.Ssl']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent']['meta_info'].parent =_meta_table['XrXml']['meta_info']
_meta_table['Netconf.Agent.Tty.Throttle']['meta_info'].parent =_meta_table['Netconf.Agent.Tty']['meta_info']
_meta_table['Netconf.Agent.Tty.Session']['meta_info'].parent =_meta_table['Netconf.Agent.Tty']['meta_info']
_meta_table['Netconf.Agent.Tty']['meta_info'].parent =_meta_table['Netconf.Agent']['meta_info']
_meta_table['Netconf.Agent']['meta_info'].parent =_meta_table['Netconf']['meta_info']
