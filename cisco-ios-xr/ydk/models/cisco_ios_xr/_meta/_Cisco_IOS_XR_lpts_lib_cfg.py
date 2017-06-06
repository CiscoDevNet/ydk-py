


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('acl-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000')], [], 
                '''                pre-ifib policer rate config commands
                ''',
                'acl_rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipv4vrf-name',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames',
            False, 
            [
            _MetaInfoClassMember('ipv4vrf-name', REFERENCE_LIST, 'Ipv4VrfName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName', 
                [], [], 
                '''                VRF name
                ''',
                'ipv4vrf_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipv4vrf-names',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Ipv4Acls.Ipv4Acl',
            False, 
            [
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                ACL name
                ''',
                'acl_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('ipv4vrf-names', REFERENCE_CLASS, 'Ipv4VrfNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames', 
                [], [], 
                '''                VRF list
                ''',
                'ipv4vrf_names',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipv4acl',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Ipv4Acls' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Ipv4Acls',
            False, 
            [
            _MetaInfoClassMember('ipv4acl', REFERENCE_LIST, 'Ipv4Acl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl', 
                [], [], 
                '''                ACL name
                ''',
                'ipv4acl',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipv4acls',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Flows.Flow.Precedences' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows.Flow.Precedences',
            False, 
            [
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Precedence values
                ''',
                'precedence',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'LptsPreIFibPrecedenceNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumberEnum', 
                        [], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'precedences',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows.Flow',
            False, 
            [
            _MetaInfoClassMember('flow-type', REFERENCE_ENUM_CLASS, 'LptsFlowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlowEnum', 
                [], [], 
                '''                LPTS Flow Type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('precedences', REFERENCE_CLASS, 'Precedences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows.Flow.Precedences', 
                [], [], 
                '''                TOS Precedence value(s)
                ''',
                'precedences',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Flows' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows.Flow', 
                [], [], 
                '''                selected flow type
                ''',
                'flow',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flows',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled
                ''',
                'enable',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows', 
                [], [], 
                '''                Table for Flows
                ''',
                'flows',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('ipv4acls', REFERENCE_CLASS, 'Ipv4Acls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Ipv4Acls', 
                [], [], 
                '''                Table for ACLs
                ''',
                'ipv4acls',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'LptsPuntFlowtrapProtoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoIdEnum', 
                [], [], 
                '''                none
                ''',
                'protocol_name',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('2', '100')], [], 
                '''                Penalty policer rate in packets-per-second
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyRates' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyRates',
            False, 
            [
            _MetaInfoClassMember('penalty-rate', REFERENCE_LIST, 'PenaltyRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate', 
                [], [], 
                '''                none
                ''',
                'penalty_rate',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-rates',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'LptsPuntFlowtrapProtoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoIdEnum', 
                [], [], 
                '''                none
                ''',
                'protocol_name',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', True),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timeout value in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyTimeouts' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyTimeouts',
            False, 
            [
            _MetaInfoClassMember('penalty-timeout', REFERENCE_LIST, 'PenaltyTimeout' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout', 
                [], [], 
                '''                none
                ''',
                'penalty_timeout',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-timeouts',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface to exclude from all traps
                ''',
                'ifname',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', True),
            _MetaInfoClassMember('id1', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled
                ''',
                'id1',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'interface-name',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.Exclude.InterfaceNames' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.Exclude.InterfaceNames',
            False, 
            [
            _MetaInfoClassMember('interface-name', REFERENCE_LIST, 'InterfaceName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName', 
                [], [], 
                '''                Name of interface to exclude from all traps
                ''',
                'interface_name',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'interface-names',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap.Exclude' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.Exclude',
            False, 
            [
            _MetaInfoClassMember('interface-names', REFERENCE_CLASS, 'InterfaceNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.Exclude.InterfaceNames', 
                [], [], 
                '''                none
                ''',
                'interface_names',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'exclude',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt.Flowtrap' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap',
            False, 
            [
            _MetaInfoClassMember('dampening', ATTRIBUTE, 'int' , None, None, 
                [('5000', '60000')], [], 
                '''                Dampening period for a bad actor flow in
                milliseconds
                ''',
                'dampening',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('et-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Should be power of 2. Any one of 1,2,4,8,16,32
                ,64,128
                ''',
                'et_size',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('eviction-search-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Eviction search limit, should be less than
                trap-size
                ''',
                'eviction_search_limit',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('eviction-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Eviction threshold, should be less than
                report-threshold
                ''',
                'eviction_threshold',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('exclude', REFERENCE_CLASS, 'Exclude' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.Exclude', 
                [], [], 
                '''                Exclude an item from all traps
                ''',
                'exclude',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('interface-based-flow', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Identify flow based on interface and flowtype
                ''',
                'interface_based_flow',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('max-flow-gap', ATTRIBUTE, 'int' , None, None, 
                [('1', '60000')], [], 
                '''                Maximum flow gap in milliseconds
                ''',
                'max_flow_gap',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('non-subscriber-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Enable trap based on source mac on
                non-subscriber interface
                ''',
                'non_subscriber_interfaces',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('penalty-rates', REFERENCE_CLASS, 'PenaltyRates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyRates', 
                [], [], 
                '''                Configure penalty policing rate
                ''',
                'penalty_rates',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('penalty-timeouts', REFERENCE_CLASS, 'PenaltyTimeouts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyTimeouts', 
                [], [], 
                '''                Configure penalty timeout value
                ''',
                'penalty_timeouts',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('report-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Threshold to cross for a flow to be considered
                as bad actor flow
                ''',
                'report_threshold',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('routing-protocols-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow routing protocols to pass through copp
                sampler
                ''',
                'routing_protocols_enable',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('sample-prob', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Probability of packets to be sampled
                ''',
                'sample_prob',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('subscriber-interfaces', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable the trap on subscriber interfaces
                ''',
                'subscriber_interfaces',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'flowtrap',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Punt' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt',
            False, 
            [
            _MetaInfoClassMember('flowtrap', REFERENCE_CLASS, 'Flowtrap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap', 
                [], [], 
                '''                excessive punt flow trap configuration commands
                ''',
                'flowtrap',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'punt',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts' : {
        'meta_info' : _MetaInfoClass('Lpts',
            False, 
            [
            _MetaInfoClassMember('ipolicer', REFERENCE_CLASS, 'Ipolicer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer', 
                [], [], 
                '''                Pre IFiB Configuration 
                ''',
                'ipolicer',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('punt', REFERENCE_CLASS, 'Punt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt', 
                [], [], 
                '''                Configure penalty timeout value
                ''',
                'punt',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-lib-cfg',
            'lpts',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
}
_meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames']['meta_info']
_meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl']['meta_info']
_meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Ipv4Acls']['meta_info']
_meta_table['Lpts.Ipolicer.Flows.Flow.Precedences']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info']
_meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Flows']['meta_info']
_meta_table['Lpts.Ipolicer.Ipv4Acls']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.Ipolicer.Flows']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.PenaltyRates']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.Exclude']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyRates']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.Exclude']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap']['meta_info']
_meta_table['Lpts.Punt.Flowtrap']['meta_info'].parent =_meta_table['Lpts.Punt']['meta_info']
_meta_table['Lpts.Ipolicer']['meta_info'].parent =_meta_table['Lpts']['meta_info']
_meta_table['Lpts.Punt']['meta_info'].parent =_meta_table['Lpts']['meta_info']
