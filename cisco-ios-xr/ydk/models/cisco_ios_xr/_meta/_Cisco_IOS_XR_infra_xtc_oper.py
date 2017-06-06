


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PceAfIdEnum' : _MetaInfoEnum('PceAfIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'none':'none',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PceIgpInfoIdEnum' : _MetaInfoEnum('PceIgpInfoIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'isis':'isis',
            'ospf':'ospf',
            'bgp':'bgp',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'LspSetupEnum' : _MetaInfoEnum('LspSetupEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'setup-rsvp':'setup_rsvp',
            'setup-sr':'setup_sr',
            'setup-unknown':'setup_unknown',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PceProtoEnum' : _MetaInfoEnum('PceProtoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'pcep':'pcep',
            'netconf':'netconf',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PceRroEnum' : _MetaInfoEnum('PceRroEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'rro-type-ipv4-address':'rro_type_ipv4_address',
            'rro-type-mpls-label':'rro_type_mpls_label',
            'rro-type-sripv4-node-sid':'rro_type_sripv4_node_sid',
            'rro-type-sripv4-adjacency-sid':'rro_type_sripv4_adjacency_sid',
            'rro-type-sr-nai-null':'rro_type_sr_nai_null',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PceAssoEnum' : _MetaInfoEnum('PceAssoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'unknown':'unknown',
            'link':'link',
            'node':'node',
            'srlg':'srlg',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'LspStateEnum' : _MetaInfoEnum('LspStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'lsp-down':'lsp_down',
            'lsp-up':'lsp_up',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PcepStateEnum' : _MetaInfoEnum('PcepStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'tcp-close':'tcp_close',
            'tcp-listen':'tcp_listen',
            'tcp-connect':'tcp_connect',
            'pcep-closed':'pcep_closed',
            'pcep-opening':'pcep_opening',
            'pcep-open':'pcep_open',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PcepLspStateEnum' : _MetaInfoEnum('PcepLspStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'lsp-down':'lsp_down',
            'lsp-up':'lsp_up',
            'lsp-active':'lsp_active',
            'lsp-going-down':'lsp_going_down',
            'lsp-being-signaled':'lsp_being_signaled',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'SidEnum' : _MetaInfoEnum('SidEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'sr-protected-adj-sid':'sr_protected_adj_sid',
            'sr-unprotected-adj-sid':'sr_unprotected_adj_sid',
            'srbgp-egress-peer-engineering-sid':'srbgp_egress_peer_engineering_sid',
            'sr-reqular-prefix-sid':'sr_reqular_prefix_sid',
            'sr-strict-prefix-sid':'sr_strict_prefix_sid',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PceSrSidEnum' : _MetaInfoEnum('PceSrSidEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper',
        {
            'ipv4-node-sid':'ipv4_node_sid',
            'ipv4-adjacency-sid':'ipv4_adjacency_sid',
            'unknown-sid':'unknown_sid',
        }, 'Cisco-IOS-XR-infra-xtc-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper']),
    'PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation',
            False, 
            [
            _MetaInfoClassMember('administrative-state', REFERENCE_ENUM_CLASS, 'LspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspStateEnum', 
                [], [], 
                '''                Admin state
                ''',
                'administrative_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('binding-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Binding SID
                ''',
                'binding_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-setup-type', REFERENCE_ENUM_CLASS, 'LspSetupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetupEnum', 
                [], [], 
                '''                LSP Setup Type
                ''',
                'lsp_setup_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('operational-state', REFERENCE_ENUM_CLASS, 'PcepLspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspStateEnum', 
                [], [], 
                '''                Operational state
                ''',
                'operational_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelInfos.TunnelInfo' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelInfos.TunnelInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('plsp-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCEP LSP ID
                ''',
                'plsp_id',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Tunnel name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('brief-lsp-information', REFERENCE_LIST, 'BriefLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation', 
                [], [], 
                '''                Brief LSP information
                ''',
                'brief_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCC address
                ''',
                'pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelInfos' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelInfos',
            False, 
            [
            _MetaInfoClassMember('tunnel-info', REFERENCE_LIST, 'TunnelInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelInfos.TunnelInfo', 
                [], [], 
                '''                Tunnel information
                ''',
                'tunnel_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.LspSummary.AllLsPs' : {
        'meta_info' : _MetaInfoClass('PceLspData.LspSummary.AllLsPs',
            False, 
            [
            _MetaInfoClassMember('admin-up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of administratively up LSPs
                ''',
                'admin_up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('all-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of all LSPs
                ''',
                'all_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rsvp-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with RSVP setup type
                ''',
                'rsvp_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sr-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with Segment routing setup type
                ''',
                'sr_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of operational LSPs
                ''',
                'up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'all-ls-ps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.LspSummary.PeerLsPsInfo.LspSummary_' : {
        'meta_info' : _MetaInfoClass('PceLspData.LspSummary.PeerLsPsInfo.LspSummary_',
            False, 
            [
            _MetaInfoClassMember('admin-up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of administratively up LSPs
                ''',
                'admin_up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('all-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of all LSPs
                ''',
                'all_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rsvp-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with RSVP setup type
                ''',
                'rsvp_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sr-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with Segment routing setup type
                ''',
                'sr_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of operational LSPs
                ''',
                'up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.LspSummary.PeerLsPsInfo' : {
        'meta_info' : _MetaInfoClass('PceLspData.LspSummary.PeerLsPsInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-summary', REFERENCE_CLASS, 'LspSummary_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.LspSummary.PeerLsPsInfo.LspSummary_', 
                [], [], 
                '''                Number of LSPs for specific peer
                ''',
                'lsp_summary',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-ls-ps-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.LspSummary' : {
        'meta_info' : _MetaInfoClass('PceLspData.LspSummary',
            False, 
            [
            _MetaInfoClassMember('all-ls-ps', REFERENCE_CLASS, 'AllLsPs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.LspSummary.AllLsPs', 
                [], [], 
                '''                Summary for all peers
                ''',
                'all_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-ls-ps-info', REFERENCE_LIST, 'PeerLsPsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.LspSummary.PeerLsPsInfo', 
                [], [], 
                '''                Number of LSPs for specific peer
                ''',
                'peer_ls_ps_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer',
            False, 
            [
            _MetaInfoClassMember('event-message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event message
                ''',
                'event_message',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Event time, relative to Jan 1, 1970
                ''',
                'time_stamp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'event-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation',
            False, 
            [
            _MetaInfoClassMember('event-buffer', REFERENCE_LIST, 'EventBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer', 
                [], [], 
                '''                LSP Event buffer
                ''',
                'event_buffer',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'private-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation',
            False, 
            [
            _MetaInfoClassMember('administrative-state', REFERENCE_ENUM_CLASS, 'LspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspStateEnum', 
                [], [], 
                '''                Admin state
                ''',
                'administrative_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('binding-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Binding SID
                ''',
                'binding_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-setup-type', REFERENCE_ENUM_CLASS, 'LspSetupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetupEnum', 
                [], [], 
                '''                LSP Setup Type
                ''',
                'lsp_setup_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('operational-state', REFERENCE_ENUM_CLASS, 'PcepLspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspStateEnum', 
                [], [], 
                '''                Operational state
                ''',
                'operational_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath',
            False, 
            [
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RSVP hop address
                ''',
                'hop_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'reported-rsvp-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath',
            False, 
            [
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'PceSrSidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSidEnum', 
                [], [], 
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'reported-sr-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath',
            False, 
            [
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RSVP hop address
                ''',
                'hop_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'computed-rsvp-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath',
            False, 
            [
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'PceSrSidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSidEnum', 
                [], [], 
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'computed-sr-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs',
            False, 
            [
            _MetaInfoClassMember('computed-hop-list-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computed Hop List Time
                ''',
                'computed_hop_list_time',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-metric-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computed Metric Type
                ''',
                'computed_metric_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-metric-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computed Metric Value
                ''',
                'computed_metric_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-rsvp-path', REFERENCE_LIST, 'ComputedRsvpPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath', 
                [], [], 
                '''                Computed RSVP path
                ''',
                'computed_rsvp_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-sr-path', REFERENCE_LIST, 'ComputedSrPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath', 
                [], [], 
                '''                Computed SR path
                ''',
                'computed_sr_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-metric-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reported Metric Type
                ''',
                'reported_metric_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-metric-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reported Metric Value
                ''',
                'reported_metric_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-rsvp-path', REFERENCE_LIST, 'ReportedRsvpPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath', 
                [], [], 
                '''                Reported RSVP path
                ''',
                'reported_rsvp_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-sr-path', REFERENCE_LIST, 'ReportedSrPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath', 
                [], [], 
                '''                Reported SR path
                ''',
                'reported_sr_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'er-os',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError',
            False, 
            [
            _MetaInfoClassMember('error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RSVP error code
                ''',
                'error_code',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('error-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RSVP error flags
                ''',
                'error_flags',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('error-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RSVP error value
                ''',
                'error_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RSVP error node address
                ''',
                'node_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'rsvp-error',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation',
            False, 
            [
            _MetaInfoClassMember('pcep-flag-a', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP admin flag
                ''',
                'pcep_flag_a',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-d', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP delegation flag
                ''',
                'pcep_flag_d',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-o', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP LSP operation flag
                ''',
                'pcep_flag_o',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-r', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP remove flag
                ''',
                'pcep_flag_r',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-s', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP state-sync flag
                ''',
                'pcep_flag_s',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcepid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCE protocol identifier
                ''',
                'pcepid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rsvp-error', REFERENCE_CLASS, 'RsvpError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError', 
                [], [], 
                '''                RSVP error info
                ''',
                'rsvp_error',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsppcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo',
            False, 
            [
            _MetaInfoClassMember('association-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association ID
                ''',
                'association_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Association Source
                ''',
                'association_source',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association Type
                ''',
                'association_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-association-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes',
            False, 
            [
            _MetaInfoClassMember('affinity-exclude-any', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Affinity exclude any
                ''',
                'affinity_exclude_any',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('affinity-include-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Affinity include all
                ''',
                'affinity_include_all',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('affinity-include-any', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Affinity include any
                ''',
                'affinity_include_any',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-protection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True, if local protection is desired
                ''',
                'local_protection',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro',
            False, 
            [
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'PceSrSidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSidEnum', 
                [], [], 
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sr-rro',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro',
            False, 
            [
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RRO Flags
                ''',
                'flags',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of RRO
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS label of RRO
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rro-type', REFERENCE_ENUM_CLASS, 'PceRroEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceRroEnum', 
                [], [], 
                '''                RRO Type
                ''',
                'rro_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sr-rro', REFERENCE_CLASS, 'SrRro' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro', 
                [], [], 
                '''                Segment Routing RRO info
                ''',
                'sr_rro',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'rro',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation',
            False, 
            [
            _MetaInfoClassMember('actual-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Actual bandwidth utilized in the data-plane
                ''',
                'actual_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('actual-bandwidth-specified', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if router notifies actual bandwidth
                ''',
                'actual_bandwidth_specified',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('brief-lsp-information', REFERENCE_CLASS, 'BriefLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation', 
                [], [], 
                '''                Brief LSP information
                ''',
                'brief_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computing-pce', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computing PCE
                ''',
                'computing_pce',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('er-os', REFERENCE_CLASS, 'ErOs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs', 
                [], [], 
                '''                Paths
                ''',
                'er_os',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-association-info', REFERENCE_CLASS, 'LspAssociationInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo', 
                [], [], 
                '''                LSP association information
                ''',
                'lsp_association_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-attributes', REFERENCE_CLASS, 'LspAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes', 
                [], [], 
                '''                LSP attributes
                ''',
                'lsp_attributes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Role
                ''',
                'lsp_role',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsppcep-information', REFERENCE_CLASS, 'LsppcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation', 
                [], [], 
                '''                PCEP related LSP information
                ''',
                'lsppcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reporting-pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Reporting PCC address
                ''',
                'reporting_pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rro', REFERENCE_LIST, 'Rro' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro', 
                [], [], 
                '''                RRO
                ''',
                'rro',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('signaled-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Signaled Bandwidth
                ''',
                'signaled_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('signaled-bandwidth-specified', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if router notifies signal bandwidth
                ''',
                'signaled_bandwidth_specified',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srlg-info', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of SLRGs used by LSP
                ''',
                'srlg_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('state-sync-pce', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                State-sync PCE
                ''',
                'state_sync_pce',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sub-delegated-pce', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Sub delegated PCE
                ''',
                'sub_delegated_pce',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'detail-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos.TunnelDetailInfo' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos.TunnelDetailInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('plsp-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCEP LSP ID
                ''',
                'plsp_id',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Tunnel name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('detail-lsp-information', REFERENCE_LIST, 'DetailLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation', 
                [], [], 
                '''                Detail LSP information
                ''',
                'detail_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCC address
                ''',
                'pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('private-lsp-information', REFERENCE_CLASS, 'PrivateLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation', 
                [], [], 
                '''                Private LSP information
                ''',
                'private_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData.TunnelDetailInfos' : {
        'meta_info' : _MetaInfoClass('PceLspData.TunnelDetailInfos',
            False, 
            [
            _MetaInfoClassMember('tunnel-detail-info', REFERENCE_LIST, 'TunnelDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos.TunnelDetailInfo', 
                [], [], 
                '''                Detailed tunnel information
                ''',
                'tunnel_detail_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-detail-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceLspData' : {
        'meta_info' : _MetaInfoClass('PceLspData',
            False, 
            [
            _MetaInfoClassMember('lsp-summary', REFERENCE_CLASS, 'LspSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.LspSummary', 
                [], [], 
                '''                LSP summary database in XTC
                ''',
                'lsp_summary',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-detail-infos', REFERENCE_CLASS, 'TunnelDetailInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelDetailInfos', 
                [], [], 
                '''                Detailed tunnel database in XTC
                ''',
                'tunnel_detail_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-infos', REFERENCE_CLASS, 'TunnelInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceLspData.TunnelInfos', 
                [], [], 
                '''                Tunnel database in XTC
                ''',
                'tunnel_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'pce-lsp-data',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation',
            False, 
            [
            _MetaInfoClassMember('capability-db-version', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DB version capability
                ''',
                'capability_db_version',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-delta-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delta Synchronization capability
                ''',
                'capability_delta_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-instantiate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Instantiation capability
                ''',
                'capability_instantiate',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-segment-routing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Segment Routing capability
                ''',
                'capability_segment_routing',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-triggered-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered Synchronization capability
                ''',
                'capability_triggered_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-update', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Update capability
                ''',
                'capability_update',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-state', REFERENCE_ENUM_CLASS, 'PcepStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepStateEnum', 
                [], [], 
                '''                PCEP State
                ''',
                'pcep_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-pcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx',
            False, 
            [
            _MetaInfoClassMember('pc-error-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error type
                ''',
                'pc_error_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pc-error-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error Value
                ''',
                'pc_error_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'last-error-rx',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx',
            False, 
            [
            _MetaInfoClassMember('pc-error-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error type
                ''',
                'pc_error_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pc-error-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error Value
                ''',
                'pc_error_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'last-error-tx',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation',
            False, 
            [
            _MetaInfoClassMember('brief-pcep-information', REFERENCE_CLASS, 'BriefPcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation', 
                [], [], 
                '''                Brief PCE protocol information
                ''',
                'brief_pcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error (for display only)
                ''',
                'error',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('keepalives', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive count
                ''',
                'keepalives',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('keychain-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keychain based Authentication Enabled
                ''',
                'keychain_enabled',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('last-error-rx', REFERENCE_CLASS, 'LastErrorRx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx', 
                [], [], 
                '''                Last PCError received
                ''',
                'last_error_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('last-error-tx', REFERENCE_CLASS, 'LastErrorTx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx', 
                [], [], 
                '''                Last PCError sent
                ''',
                'last_error_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local PCEP session ID
                ''',
                'local_session_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('maximum-dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maximum dead interval for the peer
                ''',
                'maximum_dead_interval',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('md5-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MD5 Authentication Enabled
                ''',
                'md5_enabled',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('minimum-keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum keepalive interval for the peer
                ''',
                'minimum_keepalive_interval',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('negotiated-dead-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated DT
                ''',
                'negotiated_dead_time',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('negotiated-local-keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated KA
                ''',
                'negotiated_local_keepalive',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('negotiated-remote-keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated KA
                ''',
                'negotiated_remote_keepalive',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-error-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEErr Rx
                ''',
                'pce_error_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-error-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEErr Tx
                ''',
                'pce_error_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-initiate-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEInit Rx
                ''',
                'pce_initiate_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-initiate-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEInit Tx
                ''',
                'pce_initiate_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-keepalive-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCE Keepalive Rx
                ''',
                'pce_keepalive_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-keepalive-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCE Keepalive Tx
                ''',
                'pce_keepalive_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-open-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEOpen Rx
                ''',
                'pce_open_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-open-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEOpen Tx
                ''',
                'pce_open_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-reply-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERep Rx
                ''',
                'pce_reply_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-reply-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERep Tx
                ''',
                'pce_reply_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-report-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERpt Rx
                ''',
                'pce_report_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-report-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERpt Tx
                ''',
                'pce_report_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-request-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEReq Rx
                ''',
                'pce_request_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-request-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEReq Tx
                ''',
                'pce_request_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-update-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEUpd Rx
                ''',
                'pce_update_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-update-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEUpd Tx
                ''',
                'pce_update_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-up-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEP Up Time
                ''',
                'pcep_up_time',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Remote PCEP session ID
                ''',
                'remote_session_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('speaker-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Speaker Entity ID
                ''',
                'speaker_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'detail-pcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerDetailInfos.PeerDetailInfo' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerDetailInfos.PeerDetailInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('detail-pcep-information', REFERENCE_CLASS, 'DetailPcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation', 
                [], [], 
                '''                Detailed PCE protocol information
                ''',
                'detail_pcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer address
                ''',
                'peer_address_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-protocol', REFERENCE_ENUM_CLASS, 'PceProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProtoEnum', 
                [], [], 
                '''                Protocol between PCE and peer
                ''',
                'peer_protocol',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerDetailInfos' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerDetailInfos',
            False, 
            [
            _MetaInfoClassMember('peer-detail-info', REFERENCE_LIST, 'PeerDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerDetailInfos.PeerDetailInfo', 
                [], [], 
                '''                Detailed PCE peer information
                ''',
                'peer_detail_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-detail-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerInfos.PeerInfo.BriefPcepInformation' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerInfos.PeerInfo.BriefPcepInformation',
            False, 
            [
            _MetaInfoClassMember('capability-db-version', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DB version capability
                ''',
                'capability_db_version',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-delta-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delta Synchronization capability
                ''',
                'capability_delta_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-instantiate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Instantiation capability
                ''',
                'capability_instantiate',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-segment-routing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Segment Routing capability
                ''',
                'capability_segment_routing',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-triggered-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered Synchronization capability
                ''',
                'capability_triggered_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-update', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Update capability
                ''',
                'capability_update',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-state', REFERENCE_ENUM_CLASS, 'PcepStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepStateEnum', 
                [], [], 
                '''                PCEP State
                ''',
                'pcep_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-pcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerInfos.PeerInfo' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerInfos.PeerInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('brief-pcep-information', REFERENCE_CLASS, 'BriefPcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerInfos.PeerInfo.BriefPcepInformation', 
                [], [], 
                '''                PCE protocol information
                ''',
                'brief_pcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer address
                ''',
                'peer_address_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-protocol', REFERENCE_ENUM_CLASS, 'PceProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProtoEnum', 
                [], [], 
                '''                Protocol between PCE and peer
                ''',
                'peer_protocol',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer.PeerInfos' : {
        'meta_info' : _MetaInfoClass('PcePeer.PeerInfos',
            False, 
            [
            _MetaInfoClassMember('peer-info', REFERENCE_LIST, 'PeerInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerInfos.PeerInfo', 
                [], [], 
                '''                PCE peer information
                ''',
                'peer_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PcePeer' : {
        'meta_info' : _MetaInfoClass('PcePeer',
            False, 
            [
            _MetaInfoClassMember('peer-detail-infos', REFERENCE_CLASS, 'PeerDetailInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerDetailInfos', 
                [], [], 
                '''                Detailed peers database in XTC
                ''',
                'peer_detail_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-infos', REFERENCE_CLASS, 'PeerInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcePeer.PeerInfos', 
                [], [], 
                '''                Peers database in XTC
                ''',
                'peer_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'pce-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologySummary.StatsTopologyUpdate' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologySummary.StatsTopologyUpdate',
            False, 
            [
            _MetaInfoClassMember('num-links-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links added
                ''',
                'num_links_added',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-links-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links deleted
                ''',
                'num_links_deleted',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-nodes-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes added
                ''',
                'num_nodes_added',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-nodes-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes deleted
                ''',
                'num_nodes_deleted',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-prefixes-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes added
                ''',
                'num_prefixes_added',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-prefixes-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes deleted
                ''',
                'num_prefixes_deleted',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'stats-topology-update',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologySummary' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologySummary',
            False, 
            [
            _MetaInfoClassMember('adjacency-sids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of adjacency SIDs
                ''',
                'adjacency_sids',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links
                ''',
                'links',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefix-sids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefix SIDs
                ''',
                'prefix_sids',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes
                ''',
                'prefixes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('stats-topology-update', REFERENCE_CLASS, 'StatsTopologyUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologySummary.StatsTopologyUpdate', 
                [], [], 
                '''                Statistics on topology update
                ''',
                'stats_topology_update',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('topology-consistent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if topology is consistent
                ''',
                'topology_consistent',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'topology-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sid-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.PrefixSid' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('eflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                E Flag
                ''',
                'eflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L Flag
                ''',
                'lflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                N Flag
                ''',
                'nflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P Flag
                ''',
                'pflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                R Flag
                ''',
                'rflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-prefix', REFERENCE_CLASS, 'SidPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix', 
                [], [], 
                '''                Prefix
                ''',
                'sid_prefix',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'SidEnum', 
                [], [], 
                '''                SID Type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('vflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V Flag
                ''',
                'vflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'local-igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'remote-node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sid-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('eflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                E Flag
                ''',
                'eflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L Flag
                ''',
                'lflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                N Flag
                ''',
                'nflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P Flag
                ''',
                'pflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                R Flag
                ''',
                'rflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-prefix', REFERENCE_CLASS, 'SidPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix', 
                [], [], 
                '''                Prefix
                ''',
                'sid_prefix',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'SidEnum', 
                [], [], 
                '''                SID Type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('vflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V Flag
                ''',
                'vflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'adjacency-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv4Link' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv4Link',
            False, 
            [
            _MetaInfoClassMember('adjacency-sid', REFERENCE_LIST, 'AdjacencySid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid', 
                [], [], 
                '''                Adjacency SIDs
                ''',
                'adjacency_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IGP Metric
                ''',
                'igp_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-igp-information', REFERENCE_CLASS, 'LocalIgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation', 
                [], [], 
                '''                Local node IGP information
                ''',
                'local_igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv4 address
                ''',
                'local_ipv4_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Reservable bandwidth
                ''',
                'max_reservable_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('maximum-link-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max link bandwidth
                ''',
                'maximum_link_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote IPv4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-node-protocol-identifier', REFERENCE_CLASS, 'RemoteNodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier', 
                [], [], 
                '''                Remote node protocol identifier
                ''',
                'remote_node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srlgs', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG Values
                ''',
                'srlgs',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE Metric
                ''',
                'te_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ipv4-link',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'local-igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'remote-node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sid-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('eflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                E Flag
                ''',
                'eflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L Flag
                ''',
                'lflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                N Flag
                ''',
                'nflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P Flag
                ''',
                'pflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                R Flag
                ''',
                'rflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-prefix', REFERENCE_CLASS, 'SidPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix', 
                [], [], 
                '''                Prefix
                ''',
                'sid_prefix',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'SidEnum', 
                [], [], 
                '''                SID Type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('vflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V Flag
                ''',
                'vflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'adjacency-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode.Ipv6Link' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode.Ipv6Link',
            False, 
            [
            _MetaInfoClassMember('adjacency-sid', REFERENCE_LIST, 'AdjacencySid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid', 
                [], [], 
                '''                Adjacency SIDs
                ''',
                'adjacency_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IGP Metric
                ''',
                'igp_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-igp-information', REFERENCE_CLASS, 'LocalIgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation', 
                [], [], 
                '''                Local node IGP information
                ''',
                'local_igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv6 address
                ''',
                'local_ipv6_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Reservable bandwidth
                ''',
                'max_reservable_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('maximum-link-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max link bandwidth
                ''',
                'maximum_link_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote IPv6 address
                ''',
                'remote_ipv6_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-node-protocol-identifier', REFERENCE_CLASS, 'RemoteNodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier', 
                [], [], 
                '''                Remote node protocol identifier
                ''',
                'remote_node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE Metric
                ''',
                'te_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ipv6-link',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes.TopologyNode' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes.TopologyNode',
            False, 
            [
            _MetaInfoClassMember('node-identifier', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Node Identifier
                ''',
                'node_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('ipv4-link', REFERENCE_LIST, 'Ipv4Link' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv4Link', 
                [], [], 
                '''                IPv4 Link information
                ''',
                'ipv4_link',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6-link', REFERENCE_LIST, 'Ipv6Link' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.Ipv6Link', 
                [], [], 
                '''                IPv6 Link information
                ''',
                'ipv6_link',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-identifier-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node identifier
                ''',
                'node_identifier_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-protocol-identifier', REFERENCE_CLASS, 'NodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier', 
                [], [], 
                '''                Node protocol identifier
                ''',
                'node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('overload', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Node Overload Bit
                ''',
                'overload',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_LIST, 'PrefixSid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode.PrefixSid', 
                [], [], 
                '''                Prefix SIDs
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'topology-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.TopologyNodes' : {
        'meta_info' : _MetaInfoClass('PceTopology.TopologyNodes',
            False, 
            [
            _MetaInfoClassMember('topology-node', REFERENCE_LIST, 'TopologyNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes.TopologyNode', 
                [], [], 
                '''                Node information
                ''',
                'topology_node',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'topology-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo.Address' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo.Address',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos.PrefixInfo' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos.PrefixInfo',
            False, 
            [
            _MetaInfoClassMember('node-identifier', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Node ID
                ''',
                'node_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.Address', 
                [], [], 
                '''                Prefix address
                ''',
                'address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-identifier-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node identifier
                ''',
                'node_identifier_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-protocol-identifier', REFERENCE_CLASS, 'NodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier', 
                [], [], 
                '''                Node protocol identifier
                ''',
                'node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'prefix-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology.PrefixInfos' : {
        'meta_info' : _MetaInfoClass('PceTopology.PrefixInfos',
            False, 
            [
            _MetaInfoClassMember('prefix-info', REFERENCE_LIST, 'PrefixInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos.PrefixInfo', 
                [], [], 
                '''                PCE prefix information
                ''',
                'prefix_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'prefix-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'PceTopology' : {
        'meta_info' : _MetaInfoClass('PceTopology',
            False, 
            [
            _MetaInfoClassMember('prefix-infos', REFERENCE_CLASS, 'PrefixInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.PrefixInfos', 
                [], [], 
                '''                Prefixes database in XTC
                ''',
                'prefix_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('topology-nodes', REFERENCE_CLASS, 'TopologyNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologyNodes', 
                [], [], 
                '''                Node database in XTC
                ''',
                'topology_nodes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('topology-summary', REFERENCE_CLASS, 'TopologySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceTopology.TopologySummary', 
                [], [], 
                '''                Node summary database in XTC
                ''',
                'topology_summary',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'pce-topology',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.AssociationInfos.AssociationInfo.AssociationLsp' : {
        'meta_info' : _MetaInfoClass('Pce.AssociationInfos.AssociationInfo.AssociationLsp',
            False, 
            [
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCC address
                ''',
                'pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-based', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCE Based
                ''',
                'pce_based',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('plsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PLSP ID
                ''',
                'plsp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'association-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.AssociationInfos.AssociationInfo' : {
        'meta_info' : _MetaInfoClass('Pce.AssociationInfos.AssociationInfo',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('association-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association ID
                ''',
                'association_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-lsp', REFERENCE_LIST, 'AssociationLsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.AssociationInfos.AssociationInfo.AssociationLsp', 
                [], [], 
                '''                Association LSP Info
                ''',
                'association_lsp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Association Source
                ''',
                'association_source',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association Type
                ''',
                'association_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('headends-swapped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Headends Swapped
                ''',
                'headends_swapped',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association Status
                ''',
                'status',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('strict', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Association Strict Mode
                ''',
                'strict',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sub-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sub ID
                ''',
                'sub_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'PceAssoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAssoEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'association-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.AssociationInfos' : {
        'meta_info' : _MetaInfoClass('Pce.AssociationInfos',
            False, 
            [
            _MetaInfoClassMember('association-info', REFERENCE_LIST, 'AssociationInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.AssociationInfos.AssociationInfo', 
                [], [], 
                '''                PCE Association information
                ''',
                'association_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'association-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologySummary.StatsTopologyUpdate' : {
        'meta_info' : _MetaInfoClass('Pce.TopologySummary.StatsTopologyUpdate',
            False, 
            [
            _MetaInfoClassMember('num-links-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links added
                ''',
                'num_links_added',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-links-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links deleted
                ''',
                'num_links_deleted',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-nodes-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes added
                ''',
                'num_nodes_added',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-nodes-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes deleted
                ''',
                'num_nodes_deleted',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-prefixes-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes added
                ''',
                'num_prefixes_added',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('num-prefixes-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes deleted
                ''',
                'num_prefixes_deleted',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'stats-topology-update',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologySummary' : {
        'meta_info' : _MetaInfoClass('Pce.TopologySummary',
            False, 
            [
            _MetaInfoClassMember('adjacency-sids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of adjacency SIDs
                ''',
                'adjacency_sids',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links
                ''',
                'links',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefix-sids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefix SIDs
                ''',
                'prefix_sids',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes
                ''',
                'prefixes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('stats-topology-update', REFERENCE_CLASS, 'StatsTopologyUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologySummary.StatsTopologyUpdate', 
                [], [], 
                '''                Statistics on topology update
                ''',
                'stats_topology_update',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('topology-consistent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if topology is consistent
                ''',
                'topology_consistent',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'topology-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelInfos.TunnelInfo.BriefLspInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelInfos.TunnelInfo.BriefLspInformation',
            False, 
            [
            _MetaInfoClassMember('administrative-state', REFERENCE_ENUM_CLASS, 'LspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspStateEnum', 
                [], [], 
                '''                Admin state
                ''',
                'administrative_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('binding-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Binding SID
                ''',
                'binding_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-setup-type', REFERENCE_ENUM_CLASS, 'LspSetupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetupEnum', 
                [], [], 
                '''                LSP Setup Type
                ''',
                'lsp_setup_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('operational-state', REFERENCE_ENUM_CLASS, 'PcepLspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspStateEnum', 
                [], [], 
                '''                Operational state
                ''',
                'operational_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelInfos.TunnelInfo' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelInfos.TunnelInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('plsp-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCEP LSP ID
                ''',
                'plsp_id',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Tunnel name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('brief-lsp-information', REFERENCE_LIST, 'BriefLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelInfos.TunnelInfo.BriefLspInformation', 
                [], [], 
                '''                Brief LSP information
                ''',
                'brief_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCC address
                ''',
                'pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelInfos' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelInfos',
            False, 
            [
            _MetaInfoClassMember('tunnel-info', REFERENCE_LIST, 'TunnelInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelInfos.TunnelInfo', 
                [], [], 
                '''                Tunnel information
                ''',
                'tunnel_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation' : {
        'meta_info' : _MetaInfoClass('Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation',
            False, 
            [
            _MetaInfoClassMember('capability-db-version', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DB version capability
                ''',
                'capability_db_version',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-delta-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delta Synchronization capability
                ''',
                'capability_delta_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-instantiate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Instantiation capability
                ''',
                'capability_instantiate',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-segment-routing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Segment Routing capability
                ''',
                'capability_segment_routing',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-triggered-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered Synchronization capability
                ''',
                'capability_triggered_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-update', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Update capability
                ''',
                'capability_update',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-state', REFERENCE_ENUM_CLASS, 'PcepStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepStateEnum', 
                [], [], 
                '''                PCEP State
                ''',
                'pcep_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-pcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx' : {
        'meta_info' : _MetaInfoClass('Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx',
            False, 
            [
            _MetaInfoClassMember('pc-error-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error type
                ''',
                'pc_error_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pc-error-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error Value
                ''',
                'pc_error_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'last-error-rx',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx' : {
        'meta_info' : _MetaInfoClass('Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx',
            False, 
            [
            _MetaInfoClassMember('pc-error-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error type
                ''',
                'pc_error_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pc-error-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP Error Value
                ''',
                'pc_error_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'last-error-tx',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation' : {
        'meta_info' : _MetaInfoClass('Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation',
            False, 
            [
            _MetaInfoClassMember('brief-pcep-information', REFERENCE_CLASS, 'BriefPcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation', 
                [], [], 
                '''                Brief PCE protocol information
                ''',
                'brief_pcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error (for display only)
                ''',
                'error',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('keepalives', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive count
                ''',
                'keepalives',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('keychain-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keychain based Authentication Enabled
                ''',
                'keychain_enabled',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('last-error-rx', REFERENCE_CLASS, 'LastErrorRx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx', 
                [], [], 
                '''                Last PCError received
                ''',
                'last_error_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('last-error-tx', REFERENCE_CLASS, 'LastErrorTx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx', 
                [], [], 
                '''                Last PCError sent
                ''',
                'last_error_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local PCEP session ID
                ''',
                'local_session_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('maximum-dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maximum dead interval for the peer
                ''',
                'maximum_dead_interval',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('md5-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MD5 Authentication Enabled
                ''',
                'md5_enabled',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('minimum-keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum keepalive interval for the peer
                ''',
                'minimum_keepalive_interval',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('negotiated-dead-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated DT
                ''',
                'negotiated_dead_time',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('negotiated-local-keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated KA
                ''',
                'negotiated_local_keepalive',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('negotiated-remote-keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Negotiated KA
                ''',
                'negotiated_remote_keepalive',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-error-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEErr Rx
                ''',
                'pce_error_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-error-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEErr Tx
                ''',
                'pce_error_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-initiate-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEInit Rx
                ''',
                'pce_initiate_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-initiate-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEInit Tx
                ''',
                'pce_initiate_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-keepalive-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCE Keepalive Rx
                ''',
                'pce_keepalive_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-keepalive-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCE Keepalive Tx
                ''',
                'pce_keepalive_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-open-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEOpen Rx
                ''',
                'pce_open_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-open-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEOpen Tx
                ''',
                'pce_open_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-reply-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERep Rx
                ''',
                'pce_reply_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-reply-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERep Tx
                ''',
                'pce_reply_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-report-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERpt Rx
                ''',
                'pce_report_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-report-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCERpt Tx
                ''',
                'pce_report_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-request-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEReq Rx
                ''',
                'pce_request_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-request-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEReq Tx
                ''',
                'pce_request_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-update-rx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEUpd Rx
                ''',
                'pce_update_rx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pce-update-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEUpd Tx
                ''',
                'pce_update_tx',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-up-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCEP Up Time
                ''',
                'pcep_up_time',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Remote PCEP session ID
                ''',
                'remote_session_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('speaker-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Speaker Entity ID
                ''',
                'speaker_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'detail-pcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerDetailInfos.PeerDetailInfo' : {
        'meta_info' : _MetaInfoClass('Pce.PeerDetailInfos.PeerDetailInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('detail-pcep-information', REFERENCE_CLASS, 'DetailPcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation', 
                [], [], 
                '''                Detailed PCE protocol information
                ''',
                'detail_pcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer address
                ''',
                'peer_address_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-protocol', REFERENCE_ENUM_CLASS, 'PceProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProtoEnum', 
                [], [], 
                '''                Protocol between PCE and peer
                ''',
                'peer_protocol',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerDetailInfos' : {
        'meta_info' : _MetaInfoClass('Pce.PeerDetailInfos',
            False, 
            [
            _MetaInfoClassMember('peer-detail-info', REFERENCE_LIST, 'PeerDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerDetailInfos.PeerDetailInfo', 
                [], [], 
                '''                Detailed PCE peer information
                ''',
                'peer_detail_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-detail-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sid-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('eflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                E Flag
                ''',
                'eflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L Flag
                ''',
                'lflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                N Flag
                ''',
                'nflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P Flag
                ''',
                'pflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                R Flag
                ''',
                'rflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-prefix', REFERENCE_CLASS, 'SidPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix', 
                [], [], 
                '''                Prefix
                ''',
                'sid_prefix',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'SidEnum', 
                [], [], 
                '''                SID Type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('vflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V Flag
                ''',
                'vflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'local-igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'remote-node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sid-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('eflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                E Flag
                ''',
                'eflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L Flag
                ''',
                'lflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                N Flag
                ''',
                'nflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P Flag
                ''',
                'pflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                R Flag
                ''',
                'rflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-prefix', REFERENCE_CLASS, 'SidPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix', 
                [], [], 
                '''                Prefix
                ''',
                'sid_prefix',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'SidEnum', 
                [], [], 
                '''                SID Type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('vflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V Flag
                ''',
                'vflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'adjacency-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv4Link' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv4Link',
            False, 
            [
            _MetaInfoClassMember('adjacency-sid', REFERENCE_LIST, 'AdjacencySid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid', 
                [], [], 
                '''                Adjacency SIDs
                ''',
                'adjacency_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IGP Metric
                ''',
                'igp_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-igp-information', REFERENCE_CLASS, 'LocalIgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation', 
                [], [], 
                '''                Local node IGP information
                ''',
                'local_igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv4 address
                ''',
                'local_ipv4_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Reservable bandwidth
                ''',
                'max_reservable_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('maximum-link-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max link bandwidth
                ''',
                'maximum_link_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote IPv4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-node-protocol-identifier', REFERENCE_CLASS, 'RemoteNodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier', 
                [], [], 
                '''                Remote node protocol identifier
                ''',
                'remote_node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srlgs', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG Values
                ''',
                'srlgs',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE Metric
                ''',
                'te_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ipv4-link',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'local-igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'remote-node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sid-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('eflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                E Flag
                ''',
                'eflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L Flag
                ''',
                'lflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('nflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                N Flag
                ''',
                'nflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P Flag
                ''',
                'pflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                R Flag
                ''',
                'rflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-prefix', REFERENCE_CLASS, 'SidPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix', 
                [], [], 
                '''                Prefix
                ''',
                'sid_prefix',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'SidEnum', 
                [], [], 
                '''                SID Type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('vflag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V Flag
                ''',
                'vflag',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'adjacency-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode.Ipv6Link' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode.Ipv6Link',
            False, 
            [
            _MetaInfoClassMember('adjacency-sid', REFERENCE_LIST, 'AdjacencySid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid', 
                [], [], 
                '''                Adjacency SIDs
                ''',
                'adjacency_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IGP Metric
                ''',
                'igp_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-igp-information', REFERENCE_CLASS, 'LocalIgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation', 
                [], [], 
                '''                Local node IGP information
                ''',
                'local_igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local IPv6 address
                ''',
                'local_ipv6_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Reservable bandwidth
                ''',
                'max_reservable_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('maximum-link-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max link bandwidth
                ''',
                'maximum_link_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote IPv6 address
                ''',
                'remote_ipv6_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-node-protocol-identifier', REFERENCE_CLASS, 'RemoteNodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier', 
                [], [], 
                '''                Remote node protocol identifier
                ''',
                'remote_node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE Metric
                ''',
                'te_metric',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ipv6-link',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes.TopologyNode' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes.TopologyNode',
            False, 
            [
            _MetaInfoClassMember('node-identifier', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Node Identifier
                ''',
                'node_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('ipv4-link', REFERENCE_LIST, 'Ipv4Link' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv4Link', 
                [], [], 
                '''                IPv4 Link information
                ''',
                'ipv4_link',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6-link', REFERENCE_LIST, 'Ipv6Link' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.Ipv6Link', 
                [], [], 
                '''                IPv6 Link information
                ''',
                'ipv6_link',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-identifier-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node identifier
                ''',
                'node_identifier_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-protocol-identifier', REFERENCE_CLASS, 'NodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier', 
                [], [], 
                '''                Node protocol identifier
                ''',
                'node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('overload', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Node Overload Bit
                ''',
                'overload',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_LIST, 'PrefixSid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode.PrefixSid', 
                [], [], 
                '''                Prefix SIDs
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'topology-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TopologyNodes' : {
        'meta_info' : _MetaInfoClass('Pce.TopologyNodes',
            False, 
            [
            _MetaInfoClassMember('topology-node', REFERENCE_LIST, 'TopologyNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes.TopologyNode', 
                [], [], 
                '''                Node information
                ''',
                'topology_node',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'topology-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation',
            False, 
            [
            _MetaInfoClassMember('domain-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Domain identifier
                ''',
                'domain_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISIS level
                ''',
                'level',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISIS system ID
                ''',
                'system_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf',
            False, 
            [
            _MetaInfoClassMember('area', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF area
                ''',
                'area',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OSPF router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp', 
                [], [], 
                '''                BGP information
                ''',
                'bgp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('igp-id', REFERENCE_ENUM_CLASS, 'PceIgpInfoIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoIdEnum', 
                [], [], 
                '''                IGP ID
                ''',
                'igp_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis', 
                [], [], 
                '''                ISIS information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf', 
                [], [], 
                '''                OSPF information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'igp-srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation',
            False, 
            [
            _MetaInfoClassMember('igp-srgb', REFERENCE_CLASS, 'IgpSrgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb', 
                [], [], 
                '''                IGP-specific information
                ''',
                'igp_srgb',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB size
                ''',
                'size',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRGB start
                ''',
                'start',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'srgb-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier',
            False, 
            [
            _MetaInfoClassMember('igp-information', REFERENCE_LIST, 'IgpInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation', 
                [], [], 
                '''                IGP information
                ''',
                'igp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 TE router ID
                ''',
                'ipv4bgp_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4bgp-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 BGP router ID is set
                ''',
                'ipv4bgp_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 BGP router ID
                ''',
                'ipv4te_router_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4te-router-id-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if IPv4 TE router ID is set
                ''',
                'ipv4te_router_id_set',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srgb-information', REFERENCE_LIST, 'SrgbInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation', 
                [], [], 
                '''                SRGB information
                ''',
                'srgb_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'node-protocol-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo.Address' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo.Address',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'PceAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfIdEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos.PrefixInfo' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos.PrefixInfo',
            False, 
            [
            _MetaInfoClassMember('node-identifier', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Node ID
                ''',
                'node_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.Address', 
                [], [], 
                '''                Prefix address
                ''',
                'address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-identifier-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node identifier
                ''',
                'node_identifier_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-protocol-identifier', REFERENCE_CLASS, 'NodeProtocolIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier', 
                [], [], 
                '''                Node protocol identifier
                ''',
                'node_protocol_identifier',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'prefix-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PrefixInfos' : {
        'meta_info' : _MetaInfoClass('Pce.PrefixInfos',
            False, 
            [
            _MetaInfoClassMember('prefix-info', REFERENCE_LIST, 'PrefixInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos.PrefixInfo', 
                [], [], 
                '''                PCE prefix information
                ''',
                'prefix_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'prefix-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.LspSummary.AllLsPs' : {
        'meta_info' : _MetaInfoClass('Pce.LspSummary.AllLsPs',
            False, 
            [
            _MetaInfoClassMember('admin-up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of administratively up LSPs
                ''',
                'admin_up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('all-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of all LSPs
                ''',
                'all_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rsvp-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with RSVP setup type
                ''',
                'rsvp_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sr-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with Segment routing setup type
                ''',
                'sr_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of operational LSPs
                ''',
                'up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'all-ls-ps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.LspSummary.PeerLsPsInfo.LspSummary_' : {
        'meta_info' : _MetaInfoClass('Pce.LspSummary.PeerLsPsInfo.LspSummary_',
            False, 
            [
            _MetaInfoClassMember('admin-up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of administratively up LSPs
                ''',
                'admin_up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('all-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of all LSPs
                ''',
                'all_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rsvp-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with RSVP setup type
                ''',
                'rsvp_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sr-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSPs with Segment routing setup type
                ''',
                'sr_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('up-ls-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of operational LSPs
                ''',
                'up_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.LspSummary.PeerLsPsInfo' : {
        'meta_info' : _MetaInfoClass('Pce.LspSummary.PeerLsPsInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-summary', REFERENCE_CLASS, 'LspSummary_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.LspSummary.PeerLsPsInfo.LspSummary_', 
                [], [], 
                '''                Number of LSPs for specific peer
                ''',
                'lsp_summary',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-ls-ps-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.LspSummary' : {
        'meta_info' : _MetaInfoClass('Pce.LspSummary',
            False, 
            [
            _MetaInfoClassMember('all-ls-ps', REFERENCE_CLASS, 'AllLsPs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.LspSummary.AllLsPs', 
                [], [], 
                '''                Summary for all peers
                ''',
                'all_ls_ps',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-ls-ps-info', REFERENCE_LIST, 'PeerLsPsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.LspSummary.PeerLsPsInfo', 
                [], [], 
                '''                Number of LSPs for specific peer
                ''',
                'peer_ls_ps_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerInfos.PeerInfo.BriefPcepInformation' : {
        'meta_info' : _MetaInfoClass('Pce.PeerInfos.PeerInfo.BriefPcepInformation',
            False, 
            [
            _MetaInfoClassMember('capability-db-version', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DB version capability
                ''',
                'capability_db_version',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-delta-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delta Synchronization capability
                ''',
                'capability_delta_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-instantiate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Instantiation capability
                ''',
                'capability_instantiate',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-segment-routing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Segment Routing capability
                ''',
                'capability_segment_routing',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-triggered-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered Synchronization capability
                ''',
                'capability_triggered_sync',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('capability-update', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Update capability
                ''',
                'capability_update',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-state', REFERENCE_ENUM_CLASS, 'PcepStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepStateEnum', 
                [], [], 
                '''                PCEP State
                ''',
                'pcep_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-pcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerInfos.PeerInfo' : {
        'meta_info' : _MetaInfoClass('Pce.PeerInfos.PeerInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('brief-pcep-information', REFERENCE_CLASS, 'BriefPcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerInfos.PeerInfo.BriefPcepInformation', 
                [], [], 
                '''                PCE protocol information
                ''',
                'brief_pcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer address
                ''',
                'peer_address_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-protocol', REFERENCE_ENUM_CLASS, 'PceProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProtoEnum', 
                [], [], 
                '''                Protocol between PCE and peer
                ''',
                'peer_protocol',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.PeerInfos' : {
        'meta_info' : _MetaInfoClass('Pce.PeerInfos',
            False, 
            [
            _MetaInfoClassMember('peer-info', REFERENCE_LIST, 'PeerInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerInfos.PeerInfo', 
                [], [], 
                '''                PCE peer information
                ''',
                'peer_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'peer-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer',
            False, 
            [
            _MetaInfoClassMember('event-message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event message
                ''',
                'event_message',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Event time, relative to Jan 1, 1970
                ''',
                'time_stamp',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'event-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation',
            False, 
            [
            _MetaInfoClassMember('event-buffer', REFERENCE_LIST, 'EventBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer', 
                [], [], 
                '''                LSP Event buffer
                ''',
                'event_buffer',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'private-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation',
            False, 
            [
            _MetaInfoClassMember('administrative-state', REFERENCE_ENUM_CLASS, 'LspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspStateEnum', 
                [], [], 
                '''                Admin state
                ''',
                'administrative_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('binding-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Binding SID
                ''',
                'binding_sid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-setup-type', REFERENCE_ENUM_CLASS, 'LspSetupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetupEnum', 
                [], [], 
                '''                LSP Setup Type
                ''',
                'lsp_setup_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('operational-state', REFERENCE_ENUM_CLASS, 'PcepLspStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspStateEnum', 
                [], [], 
                '''                Operational state
                ''',
                'operational_state',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'brief-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath',
            False, 
            [
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RSVP hop address
                ''',
                'hop_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'reported-rsvp-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath',
            False, 
            [
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'PceSrSidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSidEnum', 
                [], [], 
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'reported-sr-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath',
            False, 
            [
            _MetaInfoClassMember('hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RSVP hop address
                ''',
                'hop_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'computed-rsvp-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath',
            False, 
            [
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'PceSrSidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSidEnum', 
                [], [], 
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'computed-sr-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs',
            False, 
            [
            _MetaInfoClassMember('computed-hop-list-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computed Hop List Time
                ''',
                'computed_hop_list_time',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-metric-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computed Metric Type
                ''',
                'computed_metric_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-metric-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computed Metric Value
                ''',
                'computed_metric_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-rsvp-path', REFERENCE_LIST, 'ComputedRsvpPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath', 
                [], [], 
                '''                Computed RSVP path
                ''',
                'computed_rsvp_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computed-sr-path', REFERENCE_LIST, 'ComputedSrPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath', 
                [], [], 
                '''                Computed SR path
                ''',
                'computed_sr_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-metric-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reported Metric Type
                ''',
                'reported_metric_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-metric-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reported Metric Value
                ''',
                'reported_metric_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-rsvp-path', REFERENCE_LIST, 'ReportedRsvpPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath', 
                [], [], 
                '''                Reported RSVP path
                ''',
                'reported_rsvp_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reported-sr-path', REFERENCE_LIST, 'ReportedSrPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath', 
                [], [], 
                '''                Reported SR path
                ''',
                'reported_sr_path',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'er-os',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError',
            False, 
            [
            _MetaInfoClassMember('error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RSVP error code
                ''',
                'error_code',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('error-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RSVP error flags
                ''',
                'error_flags',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('error-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RSVP error value
                ''',
                'error_value',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('node-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RSVP error node address
                ''',
                'node_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'rsvp-error',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation',
            False, 
            [
            _MetaInfoClassMember('pcep-flag-a', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP admin flag
                ''',
                'pcep_flag_a',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-d', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP delegation flag
                ''',
                'pcep_flag_d',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-o', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCEP LSP operation flag
                ''',
                'pcep_flag_o',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-r', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP remove flag
                ''',
                'pcep_flag_r',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcep-flag-s', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCEP LSP state-sync flag
                ''',
                'pcep_flag_s',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcepid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCE protocol identifier
                ''',
                'pcepid',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rsvp-error', REFERENCE_CLASS, 'RsvpError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError', 
                [], [], 
                '''                RSVP error info
                ''',
                'rsvp_error',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsppcep-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo',
            False, 
            [
            _MetaInfoClassMember('association-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association ID
                ''',
                'association_id',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Association Source
                ''',
                'association_source',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('association-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Association Type
                ''',
                'association_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-association-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes',
            False, 
            [
            _MetaInfoClassMember('affinity-exclude-any', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Affinity exclude any
                ''',
                'affinity_exclude_any',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('affinity-include-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Affinity include all
                ''',
                'affinity_include_all',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('affinity-include-any', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Affinity include any
                ''',
                'affinity_include_any',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('local-protection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True, if local protection is desired
                ''',
                'local_protection',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'lsp-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro',
            False, 
            [
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'PceSrSidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSidEnum', 
                [], [], 
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'sr-rro',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro',
            False, 
            [
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RRO Flags
                ''',
                'flags',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of RRO
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS label of RRO
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rro-type', REFERENCE_ENUM_CLASS, 'PceRroEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceRroEnum', 
                [], [], 
                '''                RRO Type
                ''',
                'rro_type',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sr-rro', REFERENCE_CLASS, 'SrRro' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro', 
                [], [], 
                '''                Segment Routing RRO info
                ''',
                'sr_rro',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'rro',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation',
            False, 
            [
            _MetaInfoClassMember('actual-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Actual bandwidth utilized in the data-plane
                ''',
                'actual_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('actual-bandwidth-specified', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if router notifies actual bandwidth
                ''',
                'actual_bandwidth_specified',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('brief-lsp-information', REFERENCE_CLASS, 'BriefLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation', 
                [], [], 
                '''                Brief LSP information
                ''',
                'brief_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('computing-pce', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Computing PCE
                ''',
                'computing_pce',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('er-os', REFERENCE_CLASS, 'ErOs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs', 
                [], [], 
                '''                Paths
                ''',
                'er_os',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-association-info', REFERENCE_CLASS, 'LspAssociationInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo', 
                [], [], 
                '''                LSP association information
                ''',
                'lsp_association_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-attributes', REFERENCE_CLASS, 'LspAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes', 
                [], [], 
                '''                LSP attributes
                ''',
                'lsp_attributes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Role
                ''',
                'lsp_role',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsppcep-information', REFERENCE_CLASS, 'LsppcepInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation', 
                [], [], 
                '''                PCEP related LSP information
                ''',
                'lsppcep_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('reporting-pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Reporting PCC address
                ''',
                'reporting_pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('rro', REFERENCE_LIST, 'Rro' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro', 
                [], [], 
                '''                RRO
                ''',
                'rro',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('signaled-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Signaled Bandwidth
                ''',
                'signaled_bandwidth',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('signaled-bandwidth-specified', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if router notifies signal bandwidth
                ''',
                'signaled_bandwidth_specified',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('srlg-info', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of SLRGs used by LSP
                ''',
                'srlg_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('state-sync-pce', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                State-sync PCE
                ''',
                'state_sync_pce',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('sub-delegated-pce', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Sub delegated PCE
                ''',
                'sub_delegated_pce',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'detail-lsp-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos.TunnelDetailInfo' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos.TunnelDetailInfo',
            False, 
            [
            _MetaInfoClassMember('peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer Address
                ''',
                'peer_address',
                'Cisco-IOS-XR-infra-xtc-oper', True, [
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                    _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer Address
                        ''',
                        'peer_address',
                        'Cisco-IOS-XR-infra-xtc-oper', True),
                ]),
            _MetaInfoClassMember('plsp-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCEP LSP ID
                ''',
                'plsp_id',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Tunnel name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-infra-xtc-oper', True),
            _MetaInfoClassMember('detail-lsp-information', REFERENCE_LIST, 'DetailLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation', 
                [], [], 
                '''                Detail LSP information
                ''',
                'detail_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('pcc-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCC address
                ''',
                'pcc_address',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('private-lsp-information', REFERENCE_CLASS, 'PrivateLspInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation', 
                [], [], 
                '''                Private LSP information
                ''',
                'private_lsp_information',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name_xr',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce.TunnelDetailInfos' : {
        'meta_info' : _MetaInfoClass('Pce.TunnelDetailInfos',
            False, 
            [
            _MetaInfoClassMember('tunnel-detail-info', REFERENCE_LIST, 'TunnelDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos.TunnelDetailInfo', 
                [], [], 
                '''                Detailed tunnel information
                ''',
                'tunnel_detail_info',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'tunnel-detail-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
    'Pce' : {
        'meta_info' : _MetaInfoClass('Pce',
            False, 
            [
            _MetaInfoClassMember('association-infos', REFERENCE_CLASS, 'AssociationInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.AssociationInfos', 
                [], [], 
                '''                Associaition database in XTC
                ''',
                'association_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('lsp-summary', REFERENCE_CLASS, 'LspSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.LspSummary', 
                [], [], 
                '''                LSP summary database in XTC
                ''',
                'lsp_summary',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-detail-infos', REFERENCE_CLASS, 'PeerDetailInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerDetailInfos', 
                [], [], 
                '''                Detailed peers database in XTC
                ''',
                'peer_detail_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('peer-infos', REFERENCE_CLASS, 'PeerInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PeerInfos', 
                [], [], 
                '''                Peers database in XTC
                ''',
                'peer_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('prefix-infos', REFERENCE_CLASS, 'PrefixInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.PrefixInfos', 
                [], [], 
                '''                Prefixes database in XTC
                ''',
                'prefix_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('topology-nodes', REFERENCE_CLASS, 'TopologyNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologyNodes', 
                [], [], 
                '''                Node database in XTC
                ''',
                'topology_nodes',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('topology-summary', REFERENCE_CLASS, 'TopologySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TopologySummary', 
                [], [], 
                '''                Node summary database in XTC
                ''',
                'topology_summary',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-detail-infos', REFERENCE_CLASS, 'TunnelDetailInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelDetailInfos', 
                [], [], 
                '''                Detailed tunnel database in XTC
                ''',
                'tunnel_detail_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            _MetaInfoClassMember('tunnel-infos', REFERENCE_CLASS, 'TunnelInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Pce.TunnelInfos', 
                [], [], 
                '''                Tunnel database in XTC
                ''',
                'tunnel_infos',
                'Cisco-IOS-XR-infra-xtc-oper', False),
            ],
            'Cisco-IOS-XR-infra-xtc-oper',
            'pce',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper'
        ),
    },
}
_meta_table['PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation']['meta_info'].parent =_meta_table['PceLspData.TunnelInfos.TunnelInfo']['meta_info']
_meta_table['PceLspData.TunnelInfos.TunnelInfo']['meta_info'].parent =_meta_table['PceLspData.TunnelInfos']['meta_info']
_meta_table['PceLspData.LspSummary.PeerLsPsInfo.LspSummary_']['meta_info'].parent =_meta_table['PceLspData.LspSummary.PeerLsPsInfo']['meta_info']
_meta_table['PceLspData.LspSummary.AllLsPs']['meta_info'].parent =_meta_table['PceLspData.LspSummary']['meta_info']
_meta_table['PceLspData.LspSummary.PeerLsPsInfo']['meta_info'].parent =_meta_table['PceLspData.LspSummary']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos.TunnelDetailInfo']['meta_info'].parent =_meta_table['PceLspData.TunnelDetailInfos']['meta_info']
_meta_table['PceLspData.TunnelInfos']['meta_info'].parent =_meta_table['PceLspData']['meta_info']
_meta_table['PceLspData.LspSummary']['meta_info'].parent =_meta_table['PceLspData']['meta_info']
_meta_table['PceLspData.TunnelDetailInfos']['meta_info'].parent =_meta_table['PceLspData']['meta_info']
_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation']['meta_info'].parent =_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']
_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx']['meta_info'].parent =_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']
_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx']['meta_info'].parent =_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']
_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info'].parent =_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo']['meta_info']
_meta_table['PcePeer.PeerDetailInfos.PeerDetailInfo']['meta_info'].parent =_meta_table['PcePeer.PeerDetailInfos']['meta_info']
_meta_table['PcePeer.PeerInfos.PeerInfo.BriefPcepInformation']['meta_info'].parent =_meta_table['PcePeer.PeerInfos.PeerInfo']['meta_info']
_meta_table['PcePeer.PeerInfos.PeerInfo']['meta_info'].parent =_meta_table['PcePeer.PeerInfos']['meta_info']
_meta_table['PcePeer.PeerDetailInfos']['meta_info'].parent =_meta_table['PcePeer']['meta_info']
_meta_table['PcePeer.PeerInfos']['meta_info'].parent =_meta_table['PcePeer']['meta_info']
_meta_table['PceTopology.TopologySummary.StatsTopologyUpdate']['meta_info'].parent =_meta_table['PceTopology.TopologySummary']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.PrefixSid']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.PrefixSid']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv4Link']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode.Ipv6Link']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes.TopologyNode']['meta_info']
_meta_table['PceTopology.TopologyNodes.TopologyNode']['meta_info'].parent =_meta_table['PceTopology.TopologyNodes']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo.Address']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos.PrefixInfo']['meta_info']
_meta_table['PceTopology.PrefixInfos.PrefixInfo']['meta_info'].parent =_meta_table['PceTopology.PrefixInfos']['meta_info']
_meta_table['PceTopology.TopologySummary']['meta_info'].parent =_meta_table['PceTopology']['meta_info']
_meta_table['PceTopology.TopologyNodes']['meta_info'].parent =_meta_table['PceTopology']['meta_info']
_meta_table['PceTopology.PrefixInfos']['meta_info'].parent =_meta_table['PceTopology']['meta_info']
_meta_table['Pce.AssociationInfos.AssociationInfo.AssociationLsp']['meta_info'].parent =_meta_table['Pce.AssociationInfos.AssociationInfo']['meta_info']
_meta_table['Pce.AssociationInfos.AssociationInfo']['meta_info'].parent =_meta_table['Pce.AssociationInfos']['meta_info']
_meta_table['Pce.TopologySummary.StatsTopologyUpdate']['meta_info'].parent =_meta_table['Pce.TopologySummary']['meta_info']
_meta_table['Pce.TunnelInfos.TunnelInfo.BriefLspInformation']['meta_info'].parent =_meta_table['Pce.TunnelInfos.TunnelInfo']['meta_info']
_meta_table['Pce.TunnelInfos.TunnelInfo']['meta_info'].parent =_meta_table['Pce.TunnelInfos']['meta_info']
_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation']['meta_info'].parent =_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']
_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx']['meta_info'].parent =_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']
_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx']['meta_info'].parent =_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info']
_meta_table['Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation']['meta_info'].parent =_meta_table['Pce.PeerDetailInfos.PeerDetailInfo']['meta_info']
_meta_table['Pce.PeerDetailInfos.PeerDetailInfo']['meta_info'].parent =_meta_table['Pce.PeerDetailInfos']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.PrefixSid']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.PrefixSid']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv4Link']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode.Ipv6Link']['meta_info'].parent =_meta_table['Pce.TopologyNodes.TopologyNode']['meta_info']
_meta_table['Pce.TopologyNodes.TopologyNode']['meta_info'].parent =_meta_table['Pce.TopologyNodes']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo.Address']['meta_info'].parent =_meta_table['Pce.PrefixInfos.PrefixInfo']['meta_info']
_meta_table['Pce.PrefixInfos.PrefixInfo']['meta_info'].parent =_meta_table['Pce.PrefixInfos']['meta_info']
_meta_table['Pce.LspSummary.PeerLsPsInfo.LspSummary_']['meta_info'].parent =_meta_table['Pce.LspSummary.PeerLsPsInfo']['meta_info']
_meta_table['Pce.LspSummary.AllLsPs']['meta_info'].parent =_meta_table['Pce.LspSummary']['meta_info']
_meta_table['Pce.LspSummary.PeerLsPsInfo']['meta_info'].parent =_meta_table['Pce.LspSummary']['meta_info']
_meta_table['Pce.PeerInfos.PeerInfo.BriefPcepInformation']['meta_info'].parent =_meta_table['Pce.PeerInfos.PeerInfo']['meta_info']
_meta_table['Pce.PeerInfos.PeerInfo']['meta_info'].parent =_meta_table['Pce.PeerInfos']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo']['meta_info']
_meta_table['Pce.TunnelDetailInfos.TunnelDetailInfo']['meta_info'].parent =_meta_table['Pce.TunnelDetailInfos']['meta_info']
_meta_table['Pce.AssociationInfos']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.TopologySummary']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.TunnelInfos']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.PeerDetailInfos']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.TopologyNodes']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.PrefixInfos']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.LspSummary']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.PeerInfos']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.TunnelDetailInfos']['meta_info'].parent =_meta_table['Pce']['meta_info']
