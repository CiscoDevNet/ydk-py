


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IgpSyncStateEnum' : _MetaInfoEnum('IgpSyncStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'isync-ready':'isync_ready',
            'isync-not-ready':'isync_not_ready',
            'isync-deferred':'isync_deferred',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'LocalLabelStateEnum' : _MetaInfoEnum('LocalLabelStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'local-label-state-none':'local_label_state_none',
            'local-label-state-assigned':'local_label_state_assigned',
            'local-label-state-withdrawn':'local_label_state_withdrawn',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'SessionStateEnum' : _MetaInfoEnum('SessionStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'nonexistent':'nonexistent',
            'initialized':'initialized',
            'openrec':'openrec',
            'opensent':'opensent',
            'operational':'operational',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'AfIdEnum' : _MetaInfoEnum('AfIdEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'ldp-af-id-none':'ldp_af_id_none',
            'ldp-af-id-ipv4':'ldp_af_id_ipv4',
            'ldp-af-id-ipv6':'ldp_af_id_ipv6',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'LoopDetectionTypeEnum' : _MetaInfoEnum('LoopDetectionTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'none':'none',
            'other':'other',
            'hop-count':'hop_count',
            'path-vector':'path_vector',
            'hop-count-and-path-vector':'hop_count_and_path_vector',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'IccpStateEnum' : _MetaInfoEnum('IccpStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'nonexistent':'nonexistent',
            'initialized':'initialized',
            'capsent':'capsent',
            'caprec':'caprec',
            'connecting':'connecting',
            'operational':'operational',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'AdvLabelTypeEnum' : _MetaInfoEnum('AdvLabelTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'use-lable':'use_lable',
            'use-explicit':'use_explicit',
            'use-implicit':'use_implicit',
            'none':'none',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'NbrBgpAdvtStateEnum' : _MetaInfoEnum('NbrBgpAdvtStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'not-applicable':'not_applicable',
            'permit':'permit',
            'deny':'deny',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'AfEnum' : _MetaInfoEnum('AfEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'ldp-af-none':'ldp_af_none',
            'ldp-af-ipv4':'ldp_af_ipv4',
            'ldp-af-ipv6':'ldp_af_ipv6',
            'ldp-af-ipv4-ipv6':'ldp_af_ipv4_ipv6',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'AdjStateEnum' : _MetaInfoEnum('AdjStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'nonex':'nonex',
            'unsol-op-pdg':'unsol_op_pdg',
            'deferred':'deferred',
            'estab':'estab',
            'lib-exp-wait':'lib_exp_wait',
            'destroyed':'destroyed',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'DhcStateEnum' : _MetaInfoEnum('DhcStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'none':'none',
            'dhc-active':'dhc_active',
            'dhc-passive':'dhc_passive',
            'dhc-active-passive':'dhc_active_passive',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'LabelTypeIdentity' : {
        'meta_info' : _MetaInfoClass('LabelTypeIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathLblOwnerIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathLblOwnerIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-lbl-owner',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncStateIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncStateIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-state',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathTypeIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathTypeIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-type',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrStatusIdentity' : {
        'meta_info' : _MetaInfoClass('NsrStatusIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-status',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IcpmTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IcpmTypeIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-type',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'DownNbrReasonIdentity' : {
        'meta_info' : _MetaInfoClass('DownNbrReasonIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'down-nbr-reason',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IccpTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IccpTypeIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'iccp-type',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.OperSummary.Common' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.OperSummary.Common',
            False, 
            [
            _MetaInfoClassMember('address-families', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Families enabled
                ''',
                'address_families',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-downstream-on-demand-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Downstream-On-Demand neighbor
                ''',
                'number_of_downstream_on_demand_neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-graceful-restart-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Graceful Restart neighbor
                ''',
                'number_of_graceful_restart_neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ipv4-local-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 local addresses.
                ''',
                'number_of_ipv4_local_addresses',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ipv4-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of resolved IPv4 routes
                ''',
                'number_of_ipv4_routes',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ipv4ldp-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LDP IPv4 configured interfaces
                ''',
                'number_of_ipv4ldp_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ldp-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LDP configured interfaces
                ''',
                'number_of_ldp_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor
                ''',
                'number_of_neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('numberof-ipv4-hello-adj', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LDP discovery IPv4 hello adjacencies
                ''',
                'numberof_ipv4_hello_adj',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'common',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.OperSummary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.OperSummary',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.OperSummary.Common', 
                [], [], 
                '''                Common Summary information
                ''',
                'common',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('no-of-ipv4-rib-tbl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of ipv4 RIB tables
                ''',
                'no_of_ipv4_rib_tbl',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('no-of-ipv4-rib-tbl-reg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ipv4 RIB tables registered
                ''',
                'no_of_ipv4_rib_tbl_reg',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-autocfg-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of auto-configured interfaces.
                ''',
                'number_of_autocfg_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-fwd-ref-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Forward Reference interfaces.
                ''',
                'number_of_fwd_ref_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of known interfaces
                ''',
                'number_of_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-vrf', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of configured VRFs (including default)
                ''',
                'number_of_vrf',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-vrf-oper', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of configured operational VRFs (including
                default)
                ''',
                'number_of_vrf_oper',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'oper-summary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr',
            False, 
            [
            _MetaInfoClassMember('labeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with 1 or more paths
                labeled
                ''',
                'labeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with some (but not
                ALL) paths labeled
                ''',
                'labeled_pfxs_partial',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unlabeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with ALL paths
                unlabeled
                ''',
                'unlabeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'labeled-pfxs-aggr',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary',
            False, 
            [
            _MetaInfoClassMember('labeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with 1 or more paths
                labeled
                ''',
                'labeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with some (but not
                ALL) paths labeled
                ''',
                'labeled_pfxs_partial',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unlabeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with ALL paths
                unlabeled
                ''',
                'unlabeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'labeled-pfxs-primary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup',
            False, 
            [
            _MetaInfoClassMember('labeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with 1 or more paths
                labeled
                ''',
                'labeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with some (but not
                ALL) paths labeled
                ''',
                'labeled_pfxs_partial',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unlabeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with ALL paths
                unlabeled
                ''',
                'unlabeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'labeled-pfxs-backup',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.ForwardingSummary.Pfxs',
            False, 
            [
            _MetaInfoClassMember('ecmp-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of prefixes with ECMP
                ''',
                'ecmp_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-aggr', REFERENCE_CLASS, 'LabeledPfxsAggr' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr', 
                [], [], 
                '''                Labeled prefix count for all paths
                ''',
                'labeled_pfxs_aggr',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-backup', REFERENCE_CLASS, 'LabeledPfxsBackup' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup', 
                [], [], 
                '''                Labeled prefix count related to backup paths
                only
                ''',
                'labeled_pfxs_backup',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-primary', REFERENCE_CLASS, 'LabeledPfxsPrimary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary', 
                [], [], 
                '''                Labeled prefix count related to primary paths
                only
                ''',
                'labeled_pfxs_primary',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protected-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of FRR protected prefixes
                ''',
                'protected_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('total-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total Prefix count
                ''',
                'total_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'pfxs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.ForwardingSummary.Nhs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.ForwardingSummary.Nhs',
            False, 
            [
            _MetaInfoClassMember('backup-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of non-primary backup paths
                ''',
                'backup_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-backup-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of labeled backup paths
                ''',
                'labeled_backup_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of all labeled paths
                ''',
                'labeled_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protected-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of FRR protected paths
                ''',
                'protected_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('remote-backup-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of non-primary remote backup paths
                ''',
                'remote_backup_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('total-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total path count
                ''',
                'total_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nhs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.ForwardingSummary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.ForwardingSummary',
            False, 
            [
            _MetaInfoClassMember('intfs-fwd-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MPLS forwarding enabled interface count.
                ''',
                'intfs_fwd_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-lbls', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local label allocated count.
                ''',
                'local_lbls',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nhs', REFERENCE_CLASS, 'Nhs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.ForwardingSummary.Nhs', 
                [], [], 
                '''                MPLS LDP forwarding rewrite next-hop/path summary
                ''',
                'nhs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('pfxs', REFERENCE_CLASS, 'Pfxs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.ForwardingSummary.Pfxs', 
                [], [], 
                '''                MPLS LDP forwarding prefix rewrite summary
                ''',
                'pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'forwarding-summary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.BindingsSummary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.BindingsSummary',
            False, 
            [
            _MetaInfoClassMember('binding-local', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local bindings
                ''',
                'binding_local',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-explicit-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local explicit null bindings
                ''',
                'binding_local_explicit_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-implicit-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local implicit null bindings
                ''',
                'binding_local_implicit_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-no-route', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local bindings with no route
                ''',
                'binding_local_no_route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-non-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local non-null bindings
                ''',
                'binding_local_non_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local null bindings
                ''',
                'binding_local_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-oor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the number of local bindings needing label but which
                hit the Out-Of-Resource condition.
                ''',
                'binding_local_oor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-no-route', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bindings with no route
                ''',
                'binding_no_route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-remote', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of remote bindings
                ''',
                'binding_remote',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total bindings
                ''',
                'binding_total',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('highest-allocated-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest allocated label
                ''',
                'highest_allocated_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lowest-allocated-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest allocated label
                ''',
                'lowest_allocated_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'bindings-summary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.NsrSummaryAll' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.NsrSummaryAll',
            False, 
            [
            _MetaInfoClassMember('nsr-sum-in-label-reqs-created', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Request Records created.
                ''',
                'nsr_sum_in_label_reqs_created',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-sum-in-label-reqs-freed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Request Records freed.
                ''',
                'nsr_sum_in_label_reqs_freed',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-sum-in-label-withdraw-created', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Withdraw Records created.
                ''',
                'nsr_sum_in_label_withdraw_created',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-sum-in-label-withdraw-freed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Withdraw Records freed.
                ''',
                'nsr_sum_in_label_withdraw_freed',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-sum-lcl-addr-withdraw-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Address Withdraw cleared.
                ''',
                'nsr_sum_lcl_addr_withdraw_cleared',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-sum-lcl-addr-withdraw-set', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Address Withdraw set.
                ''',
                'nsr_sum_lcl_addr_withdraw_set',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-summary-all',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps',
            False, 
            [
            _MetaInfoClassMember('iccp-app', REFERENCE_IDENTITY_CLASS, 'IccpTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IccpTypeIdentity', 
                [], [], 
                '''                ICCP App Type.
                ''',
                'iccp_app',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('app-state', REFERENCE_ENUM_CLASS, 'IccpStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IccpStateEnum', 
                [], [], 
                '''                App State.
                ''',
                'app_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('ptcl-ver', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP App Protocol Version.
                ''',
                'ptcl_ver',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'iccp-apps',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups',
            False, 
            [
            _MetaInfoClassMember('rg-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Redundancy Group Identifier.
                ''',
                'rg_id',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('client_id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client Identifier.
                ''',
                'client_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-apps', REFERENCE_LIST, 'IccpApps' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps', 
                [], [], 
                '''                List of apps
                ''',
                'iccp_apps',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR identifier.
                ''',
                'peer_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('peer-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier.
                        ''',
                        'peer_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('peer-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier.
                        ''',
                        'peer_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ICCP State
                ''',
                'state',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'redun-groups',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols',
            False, 
            [
            _MetaInfoClassMember('icpm-type', REFERENCE_IDENTITY_CLASS, 'IcpmTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IcpmTypeIdentity', 
                [], [], 
                '''                ICPM Type.
                ''',
                'icpm_type',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('redun-groups', REFERENCE_LIST, 'RedunGroups' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups', 
                [], [], 
                '''                List of Redundancy Groups
                ''',
                'redun_groups',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-protocols',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup',
            False, 
            [
            _MetaInfoClassMember('rg-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the ICPM RG identifier.
                ''',
                'rg_id',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('icpm-protocols', REFERENCE_LIST, 'IcpmProtocols' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols', 
                [], [], 
                '''                This list contains all active icpm protocols.
                ''',
                'icpm_protocols',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'red-group',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo',
            False, 
            [
            _MetaInfoClassMember('red-group', REFERENCE_LIST, 'RedGroup' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup', 
                [], [], 
                '''                This is the data for an individual ICPM Rredundandy
                Group,
                ''',
                'red_group',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-rgid-table-info',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps',
            False, 
            [
            _MetaInfoClassMember('iccp-app', REFERENCE_IDENTITY_CLASS, 'IccpTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IccpTypeIdentity', 
                [], [], 
                '''                ICCP App Type.
                ''',
                'iccp_app',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('app-state', REFERENCE_ENUM_CLASS, 'IccpStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IccpStateEnum', 
                [], [], 
                '''                App State.
                ''',
                'app_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('ptcl-ver', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP App Protocol Version.
                ''',
                'ptcl_ver',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'iccp-apps',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups',
            False, 
            [
            _MetaInfoClassMember('rg-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Redundancy Group Identifier.
                ''',
                'rg_id',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('client_id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client Identifier.
                ''',
                'client_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-apps', REFERENCE_LIST, 'IccpApps' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps', 
                [], [], 
                '''                List of apps
                ''',
                'iccp_apps',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR identifier.
                ''',
                'peer_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('peer-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier.
                        ''',
                        'peer_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('peer-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier.
                        ''',
                        'peer_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ICCP State
                ''',
                'state',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'redun-groups',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols',
            False, 
            [
            _MetaInfoClassMember('icpm-type', REFERENCE_IDENTITY_CLASS, 'IcpmTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IcpmTypeIdentity', 
                [], [], 
                '''                ICPM Type.
                ''',
                'icpm_type',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('redun-groups', REFERENCE_LIST, 'RedunGroups' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups', 
                [], [], 
                '''                List of Redundancy Groups
                ''',
                'redun_groups',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-protocols',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the ICPM sesion identifier.
                ''',
                'session_id',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('icpm-protocols', REFERENCE_LIST, 'IcpmProtocols' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols', 
                [], [], 
                '''                This list contains all active icpm protocols.
                ''',
                'icpm_protocols',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'session-table',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable',
            False, 
            [
            _MetaInfoClassMember('session-table', REFERENCE_LIST, 'SessionTable' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable', 
                [], [], 
                '''                ICPM LDP Session Table
                ''',
                'session_table',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-session-table',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.IcpmSummaryAll' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.IcpmSummaryAll',
            False, 
            [
            _MetaInfoClassMember('iccp-rg-app-data-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG App Data count
                ''',
                'iccp_rg_app_data_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-conn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Connect count
                ''',
                'iccp_rg_conn_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-disconn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Disconnect count
                ''',
                'iccp_rg_disconn_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-notif-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Notif count
                ''',
                'iccp_rg_notif_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('icpm-rgid-table-info', REFERENCE_CLASS, 'IcpmRgidTableInfo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo', 
                [], [], 
                '''                This defines the ICPM RGID Table
                ''',
                'icpm_rgid_table_info',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('icpm-session-table', REFERENCE_CLASS, 'IcpmSessionTable' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable', 
                [], [], 
                '''                This is a list of ICPM sessions.
                ''',
                'icpm_session_table',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-summary-all',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family
                ''',
                'address_family',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('discovery-transport-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the Discovery transport address.
                ''',
                'discovery_transport_address',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('discovery-transport-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the Discovery transport address.
                        ''',
                        'discovery_transport_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('discovery-transport-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the Discovery transport address.
                        ''',
                        'discovery_transport_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('is-accepting-targeted-hellos', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Accepting targeted Hellos
                ''',
                'is_accepting_targeted_hellos',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('targeted-hello-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the filter name for targeted hellos.
                The filter type is device specific and could be
                an ACL, a prefix list, or other mechanism.
                ''',
                'targeted_hello_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'address-family-parameter',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Parameters' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Parameters',
            False, 
            [
            _MetaInfoClassMember('address-family-parameter', REFERENCE_LIST, 'AddressFamilyParameter' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter', 
                [], [], 
                '''                Per AF parameters
                ''',
                'address_family_parameter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('af-binding-withdraw-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay (sec) in Binding Withdrawal for an Address
                Family
                ''',
                'af_binding_withdraw_delay',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('discovery-quick-start-disabled-on-interfaces', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discovery quick-start disabled on some
                enabled interfaces
                ''',
                'discovery_quick_start_disabled_on_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('dod-max-hop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of hops for Downstream-on-Demand.
                ''',
                'dod_max_hop',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('feature', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                This entry describes an LDP feature available on the
                device. This does not indicate whether the feature
                is enabled, just the raw ability to support the
                feature. The features may include, but are not
                limited to: 'Auto-Configuration', 'Basic', 'ICPM',
                'IP-over-MPLS', 'IGP-Sync', 'LLAF',
                'TCP-MD5-Rollover', 'TDP', and 'NSR'.
                ''',
                'feature',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('global-md5-password-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Global MD5 password enabled
                ''',
                'global_md5_password_enabled',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive interval in seconds.
                ''',
                'keepalive_interval',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('le-no-route-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LIB entry no route timeout in second.
                ''',
                'le_no_route_timeout',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('loop-detection', REFERENCE_ENUM_CLASS, 'LoopDetectionTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'LoopDetectionTypeEnum', 
                [], [], 
                '''                A indication of whether this LSR has enabled loop
                detection. Since Loop Detection is determined during
                Session Initialization, an individual session
                may not be running with loop detection.  This
                object simply gives an indication of whether or not the
                LSR has the ability enabled to support Loop Detection
                and which types.
                ''',
                'loop_detection',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('max-intf-attached', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of LDP enabled attached
                interfaces
                ''',
                'max_intf_attached',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('max-intf-te', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of LDP enabled TE interfaces
                ''',
                'max_intf_te',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('max-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of LDP peers
                ''',
                'max_peer',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-of-mem-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is a counter of the number of times LDP
                attempted to create a label or binding and
                failed due a memory allocation failure.
                ''',
                'out_of_mem_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protocol-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol version
                ''',
                'protocol_version',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session hold time in seconds.
                ''',
                'session_hold_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'parameters',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Capabilities.Capability' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Capabilities.Capability',
            False, 
            [
            _MetaInfoClassMember('cap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Capability type (IANA assigned)
                ''',
                'cap_type',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('cap-des', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                Capability description
                ''',
                'cap_des',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-data', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capability data
                ''',
                'capability_data',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Capability data length
                ''',
                'capability_data_length',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-owner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capability owner
                ''',
                'capability_owner',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'capability',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Capabilities' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Capabilities',
            False, 
            [
            _MetaInfoClassMember('capability', REFERENCE_LIST, 'Capability' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Capabilities.Capability', 
                [], [], 
                '''                Information on LDP capability
                ''',
                'capability',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'capabilities',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.BackoffParameters' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.BackoffParameters',
            False, 
            [
            _MetaInfoClassMember('backoff-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current backoff seconds count.
                ''',
                'backoff_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('initial-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initial backoff value in seconds.
                ''',
                'initial_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('maximum-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum backoff value in seconds.
                ''',
                'maximum_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('waiting-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current backoff waiting seconds count.
                ''',
                'waiting_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'backoff-parameters',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('forwarding-state-hold-timer-remaining-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Forwarding state hold timer remaining time in
                seconds
                ''',
                'forwarding_state_hold_timer_remaining_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('graceful-restart-forwarding-state-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Graceful restart forward state hold time in
                seconds.
                ''',
                'graceful_restart_forwarding_state_hold_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('graceful-restart-reconnect-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reconnect timeout value in seconds.
                ''',
                'graceful_restart_reconnect_timeout',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-forwarding-state-hold-timer-running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Is graceful restart forwarding state hold timer
                running
                ''',
                'is_forwarding_state_hold_timer_running',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-graceful-restart-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is graceful restart configured
                ''',
                'is_graceful_restart_configured',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('address-families', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Families enabled
                ''',
                'address_families',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-downstream-on-demand-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Downstream-On-Demand neighbor
                ''',
                'number_of_downstream_on_demand_neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-graceful-restart-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Graceful Restart neighbor
                ''',
                'number_of_graceful_restart_neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ipv4-local-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 local addresses.
                ''',
                'number_of_ipv4_local_addresses',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ipv4-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of resolved IPv4 routes
                ''',
                'number_of_ipv4_routes',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ipv4ldp-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LDP IPv4 configured interfaces
                ''',
                'number_of_ipv4ldp_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-ldp-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LDP configured interfaces
                ''',
                'number_of_ldp_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('number-of-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor
                ''',
                'number_of_neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('numberof-ipv4-hello-adj', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LDP discovery IPv4 hello adjacencies
                ''',
                'numberof_ipv4_hello_adj',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('auto-config', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Auto-configured interfaces.
                ''',
                'auto_config',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('auto-config-disabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Autoconfigure disabled
                ''',
                'auto_config_disabled',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('auto-config-forward-reference-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Auto-configured forward references
                ''',
                'auto_config_forward_reference_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('configured-attached-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of attached interfaces configured in
                LDP
                ''',
                'configured_attached_interface',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('configured-te-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE tunnel interfaces configured in
                LDP
                ''',
                'configured_te_interface',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('forward-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of forward referenced interfaces
                ''',
                'forward_references',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('known-ip-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of known IP Interfaces
                ''',
                'known_ip_interface_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('known-ip-interface-ldp-enabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of known IP Interfaces with LDP Enabled
                ''',
                'known_ip_interface_ldp_enabled',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers',
            False, 
            [
            _MetaInfoClassMember('is-chkpt-created', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This is set if this peer was created due to
                check-pointing
                ''',
                'is_chkpt_created',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-gr-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is GR enabled session
                ''',
                'is_gr_enabled',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer Identifier
                ''',
                'peer_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This leaf contains the interface name for the
                IGP Synchronization information.
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('delay-timer-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining timer (seconds) until expiry of sync
                delay timer.
                ''',
                'delay_timer_remaining',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('igp-sync-down-reason', REFERENCE_IDENTITY_CLASS, 'IgpSyncDownReasonIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IgpSyncDownReasonIdentity', 
                [], [], 
                '''                Reason IGP Sync Not Achieved
                ''',
                'igp_sync_down_reason',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('igp-sync-state', REFERENCE_ENUM_CLASS, 'IgpSyncStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'IgpSyncStateEnum', 
                [], [], 
                '''                IGP Sync state
                ''',
                'igp_sync_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-delay-timer-running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This is set when the sync delay timer
                running.
                ''',
                'is_delay_timer_running',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peers', REFERENCE_LIST, 'Peers' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers', 
                [], [], 
                '''                MPLS LDP IGP Sync Interface Peer Information
                ''',
                'peers',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'sync',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp',
            False, 
            [
            _MetaInfoClassMember('sync', REFERENCE_LIST, 'Sync' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync', 
                [], [], 
                '''                LDP-IGP Synchronization related information
                for an interface
                ''',
                'sync',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family name.
                ''',
                'af_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp', 
                [], [], 
                '''                LDP IGP Synchronization related information
                ''',
                'igp',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('interface-summary', REFERENCE_CLASS, 'InterfaceSummary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary', 
                [], [], 
                '''                This container holds a summary of information
                across all interfaces in this AF,
                ''',
                'interface_summary',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af', 
                [], [], 
                '''                MPLS LDP Operational data for this Address Family.
                ''',
                'af',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.Afs', 
                [], [], 
                '''                Address Family specific operational data
                ''',
                'afs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('vrf-summary', REFERENCE_CLASS, 'VrfSummary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary', 
                [], [], 
                '''                MPLS LDP per VRF summarized Information
                ''',
                'vrf_summary',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Vrfs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs.Vrf', 
                [], [], 
                '''                MPLS LDP Operational data for a given VRF.
                ''',
                'vrf',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Discovery.DiscoveryStats' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Discovery.DiscoveryStats',
            False, 
            [
            _MetaInfoClassMember('num-of-active-ldp-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of active LDP enabled interfaces
                ''',
                'num_of_active_ldp_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-ldp-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of LDP configured interfaces.
                ''',
                'num_of_ldp_interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-lnk-disc-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of link hello discoveries in recv state
                ''',
                'num_of_lnk_disc_recv',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-lnk-disc-xmit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of link hello discoveries in xmit state
                ''',
                'num_of_lnk_disc_xmit',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-tgt-disc-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of targeted hello discoveries in recv
                state
                ''',
                'num_of_tgt_disc_recv',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-tgt-disc-xmit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of targeted hello discoveries in xmit
                state
                ''',
                'num_of_tgt_disc_xmit',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'discovery-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Discovery Interface
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('nbr-transport-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the MPLS LDP Hello Neighbor transport
                address.
                ''',
                'nbr_transport_addr',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('nbr-transport-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Hello Neighbor transport
                        address.
                        ''',
                        'nbr_transport_addr',
                        'Cisco-IOS-XE-mpls-ldp', True),
                    _MetaInfoClassMember('nbr-transport-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Hello Neighbor transport
                        address.
                        ''',
                        'nbr_transport_addr',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello interval in seconds. This is the value
                used to send hello messages.
                ''',
                'hello_interval',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('hold-time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This is the MPLS LDP Hello Discovery expiry time
                in seconds.
                If the value of this object is 65535,
                this means that the hold time is infinite
                (i.e., wait forever).
                
                Otherwise, the time remaining for
                this Hello Adjacency to receive its
                next Hello Message.
                
                This interval will change when the 'next'
                Hello Message which corresponds to this
                Hello Adjacency is received unless it
                is infinite.
                ''',
                'hold_time_remaining',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-src-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                MPLS LDP Discovery Local source address
                ''',
                'local_src_addr',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('local-src-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        MPLS LDP Discovery Local source address
                        ''',
                        'local_src_addr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('local-src-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        MPLS LDP Discovery Local source address
                        ''',
                        'local_src_addr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('local-transport-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                MPLS LDP Discovery Local transport address
                ''',
                'local_transport_addr',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('local-transport-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        MPLS LDP Discovery Local transport address
                        ''',
                        'local_transport_addr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('local-transport-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        MPLS LDP Discovery Local transport address
                        ''',
                        'local_transport_addr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('nbr-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Hello hold time which is negotiated between
                the Entity and the Peer.  The entity associated
                with this Hello Adjacency issues a proposed
                Hello Hold Time value in the
                EntityHelloHoldTimer object.  The peer
                also proposes a value and this object represents
                the negotiated value.
                
                A value of 0 means the default,
                which is 15 seconds for Link Hellos
                and 45 seconds for Targeted Hellos.
                A value of 65535 indicates an
                infinite hold time.
                ''',
                'nbr_hold_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-ldp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor LDP Identifier
                ''',
                'nbr_ldp_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-src-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the MPLS LDP Hello Neighbor source
                address.
                ''',
                'nbr_src_addr',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('nbr-src-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Hello Neighbor source
                        address.
                        ''',
                        'nbr_src_addr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('nbr-src-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Hello Neighbor source
                        address.
                        ''',
                        'nbr_src_addr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('next-hello', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next hello due time in milliseconds.
                ''',
                'next_hello',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set when the session is up for this adjacency.
                ''',
                'session_up',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'link-hellos',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Discovery.LinkHelloState' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Discovery.LinkHelloState',
            False, 
            [
            _MetaInfoClassMember('link-hellos', REFERENCE_LIST, 'LinkHellos' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos', 
                [], [], 
                '''                Each entry represents a single LDP Hello Adjacency.
                An LDP Session can have one or more Hello
                Adjacencies.
                ''',
                'link_hellos',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'link-hello-state',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('target-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The target IP Address
                ''',
                'target_address',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('target-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The target IP Address
                        ''',
                        'target_address',
                        'Cisco-IOS-XE-mpls-ldp', True),
                    _MetaInfoClassMember('target-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The target IP Address
                        ''',
                        'target_address',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('hold-time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This is the MPLS LDP Hello Discovery expiry time
                in seconds.
                If the value of this object is 65535,
                this means that the hold time is infinite
                (i.e., wait forever).
                
                Otherwise, the time remaining for
                this Hello Adjacency to receive its
                next Hello Message.
                
                This interval will change when the 'next'
                Hello Message which corresponds to this
                Hello Adjacency is received unless it
                is infinite.
                ''',
                'hold_time_remaining',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local IP Address
                ''',
                'local_address',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local IP Address
                        ''',
                        'local_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local IP Address
                        ''',
                        'local_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('nbr-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Hello hold time which is negotiated between
                the Entity and the Peer.  The entity associated
                with this Hello Adjacency issues a proposed
                Hello Hold Time value in the
                EntityHelloHoldTimer object.  The peer
                also proposes a value and this object represents
                the negotiated value.
                
                A value of 0 means the default,
                which is 15 seconds for Link Hellos
                and 45 seconds for Targeted Hellos.
                A value of 65535 indicates an
                infinite hold time.
                ''',
                'nbr_hold_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('neighbor-ldp-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor LDP Identifier
                ''',
                'neighbor_ldp_identifier',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('next-hello', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next hello due time in milliseconds.
                ''',
                'next_hello',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'DhcStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'DhcStateEnum', 
                [], [], 
                '''                This is the MPLS LDP Targeted Hello state.
                ''',
                'state',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'targeted-hello',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Discovery.TargetedHellos' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Discovery.TargetedHellos',
            False, 
            [
            _MetaInfoClassMember('targeted-hello', REFERENCE_LIST, 'TargetedHello' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello', 
                [], [], 
                '''                The LDP targeted discovery information for a specific
                target. Targetted discovery creates a single adjacency
                between two addresses and not indiviual adjacencies
                across physical interfaces.
                ''',
                'targeted_hello',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('targeted-hello-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Targeted hold time in seconds.
                ''',
                'targeted_hello_hold_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('targeted-hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Targeted Hello interval in seconds.
                ''',
                'targeted_hello_interval',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'targeted-hellos',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Discovery',
            False, 
            [
            _MetaInfoClassMember('discovery-stats', REFERENCE_CLASS, 'DiscoveryStats' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Discovery.DiscoveryStats', 
                [], [], 
                '''                MPLS LDP Discovery Summary Information
                ''',
                'discovery_stats',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('link-hello-state', REFERENCE_CLASS, 'LinkHelloState' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Discovery.LinkHelloState', 
                [], [], 
                '''                This container holds information for LDP Discovery
                using non-targeted Hellos. These are interface-based
                hellos which form one or more adjacencies for each
                interface and also form adjacencies on multiple
                intefrfaces. Link Hellos can therefore form multiple
                adjacencies with the same peer.
                ''',
                'link_hello_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('targeted-hellos', REFERENCE_CLASS, 'TargetedHellos' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Discovery.TargetedHellos', 
                [], [], 
                '''                The LDP Discovery Targeted Hello state.
                ''',
                'targeted_hellos',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr',
            False, 
            [
            _MetaInfoClassMember('labeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with 1 or more paths
                labeled
                ''',
                'labeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with some (but not
                ALL) paths labeled
                ''',
                'labeled_pfxs_partial',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unlabeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with ALL paths
                unlabeled
                ''',
                'unlabeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'labeled-pfxs-aggr',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary',
            False, 
            [
            _MetaInfoClassMember('labeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with 1 or more paths
                labeled
                ''',
                'labeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with some (but not
                ALL) paths labeled
                ''',
                'labeled_pfxs_partial',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unlabeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with ALL paths
                unlabeled
                ''',
                'unlabeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'labeled-pfxs-primary',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup',
            False, 
            [
            _MetaInfoClassMember('labeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with 1 or more paths
                labeled
                ''',
                'labeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with some (but not
                ALL) paths labeled
                ''',
                'labeled_pfxs_partial',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unlabeled-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of labeled prefixes with ALL paths
                unlabeled
                ''',
                'unlabeled_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'labeled-pfxs-backup',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs',
            False, 
            [
            _MetaInfoClassMember('ecmp-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of prefixes with ECMP
                ''',
                'ecmp_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-aggr', REFERENCE_CLASS, 'LabeledPfxsAggr' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr', 
                [], [], 
                '''                Labeled prefix count for all paths
                ''',
                'labeled_pfxs_aggr',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-backup', REFERENCE_CLASS, 'LabeledPfxsBackup' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup', 
                [], [], 
                '''                Labeled prefix count related to backup paths
                only
                ''',
                'labeled_pfxs_backup',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-pfxs-primary', REFERENCE_CLASS, 'LabeledPfxsPrimary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary', 
                [], [], 
                '''                Labeled prefix count related to primary paths
                only
                ''',
                'labeled_pfxs_primary',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protected-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Count of FRR protected prefixes
                ''',
                'protected_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('total-pfxs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total Prefix count
                ''',
                'total_pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'pfxs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs',
            False, 
            [
            _MetaInfoClassMember('backup-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of non-primary backup paths
                ''',
                'backup_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-backup-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of labeled backup paths
                ''',
                'labeled_backup_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('labeled-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of all labeled paths
                ''',
                'labeled_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protected-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of FRR protected paths
                ''',
                'protected_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('remote-backup-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of non-primary remote backup paths
                ''',
                'remote_backup_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('total-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total path count
                ''',
                'total_paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nhs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('intfs-fwd-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MPLS forwarding enabled interface count.
                ''',
                'intfs_fwd_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-lbls', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local label allocated count.
                ''',
                'local_lbls',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nhs', REFERENCE_CLASS, 'Nhs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs', 
                [], [], 
                '''                MPLS LDP forwarding rewrite next-hop/path summary
                ''',
                'nhs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('pfxs', REFERENCE_CLASS, 'Pfxs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs', 
                [], [], 
                '''                MPLS LDP forwarding prefix rewrite summary
                ''',
                'pfxs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'forwarding-vrf-summ',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms',
            False, 
            [
            _MetaInfoClassMember('forwarding-vrf-summ', REFERENCE_LIST, 'ForwardingVrfSumm' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm', 
                [], [], 
                '''                Summary of forwarding info for this VRF.
                ''',
                'forwarding_vrf_summ',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'forwarding-vrf-summs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route',
            False, 
            [
            _MetaInfoClassMember('forwarding-update-age', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Forwarding update nanosec age
                ''',
                'forwarding_update_age',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('forwarding-update-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of forwarding updates.
                ''',
                'forwarding_update_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('forwarding-update-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Forwarding update nanosec timestamp.
                ''',
                'forwarding_update_timestamp',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-local-vrf-leaked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this route leaked across local VRFs?
                ''',
                'is_local_vrf_leaked',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'local_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route metric
                ''',
                'metric',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Route priority
                ''',
                'priority',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('routing-update-age', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Routing update nanosec age
                ''',
                'routing_update_age',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('routing-update-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routing updates
                ''',
                'routing_update_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('routing-update-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last Routing update nanosec timestamp
                ''',
                'routing_update_timestamp',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Route source protocol Id
                ''',
                'source',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Route type
                ''',
                'type',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route RIB version.
                ''',
                'version',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing',
            False, 
            [
            _MetaInfoClassMember('bkup-path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Backup path Id
                ''',
                'bkup_path_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('has-remote-lfa-bkup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is true if the path has a remote LFA
                backup.
                ''',
                'has_remote_lfa_bkup',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is the interface.
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('load-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path's load metric for load balancing
                ''',
                'load_metric',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the Next Hop address.
                ''',
                'next_hop',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the Next Hop address.
                        ''',
                        'next_hop',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the Next Hop address.
                        ''',
                        'next_hop',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('next-hop-table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table ID for nexthop address
                ''',
                'next_hop_table_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nexthop Identifier
                ''',
                'nexthop_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nh-is-overriden', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This is set when the nexthop is overriden
                by LDP.
                ''',
                'nh_is_overriden',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                path Id
                ''',
                'path_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('path-type', REFERENCE_IDENTITY_CLASS, 'RoutePathTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'RoutePathTypeIdentity', 
                [], [], 
                '''                Routing path type
                ''',
                'path_type',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('remote-node-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the Remote/PQ node address.
                ''',
                'remote_node_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the Remote/PQ node address.
                        ''',
                        'remote_node_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the Remote/PQ node address.
                        ''',
                        'remote_node_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'routing',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent',
            False, 
            [
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label space identifier
                ''',
                'label_space_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lsr-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR identifier
                ''',
                'lsr_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nexthop-peer-ldp-ident',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo',
            False, 
            [
            _MetaInfoClassMember('is-from-graceful-restartable-neighbor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is from a GR neighbor
                ''',
                'is_from_graceful_restartable_neighbor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-stale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the entry stale? This may happen during a graceful
                restart.
                ''',
                'is_stale',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nexthop-peer-ldp-ident', REFERENCE_CLASS, 'NexthopPeerLdpIdent' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent', 
                [], [], 
                '''                Nexthop LDP peer
                ''',
                'nexthop_peer_ldp_ident',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'out_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-label-owner', REFERENCE_IDENTITY_CLASS, 'RoutePathLblOwnerIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'RoutePathLblOwnerIdentity', 
                [], [], 
                '''                Outgoing label owner
                ''',
                'out_label_owner',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-label-type', REFERENCE_IDENTITY_CLASS, 'LabelTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'LabelTypeIdentity', 
                [], [], 
                '''                Outgoing Label Type
                ''',
                'out_label_type',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'mpls-outgoing-info',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent',
            False, 
            [
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label space identifier
                ''',
                'label_space_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lsr-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR identifier
                ''',
                'lsr_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nexthop-peer-ldp-ident',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo',
            False, 
            [
            _MetaInfoClassMember('is-from-graceful-restartable-neighbor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is from a GR neighbor
                ''',
                'is_from_graceful_restartable_neighbor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-stale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the entry stale? This may happen during a graceful
                restart.
                ''',
                'is_stale',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nexthop-peer-ldp-ident', REFERENCE_CLASS, 'NexthopPeerLdpIdent' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent', 
                [], [], 
                '''                Nexthop LDP peer
                ''',
                'nexthop_peer_ldp_ident',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'out_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-label-owner', REFERENCE_IDENTITY_CLASS, 'RoutePathLblOwnerIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'RoutePathLblOwnerIdentity', 
                [], [], 
                '''                Outgoing label owner
                ''',
                'out_label_owner',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('out-label-type', REFERENCE_IDENTITY_CLASS, 'LabelTypeIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'LabelTypeIdentity', 
                [], [], 
                '''                Outgoing Label Type
                ''',
                'out_label_type',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'mpls-outgoing-info',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('has-remote-lfa-bkup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether path has remote LFA backup
                ''',
                'has_remote_lfa_bkup',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('mpls-outgoing-info', REFERENCE_CLASS, 'MplsOutgoingInfo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo', 
                [], [], 
                '''                Remote LFA MPLS nexthop info
                ''',
                'mpls_outgoing_info',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls',
            False, 
            [
            _MetaInfoClassMember('mpls-outgoing-info', REFERENCE_CLASS, 'MplsOutgoingInfo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo', 
                [], [], 
                '''                MPLS nexthop info
                ''',
                'mpls_outgoing_info',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa', 
                [], [], 
                '''                MPLS LDP Forwarding Path Remote LFA-FRR backup
                MPLS info
                ''',
                'remote_lfa',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths',
            False, 
            [
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls', 
                [], [], 
                '''                MPLS LDP Forwarding Path MPLS information
                ''',
                'mpls',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('routing', REFERENCE_CLASS, 'Routing' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing', 
                [], [], 
                '''                MPLS LDP Forwarding Path IP Routing information
                ''',
                'routing',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding.ForwardingDetail',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP Prefix
                ''',
                'prefix',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        The IP Prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XE-mpls-ldp', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The IP Prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('fwd-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the MPLS LDP Forward IP Prefix.
                ''',
                'fwd_prefix',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('fwd-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Forward IP Prefix.
                        ''',
                        'fwd_prefix',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('fwd-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Forward IP Prefix.
                        ''',
                        'fwd_prefix',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths', 
                [], [], 
                '''                MPLS LDP Forwarding Path info
                ''',
                'paths',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('route', REFERENCE_CLASS, 'Route' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route', 
                [], [], 
                '''                MPLS LDP Forwarding Route information
                ''',
                'route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table ID associated with IP prefix
                ''',
                'table_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'forwarding-detail',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Forwarding' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Forwarding',
            False, 
            [
            _MetaInfoClassMember('forwarding-detail', REFERENCE_LIST, 'ForwardingDetail' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingDetail', 
                [], [], 
                '''                This leaf contain the individual LDP forwarding rewrite
                for a single prefix.
                ''',
                'forwarding_detail',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('forwarding-vrf-summs', REFERENCE_CLASS, 'ForwardingVrfSumms' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms', 
                [], [], 
                '''                Summary of forwarding info for this VRF.
                ''',
                'forwarding_vrf_summs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'forwarding',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family name.
                ''',
                'af_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('binding-local', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local bindings
                ''',
                'binding_local',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-explicit-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local explicit null bindings
                ''',
                'binding_local_explicit_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-implicit-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local implicit null bindings
                ''',
                'binding_local_implicit_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-no-route', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local bindings with no route
                ''',
                'binding_local_no_route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-non-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local non-null bindings
                ''',
                'binding_local_non_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-null', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of local null bindings
                ''',
                'binding_local_null',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-local-oor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the number of local bindings needing label but which
                hit the Out-Of-Resource condition.
                ''',
                'binding_local_oor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-no-route', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bindings with no route
                ''',
                'binding_no_route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-remote', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of remote bindings
                ''',
                'binding_remote',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('binding-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total bindings
                ''',
                'binding_total',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('highest-allocated-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest allocated label
                ''',
                'highest_allocated_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lowest-allocated-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest allocated label
                ''',
                'lowest_allocated_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'binding-sum-af',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings.BindingsSumAfs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings.BindingsSumAfs',
            False, 
            [
            _MetaInfoClassMember('binding-sum-af', REFERENCE_LIST, 'BindingSumAf' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf', 
                [], [], 
                '''                Counters for the LDP Label Information Base for this
                VRF/AF.
                ''',
                'binding_sum_af',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'bindings-sum-afs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent',
            False, 
            [
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label space identifier
                ''',
                'label_space_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lsr-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR identifier
                ''',
                'lsr_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'assigning-peer-ldp-ident',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding',
            False, 
            [
            _MetaInfoClassMember('assigning-peer-ldp-ident', REFERENCE_CLASS, 'AssigningPeerLdpIdent' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent', 
                [], [], 
                '''                Assigning peer
                ''',
                'assigning_peer_ldp_ident',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-stale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the entry stale
                ''',
                'is_stale',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('remote-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the remote Label.
                ''',
                'remote_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'remote-binding',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo',
            False, 
            [
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label space identifier
                ''',
                'label_space_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lsr-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR identifier
                ''',
                'lsr_id',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR identifier
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'peers-advertised-to',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings.Binding' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings.Binding',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This leaf contains the IP Prefix being bound.
                ''',
                'prefix',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        This leaf contains the IP Prefix being bound.
                        ''',
                        'prefix',
                        'Cisco-IOS-XE-mpls-ldp', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        This leaf contains the IP Prefix being bound.
                        ''',
                        'prefix',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('advertise-lsr-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the filter name for this binding's
                Advertise LSR. The filter type is device specific
                and could be an ACL, a prefix list, or other
                mechanism.
                ''',
                'advertise_lsr_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('advertise-prefix-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the filter name for this binding's
                prefix. The filter type is device specific and
                could be an ACL, a prefix list, or other mechanism.
                ''',
                'advertise_prefix_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('config-enforced-local-label-value', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Config/User enforced local label value
                ''',
                'config_enforced_local_label_value',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('fwd-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the MPLS LDP Binding IP Prefix.
                ''',
                'fwd_prefix',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('fwd-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Binding IP Prefix.
                        ''',
                        'fwd_prefix',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('fwd-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Binding IP Prefix.
                        ''',
                        'fwd_prefix',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('is-no-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is true if the MPLS LDP Binding has no route.
                ''',
                'is_no_route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-oor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is true if the MPLS LDP Binding Label space is
                depleted, Out Of Resource. No new labels can
                be allocated.
                ''',
                'label_oor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('le-local-binding-revision', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the MPLS LDP Binding Local Binding revision.
                ''',
                'le_local_binding_revision',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('le-local-label-state', REFERENCE_ENUM_CLASS, 'LocalLabelStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'LocalLabelStateEnum', 
                [], [], 
                '''                This is the MPLS LDP Binding Local label state.
                ''',
                'le_local_label_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the MPLS LDP Binding Local label.
                ''',
                'local_label',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peers-advertised-to', REFERENCE_LIST, 'PeersAdvertisedTo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo', 
                [], [], 
                '''                Peers to which this entry is advertised.
                ''',
                'peers_advertised_to',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This is the MPLS LDP Binding Prefix Length.
                ''',
                'prefix_length',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('remote-binding', REFERENCE_LIST, 'RemoteBinding' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding', 
                [], [], 
                '''                MPLS LDP Remote Binding Information
                ''',
                'remote_binding',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Bindings' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Bindings',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings.Binding', 
                [], [], 
                '''                This list contains the MPLS LDP Label Bindings for each
                IP Prefix. Label bindings provide the local MPLS Label,
                a list of remote labels, any filters affecting
                advertisment of that filter, and a list of neighbors to
                which the label has been advertised.
                ''',
                'binding',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bindings-sum-afs', REFERENCE_CLASS, 'BindingsSumAfs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings.BindingsSumAfs', 
                [], [], 
                '''                This container holds the bindings specific to this VRF
                and AF.
                ''',
                'bindings_sum_afs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'bindings',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats',
            False, 
            [
            _MetaInfoClassMember('num-of-nbr-ipv4-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 addresses for which the neighbor is
                advertising labels.
                ''',
                'num_of_nbr_ipv4_addresses',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-nbr-ipv4-discovery', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor IPv4 discovery sources.
                ''',
                'num_of_nbr_ipv4_discovery',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-nbr-ipv4-lbl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 labels the neighbor is advertising.
                ''',
                'num_of_nbr_ipv4_lbl',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-nbr-ipv6-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 addresses for which the neighbor is
                advertising labels.
                ''',
                'num_of_nbr_ipv6_addresses',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-nbr-ipv6-discovery', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor IPv6 discovery sources.
                ''',
                'num_of_nbr_ipv6_discovery',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('num-of-nbr-ipv6-lbl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 labels the neighbor is advertising.
                ''',
                'num_of_nbr_ipv6_lbl',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('ta-pies-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MPLS LDP messages received from this
                neighbor.
                ''',
                'ta_pies_rcvd',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('ta-pies-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MPLS LDP messages sent to this neighbor.
                ''',
                'ta_pies_sent',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nbr-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency',
            False, 
            [
            _MetaInfoClassMember('down-nbr-down-reason', REFERENCE_IDENTITY_CLASS, 'DownNbrReasonIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'DownNbrReasonIdentity', 
                [], [], 
                '''                This identity provides the reason that the LDP
                Session with this neighbor is down. The reason does
                not persist if the session was down but is now
                recovered.
                ''',
                'down_nbr_down_reason',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('down-nbr-flap-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the current count of back-to-back flaps.
                ''',
                'down_nbr_flap_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-graceful-restartable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this neighbor graceful restartable?
                ''',
                'is_graceful_restartable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-liveness-timer-running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This is set if the liveness timer is running.
                ''',
                'is_liveness_timer_running',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-recovery-timer-running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This is set if the recovery timer is running.
                ''',
                'is_recovery_timer_running',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('liveness-timer-remaining-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining time from liveness timer in seconds.
                ''',
                'liveness_timer_remaining_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('reconnect-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This leaf is the reconnect timeout in
                microseconds.
                ''',
                'reconnect_timeout',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This leaf is the recovery time in microseconds.
                ''',
                'recovery_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('recovery-timer-remaining-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Recovery timer remaining time in seconds.
                ''',
                'recovery_timer_remaining_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'graceful-restart-adjacency',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation',
            False, 
            [
            _MetaInfoClassMember('foreign-host', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the foreign host address used by TCP.
                ''',
                'foreign_host',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('foreign-host', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the foreign host address used by TCP.
                        ''',
                        'foreign_host',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('foreign-host', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the foreign host address used by TCP.
                        ''',
                        'foreign_host',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port number
                ''',
                'foreign_port',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-md5-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is MD5 Digest on
                ''',
                'is_md5_on',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-host', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the local host address used by TCP.
                ''',
                'local_host',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('local-host', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the local host address used by TCP.
                        ''',
                        'local_host',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('local-host', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the local host address used by TCP.
                        ''',
                        'local_host',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port number
                ''',
                'local_port',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('up-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                up time
                ''',
                'up_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'tcp-information',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps',
            False, 
            [
            _MetaInfoClassMember('cap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Capability type (IANA assigned)
                ''',
                'cap_type',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('cap-des', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                Capability description
                ''',
                'cap_des',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-data', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capability data
                ''',
                'capability_data',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Capability data length
                ''',
                'capability_data_length',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'sent-caps',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps',
            False, 
            [
            _MetaInfoClassMember('cap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Capability type (IANA assigned)
                ''',
                'cap_type',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('cap-des', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                Capability description
                ''',
                'cap_des',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-data', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capability data
                ''',
                'capability_data',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capability-data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Capability data length
                ''',
                'capability_data_length',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'received-caps',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities',
            False, 
            [
            _MetaInfoClassMember('received-caps', REFERENCE_LIST, 'ReceivedCaps' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps', 
                [], [], 
                '''                List of received capabilities
                ''',
                'received_caps',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sent-caps', REFERENCE_LIST, 'SentCaps' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps', 
                [], [], 
                '''                List of sent capabilities
                ''',
                'sent_caps',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'capabilities',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Neighbor.SessionRoleEnum' : _MetaInfoEnum('SessionRoleEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'unknown':'unknown',
            'active':'active',
            'passive':'passive',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpState.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('lsr-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR ID of neighbor
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', True),
                    _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR ID of neighbor
                        ''',
                        'lsr_id',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('advertise-bgp-prefixes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if BGP labeled prefixes are advertised to the
                neighbor.
                ''',
                'advertise_bgp_prefixes',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bgp-advertisement-state', REFERENCE_ENUM_CLASS, 'NbrBgpAdvtStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'NbrBgpAdvtStateEnum', 
                [], [], 
                '''                BGP labeled prefixes advertisement state.
                ''',
                'bgp_advertisement_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capabilities', REFERENCE_CLASS, 'Capabilities' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities', 
                [], [], 
                '''                Capabilities sent to and received from neighbor
                ''',
                'capabilities',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('client', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Targeted Session clients.
                ''',
                'client',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('downstream-on-demand', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Label advertisement mode in Downstream On
                Demand mode or not?
                ''',
                'downstream_on_demand',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('duplicate-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Duplicate IPv4/IPv6 address bound to this peer
                ''',
                'duplicate_address',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('duplicate-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Duplicate IPv4/IPv6 address bound to this peer
                        ''',
                        'duplicate_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('duplicate-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Duplicate IPv4/IPv6 address bound to this peer
                        ''',
                        'duplicate_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('graceful-restart-adjacency', REFERENCE_CLASS, 'GracefulRestartAdjacency' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency', 
                [], [], 
                '''                This container holds the graceful restart information
                for this adjacency.
                ''',
                'graceful_restart_adjacency',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('has-sp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Session Protection enabled
                ''',
                'has_sp',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('inbound-ipv4', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This contains the IPv4 Inbound accept filter name.
                The filter type is device specific and could be an
                ACL, a prefix list, or other mechanism.
                ''',
                'inbound_ipv4',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('inbound-ipv6-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This contains the IPv6 Inbound accept filter name.
                The filter type is device specific and could be an
                ACL, a prefix list, or other mechanism.
                ''',
                'inbound_ipv6_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-bound-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the MPLS LDP Neighbor Bound IPv4/IPv6
                Address.
                ''',
                'nbr_bound_address',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('nbr-bound-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Neighbor Bound IPv4/IPv6
                        Address.
                        ''',
                        'nbr_bound_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('nbr-bound-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the MPLS LDP Neighbor Bound IPv4/IPv6
                        Address.
                        ''',
                        'nbr_bound_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('nbr-path-vector-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                If the value of this object is 0 (zero) then
                Loop Dection for Path Vectors for this neighor
                is disabled.
                
                Otherwise, if this object has a value greater than
                zero, then Loop Dection for Path  Vectors for this
                neighbor is enabled and the Path Vector Limit is
                this value.
                ''',
                'nbr_path_vector_limit',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-stats', REFERENCE_CLASS, 'NbrStats' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats', 
                [], [], 
                '''                Neighbor Statistics.
                ''',
                'nbr_stats',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('outbound-ipv4-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This contains the IPv4 Outbound advertise filter
                name. The filter type is device specific and could
                be an ACL, a prefix list, or other mechanism.
                ''',
                'outbound_ipv4_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('outbound-ipv6-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This contains the IPv6 Outbound advertise filter
                name. The filter type is device specific and could
                be an ACL, a prefix list, or other mechanism.
                ''',
                'outbound_ipv6_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session holdtime value in seconds from the peer.
                ''',
                'peer_hold_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-keep-alive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session keepalive interval in seconds from the peer.
                ''',
                'peer_keep_alive_interval',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-state', REFERENCE_ENUM_CLASS, 'AdjStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AdjStateEnum', 
                [], [], 
                '''                LDP adjacency peer state.
                ''',
                'peer_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session-prot-ver', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The version of the LDP Protocol which
                this session is using.  This is the version of
                the LDP protocol which has been negotiated
                during session initialization.
                ''',
                'session_prot_ver',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session-role', REFERENCE_ENUM_CLASS, 'SessionRoleEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.SessionRoleEnum', 
                [], [], 
                '''                During session establishment the LSR/LER takes either
                the active role or the passive role based on address
                comparisons.  This object indicates whether this
                LSR/LER was behaving in an active role or passive role
                during this session's establishment.
                
                The value of unknown(1), indicates that the role is not
                able to be determined at the present time.
                ''',
                'session_role',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sp-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session protection holdup time duration in
                seconds.
                ''',
                'sp_duration',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sp-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This contains the Session Protection filter name.
                The filter type is device specific and could be an
                ACL, a prefix list, or other mechanism.
                ''',
                'sp_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sp-has-duration', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Session Protection has non-default duration
                ''',
                'sp_has_duration',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sp-state', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                Session Protection state
                ''',
                'sp_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('spht-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Protection holdup time remaining value
                in seconds.
                ''',
                'spht_remaining',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('spht-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Session Protection holdup timer is running
                ''',
                'spht_running',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('tcp-information', REFERENCE_CLASS, 'TcpInformation' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation', 
                [], [], 
                '''                MPLS LDP Neighbor TCP Information
                ''',
                'tcp_information',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('up-time-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up time in seconds
                ''',
                'up_time_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.NbrAdjs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.NbrAdjs',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is the interface used by MPLS LDP Link
                Hello.
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the local address used to send the
                Targeted Hello.
                ''',
                'local_address',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the local address used to send the
                        Targeted Hello.
                        ''',
                        'local_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the local address used to send the
                        Targeted Hello.
                        ''',
                        'local_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('target-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the destination address used to send the
                Targeted Hello.
                ''',
                'target_address',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('target-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the destination address used to send the
                        Targeted Hello.
                        ''',
                        'target_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('target-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the destination address used to send the
                        Targeted Hello.
                        ''',
                        'target_address',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('target-state', REFERENCE_ENUM_CLASS, 'DhcStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'DhcStateEnum', 
                [], [], 
                '''                This is the state of this Targeted Hello
                instance.
                ''',
                'target_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nbr-adjs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut',
            False, 
            [
            _MetaInfoClassMember('address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address message count.
                ''',
                'address_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('address-withdraw-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address withdraw count.
                ''',
                'address_withdraw_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-app-data-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG App Data count.
                ''',
                'iccp_rg_app_data_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-conn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Connect count.
                ''',
                'iccp_rg_conn_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-disconn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Disconnect count.
                ''',
                'iccp_rg_disconn_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-notif-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Notify count
                ''',
                'iccp_rg_notif_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('init-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Init message count.
                ''',
                'init_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keep-alive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive count.
                ''',
                'keep_alive_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-abort-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label abort request count.
                ''',
                'label_abort_request_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-map-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label map count.
                ''',
                'label_map_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-release-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label release count.
                ''',
                'label_release_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label request count.
                ''',
                'label_request_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-withdraw-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label withdraw count.
                ''',
                'label_withdraw_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('notification-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Notification count.
                ''',
                'notification_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of all messages.
                ''',
                'total_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'message-out',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn',
            False, 
            [
            _MetaInfoClassMember('address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address message count.
                ''',
                'address_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('address-withdraw-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address withdraw count.
                ''',
                'address_withdraw_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-app-data-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG App Data count.
                ''',
                'iccp_rg_app_data_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-conn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Connect count.
                ''',
                'iccp_rg_conn_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-disconn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Disconnect count.
                ''',
                'iccp_rg_disconn_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('iccp-rg-notif-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP RG Notify count
                ''',
                'iccp_rg_notif_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('init-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Init message count.
                ''',
                'init_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keep-alive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive count.
                ''',
                'keep_alive_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-abort-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label abort request count.
                ''',
                'label_abort_request_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-map-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label map count.
                ''',
                'label_map_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-release-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label release count.
                ''',
                'label_release_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label request count.
                ''',
                'label_request_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-withdraw-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label withdraw count.
                ''',
                'label_withdraw_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('notification-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Notification count.
                ''',
                'notification_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of all messages.
                ''',
                'total_count',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'message-in',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.StatsInfo' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.StatsInfo',
            False, 
            [
            _MetaInfoClassMember('bad-ldpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad LDP Identifier
                Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'bad_ldpid',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bad-msg-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad Message
                Length Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'bad_msg_len',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bad-pdu-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad PDU Length
                Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'bad_pdu_len',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bad-tlv-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad TLV
                Length Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'bad_tlv_len',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('discon-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one or more of this entity's counters
                suffered a discontinuity.  The relevant counters
                are the specific instances associated with this
                entity of any counter32 object contained
                in the 'EntityStatsTable'.  If no such
                discontinuities have occurred since the last
                re-initialization of the local management
                subsystem, then this object contains a zero
                value.
                ''',
                'discon_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keep-alive-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Session Keep Alive
                Timer Expired Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'keep_alive_exp',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('malformed-tlv-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Malformed TLV
                Value Fatal Errors detected by the session(s)
                (past and present) associated with this
                LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'malformed_tlv_val',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('message-in', REFERENCE_CLASS, 'MessageIn' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn', 
                [], [], 
                '''                MPLS LDP message received counters from this
                neighbor.
                ''',
                'message_in',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('message-out', REFERENCE_CLASS, 'MessageOut' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut', 
                [], [], 
                '''                MPLS LDP message sent counters to this neighbor.
                ''',
                'message_out',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sess-rej-ad', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/Parameters
                Advertisement Mode Error Notification Messages sent
                or received by this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'sess_rej_ad',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sess-rej-lr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/Parameters
                Label Range Notification Messages sent
                or received by this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'sess_rej_lr',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sess-rej-max-pdu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/Parameters
                
                Max Pdu Length Error Notification Messages sent
                or received by this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'sess_rej_max_pdu',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sess-reject-no-hello', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/No Hello Error
                Notification Messages sent or received by
                this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'sess_reject_no_hello',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session-attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Initialization messages
                which were sent or received by this LDP Entity and
                were NAK'd.   In other words, this counter counts
                the number of session initializations that failed.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'session_attempts',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('shutdow-notif-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Shutdown Notfications
                sent related to session(s) (past and present)
                associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                
                discon-time.
                ''',
                'shutdow_notif_sent',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('shutdown-notif-rec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Shutdown Notifications
                received related to session(s) (past and present)
                associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                discon-time.
                ''',
                'shutdown_notif_rec',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'stats-info',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.Backoffs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.Backoffs',
            False, 
            [
            _MetaInfoClassMember('backoff-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current neighbor backoff count in seconds.
                ''',
                'backoff_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('waiting-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current neighbor backoff waiting count in seconds.
                ''',
                'waiting_seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'backoffs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess.StateEnum' : _MetaInfoEnum('StateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'nonexistent':'nonexistent',
            'initialized':'initialized',
            'openrec':'openrec',
            'opensent':'opensent',
            'operational':'operational',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess',
            False, 
            [
            _MetaInfoClassMember('discon-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one or more of this session's counters
                suffered a discontinuity.  The relevant counters are
                the specific instances associated with this session
                of any counter32 object contained in the
                session-stats table.
                
                The initial value of this object is the value of
                sysUpTime when the entry was created in this table.
                
                Also, a command generator can distinguish when a
                session between a given Entity and Peer goes away
                and a new session is established.  This value would
                change and thus indicate to the command generator
                that this is a different session.
                ''',
                'discon_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keep-alive-remain', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The keep alive hold time remaining for
                this session in seconds.
                ''',
                'keep_alive_remain',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keep-alive-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The negotiated KeepAlive Time which
                represents the amount of seconds between
                keep alive messages.  The
                EntityKeepAliveHoldTimer
                related to this Session is the
                value that was proposed as the
                KeepAlive Time for this session.
                
                This value is negotiated during
                session initialization between
                the entity's proposed value
                (i.e., the value configured in
                EntityKeepAliveHoldTimer)
                and the peer's proposed
                KeepAlive Hold Timer value.
                This value is the smaller
                of the two proposed values.
                ''',
                'keep_alive_time',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('last-stat-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this
                Session entered its current state as
                denoted by the SessionState
                object.
                ''',
                'last_stat_change',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('max-pdu', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of maximum allowable length for LDP PDUs
                this session.  This value may have been negotiated
                for during the Session Initialization.  This object
                is related to the EntityMaxPduLength object.  The
                EntityMaxPduLength object specifies the requested
                LDP PDU length, and this object reflects the
                negotiated LDP PDU length between the Entity and
                the Peer.
                ''',
                'max_pdu',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'StateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess.StateEnum', 
                [], [], 
                '''                The current state of the session, all of the
                states 1 to 5 are based on the state machine
                for session negotiation behavior.
                ''',
                'state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unknown-mess-err', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Unknown Message Type
                Errors detected by this LSR/LER during this session.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system,
                and at other times as indicated by the value of
                discon-time.
                ''',
                'unknown_mess_err',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('unknown-tlv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Unknown TLV Errors
                detected by this LSR/LER during this session.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system,
                and at other times as indicated by the value of
                discon-time.
                ''',
                'unknown_tlv',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nbr-sess',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail',
            False, 
            [
            _MetaInfoClassMember('nbr-sess', REFERENCE_CLASS, 'NbrSess' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess', 
                [], [], 
                '''                This container holds session information about the
                sessions between these two neighbors.
                ''',
                'nbr_sess',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-in-label-reqs-created', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Request Records created.
                ''',
                'nsr_nbr_in_label_reqs_created',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-in-label-reqs-freed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Request Records freed.
                ''',
                'nsr_nbr_in_label_reqs_freed',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-in-label-withdraw-created', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Withdraw Records created.
                ''',
                'nsr_nbr_in_label_withdraw_created',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-in-label-withdraw-freed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In label Withdraw Records freed.
                ''',
                'nsr_nbr_in_label_withdraw_freed',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-last-sync-error', REFERENCE_IDENTITY_CLASS, 'NsrPeerSyncErrIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'NsrPeerSyncErrIdentity', 
                [], [], 
                '''                This is the last NSR sync error recieved. It
                indicates the last reason the sync failed
                even if the sync has now succeeded. This
                allows this information to be viewed
                when the state is flapping, even if
                the syncronization is successful at the
                time of the query.
                ''',
                'nsr_nbr_last_sync_error',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-last-sync-nack-reason', REFERENCE_IDENTITY_CLASS, 'NsrSyncNackRsnIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'NsrSyncNackRsnIdentity', 
                [], [], 
                '''                Last NSR sync NACK reason.
                ''',
                'nsr_nbr_last_sync_nack_reason',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-lcl-addr-withdraw-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Address Withdraw cleared.
                ''',
                'nsr_nbr_lcl_addr_withdraw_cleared',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-lcl-addr-withdraw-set', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Address Withdraw set.
                ''',
                'nsr_nbr_lcl_addr_withdraw_set',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-pend-label-req-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Label-Request responses
                ''',
                'nsr_nbr_pend_label_req_resps',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-pend-label-withdraw-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Label-Withdraw responses
                ''',
                'nsr_nbr_pend_label_withdraw_resps',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-pend-lcl-addr-withdraw-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Local Address Withdraw Acks:
                ''',
                'nsr_nbr_pend_lcl_addr_withdraw_acks',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-sync-state', REFERENCE_IDENTITY_CLASS, 'NsrPeerSyncStateIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'NsrPeerSyncStateIdentity', 
                [], [], 
                '''                NSR Sync State
                ''',
                'nsr_nbr_sync_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-xmit-ctxt-deq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmit contexts dequeued.
                ''',
                'nsr_nbr_xmit_ctxt_deq',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-xmit-ctxt-enq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmit contexts enqueued.
                ''',
                'nsr_nbr_xmit_ctxt_enq',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-state', REFERENCE_IDENTITY_CLASS, 'NsrStatusIdentity' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'NsrStatusIdentity', 
                [], [], 
                '''                Non-Stop Routing State.
                ''',
                'nsr_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('path-vector-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                If the value of this object is 0 (zero) then
                Loop Dection for Path Vectors for this Peer
                is disabled.
                
                Otherwise, if this object has a value greater than
                zero, then Loop Dection for Path  Vectors for this
                Peer is enabled and the Path Vector Limit is this
                value.
                ''',
                'path_vector_limit',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-nbr-detail',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.Neighbors' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.Neighbors',
            False, 
            [
            _MetaInfoClassMember('backoffs', REFERENCE_CLASS, 'Backoffs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Backoffs', 
                [], [], 
                '''                LDP Backoff Information
                ''',
                'backoffs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-adjs', REFERENCE_LIST, 'NbrAdjs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.NbrAdjs', 
                [], [], 
                '''                For this Neighbor, this is the list of adjacencies
                between the neighbor and the local node.
                ''',
                'nbr_adjs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.Neighbor', 
                [], [], 
                '''                Information on a particular LDP neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-nbr-detail', REFERENCE_CLASS, 'NsrNbrDetail' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail', 
                [], [], 
                '''                This is the LDP NSR state for this neighbor.
                ''',
                'nsr_nbr_detail',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('stats-info', REFERENCE_CLASS, 'StatsInfo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors.StatsInfo', 
                [], [], 
                '''                MPLS LDP Statistics Information
                ''',
                'stats_info',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.LabelRanges.LabelRange' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.LabelRanges.LabelRange',
            False, 
            [
            _MetaInfoClassMember('lr-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                The minimum label configured for this range.
                ''',
                'lr_min',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('lr-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                The maximum label configured for this range.
                ''',
                'lr_max',
                'Cisco-IOS-XE-mpls-ldp', True),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-range',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState.LabelRanges' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState.LabelRanges',
            False, 
            [
            _MetaInfoClassMember('label-range', REFERENCE_LIST, 'LabelRange' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.LabelRanges.LabelRange', 
                [], [], 
                '''                This entry contains a single range of labels
                represented by the configured Upper and Lower
                Bounds pairs.  NOTE: there is NO corresponding
                LDP message which relates to the information
                in this table, however, this table does provide
                a way for a user to 'reserve' a generic label
                range.
                
                NOTE:  The ranges for a specific LDP Entity
                are UNIQUE and non-overlapping.
                ''',
                'label_range',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-ranges',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpState' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpState',
            False, 
            [
            _MetaInfoClassMember('backoff-parameters', REFERENCE_CLASS, 'BackoffParameters' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.BackoffParameters', 
                [], [], 
                '''                MPLS LDP Session Backoff Information
                ''',
                'backoff_parameters',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bindings', REFERENCE_CLASS, 'Bindings' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Bindings', 
                [], [], 
                '''                The detailed LDP Bindings.
                ''',
                'bindings',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bindings-summary', REFERENCE_CLASS, 'BindingsSummary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.BindingsSummary', 
                [], [], 
                '''                Aggregate counters for the MPLS LDP LIB.
                ''',
                'bindings_summary',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('capabilities', REFERENCE_CLASS, 'Capabilities' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Capabilities', 
                [], [], 
                '''                LDP capability database information
                ''',
                'capabilities',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Discovery', 
                [], [], 
                '''                The LDP Discovery operational state
                ''',
                'discovery',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('forwarding', REFERENCE_CLASS, 'Forwarding' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Forwarding', 
                [], [], 
                '''                Summary information regarding LDP forwarding
                setup and detailed LDP Forwarding rewrites
                ''',
                'forwarding',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('forwarding-summary', REFERENCE_CLASS, 'ForwardingSummary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.ForwardingSummary', 
                [], [], 
                '''                Summary information regarding LDP forwarding
                setup
                ''',
                'forwarding_summary',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.GracefulRestart', 
                [], [], 
                '''                MPLS LDP Graceful Restart Information
                ''',
                'graceful_restart',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('icpm-summary-all', REFERENCE_CLASS, 'IcpmSummaryAll' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.IcpmSummaryAll', 
                [], [], 
                '''                Summary info for LDP ICPM/ICCP.
                ''',
                'icpm_summary_all',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-ranges', REFERENCE_CLASS, 'LabelRanges' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.LabelRanges', 
                [], [], 
                '''                This contaions holds all the label ranges in use
                by this LDP instance.
                ''',
                'label_ranges',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Neighbors', 
                [], [], 
                '''                The LDP Neighbors Information
                ''',
                'neighbors',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr-summary-all', REFERENCE_CLASS, 'NsrSummaryAll' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.NsrSummaryAll', 
                [], [], 
                '''                This is the LDP NSR summary for the device.
                ''',
                'nsr_summary_all',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('oper-summary', REFERENCE_CLASS, 'OperSummary' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.OperSummary', 
                [], [], 
                '''                LDP operational data summary
                ''',
                'oper_summary',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('parameters', REFERENCE_CLASS, 'Parameters' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Parameters', 
                [], [], 
                '''                MPLS LDP Global Parameters
                ''',
                'parameters',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState.Vrfs', 
                [], [], 
                '''                MPLS LDP per-VRF operational data.
                ''',
                'vrfs',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'mpls-ldp-state',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.RouterId' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg.RouterId',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('force', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Force the router to use the specified identifier
                as the router ID more quickly.
                ''',
                'force',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lsr-id-if', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This defines the interface to use for the LDP LSR
                identifier address for all sessions. The IP
                address of this interface will be used as the
                identifier.
                ''',
                'lsr_id_if',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('lsr-id-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This is the IP address to be used as the LDP
                LSR ID for all sessions.
                ''',
                'lsr_id_ip',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('lsr-id-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the IP address to be used as the LDP
                        LSR ID for all sessions.
                        ''',
                        'lsr_id_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('lsr-id-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This is the IP address to be used as the LDP
                        LSR ID for all sessions.
                        ''',
                        'lsr_id_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'router-id',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable Downstream on Demand for this LSR. In this
                mode a label is not advertised to a peer, unless
                the peer explicitly requests it. At the same time,
                since the peer does not automatically advertise
                labels, the label request is sent whenever the
                next-hop points out to a peer that no remote label
                has been assigned.
                ''',
                'enabled',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This filter contains a list of peer IDs that are
                configured for downstream-on-demand mode. When the
                filter is changed or configured, the list of
                established neighbors is traversed. If a session's
                downstream-on-demand configuration has changed, the
                session is reset in order that the new
                down-stream-on-demand mode can be configured. The
                reason for resetting the session is to ensure that
                the labels are properly advertised between the
                peers. When a new session is established, the ACL
                is verified to determine whether the session should
                negotiate for downstream-on-demand mode. If the
                filter string is configured and the corresponding
                filter does not exist or is empty, then
                downstream-on-demand mode is not configured for any
                neighbor.
                The filter type is device specific and could be an
                ACL, a prefix list, or other mechanism.
                ''',
                'filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'downstream-on-demand',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection',
            False, 
            [
            _MetaInfoClassMember('enable-prot', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is set true to enable session protection.
                ''',
                'enable_prot',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('inf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This sessiom holdup duration is infinite.
                ''',
                'inf',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('peer-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is an optional filter to restrict session
                protection. If the string is null or unconfigured
                then session protection applied to all peers. The
                filter type is device specific and could be an ACL,
                a prefix list, or other mechanism.
                ''',
                'peer_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('30', '2147483')], [], 
                '''                This is the sessiom holdup duration in
                seconds.
                ''',
                'seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'protection',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.Session' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg.Session',
            False, 
            [
            _MetaInfoClassMember('backoff-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initial session backoff time (seconds).
                The LDP backoff mechanism prevents two incompatibly
                configured label switch routers (LSRs) from engaging
                in an unthrottled sequence of session setup failures.
                
                For example, an incompatibility arises when two
                neighboring routers attempt to perform LC-ATM
                (label-controlled ATM) but the two are using different
                ranges of VPI/VCI values for labels.
                
                If a session setup attempt fails due to an
                incompatibility, each LSR delays its next attempt
                (that is, backs off), increasing the delay
                exponentially with each successive failure until the
                maximum backoff delay is reached.
                
                The default settings correspond to the lowest settings
                for initial and maximum backoff values defined by the
                LDP protocol specification. You should change the
                settings from the default values only if such settings
                result in undesirable behavior.
                ''',
                'backoff_init',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('backoff-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum session backoff time (seconds)
                The LDP backoff mechanism prevents two incompatibly
                configured label switch routers (LSRs) from engaging
                in an unthrottled sequence of session setup failures.
                
                For example, an incompatibility arises when two
                neighboring routers attempt to perform LC-ATM
                (label-controlled ATM) but the two are using different
                ranges of VPI/VCI values for labels.
                
                If a session setup attempt fails due to an
                incompatibility, each LSR delays its next attempt
                (that is, backs off), increasing the delay
                exponentially with each successive failure until the
                maximum backoff delay is reached.
                
                The default settings correspond to the lowest settings
                for initial and maximum backoff values defined by the
                LDP protocol specification. You should change the
                settings from the default values only if such settings
                result in undesirable behavior.
                ''',
                'backoff_max',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('downstream-on-demand', REFERENCE_LIST, 'DownstreamOnDemand' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand', 
                [], [], 
                '''                This container holds config for Downstream on Demand.
                For it to be enabled, the Downstream on demand
                feature has to be configured on both peers of the
                session. If only one peer in the session has
                downstream-on-demand feature configured, then the
                session does not use downstream-on-demand mode.
                If, after, a label request is sent, and no remote
                label is received from the peer, the router will
                periodically resend the label request. After the
                peer advertises a label after receiving the label
                request, it will automatically readvertise the label
                if any label attribute changes subsequently.
                ''',
                'downstream_on_demand',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, the session is held indefinitely
                in the absence of LDP messages from the peer.
                ''',
                'infinite',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protection', REFERENCE_CLASS, 'Protection' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection', 
                [], [], 
                '''                Configure Session Protection parameters
                ''',
                'protection',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number from 15 to 2147483, that defines the time,
                in seconds, an LDP session is maintained in the
                absence of LDP messages from the session peer.
                ''',
                'seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family name.
                ''',
                'af_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set true, this enables MPLS forwarding for the
                ip default route.
                ''',
                'default_route',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('implicit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not advertise an explicit address in LDP
                discovery hello messages or advertise a default
                address. Use the default address for LDP
                transport.
                ''',
                'implicit',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Advertise this interface's address as the
                explicit address in LDP discovery hello messages
                and use it for LDP transport.
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('ipaddr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Advertise this address as the explicit address
                in LDP discovery hello messages and use it
                for LDP transport.
                ''',
                'ipaddr',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('ipaddr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Advertise this address as the explicit address
                        in LDP discovery hello messages and use it
                        for LDP transport.
                        ''',
                        'ipaddr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('ipaddr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Advertise this address as the explicit address
                        in LDP discovery hello messages and use it
                        for LDP transport.
                        ''',
                        'ipaddr',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'af-cfg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.PerAf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg.PerAf',
            False, 
            [
            _MetaInfoClassMember('af-cfg', REFERENCE_LIST, 'AfCfg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg', 
                [], [], 
                '''                This container holds the global per address family
                configuration.
                ''',
                'af_cfg',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'per-af',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GlobalCfg.AdminStatusEnum' : _MetaInfoEnum('AdminStatusEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpConfig.GlobalCfg.ProtocolEnum' : _MetaInfoEnum('ProtocolEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'ldp':'ldp',
            'tdp':'tdp',
            'both':'both',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpConfig.GlobalCfg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GlobalCfg',
            False, 
            [
            _MetaInfoClassMember('admin-status', REFERENCE_ENUM_CLASS, 'AdminStatusEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.AdminStatusEnum', 
                [], [], 
                '''                This leaf controls the administrative status of LDP for
                this LSR. If set to disable, then all LDP activity will
                be disabled and all LDP sessions with peers will
                terminate. The LDP configuration will remain intact.
                
                When the admin status is set back to 'enable', then
                LDP will resume operations and attempt to establish new
                sessions with the peers.
                ''',
                'admin_status',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('dcsp-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                This sets the 6-bit Differentiated Services
                Code Point (DSCP) value in the TCP packets for LDP
                messages being sent from the LSR.
                ''',
                'dcsp_val',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('disable-delay', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This choice causes IGP sync up immediately upon
                session up.
                ''',
                'disable_delay',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('disable-delay-proc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This choice causes IGP sync up immediately upon
                session up.
                ''',
                'disable_delay_proc',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('disable-quick-start', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, disable LDP discovery's quick
                start mode for this LSR.
                ''',
                'disable_quick_start',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('enable-nsr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf controls whether Non-Stop-Routing should
                be enabled to include MPLS LDP.
                ''',
                'enable_nsr',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('high-priority', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This sets the priority within the LSR for TCP
                packets for LDP messages being sent from the LSR.
                They are given a higher transmission priorty and
                will avoid being queued behind lower priority
                messages.
                ''',
                'high_priority',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('init-sess-thresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                When attempting to establish a session with
                a given Peer, the given LDP Entity should
                send out the YANG notification,
                'init-sess-thresh-ex', when
                the number of Session Initialization messages
                sent exceeds this threshold.
                
                The notification is used to notify an
                operator when this Entity and its Peer are
                possibly engaged in an endless sequence
                of messages as each NAKs the other's
                
                Initialization messages with Error Notification
                messages.  Setting this threshold which triggers
                the notification is one way to notify the
                operator.  The notification should be generated
                each time this threshold is exceeded and
                for every subsequent Initialization message
                which is NAK'd with an Error Notification
                message after this threshold is exceeded.
                
                A value of 0 (zero) for this object
                indicates that the threshold is infinity, thus
                the YANG notification will never be generated.
                ''',
                'init_sess_thresh',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('loop-detection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf enables or disables Loop Detection globally
                for the LSR.
                ''',
                'loop_detection',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('per-af', REFERENCE_CLASS, 'PerAf' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.PerAf', 
                [], [], 
                '''                This container holds the global per address family
                configuration.
                ''',
                'per_af',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'ProtocolEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.ProtocolEnum', 
                [], [], 
                '''                This leaf defines the protocol to be used. The default
                is LDP.
                ''',
                'protocol',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('router-id', REFERENCE_LIST, 'RouterId' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.RouterId', 
                [], [], 
                '''                Configuration for LDP Router ID (LDP ID)
                ''',
                'router_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Time in seconds to delay IGP sync after session
                comes up
                ''',
                'seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('seconds-delay-proc', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Time in seconds to delay IGP sync after session
                comes up
                ''',
                'seconds_delay_proc',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg.Session', 
                [], [], 
                '''                Configure session parameters. Session parameters effect
                the session between LDP peers once the session has been
                established.
                ''',
                'session',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Writing this leaf tears down all LDP sessions, withdraws
                all outgoing labels from the forwarding plane, and frees
                all local labels that have been allocated.
                ''',
                'shutdown',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'global-cfg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.AdminStatusEnum' : _MetaInfoEnum('AdminStatusEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.LabelProtocolEnum' : _MetaInfoEnum('LabelProtocolEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'ldp':'ldp',
            'tdp':'tdp',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpConfig.NbrTable.NbrCfg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.NbrTable.NbrCfg',
            False, 
            [
            _MetaInfoClassMember('nbr-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'nbr_vrf',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('nbr-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address for the LDP neighbor. This may be
                IPv4 or IPv6.
                ''',
                'nbr_ip',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('nbr-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address for the LDP neighbor. This may be
                        IPv4 or IPv6.
                        ''',
                        'nbr_ip',
                        'Cisco-IOS-XE-mpls-ldp', True),
                    _MetaInfoClassMember('nbr-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address for the LDP neighbor. This may be
                        IPv4 or IPv6.
                        ''',
                        'nbr_ip',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('admin-status', REFERENCE_ENUM_CLASS, 'AdminStatusEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.AdminStatusEnum', 
                [], [], 
                '''                The administrative status of this neighbor.
                If this object is changed from 'enable' to 'disable'
                and this entity has already attempted to establish
                contact with a neighbor, a 'tear-down' for that session
                is issued and the session and all information related
                to that session ceases to exist).
                
                When the admin status is set back to 'enable', then
                this Entity will attempt to establish a new session
                with the neighbor.
                ''',
                'admin_status',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('implicit-withdraw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable LDP implicit withdraw label for this peer.
                ''',
                'implicit_withdraw',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-binding-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Accept only labels matching this filter.
                The filter type is device specific and could be an
                ACL, a prefix list, or other mechanism.
                ''',
                'label_binding_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-protocol', REFERENCE_ENUM_CLASS, 'LabelProtocolEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.LabelProtocolEnum', 
                [], [], 
                '''                This leaf defines the protocol to be used. The default
                is LDP.
                ''',
                'label_protocol',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enables password authentication and stores the
                password using a cryptographic hash.
                ''',
                'password',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('targeted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Establish or delete a targeted session.
                ''',
                'targeted',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nbr-cfg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.NbrTable' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.NbrTable',
            False, 
            [
            _MetaInfoClassMember('nbr-cfg', REFERENCE_LIST, 'NbrCfg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.NbrTable.NbrCfg', 
                [], [], 
                '''                This entry holds the configuration of a single neighbor
                identified by the IP address of that neighbor.
                ''',
                'nbr_cfg',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nbr-table',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Passwords.Password' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Passwords.Password',
            False, 
            [
            _MetaInfoClassMember('nbr-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'nbr_vrf',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('nbr-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This leaf holds the neighbor id for this password.
                This id may be an lsr-id, an ip-address, or
                a filter describing a group of neighbors.
                ''',
                'nbr_id',
                'Cisco-IOS-XE-mpls-ldp', True, [
                    _MetaInfoClassMember('nbr-id', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        This leaf holds the neighbor id for this password.
                        This id may be an lsr-id, an ip-address, or
                        a filter describing a group of neighbors.
                        ''',
                        'nbr_id',
                        'Cisco-IOS-XE-mpls-ldp', True, [
                            _MetaInfoClassMember('nbr-id', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                This leaf holds the neighbor id for this password.
                                This id may be an lsr-id, an ip-address, or
                                a filter describing a group of neighbors.
                                ''',
                                'nbr_id',
                                'Cisco-IOS-XE-mpls-ldp', True),
                            _MetaInfoClassMember('nbr-id', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                This leaf holds the neighbor id for this password.
                                This id may be an lsr-id, an ip-address, or
                                a filter describing a group of neighbors.
                                ''',
                                'nbr_id',
                                'Cisco-IOS-XE-mpls-ldp', True),
                        ]),
                    _MetaInfoClassMember('nbr-id', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        This leaf holds the neighbor id for this password.
                        This id may be an lsr-id, an ip-address, or
                        a filter describing a group of neighbors.
                        ''',
                        'nbr_id',
                        'Cisco-IOS-XE-mpls-ldp', True),
                ]),
            _MetaInfoClassMember('password-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is a user-assigned unique number identifying a
                password for this neighbor or group of neighbors.
                Multiple passwords may be assigned to a neighbor.
                If that is the case, each password is tried starting
                with the lowest number to the highest until a
                passsword matches or the list is exhausted.
                ''',
                'password_num',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('clear-pass', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is a clear-text (non-encrypted password to be
                used with the neighbor.
                ''',
                'clear_pass',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('encrypt-pass', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is an encrypted password to be used with the
                neighbor.
                ''',
                'encrypt_pass',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('keychain-pass', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is a keychain identifier, which identifies
                an separately configured keychain to be used with
                the neighbor neighbor.
                ''',
                'keychain_pass',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('pass-required', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf is set true if the password is required
                and false if the password is not required.
                ''',
                'pass_required',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Passwords' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Passwords',
            False, 
            [
            _MetaInfoClassMember('password', REFERENCE_LIST, 'Password' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Passwords.Password', 
                [], [], 
                '''                This holds the MPLS LDP password configuration for use
                with a single LDP neighbor or group of LDP neighbors.
                ''',
                'password',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'passwords',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Session' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Session',
            False, 
            [
            _MetaInfoClassMember('backoff', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initial session backoff time (seconds)
                ''',
                'backoff',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore LDP session holdtime
                ''',
                'infinite',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Session holdtime in seconds
                ''',
                'seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter',
            False, 
            [
            _MetaInfoClassMember('prefix-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This contains the filter name for this label's
                prefix.  The filter type is device specific and
                could be an ACL, a prefix list, or other
                mechanism.
                ''',
                'prefix_filter',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('peer-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This contains the filter name for this label's
                Peer. The filter type is device specific and could
                be an ACL, a prefix list, or other mechanism.
                ''',
                'peer_filter',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is an optional interface that may be used to
                restrict the scope of the label advertisement.
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('adv-label-cfg', REFERENCE_ENUM_CLASS, 'AdvLabelTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AdvLabelTypeEnum', 
                [], [], 
                '''                This leaf controls what type of label is advertised
                for matching prefixes to the matching peers.
                ''',
                'adv_label_cfg',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'advt-filter',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family name.
                ''',
                'af_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('advt-filter', REFERENCE_LIST, 'AdvtFilter' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter', 
                [], [], 
                '''                MPLS LDP Label advertisement filter restrictions.
                ''',
                'advt_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('host-route-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if this LSR should allocate host-routes
                only.
                ''',
                'host_route_enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('prefix-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This contains the filter name for this label's
                prefix. The filter type is device specific and
                could be an ACL, a prefix list, or other
                mechanism.
                ''',
                'prefix_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-af-cfg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.LabelCfg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.LabelCfg',
            False, 
            [
            _MetaInfoClassMember('label-af-cfg', REFERENCE_LIST, 'LabelAfCfg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg', 
                [], [], 
                '''                This is an allocation filter and advertisement filters
                for LDP labels in this address family.
                ''',
                'label_af_cfg',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-cfg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Discovery.LinkHello' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Discovery.LinkHello',
            False, 
            [
            _MetaInfoClassMember('holdtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LDP discovery link hello holdtime in seconds
                ''',
                'holdtime',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LDP discovery link hello interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'link-hello',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to true if targeted hello messages may be
                accepted.
                ''',
                'enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('src-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Only respond to requests for targeted hello messages
                from sources matching this filter.
                The filter type is device specific and could be
                an ACL, a prefix list, or other mechanism.
                ''',
                'src_filter',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'accept',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Discovery.TargetedHello' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Discovery.TargetedHello',
            False, 
            [
            _MetaInfoClassMember('accept', REFERENCE_CLASS, 'Accept' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept', 
                [], [], 
                '''                Enables router to respond to requests for targeted
                hello messages
                ''',
                'accept',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to true if targeted hello messages may be
                accepted.
                ''',
                'enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('holdtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LDP discovery targeted hello holdtime in seconds.
                ''',
                'holdtime',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LDP discovery targeted hello interval in seconds.
                ''',
                'interval',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'targeted-hello',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family name.
                ''',
                'af_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('int-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Interface Name
                ''',
                'int_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('trans-int', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Advertise this interface's address as the
                address in LDP discovery hello messages
                and use it for LDP transport.
                ''',
                'trans_int',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('trans-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Advertise this address as the address in LDP
                discovery hello messages and use it for LDP
                transport.
                ''',
                'trans_ip',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('trans-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Advertise this address as the address in LDP
                        discovery hello messages and use it for LDP
                        transport.
                        ''',
                        'trans_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('trans-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Advertise this address as the address in LDP
                        discovery hello messages and use it for LDP
                        transport.
                        ''',
                        'trans_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'int-trans-addr',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs',
            False, 
            [
            _MetaInfoClassMember('int-trans-addr', REFERENCE_LIST, 'IntTransAddr' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr', 
                [], [], 
                '''                This entry contains the per-interface transport
                addresses, which overide the global and default
                values.
                ''',
                'int_trans_addr',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'int-trans-addrs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Discovery',
            False, 
            [
            _MetaInfoClassMember('instance-tlv', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set this leaf to true to disable transmit and receive
                processing for Type-Length-Value (TLV) in the discovery
                messages.
                ''',
                'instance_tlv',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('int-trans-addrs', REFERENCE_CLASS, 'IntTransAddrs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs', 
                [], [], 
                '''                This list contains the per-interface transport
                addresses, which overide the global and default
                values.
                ''',
                'int_trans_addrs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('link-hello', REFERENCE_CLASS, 'LinkHello' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Discovery.LinkHello', 
                [], [], 
                '''                This container holds the parameters for the non-targeted
                link hello.
                ''',
                'link_hello',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('targeted-hello', REFERENCE_CLASS, 'TargetedHello' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Discovery.TargetedHello', 
                [], [], 
                '''                This container holds the parameters for the targeted
                link hello.
                ''',
                'targeted_hello',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GracefulRestart.Helper' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GracefulRestart.Helper',
            False, 
            [
            _MetaInfoClassMember('helper-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'helper_vrf',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('helper-filter', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This contains the filter name for peers for which this
                LSR will act as a graceful-restart helper.
                The filter type is device specific and could be an
                ACL, a prefix list, or other mechanism.
                ''',
                'helper_filter',
                'Cisco-IOS-XE-mpls-ldp', True),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'helper',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('forwarding-holding', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Specifies the amount of time the MPLS LDP forwarding
                state must be preserved after the control plane
                restarts.
                ''',
                'forwarding_holding',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('helper', REFERENCE_LIST, 'Helper' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GracefulRestart.Helper', 
                [], [], 
                '''                This contains the filter name for peers for which this
                LSR will act as a graceful-restart helper.
                ''',
                'helper',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('is-graceful-restartable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful restartable.
                ''',
                'is_graceful_restartable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('max-recovery', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Amount of time (in seconds) that the router should hold
                stale label-FEC bindings after an LDP session has been
                reestablished.
                ''',
                'max_recovery',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-liveness', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Amount of time (in seconds) that the router must wait
                for an LDP session to be reestablished.
                ''',
                'nbr_liveness',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Log MPLS LDP password configuration changes.
                ''',
                'enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the number of messages per minute to limit
                the logging. A value of 0 indicates no limits on
                the number of logged messages.
                ''',
                'rate_limit',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'config-msg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Log MPLS LDP password rollover messages.
                ''',
                'enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the number of messages per minute to limit
                the logging. A value of 0 indicates no limits on
                the number of logged messages.
                ''',
                'rate_limit',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'rollover-msg',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Logging.Password' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Logging.Password',
            False, 
            [
            _MetaInfoClassMember('config-msg', REFERENCE_CLASS, 'ConfigMsg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg', 
                [], [], 
                '''                Log MPLS LDP password configuration changes.
                ''',
                'config_msg',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('rollover-msg', REFERENCE_CLASS, 'RolloverMsg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg', 
                [], [], 
                '''                Log MPLS LDP password rollover messages.
                ''',
                'rollover_msg',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Logging' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Logging',
            False, 
            [
            _MetaInfoClassMember('adjacency', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable logging of adjacency messages.
                ''',
                'adjacency',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable logging of graceful-restart messages.
                ''',
                'graceful_restart',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable logging of neighbor messages.
                ''',
                'neighbor',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nsr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable logging of nsr messages.
                ''',
                'nsr',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Logging.Password', 
                [], [], 
                '''                Enable logging of password messages.
                ''',
                'password',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session-protection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable logging of session-protection messages.
                ''',
                'session_protection',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist',
            False, 
            [
            _MetaInfoClassMember('advertise-to', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter of neighbors to receive BGP route
                redistributions from LDP. If the list is
                empty or unset, all LDP neighbors will
                receive redistributions.
                ''',
                'advertise_to',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First half of BGP AS number in XX.YY
                format.  Mandatory Must be a non-zero
                value if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Second half of BGP AS number in XX.YY
                format. Mandatory Must be a non-zero value
                if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is set true to allow LDP to redistribute
                BGP routes.
                ''',
                'enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'bgp-redist',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'AfEnum', 
                [], [], 
                '''                Address Family name.
                ''',
                'af_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('autoconfig-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if LDP autoconfig is explicitly disabled
                on this interface.
                ''',
                'autoconfig_disable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('bgp-redist', REFERENCE_CLASS, 'BgpRedist' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist', 
                [], [], 
                '''                MPLS LDP configuration for protocol
                redistribution. By default, redistribution of BGP
                routes is disabled. It can be enabled for all
                BGP routes or for a specific AS. Also it can be
                redistributed to all LDP peers or to a filtered
                group of peers.
                ''',
                'bgp_redist',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is set true to enable LDP on this
                interface.
                ''',
                'enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af', 
                [], [], 
                '''                MPLS LDP Operational data for this Address Family.
                ''',
                'af',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Interface Name
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs', 
                [], [], 
                '''                Address Family specific operational data
                ''',
                'afs',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('disable-delay', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This choice causes IGP sync up immediately upon
                session up.
                ''',
                'disable_delay',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('disable-quick-start-int', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, disable LDP discovery's quick
                start mode for this interface.
                ''',
                'disable_quick_start_int',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('link-hello-hold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LDP discovery link hello holdtime in seconds for this
                interface. This value overides the global setting.
                ''',
                'link_hello_hold',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('link-hello-int', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LDP discovery link hello interval in seconds for this
                interface. This value overides the global setting.
                ''',
                'link_hello_int',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Time in seconds to delay IGP sync after session
                comes up.
                ''',
                'seconds',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Interfaces.Interface', 
                [], [], 
                '''                MPLS LDP Interface configuration commands. Where a
                corresponding global configuration command exists, the
                interface level command will take precedence when
                configured.
                ''',
                'interface',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Routing.RoutingInst.LevelIdEnum' : _MetaInfoEnum('LevelIdEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp',
        {
            'level-1':'level_1',
            'level-2':'level_2',
            'level-1-2':'level_1_2',
        }, 'Cisco-IOS-XE-mpls-ldp', _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp']),
    'MplsLdp.MplsLdpConfig.Routing.RoutingInst' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Routing.RoutingInst',
            False, 
            [
            _MetaInfoClassMember('routing-inst-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the routing instance for which this MPLS LDP
                configuration applies.
                ''',
                'routing_inst_name',
                'Cisco-IOS-XE-mpls-ldp', True),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This leaf restricts the LDP Autoconfiguration
                feature to enable LDP on interfaces belonging to
                an OSPF process for a specific area. If no area
                is specified, then this applies to all interfaces
                associated with the. If an area ID is specified,
                then only interfaces associated with that OSPF
                area are automatically enabled with LDP.
                Any interface-specific ldp configuration will
                overide this setting for that interface.
                ''',
                'area_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('autoconfig-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf enables or disables LDP for all interfaces
                covered by this routing instance subject to the
                autoconfig-scope.
                ''',
                'autoconfig_enable',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('level-id', REFERENCE_ENUM_CLASS, 'LevelIdEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Routing.RoutingInst.LevelIdEnum', 
                [], [], 
                '''                This leaf restricts the LDP Autoconfiguration
                feature to enable LDP on interfaces belonging to
                an ISIS process for a specific level. If no level
                is specified, then this applies to all interfaces
                associated with the. If a level is specified,
                then only interfaces associated with that ISIS
                level are automatically enabled with LDP.
                Any interface-specific ldp configuration will
                overide this setting for that interface.
                ''',
                'level_id',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true this enables LDP IGP synchronization.
                Without syncrhonization, packet loss can occur because
                the actions of the IGP and LDP are not synchronized.
                ''',
                'sync',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'routing-inst',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.Routing' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.Routing',
            False, 
            [
            _MetaInfoClassMember('routing-inst', REFERENCE_LIST, 'RoutingInst' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Routing.RoutingInst', 
                [], [], 
                '''                This entry provides the MPLS LDP config for this
                routing instance.
                ''',
                'routing_inst',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'routing',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig.DualStack' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig.DualStack',
            False, 
            [
            _MetaInfoClassMember('max-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Wait time in seconds (0 indicates no preference)
                ''',
                'max_wait',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('prefer-ipv4-peers', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the filter name for peers where IPv4
                connections are preferred over IPv6 connections.
                The filter type is device specific and could be
                an ACL, a prefix list, or other mechanism.
                ''',
                'prefer_ipv4_peers',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'dual-stack',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp.MplsLdpConfig' : {
        'meta_info' : _MetaInfoClass('MplsLdp.MplsLdpConfig',
            False, 
            [
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Discovery', 
                [], [], 
                '''                LDP discovery
                ''',
                'discovery',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('dual-stack', REFERENCE_CLASS, 'DualStack' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.DualStack', 
                [], [], 
                '''                This container holds the configuration of dual IPv4 and
                IPv6 stack peers.
                ''',
                'dual_stack',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('global-cfg', REFERENCE_CLASS, 'GlobalCfg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GlobalCfg', 
                [], [], 
                '''                This contains hold all MPLS LDP Configuration with Global
                scope. These values affect the entire LSR unless
                overiddden by a parameter with a more localized scope.
                ''',
                'global_cfg',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.GracefulRestart', 
                [], [], 
                '''                Configure LDP Graceful Restart
                ''',
                'graceful_restart',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Interfaces', 
                [], [], 
                '''                MPLS LDP Interface configuration commands.
                ''',
                'interfaces',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('label-cfg', REFERENCE_CLASS, 'LabelCfg' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.LabelCfg', 
                [], [], 
                '''                This container holds the label allocation and
                advertisement configuration for the LDP Label Information
                Base. These control what prefixes may be allocated and
                advertised to peers.
                ''',
                'label_cfg',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Logging', 
                [], [], 
                '''                Enable LDP logging
                ''',
                'logging',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-table', REFERENCE_CLASS, 'NbrTable' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.NbrTable', 
                [], [], 
                '''                This container holds the list of neighbor configuration
                parameters.
                ''',
                'nbr_table',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('passwords', REFERENCE_CLASS, 'Passwords' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Passwords', 
                [], [], 
                '''                This holds the MPLS LDP password configuration for use
                with LDP neighbors.
                ''',
                'passwords',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('routing', REFERENCE_CLASS, 'Routing' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Routing', 
                [], [], 
                '''                This containter provides the MPLS LDP config for routing
                protocols from which it can obtain addresses to
                associate with labels.
                ''',
                'routing',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig.Session', 
                [], [], 
                '''                Configure session parameters
                ''',
                'session',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'mpls-ldp-config',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'MplsLdp' : {
        'meta_info' : _MetaInfoClass('MplsLdp',
            False, 
            [
            _MetaInfoClassMember('mpls-ldp-config', REFERENCE_CLASS, 'MplsLdpConfig' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpConfig', 
                [], [], 
                '''                MPLS LDP Configuration.
                ''',
                'mpls_ldp_config',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('mpls-ldp-state', REFERENCE_CLASS, 'MplsLdpState' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'MplsLdp.MplsLdpState', 
                [], [], 
                '''                MPLS LDP operational data.
                ''',
                'mpls_ldp_state',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'mpls-ldp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'ClearMsgCountersRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearMsgCountersRpc.Input',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR ID of the neighbor
                ''',
                'nbr_ip',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('nbr-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR ID of the neighbor
                        ''',
                        'nbr_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('nbr-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR ID of the neighbor
                        ''',
                        'nbr_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear information for all neighbors.
                ''',
                'all',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'ClearMsgCountersRpc.Output' : {
        'meta_info' : _MetaInfoClass('ClearMsgCountersRpc.Output',
            False, 
            [
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Return status will be 'OK' on success or an explanation
                string on failure.
                ''',
                'status',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'ClearMsgCountersRpc' : {
        'meta_info' : _MetaInfoClass('ClearMsgCountersRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'ClearMsgCountersRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'ClearMsgCountersRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'clear-msg-counters',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RestartNeighborRpc.Input' : {
        'meta_info' : _MetaInfoClass('RestartNeighborRpc.Input',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('nbr-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSR ID of the neighbor
                ''',
                'nbr_ip',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('nbr-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR ID of the neighbor
                        ''',
                        'nbr_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('nbr-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSR ID of the neighbor
                        ''',
                        'nbr_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Restart sessions for all neighbors.
                ''',
                'all',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RestartNeighborRpc.Output' : {
        'meta_info' : _MetaInfoClass('RestartNeighborRpc.Output',
            False, 
            [
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Return status will be 'OK' on success or an explanation
                string on failure.
                ''',
                'status',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RestartNeighborRpc' : {
        'meta_info' : _MetaInfoClass('RestartNeighborRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'RestartNeighborRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'RestartNeighborRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'restart-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'ClearForwardingRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearForwardingRpc.Input',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This contains the VRF Name, where 'default' is used
                for the default vrf.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('prefix-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This case provides the IP prefix for the forwarding
                entry whose data should be cleared.
                ''',
                'prefix_ip',
                'Cisco-IOS-XE-mpls-ldp', False, [
                    _MetaInfoClassMember('prefix-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This case provides the IP prefix for the forwarding
                        entry whose data should be cleared.
                        ''',
                        'prefix_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                    _MetaInfoClassMember('prefix-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This case provides the IP prefix for the forwarding
                        entry whose data should be cleared.
                        ''',
                        'prefix_ip',
                        'Cisco-IOS-XE-mpls-ldp', False),
                ]),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This case is used to clear the forwarding entries
                for all prefixes.
                ''',
                'all',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'ClearForwardingRpc.Output' : {
        'meta_info' : _MetaInfoClass('ClearForwardingRpc.Output',
            False, 
            [
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Return status will be 'OK' on success or an explanatory
                string on failure.
                ''',
                'status',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'ClearForwardingRpc' : {
        'meta_info' : _MetaInfoClass('ClearForwardingRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'ClearForwardingRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XE-mpls-ldp', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp', 'ClearForwardingRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-mpls-ldp', False),
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'clear-forwarding',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrSyncPrepIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrSyncPrepIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-sync-prep',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnPEndSockNotSyncedIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnPEndSockNotSyncedIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-p-end-sock-not-synced',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LabelTypeMplsIdentity' : {
        'meta_info' : _MetaInfoClass('LabelTypeMplsIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-type-mpls',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathLblOwnerLdpIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathLblOwnerLdpIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-lbl-owner-ldp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LabelTypeUnLabeledIdentity' : {
        'meta_info' : _MetaInfoClass('LabelTypeUnLabeledIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-type-un-labeled',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrNoneIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrNoneIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-none',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrRxUnexpOpenIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrRxUnexpOpenIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-rx-unexp-open',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'DownNbrReasonNaIdentity' : {
        'meta_info' : _MetaInfoClass('DownNbrReasonNaIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'down-nbr-reason-na',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'DownNbrReasonDiscHelloIdentity' : {
        'meta_info' : _MetaInfoClass('DownNbrReasonDiscHelloIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'down-nbr-reason-disc-hello',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrLdpPeerIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrLdpPeerIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-ldp-peer',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathIpNoFlagIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathIpNoFlagIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-ip-no-flag',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrTcpPeerIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrTcpPeerIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-tcp-peer',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LdpNsrPeerSyncStOperIdentity' : {
        'meta_info' : _MetaInfoClass('LdpNsrPeerSyncStOperIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'ldp-nsr-peer-sync-st-oper',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LdpNsrPeerSyncStPrepIdentity' : {
        'meta_info' : _MetaInfoClass('LdpNsrPeerSyncStPrepIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'ldp-nsr-peer-sync-st-prep',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrDhcAddIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrDhcAddIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-dhc-add',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LabelTypeUnknownIdentity' : {
        'meta_info' : _MetaInfoClass('LabelTypeUnknownIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'label-type-unknown',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathIpBackupRemoteIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathIpBackupRemoteIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-ip-backup-remote',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonNoHelloAdjIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonNoHelloAdjIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason-no-hello-adj',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrAdjAddIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrAdjAddIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-adj-add',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathLblOwnerNoneIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathLblOwnerNoneIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-lbl-owner-none',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonNaIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonNaIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason-na',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonNoPeerSessIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonNoPeerSessIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason-no-peer-sess',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathLblOwnerBgpIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathLblOwnerBgpIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-lbl-owner-bgp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonPeerUpdateNotReceivedIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonPeerUpdateNotReceivedIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason-peer-update-not-received',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnMissingElemIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnMissingElemIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-missing-elem',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnNoPEndSockIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnNoPEndSockIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-no-p-end-sock',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnNoCtxIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnNoCtxIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-no-ctx',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LdpNsrPeerSyncStReadyIdentity' : {
        'meta_info' : _MetaInfoClass('LdpNsrPeerSyncStReadyIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'ldp-nsr-peer-sync-st-ready',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathIpBackupIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathIpBackupIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-ip-backup',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrAppFailIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrAppFailIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-app-fail',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrLdpSyncNackIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrLdpSyncNackIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-ldp-sync-nack',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrAddrBindIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrAddrBindIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-addr-bind',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LdpNsrPeerSyncStAppWaitIdentity' : {
        'meta_info' : _MetaInfoClass('LdpNsrPeerSyncStAppWaitIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'ldp-nsr-peer-sync-st-app-wait',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LdpNsrPeerSyncStWaitIdentity' : {
        'meta_info' : _MetaInfoClass('LdpNsrPeerSyncStWaitIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'ldp-nsr-peer-sync-st-wait',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrAppNotFoundIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrAppNotFoundIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-app-not-found',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrRxNotifIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrRxNotifIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-rx-notif',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'DownNbrReasonNbrHoldIdentity' : {
        'meta_info' : _MetaInfoClass('DownNbrReasonNbrHoldIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'down-nbr-reason-nbr-hold',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrRxBadPieIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrRxBadPieIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-rx-bad-pie',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnNoneIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnNoneIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-none',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrTcpGblIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrTcpGblIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-tcp-gbl',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathLblOwnerStaticIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathLblOwnerStaticIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-lbl-owner-static',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnTblIdMismatchIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnTblIdMismatchIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-tbl-id-mismatch',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnPpExistsIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnPpExistsIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-pp-exists',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonInternalIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonInternalIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason-internal',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IccpTypeMlacpIdentity' : {
        'meta_info' : _MetaInfoClass('IccpTypeMlacpIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'iccp-type-mlacp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnEnomemIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnEnomemIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-enomem',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IgpSyncDownReasonPeerUpdateNotDoneIdentity' : {
        'meta_info' : _MetaInfoClass('IgpSyncDownReasonPeerUpdateNotDoneIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'igp-sync-down-reason-peer-update-not-done',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathIpBgpBackupIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathIpBgpBackupIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-ip-bgp-backup',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrPeerSyncErrLdpGblIdentity' : {
        'meta_info' : _MetaInfoClass('NsrPeerSyncErrLdpGblIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-peer-sync-err-ldp-gbl',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'LdpNsrPeerSyncStNoneIdentity' : {
        'meta_info' : _MetaInfoClass('LdpNsrPeerSyncStNoneIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'ldp-nsr-peer-sync-st-none',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'IcpmTypeIccpIdentity' : {
        'meta_info' : _MetaInfoClass('IcpmTypeIccpIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'icpm-type-iccp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrStatusDisabledIdentity' : {
        'meta_info' : _MetaInfoClass('NsrStatusDisabledIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-status-disabled',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrStatusReadyIdentity' : {
        'meta_info' : _MetaInfoClass('NsrStatusReadyIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-status-ready',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrPpCreateIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrPpCreateIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-pp-create',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrTpCreateIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrTpCreateIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-tp-create',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrUnexpPeerDownIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrUnexpPeerDownIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-unexp-peer-down',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'RoutePathIpProtectedIdentity' : {
        'meta_info' : _MetaInfoClass('RoutePathIpProtectedIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'route-path-ip-protected',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrSyncNackRsnErrAppInvalidIdentity' : {
        'meta_info' : _MetaInfoClass('NsrSyncNackRsnErrAppInvalidIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-sync-nack-rsn-err-app-invalid',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
    'NsrStatusNotReadyIdentity' : {
        'meta_info' : _MetaInfoClass('NsrStatusNotReadyIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XE-mpls-ldp',
            'nsr-status-not-ready',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-ldp'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp'
        ),
    },
}
_meta_table['MplsLdp.MplsLdpState.OperSummary.Common']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.OperSummary']['meta_info']
_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.ForwardingSummary']['meta_info']
_meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Nhs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.ForwardingSummary']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Parameters']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Capabilities.Capability']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Capabilities']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Vrfs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Discovery.LinkHelloState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Discovery.TargetedHellos']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Discovery.DiscoveryStats']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Discovery']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Discovery.LinkHelloState']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Discovery']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Discovery.TargetedHellos']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Discovery']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Forwarding']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Bindings.BindingsSumAfs']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Bindings.Binding']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Bindings.Binding']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings.BindingsSumAfs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Bindings']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings.Binding']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Bindings']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.NbrAdjs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.Backoffs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info']
_meta_table['MplsLdp.MplsLdpState.LabelRanges.LabelRange']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState.LabelRanges']['meta_info']
_meta_table['MplsLdp.MplsLdpState.OperSummary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.ForwardingSummary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.BindingsSummary']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.NsrSummaryAll']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Parameters']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Capabilities']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.BackoffParameters']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.GracefulRestart']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Vrfs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Discovery']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Forwarding']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Bindings']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpState.LabelRanges']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpState']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.PerAf']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.RouterId']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.PerAf']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.NbrTable.NbrCfg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.NbrTable']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Passwords.Password']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Passwords']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.LabelCfg']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Discovery.TargetedHello']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Discovery.LinkHello']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Discovery']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Discovery.TargetedHello']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Discovery']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Discovery']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GracefulRestart.Helper']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.GracefulRestart']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Logging.Password']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Logging.Password']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Logging.Password']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Logging']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Interfaces']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Routing.RoutingInst']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig.Routing']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GlobalCfg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.NbrTable']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Passwords']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Session']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.LabelCfg']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Discovery']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.GracefulRestart']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Logging']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Interfaces']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.Routing']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig.DualStack']['meta_info'].parent =_meta_table['MplsLdp.MplsLdpConfig']['meta_info']
_meta_table['MplsLdp.MplsLdpState']['meta_info'].parent =_meta_table['MplsLdp']['meta_info']
_meta_table['MplsLdp.MplsLdpConfig']['meta_info'].parent =_meta_table['MplsLdp']['meta_info']
_meta_table['ClearMsgCountersRpc.Input']['meta_info'].parent =_meta_table['ClearMsgCountersRpc']['meta_info']
_meta_table['ClearMsgCountersRpc.Output']['meta_info'].parent =_meta_table['ClearMsgCountersRpc']['meta_info']
_meta_table['RestartNeighborRpc.Input']['meta_info'].parent =_meta_table['RestartNeighborRpc']['meta_info']
_meta_table['RestartNeighborRpc.Output']['meta_info'].parent =_meta_table['RestartNeighborRpc']['meta_info']
_meta_table['ClearForwardingRpc.Input']['meta_info'].parent =_meta_table['ClearForwardingRpc']['meta_info']
_meta_table['ClearForwardingRpc.Output']['meta_info'].parent =_meta_table['ClearForwardingRpc']['meta_info']
