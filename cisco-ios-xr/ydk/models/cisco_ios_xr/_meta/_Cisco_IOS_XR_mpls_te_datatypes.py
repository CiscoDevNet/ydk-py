


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SrPrependEnum' : _MetaInfoEnum('SrPrependEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none-type':'NONE_TYPE',
            'next-label':'NEXT_LABEL',
            'bgp-n-hop':'BGP_N_HOP',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBandwidthLimitEnum' : _MetaInfoEnum('MplsTeBandwidthLimitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'unlimited':'UNLIMITED',
            'limited':'LIMITED',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBandwidthPoolEnum' : _MetaInfoEnum('MplsTeBandwidthPoolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'any-pool':'ANY_POOL',
            'sub-pool':'SUB_POOL',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeAttrSetEnum' : _MetaInfoEnum('MplsTeAttrSetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'not-used':'NOT_USED',
            'static':'STATIC',
            'lsp':'LSP',
            'unassigned':'UNASSIGNED',
            'auto-backup':'AUTO_BACKUP',
            'auto-mesh':'AUTO_MESH',
            'xro':'XRO',
            'p2mp-te':'P2MP_TE',
            'otn-pp':'OTN_PP',
            'p2p-te':'P2P_TE',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeSwitchingCapEnum' : _MetaInfoEnum('MplsTeSwitchingCapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'psc1':'PSC1',
            'lsc':'LSC',
            'fsc':'FSC',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBfdSessionDownActionEnum' : _MetaInfoEnum('MplsTeBfdSessionDownActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            're-setup':'RE_SETUP',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBackupBandwidthClassEnum' : _MetaInfoEnum('MplsTeBackupBandwidthClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'class0':'CLASS0',
            'class1':'CLASS1',
            'any-class':'ANY_CLASS',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeLogFrrProtectionEnum' : _MetaInfoEnum('MplsTeLogFrrProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'frr-active-primary':'FRR_ACTIVE_PRIMARY',
            'backup':'BACKUP',
            'frr-ready-primary':'FRR_READY_PRIMARY',
            'primary':'PRIMARY',
            'all':'ALL',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeTunnelAffinityEnum' : _MetaInfoEnum('MplsTeTunnelAffinityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'include':'INCLUDE',
            'include-strict':'INCLUDE_STRICT',
            'exclude':'EXCLUDE',
            'exclude-all':'EXCLUDE_ALL',
            'ignore':'IGNORE',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathOptionPropertyEnum' : _MetaInfoEnum('MplsTePathOptionPropertyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none':'NONE',
            'lockdown':'LOCKDOWN',
            'verbatim':'VERBATIM',
            'pce':'PCE',
            'segment-routing':'SEGMENT_ROUTING',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionInvalidationTimerExpireEnum' : _MetaInfoEnum('MplsTePathSelectionInvalidationTimerExpireEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'tunnel-action-tear':'TUNNEL_ACTION_TEAR',
            'tunnel-action-drop':'TUNNEL_ACTION_DROP',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnApsProtectionEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            '1plus1-unidir-no-aps':'Y_1PLUS1_UNIDIR_NO_APS',
            '1plus1-unidir-aps':'Y_1PLUS1_UNIDIR_APS',
            '1plus1-bdir-aps':'Y_1PLUS1_BDIR_APS',
            '1plus1plus-r-bidir-aps':'Y_1PLUS1PLUS_R_BIDIR_APS',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'CtypeEnum' : _MetaInfoEnum('CtypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'ctype-null':'CTYPE_NULL',
            'ctype-ipv4':'CTYPE_IPV4',
            'ctype-ipv4-p2p-tunnel':'CTYPE_IPV4_P2P_TUNNEL',
            'ctype-ipv6-p2p-tunnel':'CTYPE_IPV6_P2P_TUNNEL',
            'ctype-ipv4-uni':'CTYPE_IPV4_UNI',
            'ctype-ipv4-p2mp-tunnel':'CTYPE_IPV4_P2MP_TUNNEL',
            'ctype-ipv6-p2mp-tunnel':'CTYPE_IPV6_P2MP_TUNNEL',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeAffinityValueEnum' : _MetaInfoEnum('MplsTeAffinityValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'hex-value':'HEX_VALUE',
            'bit-position':'BIT_POSITION',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBandwidthDsteEnum' : _MetaInfoEnum('MplsTeBandwidthDsteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'standard-dste':'STANDARD_DSTE',
            'pre-standard-dste':'PRE_STANDARD_DSTE',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum' : _MetaInfoEnum('MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'not-set':'NOT_SET',
            'adj-unprotected':'ADJ_UNPROTECTED',
            'adj-protected':'ADJ_PROTECTED',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeIgpProtocolEnum' : _MetaInfoEnum('MplsTeIgpProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none':'NONE',
            'isis':'ISIS',
            'ospf':'OSPF',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionTiebreakerEnum' : _MetaInfoEnum('MplsTePathSelectionTiebreakerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'min-fill':'MIN_FILL',
            'max-fill':'MAX_FILL',
            'random':'RANDOM',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeSigNameOptionEnum' : _MetaInfoEnum('MplsTeSigNameOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'none':'NONE',
            'address':'ADDRESS',
            'name':'NAME',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'PathInvalidationActionEnum' : _MetaInfoEnum('PathInvalidationActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'tear':'TEAR',
            'drop':'DROP',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeAutorouteMetricEnum' : _MetaInfoEnum('MplsTeAutorouteMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'relative':'RELATIVE',
            'absolute':'ABSOLUTE',
            'constant':'CONSTANT',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTesrlgExcludeEnum' : _MetaInfoEnum('MplsTesrlgExcludeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'mandatory':'MANDATORY',
            'preferred':'PREFERRED',
            'weighted':'WEIGHTED',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeBackupBandwidthPoolEnum' : _MetaInfoEnum('MplsTeBackupBandwidthPoolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'any-pool':'ANY_POOL',
            'global-pool':'GLOBAL_POOL',
            'sub-pool':'SUB_POOL',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathSelectionMetricEnum' : _MetaInfoEnum('MplsTePathSelectionMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'igp':'IGP',
            'te':'TE',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathOptionProtectionEnum' : _MetaInfoEnum('MplsTePathOptionProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'active':'ACTIVE',
            'protecting':'PROTECTING',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathOptionEnum' : _MetaInfoEnum('MplsTePathOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'not-set':'NOT_SET',
            'dynamic':'DYNAMIC',
            'explicit-name':'EXPLICIT_NAME',
            'explicit-number':'EXPLICIT_NUMBER',
            'no-ero':'NO_ERO',
            'sr':'SR',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnSncModeEnum' : _MetaInfoEnum('MplsTeOtnSncModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'snc-n':'SNC_N',
            'snc-i':'SNC_I',
            'snc-s':'SNC_S',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTePathDiversityConformanceEnum' : _MetaInfoEnum('MplsTePathDiversityConformanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'strict':'STRICT',
            'best-effort':'BEST_EFFORT',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
    'MplsTeOtnApsProtectionModeEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_datatypes',
        {
            'revertive':'REVERTIVE',
            'non-revertive':'NON_REVERTIVE',
        }, 'Cisco-IOS-XR-mpls-te-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-datatypes']),
}
