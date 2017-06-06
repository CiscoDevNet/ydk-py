


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsTeIgpProtocolEnum' : _MetaInfoEnum('MplsTeIgpProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'none',
            'isis':'isis',
            'ospf':'ospf',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSignaledLabelEnum' : _MetaInfoEnum('MplsTeSignaledLabelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'not_set',
            'dwdm':'dwdm',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBandwidthLimitEnum' : _MetaInfoEnum('MplsTeBandwidthLimitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'unlimited':'unlimited',
            'limited':'limited',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnSignaledBandwidthEnum' : _MetaInfoEnum('OtnSignaledBandwidthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'odu1':'odu1',
            'odu2':'odu2',
            'odu3':'odu3',
            'odu4':'odu4',
            'odu0':'odu0',
            'odu2e':'odu2e',
            'od-uflex-cbr':'od_uflex_cbr',
            'od-uflex-gfp-resize':'od_uflex_gfp_resize',
            'od-uflex-gfp-not-resize':'od_uflex_gfp_not_resize',
            'odu1e':'odu1e',
            'odu1f':'odu1f',
            'odu2f':'odu2f',
            'odu3e1':'odu3e1',
            'odu3e2':'odu3e2',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBfdSessionDownActionEnum' : _MetaInfoEnum('MplsTeBfdSessionDownActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            're-setup':'re_setup',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnDestinationEnum' : _MetaInfoEnum('OtnDestinationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'number-ed':'number_ed',
            'un-number-ed':'un_number_ed',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'GmplsttiModeEnum' : _MetaInfoEnum('GmplsttiModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'sm':'sm',
            'pm':'pm',
            'tcm':'tcm',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingEncodeEnum' : _MetaInfoEnum('MplsTeSwitchingEncodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'none',
            'packet':'packet',
            'ethernet':'ethernet',
            'sondet-sdh':'sondet_sdh',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'LinkNextHopEnum' : _MetaInfoEnum('LinkNextHopEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'none',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathDiversityConformanceEnum' : _MetaInfoEnum('MplsTePathDiversityConformanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'strict':'strict',
            'best-effort':'best_effort',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathOptionProtectionEnum' : _MetaInfoEnum('MplsTePathOptionProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'active':'active',
            'protecting':'protecting',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum' : _MetaInfoEnum('MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'not_set',
            'adj-unprotected':'adj_unprotected',
            'adj-protected':'adj_protected',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'PathInvalidationActionEnum' : _MetaInfoEnum('PathInvalidationActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'tear':'tear',
            'drop':'drop',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsLcacFloodingIgpEnum' : _MetaInfoEnum('MplsLcacFloodingIgpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'ospf':'ospf',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnApsRestorationStyleEnum' : _MetaInfoEnum('MplsTeOtnApsRestorationStyleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'keep-failed-lsp':'keep_failed_lsp',
            'delete-failed-lsp':'delete_failed_lsp',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeTunnelIdEnum' : _MetaInfoEnum('MplsTeTunnelIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'auto':'auto',
            'explicit':'explicit',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeConfigTunnelEnum' : _MetaInfoEnum('MplsTeConfigTunnelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'p2p':'p2p',
            'p2mp':'p2mp',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnApsProtectionModeEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'revertive':'revertive',
            'non-revertive':'non_revertive',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTebfdSessionEnum' : _MetaInfoEnum('MplsTebfdSessionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'regular-bfd':'regular_bfd',
            'sbfd':'sbfd',
            'redundant-sbfd':'redundant_sbfd',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingCapEnum' : _MetaInfoEnum('MplsTeSwitchingCapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'psc1':'psc1',
            'lsc':'lsc',
            'fsc':'fsc',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'BfdReversePathEnum' : _MetaInfoEnum('BfdReversePathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'bfd-reverse-path-binding-label':'bfd_reverse_path_binding_label',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingIndexEnum' : _MetaInfoEnum('MplsTeSwitchingIndexEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'link':'link',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnPayloadEnum' : _MetaInfoEnum('OtnPayloadEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'unknown':'unknown',
            'bmp':'bmp',
            'gfp-f':'gfp_f',
            'gmp':'gmp',
            'gfp-f-ext':'gfp_f_ext',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeAutorouteMetricEnum' : _MetaInfoEnum('MplsTeAutorouteMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'relative':'relative',
            'absolute':'absolute',
            'constant':'constant',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnSignaledBandwidthFlexFramingEnum' : _MetaInfoEnum('OtnSignaledBandwidthFlexFramingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'cbr':'cbr',
            'framed-gfp-fixed':'framed_gfp_fixed',
            'framed-gfp-resize':'framed_gfp_resize',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnSncModeEnum' : _MetaInfoEnum('MplsTeOtnSncModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'snc-n':'snc_n',
            'snc-i':'snc_i',
            'snc-s':'snc_s',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathOptionEnum' : _MetaInfoEnum('MplsTePathOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'not_set',
            'dynamic':'dynamic',
            'explicit-name':'explicit_name',
            'explicit-number':'explicit_number',
            'no-ero':'no_ero',
            'sr':'sr',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'BandwidthConstraintEnum' : _MetaInfoEnum('BandwidthConstraintEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'bandwidth-constraint-maximum-allocation-model':'bandwidth_constraint_maximum_allocation_model',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionInvalidationTimerExpireEnum' : _MetaInfoEnum('MplsTePathSelectionInvalidationTimerExpireEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'tunnel-action-tear':'tunnel_action_tear',
            'tunnel-action-drop':'tunnel_action_drop',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTesrlgExcludeEnum' : _MetaInfoEnum('MplsTesrlgExcludeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'mandatory':'mandatory',
            'preferred':'preferred',
            'weighted':'weighted',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'BindingSegmentIdEnum' : _MetaInfoEnum('BindingSegmentIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'any-label':'any_label',
            'specified-label':'specified_label',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnProtectionSwitchLockoutEnum' : _MetaInfoEnum('OtnProtectionSwitchLockoutEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'none',
            'working':'working',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingEncodingEnum' : _MetaInfoEnum('MplsTeSwitchingEncodingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'packet':'packet',
            'ethernet':'ethernet',
            'sondet-sdh':'sondet_sdh',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OspfAreaModeEnum' : _MetaInfoEnum('OspfAreaModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'ospf-int':'ospf_int',
            'ospfip-addr':'ospfip_addr',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBackupBandwidthClassEnum' : _MetaInfoEnum('MplsTeBackupBandwidthClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'class0':'class0',
            'class1':'class1',
            'any-class':'any_class',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeLogFrrProtectionEnum' : _MetaInfoEnum('MplsTeLogFrrProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'frr-active-primary':'frr_active_primary',
            'backup':'backup',
            'frr-ready-primary':'frr_ready_primary',
            'primary':'primary',
            'all':'all',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeTunnelAffinityEnum' : _MetaInfoEnum('MplsTeTunnelAffinityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'include':'include',
            'include-strict':'include_strict',
            'exclude':'exclude',
            'exclude-all':'exclude_all',
            'ignore':'ignore',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'RoutePriorityRoleEnum' : _MetaInfoEnum('RoutePriorityRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'route-priority-role-head-back-up':'route_priority_role_head_back_up',
            'route-priority-role-head-primary':'route_priority_role_head_primary',
            'route-priority-role-middle':'route_priority_role_middle',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBandwidthDsteEnum' : _MetaInfoEnum('MplsTeBandwidthDsteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'standard-dste':'standard_dste',
            'pre-standard-dste':'pre_standard_dste',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'SrPrependEnum' : _MetaInfoEnum('SrPrependEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none-type':'none_type',
            'next-label':'next_label',
            'bgp-n-hop':'bgp_n_hop',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnStaticUniEnum' : _MetaInfoEnum('OtnStaticUniEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'unknown':'unknown',
            'xc':'xc',
            'termination':'termination',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'IetfModeEnum' : _MetaInfoEnum('IetfModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'standard':'standard',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBackupBandwidthPoolEnum' : _MetaInfoEnum('MplsTeBackupBandwidthPoolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'any-pool':'any_pool',
            'global-pool':'global_pool',
            'sub-pool':'sub_pool',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeAffinityValueEnum' : _MetaInfoEnum('MplsTeAffinityValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'hex-value':'hex_value',
            'bit-position':'bit_position',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathOptionPropertyEnum' : _MetaInfoEnum('MplsTePathOptionPropertyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'none',
            'lockdown':'lockdown',
            'verbatim':'verbatim',
            'pce':'pce',
            'segment-routing':'segment_routing',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathComputationMethodEnum' : _MetaInfoEnum('MplsTePathComputationMethodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'not_set',
            'dynamic':'dynamic',
            'pce':'pce',
            'explicit':'explicit',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSigNameOptionEnum' : _MetaInfoEnum('MplsTeSigNameOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'none',
            'address':'address',
            'name':'name',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionMetricEnum' : _MetaInfoEnum('MplsTePathSelectionMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'igp':'igp',
            'te':'te',
            'delay':'delay',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnApsProtectionEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            '1plus1-unidir-no-aps':'Y_1plus1_unidir_no_aps',
            '1plus1-unidir-aps':'Y_1plus1_unidir_aps',
            '1plus1-bdir-aps':'Y_1plus1_bdir_aps',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionTiebreakerEnum' : _MetaInfoEnum('MplsTePathSelectionTiebreakerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg',
        {
            'min-fill':'min_fill',
            'max-fill':'max_fill',
            'random':'random',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTe.DiffServTrafficEngineering.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('MplsTe.DiffServTrafficEngineering.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                DS-TE class number
                ''',
                'class_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('class-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Class-type priority
                ''',
                'class_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Class type number
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('unused', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to skip classtype and class priority
                provisioning FALSE to provision them
                ''',
                'unused',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.DiffServTrafficEngineering.Classes' : {
        'meta_info' : _MetaInfoClass('MplsTe.DiffServTrafficEngineering.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.DiffServTrafficEngineering.Classes.Class_', 
                [], [], 
                '''                DSTE class number
                ''',
                'class_',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.DiffServTrafficEngineering' : {
        'meta_info' : _MetaInfoClass('MplsTe.DiffServTrafficEngineering',
            False, 
            [
            _MetaInfoClassMember('bandwidth-constraint-model', REFERENCE_ENUM_CLASS, 'BandwidthConstraintEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'BandwidthConstraintEnum', 
                [], [], 
                '''                Diff-Serv Traffic-Engineering Bandwidth
                Constraint Model
                ''',
                'bandwidth_constraint_model',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.DiffServTrafficEngineering.Classes', 
                [], [], 
                '''                Configure Diff-Serv Traffic-Engineering Classes
                ''',
                'classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mode-ietf', REFERENCE_ENUM_CLASS, 'IetfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'IetfModeEnum', 
                [], [], 
                '''                Diff-Serv Traffic-Engineering IETF mode
                ''',
                'mode_ietf',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'diff-serv-traffic-engineering',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation',
            False, 
            [
            _MetaInfoClassMember('explicit-path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Explicit Path Name
                ''',
                'explicit_path_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-computation-method', REFERENCE_ENUM_CLASS, 'MplsTePathComputationMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathComputationMethodEnum', 
                [], [], 
                '''                Path computation method
                ''',
                'path_computation_method',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Path Computation Server Address
                ''',
                'path_computation_server',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-computation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup',
            False, 
            [
            _MetaInfoClassMember('path-setup-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Path Name
                ''',
                'path_setup_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-computation', REFERENCE_CLASS, 'PathComputation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation', 
                [], [], 
                '''                Path computation method
                ''',
                'path_computation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path preference level
                ''',
                'preference',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-setup',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups',
            False, 
            [
            _MetaInfoClassMember('path-setup', REFERENCE_LIST, 'PathSetup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup', 
                [], [], 
                '''                Tunnel path setup
                ''',
                'path_setup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-setups',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation',
            False, 
            [
            _MetaInfoClassMember('path-invalidation-action', REFERENCE_ENUM_CLASS, 'PathInvalidationActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'PathInvalidationActionEnum', 
                [], [], 
                '''                Path Invalidation Action
                ''',
                'path_invalidation_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '60000')], [], 
                '''                Path Invalidation Timeout
                ''',
                'path_invalidation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection',
            False, 
            [
            _MetaInfoClassMember('invalidation', REFERENCE_CLASS, 'Invalidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation', 
                [], [], 
                '''                Path invalidation configuration for this
                specific tunnel
                ''',
                'invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-cost-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Path selection cost limit configuration for this
                specific tunnel
                ''',
                'path_selection_cost_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Path selection hop limit configuration for this
                specific tunnel
                ''',
                'path_selection_hop_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionTiebreakerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionTiebreakerEnum', 
                [], [], 
                '''                CSPF tiebreaker to use in path calculation
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow',
            False, 
            [
            _MetaInfoClassMember('underflow-threshold-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Number of consecutive collections exceeding
                threshold
                ''',
                'underflow_threshold_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Bandwidth change percent to trigger an
                underflow
                ''',
                'underflow_threshold_percent',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [('10', '4294967295')], [], 
                '''                Bandwidth change value to trigger an underflow
                (kbps)
                ''',
                'underflow_threshold_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'underflow',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow',
            False, 
            [
            _MetaInfoClassMember('overflow-threshold-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Number of consecutive collections exceeding
                threshold
                ''',
                'overflow_threshold_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Bandwidth change percent to trigger an
                overflow
                ''',
                'overflow_threshold_percent',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [('10', '4294967295')], [], 
                '''                Bandwidth change value to trigger an overflow
                (kbps)
                ''',
                'overflow_threshold_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'overflow',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits',
            False, 
            [
            _MetaInfoClassMember('bandwidth-max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set maximum bandwidth auto-bw can apply on a
                tunnel
                ''',
                'bandwidth_max_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-min-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set minimum bandwidth auto-bw can apply on a
                tunnel
                ''',
                'bandwidth_min_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth-limits',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold',
            False, 
            [
            _MetaInfoClassMember('adjustment-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Bandwidth change percent to trigger adjustment
                ''',
                'adjustment_threshold_percent',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('adjustment-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [('10', '4294967295')], [], 
                '''                Bandwidth change value to trigger adjustment
                (kbps)
                ''',
                'adjustment_threshold_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'adjustment-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth',
            False, 
            [
            _MetaInfoClassMember('adjustment-threshold', REFERENCE_CLASS, 'AdjustmentThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold', 
                [], [], 
                '''                Set the bandwidth change threshold to trigger
                adjustment
                ''',
                'adjustment_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('application-frequency', ATTRIBUTE, 'int' , None, None, 
                [('5', '10080')], [], 
                '''                Set the tunnel auto-bw application frequency in
                minutes
                ''',
                'application_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-limits', REFERENCE_CLASS, 'BandwidthLimits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits', 
                [], [], 
                '''                Set min/max bandwidth auto-bw can apply on a
                tunnel
                ''',
                'bandwidth_limits',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('collection-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable bandwidth collection only, no auto-bw
                adjustment
                ''',
                'collection_only',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is only valid for tunnel interfaces
                and it controls whether that interface has
                auto-bw enabled on it or not.The object must be
                set before any other auto-bw configuration is
                supplied for the interface, and must be the
                last auto-bw configuration object to be removed
                .
                ''',
                'enabled',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow', REFERENCE_CLASS, 'Overflow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow', 
                [], [], 
                '''                Configuring the tunnel overflow detection
                ''',
                'overflow',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable auto bandwidth overflow detection
                ''',
                'overflow_enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow', REFERENCE_CLASS, 'Underflow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow', 
                [], [], 
                '''                Configuring the tunnel underflow detection
                ''',
                'underflow',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable auto bandwidth underflow detection
                ''',
                'underflow_enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all events for a tunnel
                ''',
                'all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BFD session state change alarm
                ''',
                'bfd_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-switch-over-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'lsp_switch_over_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel record-route messages
                ''',
                'record_route_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel rereoute messages
                ''',
                'reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Class type for the bandwidth allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Metric' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Metric',
            False, 
            [
            _MetaInfoClassMember('absolute-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The absolute metric value
                ''',
                'absolute_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('constant-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The constant metric value
                ''',
                'constant_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'MplsTeAutorouteMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeAutorouteMetricEnum', 
                [], [], 
                '''                Autoroute tunnel metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('relative-metric', ATTRIBUTE, 'int' , None, None, 
                [('-10', '10')], [], 
                '''                The value of the adjustment
                ''',
                'relative_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic',
            False, 
            [
            _MetaInfoClassMember('segment-routing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Exclude tunnel in IGP for SR prefixes
                ''',
                'segment_routing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'exclude-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric',
            False, 
            [
            _MetaInfoClassMember('absolute-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The absolute metric value
                ''',
                'absolute_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('constant-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The constant metric value
                ''',
                'constant_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'MplsTeAutorouteMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeAutorouteMetricEnum', 
                [], [], 
                '''                Autoroute tunnel metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('relative-metric', ATTRIBUTE, 'int' , None, None, 
                [('-10', '10')], [], 
                '''                The value of the adjustment
                ''',
                'relative_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable autoroute announce
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('exclude-traffic', REFERENCE_CLASS, 'ExcludeTraffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic', 
                [], [], 
                '''                Exclude traffic on autorouted tunnel
                ''',
                'exclude_traffic',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('include-ipv6', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that the tunnel should be an IPv6
                autoroute announce also
                ''',
                'include_ipv6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric', REFERENCE_CLASS, 'Metric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric', 
                [], [], 
                '''                Specify MPLS tunnel metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'autoroute-announce',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr.Destination' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr.Destination',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of destination
                ''',
                'destination_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr.Destination', 
                [], [], 
                '''                Destination address to add in RIB
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute',
            False, 
            [
            _MetaInfoClassMember('autoroute-announce', REFERENCE_CLASS, 'AutorouteAnnounce' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce', 
                [], [], 
                '''                Announce tunnel to IGP
                ''',
                'autoroute_announce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Deprecated: do NOT use
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-xr', REFERENCE_CLASS, 'DestinationXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr', 
                [], [], 
                '''                Tunnel Autoroute Destination(s)
                ''',
                'destination_xr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric', REFERENCE_CLASS, 'Metric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Metric', 
                [], [], 
                '''                Specify MPLS tunnel metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'autoroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity-affinity-type', REFERENCE_LIST, 'NewStyleAffinityAffinityType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-types',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute',
            False, 
            [
            _MetaInfoClassMember('bandwidth-protection', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Bandwidth Protection
                ''',
                'bandwidth_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-protection', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Node Protection
                ''',
                'node_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-bandwidth', REFERENCE_CLASS, 'AutoBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth', 
                [], [], 
                '''                Tunnel Interface Auto-bandwidth configuration
                data
                ''',
                'auto_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('autoroute', REFERENCE_CLASS, 'Autoroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute', 
                [], [], 
                '''                Parameters for IGP routing over tunnel
                ''',
                'autoroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Set the destination of the tunnel
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute', 
                [], [], 
                '''                Specify MPLS tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('1', '7')], [], 
                '''                Forward class value
                ''',
                'forward_class',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('load-share', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tunnel loadsharing metric
                ''',
                'load_share',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-types', REFERENCE_CLASS, 'NewStyleAffinityAffinityTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinity_affinity_types',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Path selection metric to use in path calculation
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-setups', REFERENCE_CLASS, 'PathSetups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups', 
                [], [], 
                '''                Tunnel path setup table
                ''',
                'path_setups',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                shutdown the tunnel
                ''',
                'shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soft-preemption', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the soft-preemption feature on the tunnel
                ''',
                'soft_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-path-selection', REFERENCE_CLASS, 'TunnelPathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'tunnel_path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId',
            False, 
            [
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelIdEnum', 
                [], [], 
                '''                Tunnel ID Type
                ''',
                'tunnel_id_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels.Tunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels.Tunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 59)], [], 
                '''                Tunnel name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('tunnel-type', REFERENCE_ENUM_CLASS, 'MplsTeConfigTunnelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeConfigTunnelEnum', 
                [], [], 
                '''                Tunnel Type
                ''',
                'tunnel_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-attributes', REFERENCE_CLASS, 'TunnelAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes', 
                [], [], 
                '''                MPLS tunnel attributes
                ''',
                'tunnel_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', REFERENCE_CLASS, 'TunnelId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId', 
                [], [], 
                '''                Set the tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels.Tunnels' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels.Tunnels',
            False, 
            [
            _MetaInfoClassMember('tunnel', REFERENCE_LIST, 'Tunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels.Tunnel', 
                [], [], 
                '''                Configure a MPLS TE tunnel
                ''',
                'tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.NamedTunnels' : {
        'meta_info' : _MetaInfoClass('MplsTe.NamedTunnels',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Named Tunnels
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnels', REFERENCE_CLASS, 'Tunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels.Tunnels', 
                [], [], 
                '''                Configure MPLS TE tunnel
                ''',
                'tunnels',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'named-tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('5', '3600')], [], 
                '''                Maximum holddown (seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('5', '3600')], [], 
                '''                Minimum holddown (seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'holddown',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Timers.PathOptionTimers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Timers.PathOptionTimers',
            False, 
            [
            _MetaInfoClassMember('holddown', REFERENCE_CLASS, 'Holddown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown', 
                [], [], 
                '''                GMPLS-UNI path-option holddown timer
                configuration
                ''',
                'holddown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Timers',
            False, 
            [
            _MetaInfoClassMember('path-option-timers', REFERENCE_CLASS, 'PathOptionTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Timers.PathOptionTimers', 
                [], [], 
                '''                GMPLS-UNI path-option timer configuration
                ''',
                'path_option_timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.Announce' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.Announce',
            False, 
            [
            _MetaInfoClassMember('srl-gs', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable announcement of discovered SRLGs
                ''',
                'srl_gs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'announce',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.ControllerLogging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.ControllerLogging',
            False, 
            [
            _MetaInfoClassMember('discovered-srlg-change-logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of changes to of discovered
                SRLGs
                ''',
                'discovered_srlg_change_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption',
            False, 
            [
            _MetaInfoClassMember('preference-level', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Preference level for this path option
                ''',
                'preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('dwdm-channel', ATTRIBUTE, 'int' , None, None, 
                [('1', '89')], [], 
                '''                DWDM channel number
                ''',
                'dwdm_channel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lockdown', REFERENCE_ENUM_CLASS, 'MplsTePathOptionPropertyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionPropertyEnum', 
                [], [], 
                '''                Path option properties: must be Lockdown
                ''',
                'lockdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The ID of the explicit path associated
                with this option
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the explicit path associated
                with this option
                ''',
                'path_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsTePathOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionEnum', 
                [], [], 
                '''                The type of the path option
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signaled-label', REFERENCE_ENUM_CLASS, 'MplsTeSignaledLabelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSignaledLabelEnum', 
                [], [], 
                '''                Signaled label type
                ''',
                'signaled_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('verbatim', REFERENCE_ENUM_CLASS, 'MplsTePathOptionPropertyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionPropertyEnum', 
                [], [], 
                '''                Path option properties: must be verbatim
                if set
                ''',
                'verbatim',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The name of the XRO attribute set to be
                used for this path-option
                ''',
                'xro_attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-type', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The route-exclusion type
                ''',
                'xro_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions',
            False, 
            [
            _MetaInfoClassMember('path-option', REFERENCE_LIST, 'PathOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption', 
                [], [], 
                '''                A Path-option
                ''',
                'path_option',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-options',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording',
            False, 
            [
            _MetaInfoClassMember('srlg', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG-recording during signaling
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'recording',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging',
            False, 
            [
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Set the destination of the tunnel
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set link as a GMPLS tunnel head
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging', 
                [], [], 
                '''                Tunnel event logging
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-options', REFERENCE_CLASS, 'PathOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions', 
                [], [], 
                '''                Path-option configuration
                ''',
                'path_options',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('recording', REFERENCE_CLASS, 'Recording' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording', 
                [], [], 
                '''                Tunnel property recording
                ''',
                'recording',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 254)], [], 
                '''                The name of the tunnel to be included in
                signalling messages
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                GMPLS-UNI head tunnel-id
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'gmpls-unitunnel-head',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('announce', REFERENCE_CLASS, 'Announce' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.Announce', 
                [], [], 
                '''                Announce discovered tunnel properties to
                system
                ''',
                'announce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('controller-logging', REFERENCE_CLASS, 'ControllerLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.ControllerLogging', 
                [], [], 
                '''                Controller logging
                ''',
                'controller_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GMPLS-UNI on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('gmpls-unitunnel-head', REFERENCE_CLASS, 'GmplsUnitunnelHead' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead', 
                [], [], 
                '''                GMPLS-UNI tunnel-head properties
                ''',
                'gmpls_unitunnel_head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller', 
                [], [], 
                '''                Configure a GMPLS controller
                ''',
                'controller',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni',
            False, 
            [
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers', 
                [], [], 
                '''                GMPLS-UNI controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Timers', 
                [], [], 
                '''                GMPLS-UNI timer configuration
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'gmpls-uni',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Pcc' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Pcc',
            False, 
            [
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange', 
                [], [], 
                '''                Configure tunnel ID range for auto-tunnel
                features
                ''',
                'tunnel_range',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pcc',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange', 
                [], [], 
                '''                Configure tunnel ID range for auto-tunnel
                features
                ''',
                'tunnel_range',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2p-auto-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal',
            False, 
            [
            _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                [('0', '10080')], [], 
                '''                Auto-tunnel backup unused timeout in minutes
                (0=never timeout)
                ''',
                'unused',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'removal',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers',
            False, 
            [
            _MetaInfoClassMember('removal', REFERENCE_CLASS, 'Removal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal', 
                [], [], 
                '''                Configure auto-tunnel backup removal timers
                value
                ''',
                'removal',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup',
            False, 
            [
            _MetaInfoClassMember('affinity-ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore affinity during CSPF for auto backup
                tunnels
                ''',
                'affinity_ignore',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers', 
                [], [], 
                '''                Configure auto-tunnel backup timers value
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange', 
                [], [], 
                '''                Configure tunnel ID range for auto-tunnel
                features
                ''',
                'tunnel_range',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup',
            False, 
            [
            _MetaInfoClassMember('mesh-group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mesh group ID
                ''',
                'mesh_group_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('attribute-set', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The name of auto-mesh attribute set to be
                applied to this group
                ''',
                'attribute_set',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Auto-mesh group enable object that controls
                whether this group is configured or not
                .This object must be set before other
                configuration supplied for this group
                ''',
                'create',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The name of prefix-list to be applied to
                this destination-list
                ''',
                'destination_list',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disables mesh group
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('one-hop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Automatically create tunnel to all
                next-hops
                ''',
                'one_hop',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mesh-group',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups',
            False, 
            [
            _MetaInfoClassMember('mesh-group', REFERENCE_LIST, 'MeshGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup', 
                [], [], 
                '''                Auto-mesh group identifier
                ''',
                'mesh_group',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mesh-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal',
            False, 
            [
            _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                [('0', '10080')], [], 
                '''                Auto-tunnel backup unused timeout in minutes
                (0=never timeout)
                ''',
                'unused',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'removal',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers',
            False, 
            [
            _MetaInfoClassMember('removal', REFERENCE_CLASS, 'Removal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal', 
                [], [], 
                '''                Configure auto-tunnel backup removal timers
                value
                ''',
                'removal',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh',
            False, 
            [
            _MetaInfoClassMember('mesh-groups', REFERENCE_CLASS, 'MeshGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups', 
                [], [], 
                '''                Configure auto-tunnel mesh group
                ''',
                'mesh_groups',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers', 
                [], [], 
                '''                Configure auto-tunnel backup timers value
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange', 
                [], [], 
                '''                Configure tunnel ID range for auto-tunnel
                features
                ''',
                'tunnel_range',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mesh',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange', 
                [], [], 
                '''                Configure tunnel ID range for auto-tunnel
                features
                ''',
                'tunnel_range',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2mp-auto-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel',
            False, 
            [
            _MetaInfoClassMember('backup', REFERENCE_CLASS, 'Backup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup', 
                [], [], 
                '''                Configure auto-tunnel backup feature
                ''',
                'backup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mesh', REFERENCE_CLASS, 'Mesh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh', 
                [], [], 
                '''                Configure auto-tunnel mesh feature
                ''',
                'mesh',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2mp-auto-tunnel', REFERENCE_CLASS, 'P2MpAutoTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel', 
                [], [], 
                '''                Configure P2MP auto-tunnel feature
                ''',
                'p2mp_auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2p-auto-tunnel', REFERENCE_CLASS, 'P2PAutoTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel', 
                [], [], 
                '''                Configure P2P auto-tunnel feature
                ''',
                'p2p_auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcc', REFERENCE_CLASS, 'Pcc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Pcc', 
                [], [], 
                '''                Configure auto-tunnel PCC (Path Computation
                Client) feature
                ''',
                'pcc',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState',
            False, 
            [
            _MetaInfoClassMember('oor-accept-lsp-min-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Only accept LSPs with at least the specified
                bandwidth (in kbps).
                ''',
                'oor_accept_lsp_min_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-accept-reopt-lsp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow the setup of reoptimized LSPs over the
                link in this OOR State
                ''',
                'oor_accept_reopt_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-available-bandwidth-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Flood a specific percentage of the available
                bandwidth
                ''',
                'oor_available_bandwidth_percentage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-metric-te-penalty', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Penalty applied to the TE metric of a link in
                OOR state
                ''',
                'oor_metric_te_penalty',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-node-protection-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable FRR node-protection when the link is in
                this OOR State
                ''',
                'oor_node_protection_disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'oor-red-state',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState',
            False, 
            [
            _MetaInfoClassMember('oor-accept-lsp-min-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Only accept LSPs with at least the specified
                bandwidth (in kbps).
                ''',
                'oor_accept_lsp_min_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-accept-reopt-lsp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow the setup of reoptimized LSPs over the
                link in this OOR State
                ''',
                'oor_accept_reopt_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-available-bandwidth-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Flood a specific percentage of the available
                bandwidth
                ''',
                'oor_available_bandwidth_percentage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-metric-te-penalty', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Penalty applied to the TE metric of a link in
                OOR state
                ''',
                'oor_metric_te_penalty',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-node-protection-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable FRR node-protection when the link is in
                this OOR State
                ''',
                'oor_node_protection_disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'oor-yellow-state',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState',
            False, 
            [
            _MetaInfoClassMember('oor-accept-lsp-min-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Only accept LSPs with at least the specified
                bandwidth (in kbps).
                ''',
                'oor_accept_lsp_min_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-accept-reopt-lsp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow the setup of reoptimized LSPs over the
                link in this OOR State
                ''',
                'oor_accept_reopt_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-available-bandwidth-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Flood a specific percentage of the available
                bandwidth
                ''',
                'oor_available_bandwidth_percentage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-metric-te-penalty', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Penalty applied to the TE metric of a link in
                OOR state
                ''',
                'oor_metric_te_penalty',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-node-protection-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable FRR node-protection when the link is in
                this OOR State
                ''',
                'oor_node_protection_disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-recovery-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '10080')], [], 
                '''                Period of time (minutes) during which the
                action in Green state are applied. After this
                period, the processing in TE goes back to
                normal state
                ''',
                'oor_recovery_duration',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'oor-green-state',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.HardwareOutOfResource' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.HardwareOutOfResource',
            False, 
            [
            _MetaInfoClassMember('oor-green-state', REFERENCE_CLASS, 'OorGreenState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState', 
                [], [], 
                '''                Configuration for HW OOR Green State
                ''',
                'oor_green_state',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-red-state', REFERENCE_CLASS, 'OorRedState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState', 
                [], [], 
                '''                Configuration for HW OOR Red State
                ''',
                'oor_red_state',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oor-yellow-state', REFERENCE_CLASS, 'OorYellowState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState', 
                [], [], 
                '''                Configuration for HW OOR Yellow State
                ''',
                'oor_yellow_state',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'hardware-out-of-resource',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId',
            False, 
            [
            _MetaInfoClassMember('secondary-router-id-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary TE Router ID
                ''',
                'secondary_router_id_value',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'secondary-router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.SecondaryRouterIds' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.SecondaryRouterIds',
            False, 
            [
            _MetaInfoClassMember('secondary-router-id', REFERENCE_LIST, 'SecondaryRouterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId', 
                [], [], 
                '''                Secondary Router ID
                ''',
                'secondary_router_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'secondary-router-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember',
            False, 
            [
            _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                From address
                ''',
                'from_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('to-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                To Addres
                ''',
                'to_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'static-srlg-member',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers',
            False, 
            [
            _MetaInfoClassMember('static-srlg-member', REFERENCE_LIST, 'StaticSrlgMember' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember', 
                [], [], 
                '''                A mapping of the local static SRLG member
                ''',
                'static_srlg_member',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'static-srlg-members',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Names.Name' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Names.Name',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG membership name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Administrative weight for the SRLG value
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('static-srlg-members', REFERENCE_CLASS, 'StaticSrlgMembers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers', 
                [], [], 
                '''                Configure static SRLG members list
                ''',
                'static_srlg_members',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Names' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Names',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Names.Name', 
                [], [], 
                '''                SRLG name and its MPLS-TE properties
                ''',
                'name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'names',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap',
            False, 
            [
            _MetaInfoClassMember('outgoing-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Outgoing v4 address
                ''',
                'outgoing_ipv4_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('remote-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote v4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ipv4-address-map',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-map', REFERENCE_LIST, 'Ipv4AddressMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap', 
                [], [], 
                '''                A mapping of the remote and local addresses
                of a link to an SRLG value
                ''',
                'ipv4_address_map',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ipv4-address-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values.Value' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values.Value',
            False, 
            [
            _MetaInfoClassMember('srlg-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG membership number
                ''',
                'srlg_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Administrative weight for the SRLG value
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ipv4-address-maps', REFERENCE_CLASS, 'Ipv4AddressMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps', 
                [], [], 
                '''                Configure outgoing and remote link addresses
                for a given SRLG value
                ''',
                'ipv4_address_maps',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'value',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values',
            False, 
            [
            _MetaInfoClassMember('value', REFERENCE_LIST, 'Value' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values.Value', 
                [], [], 
                '''                SRLG value and its MPLS-TE properties
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'values',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg',
            False, 
            [
            _MetaInfoClassMember('default-admin-weight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Default Admin weight any SRLG value that does
                not have one
                ''',
                'default_admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter SRLG property configuration
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('names', REFERENCE_CLASS, 'Names' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Names', 
                [], [], 
                '''                Configure SRLG identified by names
                ''',
                'names',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('values', REFERENCE_CLASS, 'Values' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values', 
                [], [], 
                '''                Configure SRLG values and MPLS-TE properties
                ''',
                'values',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Queues.Queue' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Queues.Queue',
            False, 
            [
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'RoutePriorityRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'RoutePriorityRoleEnum', 
                [], [], 
                '''                Route Priority Tunnel Role
                ''',
                'role',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '12')], [], 
                '''                Route priority queue value
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Queues' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Queues',
            False, 
            [
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Queues.Queue', 
                [], [], 
                '''                Configure route priority queue value
                ''',
                'queue',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'queues',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Mib' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Mib',
            False, 
            [
            _MetaInfoClassMember('midpoint-lsp-stats-collection-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disables mib midpoint LSP traffic stats
                collection
                ''',
                'midpoint_lsp_stats_collection_disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath',
            False, 
            [
            _MetaInfoClassMember('bfd-reverse-path-type', REFERENCE_ENUM_CLASS, 'BfdReversePathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'BfdReversePathEnum', 
                [], [], 
                '''                BFD reverse path type
                ''',
                'bfd_reverse_path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('binding-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                BFD reverse path binding label
                ''',
                'binding_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd-reverse-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation',
            False, 
            [
            _MetaInfoClassMember('path-invalidation-action', REFERENCE_ENUM_CLASS, 'PathInvalidationActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'PathInvalidationActionEnum', 
                [], [], 
                '''                Path Invalidation Action
                ''',
                'path_invalidation_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '60000')], [], 
                '''                Path Invalidation Timeout
                ''',
                'path_invalidation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter path selection configuration
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('invalidation', REFERENCE_CLASS, 'Invalidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation', 
                [], [], 
                '''                Path invalidation configuration for this
                specific tunnel
                ''',
                'invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-cost-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Path selection cost limit configuration for this
                specific tunnel
                ''',
                'path_selection_cost_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-exclude-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Path selection exclude list name
                configuration
                ''',
                'path_selection_exclude_list',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'att-path-option-path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional',
            False, 
            [
            _MetaInfoClassMember('bd-group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Bidirectional Group ID
                ''',
                'bd_group_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bd-source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Bidirectional Source IP Address
                ''',
                'bd_source_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bidirectional',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath',
            False, 
            [
            _MetaInfoClassMember('dp-group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Disjoint Path Group ID
                ''',
                'dp_group_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dp-source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Disjoint Path Source IP Address
                ''',
                'dp_source_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dp-type', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Disjoint Path Type
                ''',
                'dp_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'disjoint-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce',
            False, 
            [
            _MetaInfoClassMember('bidirectional', REFERENCE_CLASS, 'Bidirectional' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional', 
                [], [], 
                '''                Bidirectional parameters
                ''',
                'bidirectional',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('disjoint-path', REFERENCE_CLASS, 'DisjointPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath', 
                [], [], 
                '''                Disjoint path parameters
                ''',
                'disjoint_path',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Class type for the bandwidth allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity-affinity-type', REFERENCE_LIST, 'NewStyleAffinityAffinityType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-types',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('att-path-option-path-selection', REFERENCE_CLASS, 'AttPathOptionPathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'att_path_option_path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-reverse-path', REFERENCE_CLASS, 'BfdReversePath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath', 
                [], [], 
                '''                Configure BFD reverse path
                ''',
                'bfd_reverse_path',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-types', REFERENCE_CLASS, 'NewStyleAffinityAffinityTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinity_affinity_types',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce', REFERENCE_CLASS, 'Pce' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce', 
                [], [], 
                '''                Configure pce properties
                ''',
                'pce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes',
            False, 
            [
            _MetaInfoClassMember('path-option-attribute', REFERENCE_LIST, 'PathOptionAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute', 
                [], [], 
                '''                Path Option Attribute
                ''',
                'path_option_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Class type for the bandwidth allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable path selection
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity-affinity-type', REFERENCE_LIST, 'NewStyleAffinityAffinityType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-types',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute',
            False, 
            [
            _MetaInfoClassMember('bandwidth-protection', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Bandwidth Protection
                ''',
                'bandwidth_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-protection', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Node Protection
                ''',
                'node_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all events for a tunnel
                ''',
                'all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel bandwidth change messages
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel rereoute messages
                ''',
                'reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('sub-lsp-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel sub-LSP state messages
                ''',
                'sub_lsp_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute', 
                [], [], 
                '''                Specify MPLS tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interface-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The bandwidth of the interface in kbps
                ''',
                'interface_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-types', REFERENCE_CLASS, 'NewStyleAffinityAffinityTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinity_affinity_types',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2mpte-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes',
            False, 
            [
            _MetaInfoClassMember('p2mpte-attribute', REFERENCE_LIST, 'P2MpteAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute', 
                [], [], 
                '''                P2MP-TE Tunnel Attribute
                ''',
                'p2mpte_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2mpte-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index',
            False, 
            [
            _MetaInfoClassMember('index-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Index number
                ''',
                'index_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('prepend-type', REFERENCE_ENUM_CLASS, 'SrPrependEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'SrPrependEnum', 
                [], [], 
                '''                Prepend type
                ''',
                'prepend_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'index',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes',
            False, 
            [
            _MetaInfoClassMember('index', REFERENCE_LIST, 'Index' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index', 
                [], [], 
                '''                Prepend index information
                ''',
                'index',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter path selection segment routing
                prepend submode
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('indexes', REFERENCE_CLASS, 'Indexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes', 
                [], [], 
                '''                Segment routing prepend index table
                ''',
                'indexes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'segment-routing-prepend',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation',
            False, 
            [
            _MetaInfoClassMember('invalidation-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '60000')], [], 
                '''                Path selection invalidation timer value
                (milliseconds)
                ''',
                'invalidation_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('invalidation-timer-expire-type', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionInvalidationTimerExpireEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionInvalidationTimerExpireEnum', 
                [], [], 
                '''                Path selection invalidation timer expire
                type
                ''',
                'invalidation_timer_expire_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter path selection configuration
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('invalidation', REFERENCE_CLASS, 'Invalidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation', 
                [], [], 
                '''                Path selection invalidation configuration
                ''',
                'invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Path selection metric to use in path
                calculation
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-segment-routing-adjacency-protection', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum', 
                [], [], 
                '''                Segment routing adjacency protection type
                to use in path calculation
                ''',
                'path_selection_segment_routing_adjacency_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('segment-routing-prepend', REFERENCE_CLASS, 'SegmentRoutingPrepend' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend', 
                [], [], 
                '''                Path selection segment routing prepend
                configuration
                ''',
                'segment_routing_prepend',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional',
            False, 
            [
            _MetaInfoClassMember('bd-group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Bidirectional Group ID
                ''',
                'bd_group_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bd-source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Bidirectional Source IP Address
                ''',
                'bd_source_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bidirectional',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath',
            False, 
            [
            _MetaInfoClassMember('dp-group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Disjoint Path Group ID
                ''',
                'dp_group_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dp-source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Disjoint Path Source IP Address
                ''',
                'dp_source_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dp-type', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Disjoint Path Type
                ''',
                'dp_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'disjoint-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce',
            False, 
            [
            _MetaInfoClassMember('bidirectional', REFERENCE_CLASS, 'Bidirectional' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional', 
                [], [], 
                '''                Bidirectional parameters
                ''',
                'bidirectional',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('disjoint-path', REFERENCE_CLASS, 'DisjointPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath', 
                [], [], 
                '''                Disjoint path parameters
                ''',
                'disjoint_path',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all events for a tunnel
                ''',
                'all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BFD session state change alarm
                ''',
                'bfd_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-switch-over-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'lsp_switch_over_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel record-route messages
                ''',
                'record_route_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel rereoute messages
                ''',
                'reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity-affinity-type', REFERENCE_LIST, 'NewStyleAffinityAffinityType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-types',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-types', REFERENCE_CLASS, 'NewStyleAffinityAffinityTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinity_affinity_types',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce', REFERENCE_CLASS, 'Pce' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce', 
                [], [], 
                '''                Configure pce properties
                ''',
                'pce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2p-te-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes',
            False, 
            [
            _MetaInfoClassMember('p2p-te-attribute', REFERENCE_LIST, 'P2PTeAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute', 
                [], [], 
                '''                P2P-TE Tunnel Attribute
                ''',
                'p2p_te_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2p-te-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName',
            False, 
            [
            _MetaInfoClassMember('mp-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set if merge-point address is to be
                appended
                ''',
                'mp_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Signalled name
                ''',
                'name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protected-interface-type', REFERENCE_ENUM_CLASS, 'MplsTeSigNameOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSigNameOptionEnum', 
                [], [], 
                '''                Protected-interface address or name
                ''',
                'protected_interface_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('source-type', REFERENCE_ENUM_CLASS, 'MplsTeSigNameOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSigNameOptionEnum', 
                [], [], 
                '''                Source address or name
                ''',
                'source_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'signalled-name',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging',
            False, 
            [
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-backup-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable path selection
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses',
            False, 
            [
            _MetaInfoClassMember('policy-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Array of Policy class
                ''',
                'policy_class',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=7),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'policy-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity-affinity-type', REFERENCE_LIST, 'NewStyleAffinityAffinityType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-types',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-backup-logging', REFERENCE_CLASS, 'AutoBackupLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'auto_backup_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-types', REFERENCE_CLASS, 'NewStyleAffinityAffinityTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinity_affinity_types',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('policy-classes', REFERENCE_CLASS, 'PolicyClasses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses', 
                [], [], 
                '''                Policy classes for PBTS
                ''',
                'policy_classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-name', REFERENCE_CLASS, 'SignalledName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName', 
                [], [], 
                '''                Signalled name
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-backup-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-backup-attribute', REFERENCE_LIST, 'AutoBackupAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute', 
                [], [], 
                '''                Auto-backup Tunnel Attribute
                ''',
                'auto_backup_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-backup-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration',
            False, 
            [
            _MetaInfoClassMember('hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '167')], [], 
                '''                Hour of day
                ''',
                'hour',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minute of the hour
                ''',
                'minutes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'schedule-duration',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate',
            False, 
            [
            _MetaInfoClassMember('day', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                Day of the month
                ''',
                'day',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Hour of day
                ''',
                'hour',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minute of the hour
                ''',
                'minutes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('month', ATTRIBUTE, 'int' , None, None, 
                [('0', '11')], [], 
                '''                Month of the year
                ''',
                'month',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('year', ATTRIBUTE, 'int' , None, None, 
                [('2015', '2035')], [], 
                '''                Year
                ''',
                'year',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'schedule-date',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName',
            False, 
            [
            _MetaInfoClassMember('schedule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 254)], [], 
                '''                Enter 64 characters for revert schedule
                name
                ''',
                'schedule_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('revert-schedule-frequency', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Frequency set as Once, Daily, Weekly
                ''',
                'revert_schedule_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('revert-schedule-max-tries', ATTRIBUTE, 'int' , None, None, 
                [('1', '2016')], [], 
                '''                Revert Schedule Max tries
                ''',
                'revert_schedule_max_tries',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('sch-name-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Schedule name enable object
                ''',
                'sch_name_enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('schedule-date', REFERENCE_CLASS, 'ScheduleDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate', 
                [], [], 
                '''                Set date in format hh:mm MMM DD YYYY
                ''',
                'schedule_date',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('schedule-duration', REFERENCE_CLASS, 'ScheduleDuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration', 
                [], [], 
                '''                Set duration in format hh:mm
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'revert-schedule-name',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames',
            False, 
            [
            _MetaInfoClassMember('revert-schedule-name', REFERENCE_LIST, 'RevertScheduleName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName', 
                [], [], 
                '''                Name Identifier for revert schedule
                ''',
                'revert_schedule_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'revert-schedule-names',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode',
            False, 
            [
            _MetaInfoClassMember('connection-mode', REFERENCE_ENUM_CLASS, 'MplsTeOtnSncModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnSncModeEnum', 
                [], [], 
                '''                The sub-network connection mode
                ''',
                'connection_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('connection-monitoring-mode', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                Tandem Connection Monitoring ID for the
                interface
                ''',
                'connection_monitoring_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'sub-network-connection-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers',
            False, 
            [
            _MetaInfoClassMember('aps-hold-off', ATTRIBUTE, 'int' , None, None, 
                [('100', '10000')], [], 
                '''                G.709 OTN path protection hold-off timer in
                milliseconds
                ''',
                'aps_hold_off',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('aps-wait-to-restore', ATTRIBUTE, 'int' , None, None, 
                [('0', '720')], [], 
                '''                G.709 OTN path protection wait to restore
                timer in seconds
                ''',
                'aps_wait_to_restore',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable path selection
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('aps-protection-mode', REFERENCE_ENUM_CLASS, 'MplsTeOtnApsProtectionModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnApsProtectionModeEnum', 
                [], [], 
                '''                The APS protecion mode
                ''',
                'aps_protection_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('aps-protection-type', REFERENCE_ENUM_CLASS, 'MplsTeOtnApsProtectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnApsProtectionEnum', 
                [], [], 
                '''                The APS protecion type
                ''',
                'aps_protection_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('aps-restoration-style', REFERENCE_ENUM_CLASS, 'MplsTeOtnApsRestorationStyleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnApsRestorationStyleEnum', 
                [], [], 
                '''                The APS restoration style
                ''',
                'aps_restoration_style',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('revert-schedule-names', REFERENCE_CLASS, 'RevertScheduleNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames', 
                [], [], 
                '''                Specify APS revert schedule
                ''',
                'revert_schedule_names',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('sub-network-connection-mode', REFERENCE_CLASS, 'SubNetworkConnectionMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode', 
                [], [], 
                '''                Sub-network connection mode
                ''',
                'sub_network_connection_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers', 
                [], [], 
                '''                Timers
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'otn-pp-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes',
            False, 
            [
            _MetaInfoClassMember('otn-pp-attribute', REFERENCE_LIST, 'OtnPpAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute', 
                [], [], 
                '''                OTN Path Protection Attribute
                ''',
                'otn_pp_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'otn-pp-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging',
            False, 
            [
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel rereoute messages
                ''',
                'reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-mesh-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Class type for the bandwidth allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable path selection
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses',
            False, 
            [
            _MetaInfoClassMember('policy-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Array of Policy class
                ''',
                'policy_class',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=7),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'policy-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity-affinity-type', REFERENCE_LIST, 'NewStyleAffinityAffinityType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10', REFERENCE_LIST, 'NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity-affinity-types',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute',
            False, 
            [
            _MetaInfoClassMember('bandwidth-protection', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Bandwidth Protection
                ''',
                'bandwidth_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-protection', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Node Protection
                ''',
                'node_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-mesh-logging', REFERENCE_CLASS, 'AutoMeshLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'auto_mesh_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('autoroute-announce', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable autoroute announce
                ''',
                'autoroute_announce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('collection-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable bandwidth collection only, no auto-bw
                adjustment
                ''',
                'collection_only',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute', 
                [], [], 
                '''                Specify MPLS tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('1', '7')], [], 
                '''                Forward class value
                ''',
                'forward_class',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interface-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The bandwidth of the interface in kbps
                ''',
                'interface_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('load-share', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tunnel loadsharing metric
                ''',
                'load_share',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinity-affinity-types', REFERENCE_CLASS, 'NewStyleAffinityAffinityTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinity_affinity_types',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('policy-classes', REFERENCE_CLASS, 'PolicyClasses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses', 
                [], [], 
                '''                Policy classes for PBTS
                ''',
                'policy_classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soft-preemption', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the soft-preemption feature on the tunnel
                ''',
                'soft_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-mesh-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-mesh-attribute', REFERENCE_LIST, 'AutoMeshAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute', 
                [], [], 
                '''                Auto-mesh Tunnel Attribute
                ''',
                'auto_mesh_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-mesh-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg',
            False, 
            [
            _MetaInfoClassMember('srlg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('conformance', REFERENCE_ENUM_CLASS, 'MplsTePathDiversityConformanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathDiversityConformanceEnum', 
                [], [], 
                '''                The diversity conformance requirements
                ''',
                'conformance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs',
            False, 
            [
            _MetaInfoClassMember('srlg', REFERENCE_LIST, 'Srlg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg', 
                [], [], 
                '''                SRLG-based path-diversity element
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlgs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel id
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel-id
                ''',
                'extended_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSP id
                ''',
                'lsp_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('conformance', REFERENCE_ENUM_CLASS, 'MplsTePathDiversityConformanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathDiversityConformanceEnum', 
                [], [], 
                '''                The diversity conformance requirements
                ''',
                'conformance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fec',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs',
            False, 
            [
            _MetaInfoClassMember('fec', REFERENCE_LIST, 'Fec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec', 
                [], [], 
                '''                LSP-based path-diversity, referenced by
                FEC
                ''',
                'fec',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fecs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp',
            False, 
            [
            _MetaInfoClassMember('fecs', REFERENCE_CLASS, 'Fecs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs', 
                [], [], 
                '''                FEC LSP-based path diversity
                ''',
                'fecs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity',
            False, 
            [
            _MetaInfoClassMember('lsp', REFERENCE_CLASS, 'Lsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp', 
                [], [], 
                '''                LSP-based path diversity
                ''',
                'lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('srlgs', REFERENCE_CLASS, 'Srlgs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs', 
                [], [], 
                '''                SRLG-based path diversity
                ''',
                'srlgs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-diversity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable path selection
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-set enable object that controls
                whether this attribute-set is configured or not
                .This object must be set before other
                configuration supplied for this attribute-set
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-diversity', REFERENCE_CLASS, 'PathDiversity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity', 
                [], [], 
                '''                Path diversity
                ''',
                'path_diversity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'xro-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes',
            False, 
            [
            _MetaInfoClassMember('xro-attribute', REFERENCE_LIST, 'XroAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute', 
                [], [], 
                '''                XRO Attribute
                ''',
                'xro_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'xro-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet',
            False, 
            [
            _MetaInfoClassMember('auto-backup-attributes', REFERENCE_CLASS, 'AutoBackupAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes', 
                [], [], 
                '''                Auto-backup Tunnel Attribute Table
                ''',
                'auto_backup_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-mesh-attributes', REFERENCE_CLASS, 'AutoMeshAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes', 
                [], [], 
                '''                Auto-mesh Tunnel AttributeSets Table
                ''',
                'auto_mesh_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('otn-pp-attributes', REFERENCE_CLASS, 'OtnPpAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes', 
                [], [], 
                '''                OTN Path Protection Attributes table
                ''',
                'otn_pp_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2mpte-attributes', REFERENCE_CLASS, 'P2MpteAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes', 
                [], [], 
                '''                P2MP-TE Tunnel AttributeSets Table
                ''',
                'p2mpte_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2p-te-attributes', REFERENCE_CLASS, 'P2PTeAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes', 
                [], [], 
                '''                P2P-TE Tunnel AttributeSets Table
                ''',
                'p2p_te_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-option-attributes', REFERENCE_CLASS, 'PathOptionAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes', 
                [], [], 
                '''                Path Option Attribute-Set Table
                ''',
                'path_option_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-attributes', REFERENCE_CLASS, 'XroAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes', 
                [], [], 
                '''                XRO Tunnel Attributes table
                ''',
                'xro_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'attribute-set',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.BfdOverLsp.Tail' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.BfdOverLsp.Tail',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('50', '30000')], [], 
                '''                Specify BFD over LSP tail minimum interval
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [('3', '10')], [], 
                '''                Specify BFD over LSP tail multiplier
                ''',
                'multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tail',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.BfdOverLsp.Head' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.BfdOverLsp.Head',
            False, 
            [
            _MetaInfoClassMember('down-action', REFERENCE_ENUM_CLASS, 'MplsTeBfdSessionDownActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBfdSessionDownActionEnum', 
                [], [], 
                '''                Specify BFD session down action
                ''',
                'down_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reopt-timeout', ATTRIBUTE, 'int' , None, None, 
                [('120', '4294967295')], [], 
                '''                BFD session down reopt timeout
                ''',
                'reopt_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'head',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.BfdOverLsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.BfdOverLsp',
            False, 
            [
            _MetaInfoClassMember('head', REFERENCE_CLASS, 'Head' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.BfdOverLsp.Head', 
                [], [], 
                '''                BFD over LSP Head Global Configurations
                ''',
                'head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tail', REFERENCE_CLASS, 'Tail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.BfdOverLsp.Tail', 
                [], [], 
                '''                BFD over LSP Tail Global Configurations
                ''',
                'tail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd-over-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers',
            False, 
            [
            _MetaInfoClassMember('redelegation-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Timer for static tunnel redelegation in
                seconds, default is 180 seconds
                ''',
                'redelegation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                State timeout for LSPs without delegation in
                seconds, zero means immediate removal,
                default is 180 seconds
                ''',
                'state_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'stateful-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.PceStateful' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.PceStateful',
            False, 
            [
            _MetaInfoClassMember('cisco-extension', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable processing of PCEP Cisco extension
                ''',
                'cisco_extension',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('delegation', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Delegate all statically configured tunnels
                ''',
                'delegation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PCE stateful capability
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-repair', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable reoptimization by PCC after path
                failures
                ''',
                'fast_repair',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('instantiation', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PCE stateful instantiation capability
                ''',
                'instantiation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('report', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Report all statically configured tunnels
                ''',
                'report',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('stateful-timers', REFERENCE_CLASS, 'StatefulTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers', 
                [], [], 
                '''                Configure Stateful PCE (Path Computation
                Element) timers
                ''',
                'stateful_timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce-stateful',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Timer' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Timer',
            False, 
            [
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timer',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('pce-peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of PCE Peer
                ''',
                'pce_peer_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled PCE peer (default source address
                uses local)
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                MD5 password
                ''',
                'password',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Precedence order
                ''',
                'precedence',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Peers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Peers.Peer', 
                [], [], 
                '''                PCE peer
                ''',
                'peer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Logging.Events' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Logging.Events',
            False, 
            [
            _MetaInfoClassMember('peer-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Peer status changes logging
                ''',
                'peer_status',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'events',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Logging',
            False, 
            [
            _MetaInfoClassMember('events', REFERENCE_CLASS, 'Events' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Logging.Events', 
                [], [], 
                '''                Configure logging events
                ''',
                'events',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of this PCE
                ''',
                'address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('deadtimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Deadtimer interval in seconds
                ''',
                'deadtimer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Keepalive interval in seconds
                ''',
                'keepalive',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keepalive-tolerance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Keepalive interval tolerance in seconds
                ''',
                'keepalive_tolerance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Logging', 
                [], [], 
                '''                Configure PCE (Path Computation Element)
                logging feature
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                MD5 password
                ''',
                'password',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce-stateful', REFERENCE_CLASS, 'PceStateful' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.PceStateful', 
                [], [], 
                '''                PCE Stateful
                ''',
                'pce_stateful',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('peer-source-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCE Peer Source Address
                ''',
                'peer_source_addr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Peers', 
                [], [], 
                '''                Configure PCE peers
                ''',
                'peers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Precedence order
                ''',
                'precedence',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-period', ATTRIBUTE, 'int' , None, None, 
                [('60', '604800')], [], 
                '''                PCE reoptimization period for PCE-based paths
                ''',
                'reoptimize_period',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('request-timeout', ATTRIBUTE, 'int' , None, None, 
                [('5', '100')], [], 
                '''                Request timeout value in seconds
                ''',
                'request_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('segment-routing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PCE segment routing capability
                ''',
                'segment_routing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('speaker-entity-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 256)], [], 
                '''                PCE speaker entity identifier
                ''',
                'speaker_entity_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Timer', 
                [], [], 
                '''                Configure PCE (Path Computation Element)
                timers
                ''',
                'timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState',
            False, 
            [
            _MetaInfoClassMember('all-transit-lsp-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold for all transit LSPs
                ''',
                'all_transit_lsp_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('unprotected-transit-lsp-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold for unprotected transit LSPs
                ''',
                'unprotected_transit_lsp_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lsp-oor-red-state',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState',
            False, 
            [
            _MetaInfoClassMember('all-transit-lsp-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold for all transit LSPs
                ''',
                'all_transit_lsp_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('unprotected-transit-lsp-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold for unprotected transit LSPs
                ''',
                'unprotected_transit_lsp_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lsp-oor-yellow-state',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.LspOutOfResource' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.LspOutOfResource',
            False, 
            [
            _MetaInfoClassMember('lsp-oor-red-state', REFERENCE_CLASS, 'LspOorRedState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState', 
                [], [], 
                '''                Configuration for LSP OOR Red/Major State
                ''',
                'lsp_oor_red_state',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-oor-yellow-state', REFERENCE_CLASS, 'LspOorYellowState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState', 
                [], [], 
                '''                Configuration for LSP OOR Yellow/Minor State
                ''',
                'lsp_oor_yellow_state',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lsp-out-of-resource',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.SoftPreemption' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.SoftPreemption',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object controls whether soft preemption
                is enabled. This object must be set before
                setting any other objects under the
                SoftPreemption class.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('frr-rewrite', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object controls whether FRR rewrite
                during soft preemption is enabled.
                ''',
                'frr_rewrite',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '300')], [], 
                '''                This object sets the timeout in seconds before
                hard preemption is triggered.
                ''',
                'timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'soft-preemption',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.FastReroute.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.FastReroute.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-backup', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Seconds before backup declared UP (0 disables
                hold-timer)
                ''',
                'hold_backup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('promotion', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                The value of the promotion timer in seconds
                ''',
                'promotion',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.FastReroute',
            False, 
            [
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.FastReroute.Timers', 
                [], [], 
                '''                Configure fast reroute timers
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric',
            False, 
            [
            _MetaInfoClassMember('class-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Path Selection class Type
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Metric to use for ERO Expansion
                ''',
                'metric_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'loose-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection.LooseMetrics' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection.LooseMetrics',
            False, 
            [
            _MetaInfoClassMember('loose-metric', REFERENCE_LIST, 'LooseMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric', 
                [], [], 
                '''                Path selection Loose ERO Metric configuration
                ''',
                'loose_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'loose-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection.Invalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection.Invalidation',
            False, 
            [
            _MetaInfoClassMember('path-invalidation-action', REFERENCE_ENUM_CLASS, 'PathInvalidationActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'PathInvalidationActionEnum', 
                [], [], 
                '''                Path Invalidation Action
                ''',
                'path_invalidation_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '60000')], [], 
                '''                Path Invalidation Timeout
                ''',
                'path_invalidation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole',
            False, 
            [
            _MetaInfoClassMember('head', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set if the OL-bit is to be applied to tunnel
                heads
                ''',
                'head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set if the OL-bit is to be applied to tunnel
                midpoints
                ''',
                'mid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tail', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set if the OL-bit is to be applied to tunnel
                tails
                ''',
                'tail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ignore-overload-role',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity',
            False, 
            [
            _MetaInfoClassMember('class-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Path Selection class Type
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'loose-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection.LooseAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection.LooseAffinities',
            False, 
            [
            _MetaInfoClassMember('loose-affinity', REFERENCE_LIST, 'LooseAffinity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity', 
                [], [], 
                '''                Path selection Loose ERO Affinity
                configuration
                ''',
                'loose_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'loose-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelection',
            False, 
            [
            _MetaInfoClassMember('cost-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Path selection cost limit configuration for
                all tunnels
                ''',
                'cost_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ignore-overload-role', REFERENCE_CLASS, 'IgnoreOverloadRole' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole', 
                [], [], 
                '''                Path selection to ignore overload node during
                CSPF
                ''',
                'ignore_overload_role',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('invalidation', REFERENCE_CLASS, 'Invalidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection.Invalidation', 
                [], [], 
                '''                Path invalidation configuration for all
                tunnels
                ''',
                'invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('loose-affinities', REFERENCE_CLASS, 'LooseAffinities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection.LooseAffinities', 
                [], [], 
                '''                Path selection Loose ERO Affinity Class
                configuration
                ''',
                'loose_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('loose-domain-match', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only the IGP instance of the incoming
                interface
                ''',
                'loose_domain_match',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('loose-metrics', REFERENCE_CLASS, 'LooseMetrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection.LooseMetrics', 
                [], [], 
                '''                Path selection Loose ERO Metric Class
                configuration
                ''',
                'loose_metrics',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Metric to use in path calculation
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionTiebreakerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionTiebreakerEnum', 
                [], [], 
                '''                CSPF tiebreaker to use in path calculation
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Affinity Name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Affinity Value in Hex number or by Bit
                position
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('value-type', REFERENCE_ENUM_CLASS, 'MplsTeAffinityValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeAffinityValueEnum', 
                [], [], 
                '''                Affinity value type
                ''',
                'value_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AffinityMappings' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AffinityMappings',
            False, 
            [
            _MetaInfoClassMember('affinity-mapping', REFERENCE_LIST, 'AffinityMapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping', 
                [], [], 
                '''                Affinity Mapping configuration
                ''',
                'affinity_mapping',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes',
            False, 
            [
            _MetaInfoClassMember('advertise-explicit-nulls', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable explicit-null advertising to PHOP
                ''',
                'advertise_explicit_nulls',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('affinity-mappings', REFERENCE_CLASS, 'AffinityMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AffinityMappings', 
                [], [], 
                '''                Affinity Mapping Table configuration
                ''',
                'affinity_mappings',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-set', REFERENCE_CLASS, 'AttributeSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet', 
                [], [], 
                '''                Attribute AttributeSets
                ''',
                'attribute_set',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-bandwidth-collect-frequency', ATTRIBUTE, 'int' , None, None, 
                [('1', '10080')], [], 
                '''                Auto-bandwidth global collection frequency in
                minutes
                ''',
                'auto_bandwidth_collect_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-tunnel', REFERENCE_CLASS, 'AutoTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel', 
                [], [], 
                '''                Configure auto-tunnels feature
                ''',
                'auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-over-lsp', REFERENCE_CLASS, 'BfdOverLsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.BfdOverLsp', 
                [], [], 
                '''                BFD over MPLS TE Global Configurations
                ''',
                'bfd_over_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('disable-reoptimize-affinity-failure', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable reoptimization after affinity failures
                ''',
                'disable_reoptimize_affinity_failure',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable-unequal-load-balancing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable unequal load-balancing over tunnels to
                the same destination
                ''',
                'enable_unequal_load_balancing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.FastReroute', 
                [], [], 
                '''                Configure fast reroute attributes
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault-oam', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Fault-OAM functionality for
                bidirectional tunnels
                ''',
                'fault_oam',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('graceful-preemption-on-bandwidth-reduction', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable graceful preemption when there is a
                bandwidth reduction
                ''',
                'graceful_preemption_on_bandwidth_reduction',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hardware-out-of-resource', REFERENCE_CLASS, 'HardwareOutOfResource' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.HardwareOutOfResource', 
                [], [], 
                '''                Configure HW OOR processing in MPLS-TE
                ''',
                'hardware_out_of_resource',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('link-holddown-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Holddown time for links which had Path Errors
                in seconds
                ''',
                'link_holddown_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'log_all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-frr-protection', REFERENCE_ENUM_CLASS, 'MplsTeLogFrrProtectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeLogFrrProtectionEnum', 
                [], [], 
                '''                Log FRR Protection messages
                ''',
                'log_frr_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-head', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all head tunnel events
                ''',
                'log_head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-issu-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log ISSU status messages
                ''',
                'log_issu_status',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-mid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all mid tunnel events
                ''',
                'log_mid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-nsr-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log NSR status messages
                ''',
                'log_nsr_status',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-preemption', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel preemption messages
                ''',
                'log_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-tail', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tail tunnel events
                ''',
                'log_tail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('loose-path-retry-period', ATTRIBUTE, 'int' , None, None, 
                [('30', '600')], [], 
                '''                Signalling retry for tunnels terminating
                outside the headend area
                ''',
                'loose_path_retry_period',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-out-of-resource', REFERENCE_CLASS, 'LspOutOfResource' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.LspOutOfResource', 
                [], [], 
                '''                Configure LSP OOR attributes in MPLS-TE
                ''',
                'lsp_out_of_resource',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('maximum-tunnels', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                The maximum number of tunnel heads that will be
                allowed.
                ''',
                'maximum_tunnels',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mib', REFERENCE_CLASS, 'Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Mib', 
                [], [], 
                '''                MPLS-TE MIB properties
                ''',
                'mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelection', 
                [], [], 
                '''                Path selection configuration
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-ignore-overload', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Deprecated - do not use
                ''',
                'path_selection_ignore_overload',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce-attributes', REFERENCE_CLASS, 'PceAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes', 
                [], [], 
                '''                Configuration MPLS TE PCE attributes
                ''',
                'pce_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('queues', REFERENCE_CLASS, 'Queues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Queues', 
                [], [], 
                '''                Configure MPLS TE route priority
                ''',
                'queues',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reopt-delay-path-protect-switchover-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Seconds between path protect switchover and
                tunnel re-optimization. Set to 0 to disable
                ''',
                'reopt_delay_path_protect_switchover_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-after-affinity-failure-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Delay reoptimizing current LSP after affinity
                failures
                ''',
                'reoptimize_delay_after_affinity_failure_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-after-frr-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '120')], [], 
                '''                Reoptimization Delay After FRR Value (seconds)
                ''',
                'reoptimize_delay_after_frr_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-cleanup-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Reoptimization Delay Cleanup Value (seconds)
                ''',
                'reoptimize_delay_cleanup_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-install-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Reoptimization Delay Install Value (seconds)
                ''',
                'reoptimize_delay_install_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-link-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable reoptimization based on link-up events
                ''',
                'reoptimize_link_up',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-load-balancing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Load balance bandwidth during reoptimization
                ''',
                'reoptimize_load_balancing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-timer-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Reoptimize timers period in seconds
                ''',
                'reoptimize_timer_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('secondary-router-ids', REFERENCE_CLASS, 'SecondaryRouterIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.SecondaryRouterIds', 
                [], [], 
                '''                Configure MPLS TE Secondary Router ID
                ''',
                'secondary_router_ids',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soft-preemption', REFERENCE_CLASS, 'SoftPreemption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.SoftPreemption', 
                [], [], 
                '''                Soft preemption configuration data
                ''',
                'soft_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('srlg', REFERENCE_CLASS, 'Srlg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg', 
                [], [], 
                '''                Configure SRLG values and MPLS-TE properties
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'global-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable protection switching due to LDI
                event
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ldi',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable protection switching due to LKR
                event
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lkr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Fault.ProtectionTrigger' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Fault.ProtectionTrigger',
            False, 
            [
            _MetaInfoClassMember('ais', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable protection switching due to AIS event
                ''',
                'ais',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ldi', REFERENCE_CLASS, 'Ldi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi', 
                [], [], 
                '''                Protection switching due to LDI event
                ''',
                'ldi',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lkr', REFERENCE_CLASS, 'Lkr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr', 
                [], [], 
                '''                Protection switching due to LKR event
                ''',
                'lkr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'protection-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Fault' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Fault',
            False, 
            [
            _MetaInfoClassMember('protection-trigger', REFERENCE_CLASS, 'ProtectionTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault.ProtectionTrigger', 
                [], [], 
                '''                OAM events that trigger protection switching
                ''',
                'protection_trigger',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('refresh-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                Periodic refresh interval for fault OAM
                messages
                ''',
                'refresh_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('wait-to-restore-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Waiting time before restoring working LSP
                ''',
                'wait_to_restore_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fault',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Alarm.SuppressEvent' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Alarm.SuppressEvent',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable alarm suppression
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'suppress-event',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Alarm' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Alarm',
            False, 
            [
            _MetaInfoClassMember('enable-alarm', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Transport Profile Alarm
                ''',
                'enable_alarm',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soak-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Duration of soaking alarms
                ''',
                'soak_time',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('suppress-event', REFERENCE_CLASS, 'SuppressEvent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Alarm.SuppressEvent', 
                [], [], 
                '''                Suppress all tunnel/LSP alarms
                ''',
                'suppress_event',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'alarm',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Bfd.MinIntervalStandby' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Bfd.MinIntervalStandby',
            False, 
            [
            _MetaInfoClassMember('interval-standby-ms', ATTRIBUTE, 'int' , None, None, 
                [('3', '5000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval_standby_ms',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval-standby-us', ATTRIBUTE, 'int' , None, None, 
                [('3000', '5000000')], [], 
                '''                Hello interval in micro-seconds
                ''',
                'interval_standby_us',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'min-interval-standby',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Bfd.MinInterval' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Bfd.MinInterval',
            False, 
            [
            _MetaInfoClassMember('interval-ms', ATTRIBUTE, 'int' , None, None, 
                [('3', '5000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval_ms',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval-us', ATTRIBUTE, 'int' , None, None, 
                [('3000', '5000000')], [], 
                '''                Hello interval in micro-seconds
                ''',
                'interval_us',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'min-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Bfd' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('detection-multiplier-standby', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Detect multiplier for standby transport
                profile LSP
                ''',
                'detection_multiplier_standby',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-interval', REFERENCE_CLASS, 'MinInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Bfd.MinInterval', 
                [], [], 
                '''                Hello interval, either in milli-seconds or in
                micro-seconds
                ''',
                'min_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-interval-standby', REFERENCE_CLASS, 'MinIntervalStandby' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Bfd.MinIntervalStandby', 
                [], [], 
                '''                Hello interval for standby transport profile
                LSPs, either in milli-seconds or in
                micro-seconds
                ''',
                'min_interval_standby',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.Source' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.Source',
            False, 
            [
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Global identifier in numeric value
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel identifier in numeric value
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'source',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.Destination' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.Destination',
            False, 
            [
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Global identifier in numeric value
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel identifier in numeric value
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '4015')], [], 
                '''                MPLS label
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing MPLS label
                ''',
                'out_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-link', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Transport profile identifier of outgoing
                link
                ''',
                'out_link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'forward-io-map',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp',
            False, 
            [
            _MetaInfoClassMember('forward-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bandwidth of forward transport profile LSP
                ''',
                'forward_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-io-map', REFERENCE_CLASS, 'ForwardIoMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap', 
                [], [], 
                '''                Label cross-connect of forward transport
                profile LSP
                ''',
                'forward_io_map',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'forward-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '4015')], [], 
                '''                MPLS label
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing MPLS label
                ''',
                'out_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-link', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Transport profile identifier of outgoing
                link
                ''',
                'out_link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'reverse-io-map',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp',
            False, 
            [
            _MetaInfoClassMember('reverse-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bandwidth of reverse transport profile LSP
                ''',
                'reverse_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reverse-io-map', REFERENCE_CLASS, 'ReverseIoMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap', 
                [], [], 
                '''                Label cross-connect of reverse transport
                profile LSP
                ''',
                'reverse_io_map',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'reverse-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint',
            False, 
            [
            _MetaInfoClassMember('midpoint-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Name of mid-point
                ''',
                'midpoint_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.Destination', 
                [], [], 
                '''                Node identifier, tunnel identifier and
                optional global identifier of the destination
                of the LSP
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-lsp', REFERENCE_CLASS, 'ForwardLsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp', 
                [], [], 
                '''                Forward transport profile LSP
                ''',
                'forward_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Numeric identifier
                ''',
                'lsp_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-protect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable LSP protection
                ''',
                'lsp_protect',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reverse-lsp', REFERENCE_CLASS, 'ReverseLsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp', 
                [], [], 
                '''                none
                ''',
                'reverse_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.Source', 
                [], [], 
                '''                Node identifier, tunnel identifier and
                optional global identifier of the source of
                the LSP
                ''',
                'source',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints',
            False, 
            [
            _MetaInfoClassMember('midpoint', REFERENCE_LIST, 'Midpoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint', 
                [], [], 
                '''                Transport profile mid-point identifier
                ''',
                'midpoint',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'midpoints',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile',
            False, 
            [
            _MetaInfoClassMember('alarm', REFERENCE_CLASS, 'Alarm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Alarm', 
                [], [], 
                '''                Alarm management
                ''',
                'alarm',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault', REFERENCE_CLASS, 'Fault' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault', 
                [], [], 
                '''                Fault management
                ''',
                'fault',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Transport profile global identifier
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('midpoints', REFERENCE_CLASS, 'Midpoints' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints', 
                [], [], 
                '''                MPLS-TP tunnel mid-point table
                ''',
                'midpoints',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'transport-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link',
            False, 
            [
            _MetaInfoClassMember('link-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Numeric link identifier
                ''',
                'link_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop address in IPv4 format
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('next-hop-type', REFERENCE_ENUM_CLASS, 'LinkNextHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'LinkNextHopEnum', 
                [], [], 
                '''                Next hop type
                ''',
                'next_hop_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'link',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.TransportProfileLink.Links' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.TransportProfileLink.Links',
            False, 
            [
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link', 
                [], [], 
                '''                Transport profile link
                ''',
                'link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'links',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.TransportProfileLink' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.TransportProfileLink',
            False, 
            [
            _MetaInfoClassMember('links', REFERENCE_CLASS, 'Links' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.TransportProfileLink.Links', 
                [], [], 
                '''                Transport profile link table
                ''',
                'links',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'transport-profile-link',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Switchings.Switching' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Switchings.Switching',
            False, 
            [
            _MetaInfoClassMember('switching-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Switching index
                ''',
                'switching_id',
                'Cisco-IOS-XR-mpls-te-cfg', True, [
                    _MetaInfoClassMember('switching-id', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingIndexEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingIndexEnum', 
                        [], [], 
                        '''                        Switching index
                        ''',
                        'switching_id',
                        'Cisco-IOS-XR-mpls-te-cfg', True),
                    _MetaInfoClassMember('switching-id', ATTRIBUTE, 'int' , None, None, 
                        [('1', '255')], [], 
                        '''                        Switching index
                        ''',
                        'switching_id',
                        'Cisco-IOS-XR-mpls-te-cfg', True),
                ]),
            _MetaInfoClassMember('capability', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingCapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingCapEnum', 
                [], [], 
                '''                Set the local switching capability
                ''',
                'capability',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingEncodingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingEncodingEnum', 
                [], [], 
                '''                Set the local encoding type
                ''',
                'encoding',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'switching',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Switchings' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Switchings',
            False, 
            [
            _MetaInfoClassMember('switching', REFERENCE_LIST, 'Switching' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Switchings.Switching', 
                [], [], 
                '''                The te-link switching attributes
                ''',
                'switching',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'switchings',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.FloodArea' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.FloodArea',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Area ID
                ''',
                'area_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('igp-type', REFERENCE_ENUM_CLASS, 'MplsLcacFloodingIgpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsLcacFloodingIgpEnum', 
                [], [], 
                '''                IGP type
                ''',
                'igp_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'flood-area',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.AttributeNameXr' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.AttributeNameXr',
            False, 
            [
            _MetaInfoClassMember('attribute-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Array of Attribute Names
                ''',
                'attribute_name',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=32),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'attribute-name-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName',
            False, 
            [
            _MetaInfoClassMember('affinity-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '9')], [], 
                '''                Specify the entry index
                ''',
                'affinity_index',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('value', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Array of Attribute Names
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=32, min_elements=1),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'attribute-name',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.AttributeNames' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.AttributeNames',
            False, 
            [
            _MetaInfoClassMember('attribute-name', REFERENCE_LIST, 'AttributeName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName', 
                [], [], 
                '''                Set the interface attribute names
                ''',
                'attribute_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'attribute-names',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg',
            False, 
            [
            _MetaInfoClassMember('srlg-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG membership number
                ''',
                'srlg_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Srlgs' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Srlgs',
            False, 
            [
            _MetaInfoClassMember('srlg', REFERENCE_LIST, 'Srlg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg', 
                [], [], 
                '''                SRLG membership number
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlgs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.UpThresholds' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.UpThresholds',
            False, 
            [
            _MetaInfoClassMember('up-threshold', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Array of up threshold percentage
                ''',
                'up_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=14),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'up-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.DownThresholds' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.DownThresholds',
            False, 
            [
            _MetaInfoClassMember('down-threshold', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Array of down threshold percentage
                ''',
                'down_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=14),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'down-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac',
            False, 
            [
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set administrative weight for the interface
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-flags', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Set user defined interface attribute flags
                ''',
                'attribute_flags',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-name-xr', REFERENCE_CLASS, 'AttributeNameXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.AttributeNameXr', 
                [], [], 
                '''                Set the interface attribute names
                ''',
                'attribute_name_xr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-names', REFERENCE_CLASS, 'AttributeNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.AttributeNames', 
                [], [], 
                '''                Attribute name table
                ''',
                'attribute_names',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down-thresholds', REFERENCE_CLASS, 'DownThresholds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.DownThresholds', 
                [], [], 
                '''                Set thresholds for decreased resource
                availability in %
                ''',
                'down_thresholds',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS-TE on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault-oam-lockout', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Lockout protection on the interface for Flex
                LSP
                ''',
                'fault_oam_lockout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('flood-area', REFERENCE_CLASS, 'FloodArea' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.FloodArea', 
                [], [], 
                '''                Set the IGP instance into which this
                interface is to be flooded (GMPLS only)
                ''',
                'flood_area',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('srlgs', REFERENCE_CLASS, 'Srlgs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Srlgs', 
                [], [], 
                '''                Configure SRLG membership for the interface
                ''',
                'srlgs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('switchings', REFERENCE_CLASS, 'Switchings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Switchings', 
                [], [], 
                '''                Set the te-link switching attributes
                ''',
                'switchings',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('up-thresholds', REFERENCE_CLASS, 'UpThresholds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.UpThresholds', 
                [], [], 
                '''                Set thresholds for increased resource
                availability in %
                ''',
                'up_thresholds',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lcac',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 59)], [], 
                '''                Tunnel name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels',
            False, 
            [
            _MetaInfoClassMember('backup-tunnel', REFERENCE_LIST, 'BackupTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel', 
                [], [], 
                '''                Tunnel name
                ''',
                'backup_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude',
            False, 
            [
            _MetaInfoClassMember('srlg-mode', REFERENCE_ENUM_CLASS, 'MplsTesrlgExcludeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTesrlgExcludeEnum', 
                [], [], 
                '''                Set exclude SRLG mode for auto-tunnel
                backup on this TE link
                ''',
                'srlg_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'exclude',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup',
            False, 
            [
            _MetaInfoClassMember('attribute-set', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The name of attribute set to be applied to
                this auto backup lsp
                ''',
                'attribute_set',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable auto-tunnel backup on this TE link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('exclude', REFERENCE_CLASS, 'Exclude' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude', 
                [], [], 
                '''                Auto-tunnel backup exclusion criteria
                ''',
                'exclude',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('next-hop-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable NHOP-only mode for auto-tunnel
                backup on this TE link
                ''',
                'next_hop_only',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel',
            False, 
            [
            _MetaInfoClassMember('backup', REFERENCE_CLASS, 'Backup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup', 
                [], [], 
                '''                Auto tunnel backup configuration
                ''',
                'backup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath',
            False, 
            [
            _MetaInfoClassMember('tunnel-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel interface number
                ''',
                'tunnel_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths',
            False, 
            [
            _MetaInfoClassMember('backup-path', REFERENCE_LIST, 'BackupPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath', 
                [], [], 
                '''                Tunnel interface number
                ''',
                'backup_path',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-tunnel', REFERENCE_CLASS, 'AutoTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel', 
                [], [], 
                '''                Auto tunnel configuration
                ''',
                'auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('backup-paths', REFERENCE_CLASS, 'BackupPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths', 
                [], [], 
                '''                Configure MPLS TE backup tunnels for this
                interface
                ''',
                'backup_paths',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('backup-tunnels', REFERENCE_CLASS, 'BackupTunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels', 
                [], [], 
                '''                Configure MPLS TE backup tunnels for this
                interface
                ''',
                'backup_tunnels',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'global-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('global-attributes', REFERENCE_CLASS, 'GlobalAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes', 
                [], [], 
                '''                MPLS TE global interface configuration
                ''',
                'global_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lcac', REFERENCE_CLASS, 'Lcac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac', 
                [], [], 
                '''                LCAC specific MPLS interface configuration
                ''',
                'lcac',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('transport-profile-link', REFERENCE_CLASS, 'TransportProfileLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.TransportProfileLink', 
                [], [], 
                '''                MPLS transport profile capable link
                ''',
                'transport_profile_link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface', 
                [], [], 
                '''                Configure an MPLS TE interface
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode',
            False, 
            [
            _MetaInfoClassMember('tcmid', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                Tandem Connection Monitoring ID for the
                interface
                ''',
                'tcmid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tti-mode-type', REFERENCE_ENUM_CLASS, 'GmplsttiModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'GmplsttiModeEnum', 
                [], [], 
                '''                Type of Trail Trace Identifier
                ''',
                'tti_mode_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tti-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set administrative weight for the
                interface
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Set link delay for the interface
                ''',
                'delay',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GMPLS-NNI on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tti-mode', REFERENCE_CLASS, 'TtiMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode', 
                [], [], 
                '''                Set tandem connection monitoring for the
                interface
                ''',
                'tti_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller', 
                [], [], 
                '''                Configure a GMPLS NNI controller
                ''',
                'controller',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt',
            False, 
            [
            _MetaInfoClassMember('igp-area', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                IGP area
                ''',
                'igp_area',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers', 
                [], [], 
                '''                GMPLS-NNI controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ospf-int',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode',
            False, 
            [
            _MetaInfoClassMember('tcmid', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                Tandem Connection Monitoring ID for the
                interface
                ''',
                'tcmid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tti-mode-type', REFERENCE_ENUM_CLASS, 'GmplsttiModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'GmplsttiModeEnum', 
                [], [], 
                '''                Type of Trail Trace Identifier
                ''',
                'tti_mode_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tti-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set administrative weight for the
                interface
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Set link delay for the interface
                ''',
                'delay',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GMPLS-NNI on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tti-mode', REFERENCE_CLASS, 'TtiMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode', 
                [], [], 
                '''                Set tandem connection monitoring for the
                interface
                ''',
                'tti_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller', 
                [], [], 
                '''                Configure a GMPLS NNI controller
                ''',
                'controller',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID if in IP address format
                ''',
                'address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers', 
                [], [], 
                '''                GMPLS-NNI controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ospfip-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance',
            False, 
            [
            _MetaInfoClassMember('ospf-area-type', REFERENCE_ENUM_CLASS, 'OspfAreaModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OspfAreaModeEnum', 
                [], [], 
                '''                OSPF area format
                ''',
                'ospf_area_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('igp-instance-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Name of IGP instance
                ''',
                'igp_instance_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('igp-type', REFERENCE_ENUM_CLASS, 'MplsTeIgpProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeIgpProtocolEnum', 
                [], [], 
                '''                IGP type
                ''',
                'igp_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('ospf-int', REFERENCE_LIST, 'OspfInt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt', 
                [], [], 
                '''                ospf int
                ''',
                'ospf_int',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ospfip-addr', REFERENCE_LIST, 'OspfipAddr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr', 
                [], [], 
                '''                ospfip addr
                ''',
                'ospfip_addr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'topology-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances',
            False, 
            [
            _MetaInfoClassMember('topology-instance', REFERENCE_LIST, 'TopologyInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance', 
                [], [], 
                '''                GMPLS-NNI topology instance configuration
                ''',
                'topology_instance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'topology-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth',
            False, 
            [
            _MetaInfoClassMember('bitrate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Bitrate value in Kbps for ODUflex framing
                type
                ''',
                'bitrate',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('od-uflex-framing-type', REFERENCE_ENUM_CLASS, 'OtnSignaledBandwidthFlexFramingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnSignaledBandwidthFlexFramingEnum', 
                [], [], 
                '''                Framing type in case of ODUflex signal type
                ''',
                'od_uflex_framing_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-bandwidth-type', REFERENCE_ENUM_CLASS, 'OtnSignaledBandwidthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnSignaledBandwidthEnum', 
                [], [], 
                '''                The g.709 signal type requested
                ''',
                'signalled_bandwidth_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'signalled-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 tunnel destination
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-type', REFERENCE_ENUM_CLASS, 'OtnDestinationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnDestinationEnum', 
                [], [], 
                '''                Destination type whether it is unicast or
                unnumbered
                ''',
                'destination_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interface-if-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface index of port
                ''',
                'interface_if_index',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching',
            False, 
            [
            _MetaInfoClassMember('lockout', REFERENCE_ENUM_CLASS, 'OtnProtectionSwitchLockoutEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnProtectionSwitchLockoutEnum', 
                [], [], 
                '''                The configuration is used to prevent switch
                over for a particular path type in tunnel
                ''',
                'lockout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'protection-switching',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging',
            False, 
            [
            _MetaInfoClassMember('active-lsp-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel messages for changes in
                Active LSP
                ''',
                'active_lsp_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('homepath-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all messages for changes in state of
                Homepath of Working LSP
                ''',
                'homepath_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient
                bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel messages for changes in
                path-change
                ''',
                'path_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalling-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel sub-LSP state messages
                ''',
                'signalling_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('static-cross-connect-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel messages for static
                cross-connect messages
                ''',
                'static_cross_connect_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel messages for changes in
                tunnel-state
                ''',
                'tunnel_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption',
            False, 
            [
            _MetaInfoClassMember('preference-level', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Preference level for this path option
                ''',
                'preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('lockdown', REFERENCE_ENUM_CLASS, 'MplsTePathOptionPropertyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionPropertyEnum', 
                [], [], 
                '''                Lockdown properties
                ''',
                'lockdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The ID of the IP explicit path associated
                with this option
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the IP explicit path associated
                with this option
                ''',
                'path_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsTePathOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionEnum', 
                [], [], 
                '''                The type of the path option
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protected-by-preference-level', ATTRIBUTE, 'int' , None, None, 
                [('1', '1001')], [], 
                '''                Preference level of the protecting explicit
                path. 
                ''',
                'protected_by_preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('restore-by-preference-level', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Preference level of the restore path. 
                ''',
                'restore_by_preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The name of the XRO attribute set to be
                used for this path-option
                ''',
                'xro_attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-type', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The route-exclusion type
                ''',
                'xro_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions',
            False, 
            [
            _MetaInfoClassMember('path-option', REFERENCE_LIST, 'PathOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption', 
                [], [], 
                '''                The existence of this configuration
                indicates the path options have been set for
                the tunnel
                ''',
                'path_option',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-options',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni',
            False, 
            [
            _MetaInfoClassMember('egress-controller-if-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface index of Egress controller
                ''',
                'egress_controller_if_index',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('egress-type', REFERENCE_ENUM_CLASS, 'OtnStaticUniEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnStaticUniEnum', 
                [], [], 
                '''                Egress type whether it is xconnect or
                terminated
                ''',
                'egress_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ingress-controller-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Name of  ingress controller
                ''',
                'ingress_controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ingress-type', REFERENCE_ENUM_CLASS, 'OtnStaticUniEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnStaticUniEnum', 
                [], [], 
                '''                Ingress type whether it is xconnect or
                terminated
                ''',
                'ingress_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'static-uni',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead',
            False, 
            [
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('current-lsp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the current/working LSP of tunnel is shutdown
                ''',
                'current_lsp_shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination', 
                [], [], 
                '''                The existence of this configuration indicates
                the destination has been set for the tunnel
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the a new GMPLS NNI tunnel has been enabled
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging', 
                [], [], 
                '''                Tunnel event logging
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-options', REFERENCE_CLASS, 'PathOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions', 
                [], [], 
                '''                GMPLS NNI path options
                ''',
                'path_options',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-protection-attribute-set-profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The name of the path-protection profile to be
                included in signalling messages
                ''',
                'path_protection_attribute_set_profile',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Path selection configuration for this
                specific tunnel
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('payload', REFERENCE_ENUM_CLASS, 'OtnPayloadEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'OtnPayloadEnum', 
                [], [], 
                '''                The existence of this configuration indicates
                the Payload type have been set for the tunnel
                ''',
                'payload',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protection-switching', REFERENCE_CLASS, 'ProtectionSwitching' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching', 
                [], [], 
                '''                The configuration for a GMPLS NNI tunnel
                protection switch
                ''',
                'protection_switching',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('restore-lsp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the restore LSP of tunnel is shutdown
                ''',
                'restore_lsp_shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the tunnel is shutdown
                ''',
                'shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-bandwidth', REFERENCE_CLASS, 'SignalledBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth', 
                [], [], 
                '''                The existence of this configuration indicates
                the signalled bandwidth has been set for the
                tunnel
                ''',
                'signalled_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 254)], [], 
                '''                The name of the tunnel to be included in
                signalling messages
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('standby-lsp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the standby/protect LSP of tunnel is shutdown
                ''',
                'standby_lsp_shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('static-uni', REFERENCE_CLASS, 'StaticUni' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni', 
                [], [], 
                '''                The existence of this configuration indicates
                the static UNI endpoints have been set for
                the tunnel
                ''',
                'static_uni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-head',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads',
            False, 
            [
            _MetaInfoClassMember('tunnel-head', REFERENCE_LIST, 'TunnelHead' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead', 
                [], [], 
                '''                The configuration for a GMPLS NNI tunnel
                head-end
                ''',
                'tunnel_head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-heads',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni',
            False, 
            [
            _MetaInfoClassMember('enable-gmpls-nni', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS Traffic Engineering GMPLS-NNI
                ''',
                'enable_gmpls_nni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Path selection configuration for all gmpls nni
                tunnels
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('topology-instances', REFERENCE_CLASS, 'TopologyInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances', 
                [], [], 
                '''                GMPLS-NNI topology instance table
                ''',
                'topology_instances',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-heads', REFERENCE_CLASS, 'TunnelHeads' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads', 
                [], [], 
                '''                GMPLS-NNI tunnel-head table
                ''',
                'tunnel_heads',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'gmpls-nni',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Lcac.Bfd' : {
        'meta_info' : _MetaInfoClass('MplsTe.Lcac.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Detection multiplier for BFD sessions created
                by TE
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('15', '200')], [], 
                '''                Hello interval for BFD sessions created by TE
                ''',
                'interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Lcac.FloodingThreshold' : {
        'meta_info' : _MetaInfoClass('MplsTe.Lcac.FloodingThreshold',
            False, 
            [
            _MetaInfoClassMember('down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Downward flooding Threshold in percentages of
                total bandwidth
                ''',
                'down_stream',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Upward flooding Threshold in percentages of
                total bandwidth
                ''',
                'up_stream',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'flooding-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Lcac' : {
        'meta_info' : _MetaInfoClass('MplsTe.Lcac',
            False, 
            [
            _MetaInfoClassMember('bandwidth-hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '300')], [], 
                '''                Bandwidth hold timer value (seconds)
                ''',
                'bandwidth_hold_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Lcac.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('delay-preempt-bundle-capacity-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Bundle capacity preemption timer value
                (seconds)
                ''',
                'delay_preempt_bundle_capacity_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('flooding-threshold', REFERENCE_CLASS, 'FloodingThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Lcac.FloodingThreshold', 
                [], [], 
                '''                Configure flooding threshold as percentage of
                total link bandwidth.
                ''',
                'flooding_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('periodic-flooding-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Periodic flooding value (seconds)
                ''',
                'periodic_flooding_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lcac',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe' : {
        'meta_info' : _MetaInfoClass('MplsTe',
            False, 
            [
            _MetaInfoClassMember('diff-serv-traffic-engineering', REFERENCE_CLASS, 'DiffServTrafficEngineering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.DiffServTrafficEngineering', 
                [], [], 
                '''                Configure Diff-Serv Traffic-Engineering
                ''',
                'diff_serv_traffic_engineering',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable-traffic-engineering', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS Traffic Engineering
                ''',
                'enable_traffic_engineering',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-attributes', REFERENCE_CLASS, 'GlobalAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes', 
                [], [], 
                '''                Configure MPLS TE global attributes
                ''',
                'global_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('gmpls-nni', REFERENCE_CLASS, 'GmplsNni' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni', 
                [], [], 
                '''                GMPLS-NNI configuration
                ''',
                'gmpls_nni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('gmpls-uni', REFERENCE_CLASS, 'GmplsUni' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni', 
                [], [], 
                '''                GMPLS-UNI configuration
                ''',
                'gmpls_uni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces', 
                [], [], 
                '''                Configure MPLS TE interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lcac', REFERENCE_CLASS, 'Lcac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Lcac', 
                [], [], 
                '''                LCAC specific MPLS global configuration
                ''',
                'lcac',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('named-tunnels', REFERENCE_CLASS, 'NamedTunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.NamedTunnels', 
                [], [], 
                '''                Configure MPLS TE tunnel
                ''',
                'named_tunnels',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('transport-profile', REFERENCE_CLASS, 'TransportProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile', 
                [], [], 
                '''                MPLS transport profile configuration data
                ''',
                'transport_profile',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
}
_meta_table['MplsTe.DiffServTrafficEngineering.Classes.Class_']['meta_info'].parent =_meta_table['MplsTe.DiffServTrafficEngineering.Classes']['meta_info']
_meta_table['MplsTe.DiffServTrafficEngineering.Classes']['meta_info'].parent =_meta_table['MplsTe.DiffServTrafficEngineering']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr.Destination']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Metric']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.DestinationXr']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels.Tunnel']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels.Tunnels']['meta_info']
_meta_table['MplsTe.NamedTunnels.Tunnels']['meta_info'].parent =_meta_table['MplsTe.NamedTunnels']['meta_info']
_meta_table['MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Timers.PathOptionTimers']['meta_info']
_meta_table['MplsTe.GmplsUni.Timers.PathOptionTimers']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Timers']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.Announce']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.ControllerLogging']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers.Controller']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers.Controller']['meta_info'].parent =_meta_table['MplsTe.GmplsUni.Controllers']['meta_info']
_meta_table['MplsTe.GmplsUni.Timers']['meta_info'].parent =_meta_table['MplsTe.GmplsUni']['meta_info']
_meta_table['MplsTe.GmplsUni.Controllers']['meta_info'].parent =_meta_table['MplsTe.GmplsUni']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Pcc']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Pcc']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource']['meta_info']
_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource']['meta_info']
_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource']['meta_info']
_meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Names']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Values']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Names']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Queues.Queue']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Queues']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']
_meta_table['MplsTe.GlobalAttributes.BfdOverLsp.Tail']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.BfdOverLsp']['meta_info']
_meta_table['MplsTe.GlobalAttributes.BfdOverLsp.Head']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.BfdOverLsp']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes.PceStateful']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.Peers.Peer']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes.Peers']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.Logging.Events']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes.Logging']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.PceStateful']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.Timer']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.Peers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes.Logging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.LspOutOfResource']['meta_info']
_meta_table['MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.LspOutOfResource']['meta_info']
_meta_table['MplsTe.GlobalAttributes.FastReroute.Timers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.FastReroute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelection.LooseMetrics']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelection.LooseAffinities']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection.LooseMetrics']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection.Invalidation']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection.LooseAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AffinityMappings']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.HardwareOutOfResource']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Queues']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Mib']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.BfdOverLsp']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.LspOutOfResource']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.SoftPreemption']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.FastReroute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AffinityMappings']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger']['meta_info']
_meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger']['meta_info']
_meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Fault']['meta_info']
_meta_table['MplsTe.TransportProfile.Alarm.SuppressEvent']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Alarm']['meta_info']
_meta_table['MplsTe.TransportProfile.Bfd.MinIntervalStandby']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Bfd']['meta_info']
_meta_table['MplsTe.TransportProfile.Bfd.MinInterval']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Bfd']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.Source']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.Destination']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints.Midpoint']['meta_info'].parent =_meta_table['MplsTe.TransportProfile.Midpoints']['meta_info']
_meta_table['MplsTe.TransportProfile.Fault']['meta_info'].parent =_meta_table['MplsTe.TransportProfile']['meta_info']
_meta_table['MplsTe.TransportProfile.Alarm']['meta_info'].parent =_meta_table['MplsTe.TransportProfile']['meta_info']
_meta_table['MplsTe.TransportProfile.Bfd']['meta_info'].parent =_meta_table['MplsTe.TransportProfile']['meta_info']
_meta_table['MplsTe.TransportProfile.Midpoints']['meta_info'].parent =_meta_table['MplsTe.TransportProfile']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.TransportProfileLink.Links']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.TransportProfileLink.Links']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.TransportProfileLink']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.Switchings.Switching']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac.Switchings']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNames']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac.Srlgs']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.Switchings']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.FloodArea']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNameXr']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNames']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.Srlgs']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.UpThresholds']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac.DownThresholds']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.TransportProfileLink']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface']['meta_info']
_meta_table['MplsTe.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsTe.Interfaces']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TopologyInstances']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances']['meta_info'].parent =_meta_table['MplsTe.GmplsNni']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads']['meta_info'].parent =_meta_table['MplsTe.GmplsNni']['meta_info']
_meta_table['MplsTe.Lcac.Bfd']['meta_info'].parent =_meta_table['MplsTe.Lcac']['meta_info']
_meta_table['MplsTe.Lcac.FloodingThreshold']['meta_info'].parent =_meta_table['MplsTe.Lcac']['meta_info']
_meta_table['MplsTe.DiffServTrafficEngineering']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.NamedTunnels']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.GmplsUni']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.GlobalAttributes']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.TransportProfile']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.Interfaces']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.GmplsNni']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.Lcac']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
