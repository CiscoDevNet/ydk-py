


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'StatusTypeEnum' : _MetaInfoEnum('StatusTypeEnum', 'ydk.models.ietf.ietf_ethernet_segment',
        {
            'up':'up',
            'down':'down',
        }, 'ietf-ethernet-segment', _yang_ns._namespaces['ietf-ethernet-segment']),
    'EthernetSegments.EthernetSegment.PbbParameters' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment.PbbParameters',
            False, 
            [
            _MetaInfoClassMember('backbone-src-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                backbone-src-mac, only if this is a PBB
                ''',
                'backbone_src_mac',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'pbb-parameters',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt.VpnTarget' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt.VpnTarget',
            False, 
            [
            _MetaInfoClassMember('route-target', ATTRIBUTE, 'str' , None, None, 
                [], ['(0:(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d):(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d))|(1:(((\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.){3}(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))|(2:(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))'], 
                '''                Route Target value
                ''',
                'route_target',
                'ietf-ethernet-segment', True),
            _MetaInfoClassMember('route-target-type', REFERENCE_ENUM_CLASS, 'RouteTargetTypeEnum' , 'ydk.models.ietf.ietf_routing_types', 'RouteTargetTypeEnum', 
                [], [], 
                '''                Import/export type of the Route Target.
                ''',
                'route_target_type',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'vpn-target',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt',
            False, 
            [
            _MetaInfoClassMember('route-distinguisher', ATTRIBUTE, 'str' , None, None, 
                [], ['(0:(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d):(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d))|(1:(((\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.){3}(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))|(2:(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))|(([3-9a-fA-F]|[1-9a-fA-F][\\da-fA-F]{1,3}):[\\da-fA-F]{1,12})'], 
                '''                Route distinguisher
                ''',
                'route_distinguisher',
                'ietf-ethernet-segment', True),
            _MetaInfoClassMember('vpn-target', REFERENCE_LIST, 'VpnTarget' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt.VpnTarget', 
                [], [], 
                '''                List of Route Targets.
                ''',
                'vpn_target',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'rd-rt',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments.EthernetSegment.BgpParameters.Common' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment.BgpParameters.Common',
            False, 
            [
            _MetaInfoClassMember('rd-rt', REFERENCE_LIST, 'RdRt' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt', 
                [], [], 
                '''                A list of route distinguishers and corresponding VPN route targets
                ''',
                'rd_rt',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'common',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments.EthernetSegment.BgpParameters' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment.BgpParameters',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment.BgpParameters.Common', 
                [], [], 
                '''                BGP parameters common to all pseudowires
                ''',
                'common',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'bgp-parameters',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments.EthernetSegment.DfElection' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment.DfElection',
            False, 
            [
            _MetaInfoClassMember('election-wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                election-wait-time
                ''',
                'election_wait_time',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('hrw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable (TRUE) or disable (FALSE) highest random weight
                ''',
                'hrw',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'df-election',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments.EthernetSegment' : {
        'meta_info' : _MetaInfoClass('EthernetSegments.EthernetSegment',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the ethernet segment
                ''',
                'name',
                'ietf-ethernet-segment', True),
            _MetaInfoClassMember('ac', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Eventual reference to standard attachment circuit definition
                ''',
                'ac',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('all-active-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                all-active-mode
                ''',
                'all_active_mode',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('bgp-parameters', REFERENCE_CLASS, 'BgpParameters' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment.BgpParameters', 
                [], [], 
                '''                BGP parameters
                ''',
                'bgp_parameters',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('df-election', REFERENCE_CLASS, 'DfElection' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment.DfElection', 
                [], [], 
                '''                df-election
                ''',
                'df_election',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('ead-evi-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable (true) or disable (false) ead-evi-route
                ''',
                'ead_evi_route',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('ethernet-segment-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet segment identifier (esi)
                ''',
                'ethernet_segment_identifier',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('pbb-parameters', REFERENCE_CLASS, 'PbbParameters' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment.PbbParameters', 
                [], [], 
                '''                PBB configuration
                ''',
                'pbb_parameters',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('pw', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Eventual reference to standard pseudowire definition
                ''',
                'pw',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('single-active-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                single-active-mode
                ''',
                'single_active_mode',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'ethernet-segment',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegments' : {
        'meta_info' : _MetaInfoClass('EthernetSegments',
            False, 
            [
            _MetaInfoClassMember('ethernet-segment', REFERENCE_LIST, 'EthernetSegment' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegments.EthernetSegment', 
                [], [], 
                '''                An ethernet segment
                ''',
                'ethernet_segment',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'ethernet-segments',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.PbbParameters' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.PbbParameters',
            False, 
            [
            _MetaInfoClassMember('backbone-src-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                backbone-src-mac, only if this is a PBB
                ''',
                'backbone_src_mac',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'pbb-parameters',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt.VpnTarget' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt.VpnTarget',
            False, 
            [
            _MetaInfoClassMember('route-target', ATTRIBUTE, 'str' , None, None, 
                [], ['(0:(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d):(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d))|(1:(((\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.){3}(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))|(2:(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))'], 
                '''                Route Target value
                ''',
                'route_target',
                'ietf-ethernet-segment', True),
            _MetaInfoClassMember('route-target-type', REFERENCE_ENUM_CLASS, 'RouteTargetTypeEnum' , 'ydk.models.ietf.ietf_routing_types', 'RouteTargetTypeEnum', 
                [], [], 
                '''                Import/export type of the Route Target.
                ''',
                'route_target_type',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'vpn-target',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt',
            False, 
            [
            _MetaInfoClassMember('route-distinguisher', ATTRIBUTE, 'str' , None, None, 
                [], ['(0:(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d):(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d))|(1:(((\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.){3}(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))|(2:(429496729[0-5]|42949672[0-8]\\d|4294967[01]\\d{2}|429496[0-6]\\d{3}|42949[0-5]\\d{4}|4294[0-8]\\d{5}|429[0-3]\\d{6}|42[0-8]\\d{7}|4[01]\\d{8}|[0-3]?\\d{0,8}\\d):(6553[0-5]|655[0-2]\\d|65[0-4]\\d{2}|6[0-4]\\d{3}|[0-5]?\\d{0,3}\\d))|(([3-9a-fA-F]|[1-9a-fA-F][\\da-fA-F]{1,3}):[\\da-fA-F]{1,12})'], 
                '''                Route distinguisher
                ''',
                'route_distinguisher',
                'ietf-ethernet-segment', True),
            _MetaInfoClassMember('vpn-target', REFERENCE_LIST, 'VpnTarget' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt.VpnTarget', 
                [], [], 
                '''                List of Route Targets.
                ''',
                'vpn_target',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'rd-rt',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common',
            False, 
            [
            _MetaInfoClassMember('rd-rt', REFERENCE_LIST, 'RdRt' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt', 
                [], [], 
                '''                A list of route distinghishers and corresponding route targets
                ''',
                'rd_rt',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'common',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.BgpParameters' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.BgpParameters',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common', 
                [], [], 
                '''                BGP parameters common to all pseudowires
                ''',
                'common',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'bgp-parameters',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.DfElection' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.DfElection',
            False, 
            [
            _MetaInfoClassMember('election-wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                election-wait-time
                ''',
                'election_wait_time',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('hrw-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                hrw-enabled is enabled (TRUE) or disabled (FALSE)
                ''',
                'hrw_enabled',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'df-election',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.Member' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.Member',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ip-address
                ''',
                'ip_address',
                'ietf-ethernet-segment', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ip-address
                        ''',
                        'ip_address',
                        'ietf-ethernet-segment', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ip-address
                        ''',
                        'ip_address',
                        'ietf-ethernet-segment', False),
                ]),
            ],
            'ietf-ethernet-segment',
            'member',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState.Df' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState.Df',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ip-address
                ''',
                'ip_address',
                'ietf-ethernet-segment', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ip-address
                        ''',
                        'ip_address',
                        'ietf-ethernet-segment', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ip-address
                        ''',
                        'ip_address',
                        'ietf-ethernet-segment', False),
                ]),
            _MetaInfoClassMember('service-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                service-identifier
                ''',
                'service_identifier',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                vlan
                ''',
                'vlan',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'df',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState.EthernetSegmentState' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState.EthernetSegmentState',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the ethernet segment
                ''',
                'name',
                'ietf-ethernet-segment', True),
            _MetaInfoClassMember('ac', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attachment circuit
                ''',
                'ac',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('active-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Single-active-mode/all-active-mode
                ''',
                'active_mode',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('bgp-parameters', REFERENCE_CLASS, 'BgpParameters' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.BgpParameters', 
                [], [], 
                '''                BGP parameters
                ''',
                'bgp_parameters',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('df', REFERENCE_LIST, 'Df' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.Df', 
                [], [], 
                '''                df of an evpn instance's vlan
                ''',
                'df',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('df-election', REFERENCE_CLASS, 'DfElection' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.DfElection', 
                [], [], 
                '''                df-election
                ''',
                'df_election',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('ead-evi-route-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ead-evi-route is enabled (TRUE) or disabled (FALSE)
                ''',
                'ead_evi_route_enabled',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('esi-label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                esi-label
                ''',
                'esi_label',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('ethernet-segment-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet segment identifier (esi)
                ''',
                'ethernet_segment_identifier',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'StatusTypeEnum' , 'ydk.models.ietf.ietf_ethernet_segment', 'StatusTypeEnum', 
                [], [], 
                '''                interface status
                ''',
                'interface_status',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.Member', 
                [], [], 
                '''                member of the ethernet segment
                ''',
                'member',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('pbb-parameters', REFERENCE_CLASS, 'PbbParameters' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState.PbbParameters', 
                [], [], 
                '''                PBB configuration
                ''',
                'pbb_parameters',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('pw', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of pseudowire
                ''',
                'pw',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('service-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                service-type
                ''',
                'service_type',
                'ietf-ethernet-segment', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusTypeEnum' , 'ydk.models.ietf.ietf_ethernet_segment', 'StatusTypeEnum', 
                [], [], 
                '''                Ethernet segment status
                ''',
                'status',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'ethernet-segment-state',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
    'EthernetSegmentsState' : {
        'meta_info' : _MetaInfoClass('EthernetSegmentsState',
            False, 
            [
            _MetaInfoClassMember('ethernet-segment-state', REFERENCE_LIST, 'EthernetSegmentState' , 'ydk.models.ietf.ietf_ethernet_segment', 'EthernetSegmentsState.EthernetSegmentState', 
                [], [], 
                '''                An ethernet segment
                ''',
                'ethernet_segment_state',
                'ietf-ethernet-segment', False),
            ],
            'ietf-ethernet-segment',
            'ethernet-segments-state',
            _yang_ns._namespaces['ietf-ethernet-segment'],
        'ydk.models.ietf.ietf_ethernet_segment'
        ),
    },
}
_meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt.VpnTarget']['meta_info'].parent =_meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt']['meta_info']
_meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common.RdRt']['meta_info'].parent =_meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common']['meta_info']
_meta_table['EthernetSegments.EthernetSegment.BgpParameters.Common']['meta_info'].parent =_meta_table['EthernetSegments.EthernetSegment.BgpParameters']['meta_info']
_meta_table['EthernetSegments.EthernetSegment.PbbParameters']['meta_info'].parent =_meta_table['EthernetSegments.EthernetSegment']['meta_info']
_meta_table['EthernetSegments.EthernetSegment.BgpParameters']['meta_info'].parent =_meta_table['EthernetSegments.EthernetSegment']['meta_info']
_meta_table['EthernetSegments.EthernetSegment.DfElection']['meta_info'].parent =_meta_table['EthernetSegments.EthernetSegment']['meta_info']
_meta_table['EthernetSegments.EthernetSegment']['meta_info'].parent =_meta_table['EthernetSegments']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt.VpnTarget']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common.RdRt']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters.Common']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.PbbParameters']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.BgpParameters']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.DfElection']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.Member']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState.Df']['meta_info'].parent =_meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info']
_meta_table['EthernetSegmentsState.EthernetSegmentState']['meta_info'].parent =_meta_table['EthernetSegmentsState']['meta_info']
