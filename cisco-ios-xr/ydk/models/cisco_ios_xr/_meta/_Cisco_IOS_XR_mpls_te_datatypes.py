


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsTeIgpProtocolEnum' : _MetaInfoEnum('MplsTeIgpProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none':'none',
            'isis':'isis',
            'ospf':'ospf',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBandwidthLimitEnum' : _MetaInfoEnum('MplsTeBandwidthLimitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'unlimited':'unlimited',
            'limited':'limited',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'CtypeEnum' : _MetaInfoEnum('CtypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'ctype-null':'ctype_null',
            'ctype-ipv4':'ctype_ipv4',
            'ctype-ipv4-p2p-tunnel':'ctype_ipv4_p2p_tunnel',
            'ctype-ipv6-p2p-tunnel':'ctype_ipv6_p2p_tunnel',
            'ctype-ipv4-uni':'ctype_ipv4_uni',
            'ctype-ipv4-p2mp-tunnel':'ctype_ipv4_p2mp_tunnel',
            'ctype-ipv6-p2mp-tunnel':'ctype_ipv6_p2mp_tunnel',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBfdSessionDownActionEnum' : _MetaInfoEnum('MplsTeBfdSessionDownActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            're-setup':'re_setup',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnApsProtectionModeEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'revertive':'revertive',
            'non-revertive':'non_revertive',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathOptionProtectionEnum' : _MetaInfoEnum('MplsTePathOptionProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'active':'active',
            'protecting':'protecting',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeLogFrrProtectionEnum' : _MetaInfoEnum('MplsTeLogFrrProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'frr-active-primary':'frr_active_primary',
            'backup':'backup',
            'frr-ready-primary':'frr_ready_primary',
            'primary':'primary',
            'all':'all',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnApsProtectionEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            '1plus1-unidir-no-aps':'Y_1plus1_unidir_no_aps',
            '1plus1-unidir-aps':'Y_1plus1_unidir_aps',
            '1plus1-bdir-aps':'Y_1plus1_bdir_aps',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeTunnelAffinityEnum' : _MetaInfoEnum('MplsTeTunnelAffinityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'include':'include',
            'include-strict':'include_strict',
            'exclude':'exclude',
            'exclude-all':'exclude_all',
            'ignore':'ignore',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathDiversityConformanceEnum' : _MetaInfoEnum('MplsTePathDiversityConformanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'strict':'strict',
            'best-effort':'best_effort',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBandwidthDsteEnum' : _MetaInfoEnum('MplsTeBandwidthDsteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'standard-dste':'standard_dste',
            'pre-standard-dste':'pre_standard_dste',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeAttrSetEnum' : _MetaInfoEnum('MplsTeAttrSetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'not-used':'not_used',
            'static':'static',
            'lsp':'lsp',
            'unassigned':'unassigned',
            'auto-backup':'auto_backup',
            'auto-mesh':'auto_mesh',
            'xro':'xro',
            'p2mp-te':'p2mp_te',
            'otn-pp':'otn_pp',
            'p2p-te':'p2p_te',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionTiebreakerEnum' : _MetaInfoEnum('MplsTePathSelectionTiebreakerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'min-fill':'min_fill',
            'max-fill':'max_fill',
            'random':'random',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'PathInvalidationActionEnum' : _MetaInfoEnum('PathInvalidationActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'tear':'tear',
            'drop':'drop',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTesrlgExcludeEnum' : _MetaInfoEnum('MplsTesrlgExcludeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'mandatory':'mandatory',
            'preferred':'preferred',
            'weighted':'weighted',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnApsRestorationStyleEnum' : _MetaInfoEnum('MplsTeOtnApsRestorationStyleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'keep-failed-lsp':'keep_failed_lsp',
            'delete-failed-lsp':'delete_failed_lsp',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBackupBandwidthClassEnum' : _MetaInfoEnum('MplsTeBackupBandwidthClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'class0':'class0',
            'class1':'class1',
            'any-class':'any_class',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum' : _MetaInfoEnum('MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'not-set':'not_set',
            'adj-unprotected':'adj_unprotected',
            'adj-protected':'adj_protected',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBackupBandwidthPoolEnum' : _MetaInfoEnum('MplsTeBackupBandwidthPoolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'any-pool':'any_pool',
            'global-pool':'global_pool',
            'sub-pool':'sub_pool',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeAffinityValueEnum' : _MetaInfoEnum('MplsTeAffinityValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'hex-value':'hex_value',
            'bit-position':'bit_position',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathOptionPropertyEnum' : _MetaInfoEnum('MplsTePathOptionPropertyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none':'none',
            'lockdown':'lockdown',
            'verbatim':'verbatim',
            'pce':'pce',
            'segment-routing':'segment_routing',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeSwitchingCapEnum' : _MetaInfoEnum('MplsTeSwitchingCapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'psc1':'psc1',
            'lsc':'lsc',
            'fsc':'fsc',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'BfdReversePathEnum' : _MetaInfoEnum('BfdReversePathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'bfd-reverse-path-binding-label':'bfd_reverse_path_binding_label',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeAutorouteMetricEnum' : _MetaInfoEnum('MplsTeAutorouteMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'relative':'relative',
            'absolute':'absolute',
            'constant':'constant',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathOptionEnum' : _MetaInfoEnum('MplsTePathOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'not-set':'not_set',
            'dynamic':'dynamic',
            'explicit-name':'explicit_name',
            'explicit-number':'explicit_number',
            'no-ero':'no_ero',
            'sr':'sr',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionMetricEnum' : _MetaInfoEnum('MplsTePathSelectionMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'igp':'igp',
            'te':'te',
            'delay':'delay',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnSncModeEnum' : _MetaInfoEnum('MplsTeOtnSncModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'snc-n':'snc_n',
            'snc-i':'snc_i',
            'snc-s':'snc_s',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBandwidthPoolEnum' : _MetaInfoEnum('MplsTeBandwidthPoolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'any-pool':'any_pool',
            'sub-pool':'sub_pool',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'SrPrependEnum' : _MetaInfoEnum('SrPrependEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none-type':'none_type',
            'next-label':'next_label',
            'bgp-n-hop':'bgp_n_hop',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeSigNameOptionEnum' : _MetaInfoEnum('MplsTeSigNameOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none':'none',
            'address':'address',
            'name':'name',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionInvalidationTimerExpireEnum' : _MetaInfoEnum('MplsTePathSelectionInvalidationTimerExpireEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'tunnel-action-tear':'tunnel_action_tear',
            'tunnel-action-drop':'tunnel_action_drop',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
}
