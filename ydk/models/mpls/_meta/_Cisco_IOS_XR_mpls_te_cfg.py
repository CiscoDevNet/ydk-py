


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SrPrependEnum' : _MetaInfoEnum('SrPrependEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none-type':'NONE_TYPE',
            'next-label':'NEXT_LABEL',
            'bgp-n-hop':'BGP_N_HOP',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnDestinationEnum' : _MetaInfoEnum('OtnDestinationEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'un-number-ed':'UN_NUMBER_ED',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingCapEnum' : _MetaInfoEnum('MplsTeSwitchingCapEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'psc1':'PSC1',
            'lsc':'LSC',
            'fsc':'FSC',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBfdSessionDownActionEnum' : _MetaInfoEnum('MplsTeBfdSessionDownActionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            're-setup':'RE_SETUP',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'RoutePriorityRoleEnum' : _MetaInfoEnum('RoutePriorityRoleEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'route-priority-role-head-back-up':'ROUTE_PRIORITY_ROLE_HEAD_BACK_UP',
            'route-priority-role-head-primary':'ROUTE_PRIORITY_ROLE_HEAD_PRIMARY',
            'route-priority-role-middle':'ROUTE_PRIORITY_ROLE_MIDDLE',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingEncodeEnum' : _MetaInfoEnum('MplsTeSwitchingEncodeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'NONE',
            'packet':'PACKET',
            'ethernet':'ETHERNET',
            'sondet-sdh':'SONDET_SDH',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeLogFrrProtectionEnum' : _MetaInfoEnum('MplsTeLogFrrProtectionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'frr-active-primary':'FRR_ACTIVE_PRIMARY',
            'backup':'BACKUP',
            'frr-ready-primary':'FRR_READY_PRIMARY',
            'primary':'PRIMARY',
            'all':'ALL',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeTunnelAffinityEnum' : _MetaInfoEnum('MplsTeTunnelAffinityEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'include':'INCLUDE',
            'include-strict':'INCLUDE_STRICT',
            'exclude':'EXCLUDE',
            'exclude-all':'EXCLUDE_ALL',
            'ignore':'IGNORE',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'IetfModeEnum' : _MetaInfoEnum('IetfModeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'standard':'STANDARD',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathOptionPropertyEnum' : _MetaInfoEnum('MplsTePathOptionPropertyEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'NONE',
            'lockdown':'LOCKDOWN',
            'verbatim':'VERBATIM',
            'pce':'PCE',
            'segment-routing':'SEGMENT_ROUTING',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'GmplsttiModeEnum' : _MetaInfoEnum('GmplsttiModeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'sm':'SM',
            'pm':'PM',
            'tcm':'TCM',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionInvalidationTimerExpireEnum' : _MetaInfoEnum('MplsTePathSelectionInvalidationTimerExpireEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'tunnel-action-tear':'TUNNEL_ACTION_TEAR',
            'tunnel-action-drop':'TUNNEL_ACTION_DROP',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnApsProtectionEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            '1plus1-unidir-no-aps':'Y_1PLUS1_UNIDIR_NO_APS',
            '1plus1-unidir-aps':'Y_1PLUS1_UNIDIR_APS',
            '1plus1-bdir-aps':'Y_1PLUS1_BDIR_APS',
            '1plus1plus-r-bidir-aps':'Y_1PLUS1PLUS_R_BIDIR_APS',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingEncodingEnum' : _MetaInfoEnum('MplsTeSwitchingEncodingEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'packet':'PACKET',
            'ethernet':'ETHERNET',
            'sondet-sdh':'SONDET_SDH',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSigNameOptionEnum' : _MetaInfoEnum('MplsTeSigNameOptionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'NONE',
            'address':'ADDRESS',
            'name':'NAME',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBackupBandwidthClassEnum' : _MetaInfoEnum('MplsTeBackupBandwidthClassEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'class0':'CLASS0',
            'class1':'CLASS1',
            'any-class':'ANY_CLASS',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeAffinityValueEnum' : _MetaInfoEnum('MplsTeAffinityValueEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'hex-value':'HEX_VALUE',
            'bit-position':'BIT_POSITION',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnStaticUniEnum' : _MetaInfoEnum('OtnStaticUniEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'unknown':'UNKNOWN',
            'xc':'XC',
            'termination':'TERMINATION',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnSncModeEnum' : _MetaInfoEnum('MplsTeOtnSncModeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'snc-n':'SNC_N',
            'snc-i':'SNC_I',
            'snc-s':'SNC_S',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnPayloadEnum' : _MetaInfoEnum('OtnPayloadEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'unknown':'UNKNOWN',
            'bmp':'BMP',
            'gfp-f':'GFP_F',
            'gmp':'GMP',
            'gfp-f-ext':'GFP_F_EXT',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OspfAreaModeEnum' : _MetaInfoEnum('OspfAreaModeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'ospf-int':'OSPF_INT',
            'ospfip-addr':'OSPFIP_ADDR',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeIgpProtocolEnum' : _MetaInfoEnum('MplsTeIgpProtocolEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'NONE',
            'isis':'ISIS',
            'ospf':'OSPF',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionTiebreakerEnum' : _MetaInfoEnum('MplsTePathSelectionTiebreakerEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'min-fill':'MIN_FILL',
            'max-fill':'MAX_FILL',
            'random':'RANDOM',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathOptionEnum' : _MetaInfoEnum('MplsTePathOptionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'NOT_SET',
            'dynamic':'DYNAMIC',
            'explicit-name':'EXPLICIT_NAME',
            'explicit-number':'EXPLICIT_NUMBER',
            'no-ero':'NO_ERO',
            'sr':'SR',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'PathInvalidationActionEnum' : _MetaInfoEnum('PathInvalidationActionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'tear':'TEAR',
            'drop':'DROP',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnSignaledBandwidthEnum' : _MetaInfoEnum('OtnSignaledBandwidthEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'odu1':'ODU1',
            'odu2':'ODU2',
            'odu3':'ODU3',
            'odu4':'ODU4',
            'odu0':'ODU0',
            'odu2e':'ODU2E',
            'od-uflex-cbr':'OD_UFLEX_CBR',
            'od-uflex-gfp-resize':'OD_UFLEX_GFP_RESIZE',
            'od-uflex-gfp-not-resize':'OD_UFLEX_GFP_NOT_RESIZE',
            'odu1e':'ODU1E',
            'odu1f':'ODU1F',
            'odu2f':'ODU2F',
            'odu3e1':'ODU3E1',
            'odu3e2':'ODU3E2',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeAutorouteMetricEnum' : _MetaInfoEnum('MplsTeAutorouteMetricEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'relative':'RELATIVE',
            'absolute':'ABSOLUTE',
            'constant':'CONSTANT',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'BindingSegmentIdEnum' : _MetaInfoEnum('BindingSegmentIdEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'any-label':'ANY_LABEL',
            'specified-label':'SPECIFIED_LABEL',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTesrlgExcludeEnum' : _MetaInfoEnum('MplsTesrlgExcludeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'mandatory':'MANDATORY',
            'preferred':'PREFERRED',
            'weighted':'WEIGHTED',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBackupBandwidthPoolEnum' : _MetaInfoEnum('MplsTeBackupBandwidthPoolEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'any-pool':'ANY_POOL',
            'global-pool':'GLOBAL_POOL',
            'sub-pool':'SUB_POOL',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSignaledLabelEnum' : _MetaInfoEnum('MplsTeSignaledLabelEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'NOT_SET',
            'dwdm':'DWDM',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'BandwidthConstraintEnum' : _MetaInfoEnum('BandwidthConstraintEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'bandwidth-constraint-maximum-allocation-model':'BANDWIDTH_CONSTRAINT_MAXIMUM_ALLOCATION_MODEL',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionMetricEnum' : _MetaInfoEnum('MplsTePathSelectionMetricEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'igp':'IGP',
            'te':'TE',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathOptionProtectionEnum' : _MetaInfoEnum('MplsTePathOptionProtectionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'active':'ACTIVE',
            'protecting':'PROTECTING',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'OtnSignaledBandwidthFlexFramingEnum' : _MetaInfoEnum('OtnSignaledBandwidthFlexFramingEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'cbr':'CBR',
            'framed-gfp-fixed':'FRAMED_GFP_FIXED',
            'framed-gfp-resize':'FRAMED_GFP_RESIZE',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBandwidthLimitEnum' : _MetaInfoEnum('MplsTeBandwidthLimitEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'unlimited':'UNLIMITED',
            'limited':'LIMITED',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum' : _MetaInfoEnum('MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'not-set':'NOT_SET',
            'adj-unprotected':'ADJ_UNPROTECTED',
            'adj-protected':'ADJ_PROTECTED',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'LinkNextHopEnum' : _MetaInfoEnum('LinkNextHopEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'none':'NONE',
            'ipv4-address':'IPV4_ADDRESS',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsLcacFloodingIgpEnum' : _MetaInfoEnum('MplsLcacFloodingIgpEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'ospf':'OSPF',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeBandwidthDsteEnum' : _MetaInfoEnum('MplsTeBandwidthDsteEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'standard-dste':'STANDARD_DSTE',
            'pre-standard-dste':'PRE_STANDARD_DSTE',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTePathDiversityConformanceEnum' : _MetaInfoEnum('MplsTePathDiversityConformanceEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'strict':'STRICT',
            'best-effort':'BEST_EFFORT',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeOtnApsProtectionModeEnum' : _MetaInfoEnum('MplsTeOtnApsProtectionModeEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'revertive':'REVERTIVE',
            'non-revertive':'NON_REVERTIVE',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTeSwitchingIndexEnum' : _MetaInfoEnum('MplsTeSwitchingIndexEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg',
        {
            'link':'LINK',
        }, 'Cisco-IOS-XR-mpls-te-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg']),
    'MplsTe.DiffServTrafficEngineering.Classes.Class' : {
        'meta_info' : _MetaInfoClass('MplsTe.DiffServTrafficEngineering.Classes.Class',
            False, 
            [
            _MetaInfoClassMember('class-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                DS-TE class number
                ''',
                'class_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('class-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Class type number
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Class-type priority
                ''',
                'class_priority',
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.DiffServTrafficEngineering.Classes' : {
        'meta_info' : _MetaInfoClass('MplsTe.DiffServTrafficEngineering.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.DiffServTrafficEngineering.Classes.Class', 
                [], [], 
                '''                DSTE class number
                ''',
                'class_',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.DiffServTrafficEngineering' : {
        'meta_info' : _MetaInfoClass('MplsTe.DiffServTrafficEngineering',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.DiffServTrafficEngineering.Classes', 
                [], [], 
                '''                Configure Diff-Serv Traffic-Engineering Classes
                ''',
                'classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-constraint-model', REFERENCE_ENUM_CLASS, 'BandwidthConstraintEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'BandwidthConstraintEnum', 
                [], [], 
                '''                Diff-Serv Traffic-Engineering Bandwidth
                Constraint Model
                ''',
                'bandwidth_constraint_model',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mode-ietf', REFERENCE_ENUM_CLASS, 'IetfModeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'IetfModeEnum', 
                [], [], 
                '''                Diff-Serv Traffic-Engineering IETF mode
                ''',
                'mode_ietf',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'diff-serv-traffic-engineering',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown',
            False, 
            [
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(5, 3600)], [], 
                '''                Minimum holddown (seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(5, 3600)], [], 
                '''                Maximum holddown (seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'holddown',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Timers.PathOptionTimers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Timers.PathOptionTimers',
            False, 
            [
            _MetaInfoClassMember('holddown', REFERENCE_CLASS, 'Holddown' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Timers',
            False, 
            [
            _MetaInfoClassMember('path-option-timers', REFERENCE_CLASS, 'PathOptionTimers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Timers.PathOptionTimers', 
                [], [], 
                '''                GMPLS-UNI path-option timer configuration
                ''',
                'path_option_timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption',
            False, 
            [
            _MetaInfoClassMember('preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Preference level for this path option
                ''',
                'preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsTePathOptionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionEnum', 
                [], [], 
                '''                The type of the path option
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
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
            _MetaInfoClassMember('xro-type', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The route-exclusion type
                ''',
                'xro_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The name of the XRO attribute set to be
                used for this path-option
                ''',
                'xro_attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lockdown', REFERENCE_ENUM_CLASS, 'MplsTePathOptionPropertyEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionPropertyEnum', 
                [], [], 
                '''                Path option properties: must be Lockdown
                ''',
                'lockdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('verbatim', REFERENCE_ENUM_CLASS, 'MplsTePathOptionPropertyEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionPropertyEnum', 
                [], [], 
                '''                Path option properties: must be verbatim
                if set
                ''',
                'verbatim',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signaled-label', REFERENCE_ENUM_CLASS, 'MplsTeSignaledLabelEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSignaledLabelEnum', 
                [], [], 
                '''                Signaled label type
                ''',
                'signaled_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dwdm-channel', ATTRIBUTE, 'int' , None, None, 
                [(1, 89)], [], 
                '''                DWDM channel number
                ''',
                'dwdm_channel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions',
            False, 
            [
            _MetaInfoClassMember('path-option', REFERENCE_LIST, 'PathOption' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption', 
                [], [], 
                '''                A Path-option
                ''',
                'path_option',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-options',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority',
            False, 
            [
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead',
            False, 
            [
            _MetaInfoClassMember('path-options', REFERENCE_CLASS, 'PathOptions' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions', 
                [], [], 
                '''                Path-option configuration
                ''',
                'path_options',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('recording', REFERENCE_CLASS, 'Recording' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording', 
                [], [], 
                '''                Tunnel property recording
                ''',
                'recording',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging', 
                [], [], 
                '''                Tunnel event logging
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                GMPLS-UNI head tunnel-id
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set link as a GMPLS tunnel head
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Set the destination of the tunnel
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority', 
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
            _MetaInfoClassMember('signalled-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 254)], [], 
                '''                The name of the tunnel to be included in
                signalling messages
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'gmpls-unitunnel-head',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('announce', REFERENCE_CLASS, 'Announce' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.Announce', 
                [], [], 
                '''                Announce discovered tunnel properties to
                system
                ''',
                'announce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('controller-logging', REFERENCE_CLASS, 'ControllerLogging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.ControllerLogging', 
                [], [], 
                '''                Controller logging
                ''',
                'controller_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('gmpls-unitunnel-head', REFERENCE_CLASS, 'GmplsUnitunnelHead' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead', 
                [], [], 
                '''                GMPLS-UNI tunnel-head properties
                ''',
                'gmpls_unitunnel_head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GMPLS-UNI on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni.Controllers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers.Controller', 
                [], [], 
                '''                Configure a GMPLS controller
                ''',
                'controller',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsUni' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsUni',
            False, 
            [
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Timers', 
                [], [], 
                '''                GMPLS-UNI timer configuration
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni.Controllers', 
                [], [], 
                '''                GMPLS-UNI controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'gmpls-uni',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelectionLooseAffinities.PathSelectionLooseAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelectionLooseAffinities.PathSelectionLooseAffinity',
            False, 
            [
            _MetaInfoClassMember('class-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Path Selection class Type
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection-loose-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelectionLooseAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelectionLooseAffinities',
            False, 
            [
            _MetaInfoClassMember('path-selection-loose-affinity', REFERENCE_LIST, 'PathSelectionLooseAffinity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelectionLooseAffinities.PathSelectionLooseAffinity', 
                [], [], 
                '''                Path selection Loose ERO Affinity
                configuration
                ''',
                'path_selection_loose_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection-loose-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Pcc' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Pcc',
            False, 
            [
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal',
            False, 
            [
            _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                [(0, 10080)], [], 
                '''                Auto-tunnel backup unused timeout in minutes
                (0=never timeout)
                ''',
                'unused',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'removal',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers',
            False, 
            [
            _MetaInfoClassMember('removal', REFERENCE_CLASS, 'Removal' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers', 
                [], [], 
                '''                Configure auto-tunnel backup timers value
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup',
            False, 
            [
            _MetaInfoClassMember('mesh-group-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Mesh group ID
                ''',
                'mesh_group_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('destination-list', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
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
            _MetaInfoClassMember('attribute-set', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups',
            False, 
            [
            _MetaInfoClassMember('mesh-group', REFERENCE_LIST, 'MeshGroup' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup', 
                [], [], 
                '''                Auto-mesh group identifier
                ''',
                'mesh_group',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mesh-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal',
            False, 
            [
            _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                [(0, 10080)], [], 
                '''                Auto-tunnel backup unused timeout in minutes
                (0=never timeout)
                ''',
                'unused',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'removal',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers',
            False, 
            [
            _MetaInfoClassMember('removal', REFERENCE_CLASS, 'Removal' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.Mesh' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.Mesh',
            False, 
            [
            _MetaInfoClassMember('mesh-groups', REFERENCE_CLASS, 'MeshGroups' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups', 
                [], [], 
                '''                Configure auto-tunnel mesh group
                ''',
                'mesh_groups',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers', 
                [], [], 
                '''                Configure auto-tunnel backup timers value
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange',
            False, 
            [
            _MetaInfoClassMember('min-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Minimum tunnel ID for auto-tunnels
                ''',
                'min_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('max-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Maximum tunnel ID for auto-tunnels
                ''',
                'max_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-range', REFERENCE_CLASS, 'TunnelRange' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AutoTunnel',
            False, 
            [
            _MetaInfoClassMember('pcc', REFERENCE_CLASS, 'Pcc' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Pcc', 
                [], [], 
                '''                Configure auto-tunnel PCC (Path Computation
                Client) feature
                ''',
                'pcc',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2p-auto-tunnel', REFERENCE_CLASS, 'P2PAutoTunnel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel', 
                [], [], 
                '''                Configure P2P auto-tunnel feature
                ''',
                'p2p_auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('backup', REFERENCE_CLASS, 'Backup' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Backup', 
                [], [], 
                '''                Configure auto-tunnel backup feature
                ''',
                'backup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mesh', REFERENCE_CLASS, 'Mesh' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.Mesh', 
                [], [], 
                '''                Configure auto-tunnel mesh feature
                ''',
                'mesh',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2mp-auto-tunnel', REFERENCE_CLASS, 'P2MpAutoTunnel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel', 
                [], [], 
                '''                Configure P2MP auto-tunnel feature
                ''',
                'p2mp_auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId',
            False, 
            [
            _MetaInfoClassMember('secondary-router-id-value', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary TE Router ID
                ''',
                'secondary_router_id_value',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'secondary-router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.SecondaryRouterIds' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.SecondaryRouterIds',
            False, 
            [
            _MetaInfoClassMember('secondary-router-id', REFERENCE_LIST, 'SecondaryRouterId' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId', 
                [], [], 
                '''                Secondary Router ID
                ''',
                'secondary_router_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'secondary-router-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Names.Name' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Names.Name',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                SRLG membership name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Administrative weight for the SRLG value
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Names' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Names',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Names.Name', 
                [], [], 
                '''                SRLG name and its MPLS-TE properties
                ''',
                'name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'names',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap',
            False, 
            [
            _MetaInfoClassMember('outgoing-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Outgoing v4 address
                ''',
                'outgoing_ipv4_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('remote-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote v4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ipv4-address-map',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-map', REFERENCE_LIST, 'Ipv4AddressMap' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values.Value' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values.Value',
            False, 
            [
            _MetaInfoClassMember('srlg-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                SRLG membership number
                ''',
                'srlg_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('ipv4-address-maps', REFERENCE_CLASS, 'Ipv4AddressMaps' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps', 
                [], [], 
                '''                Configure outgoing and remote link addresses
                for a given SRLG value
                ''',
                'ipv4_address_maps',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Administrative weight for the SRLG value
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'value',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg.Values' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg.Values',
            False, 
            [
            _MetaInfoClassMember('value', REFERENCE_LIST, 'Value' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values.Value', 
                [], [], 
                '''                SRLG value and its MPLS-TE properties
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'values',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Srlg' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Srlg',
            False, 
            [
            _MetaInfoClassMember('names', REFERENCE_CLASS, 'Names' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Names', 
                [], [], 
                '''                Configure SRLG identified by names
                ''',
                'names',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('values', REFERENCE_CLASS, 'Values' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg.Values', 
                [], [], 
                '''                Configure SRLG values and MPLS-TE properties
                ''',
                'values',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('default-admin-weight', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Queues.Queue' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Queues.Queue',
            False, 
            [
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'RoutePriorityRoleEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'RoutePriorityRoleEnum', 
                [], [], 
                '''                Route Priority Tunnel Role
                ''',
                'role',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [(0, 12)], [], 
                '''                Route priority queue value
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.Queues' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.Queues',
            False, 
            [
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Queues.Queue', 
                [], [], 
                '''                Configure route priority queue value
                ''',
                'queue',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'queues',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelectionLooseMetrics.PathSelectionLooseMetric' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelectionLooseMetrics.PathSelectionLooseMetric',
            False, 
            [
            _MetaInfoClassMember('class-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Path Selection class Type
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Metric to use for ERO Expansion
                ''',
                'metric_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection-loose-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelectionLooseMetrics' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelectionLooseMetrics',
            False, 
            [
            _MetaInfoClassMember('path-selection-loose-metric', REFERENCE_LIST, 'PathSelectionLooseMetric' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelectionLooseMetrics.PathSelectionLooseMetric', 
                [], [], 
                '''                Path selection Loose ERO Metric configuration
                ''',
                'path_selection_loose_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection-loose-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Class type for the bandwith allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation',
            False, 
            [
            _MetaInfoClassMember('path-invalidation-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 60000)], [], 
                '''                Path Invalidation Timeout
                ''',
                'path_invalidation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation-action', REFERENCE_ENUM_CLASS, 'PathInvalidationActionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'PathInvalidationActionEnum', 
                [], [], 
                '''                Path Invalidation Action
                ''',
                'path_invalidation_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('path-selection-exclude-list', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Path selection exclude list name
                configuration
                ''',
                'path_selection_exclude_list',
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
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-cost-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Path selection cost limit configuration for this
                specific tunnel
                ''',
                'path_selection_cost_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation', REFERENCE_CLASS, 'PathInvalidation' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation', 
                [], [], 
                '''                Path invalidation configuration for this
                specific tunnel
                ''',
                'path_invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes',
            False, 
            [
            _MetaInfoClassMember('path-option-attribute', REFERENCE_LIST, 'PathOptionAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute', 
                [], [], 
                '''                Path Option Attribute
                ''',
                'path_option_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority',
            False, 
            [
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Class type for the bandwith allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute',
            False, 
            [
            _MetaInfoClassMember('bandwidth-protection', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Bandwidth Protection
                ''',
                'bandwidth_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-protection', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Node Protection
                ''',
                'node_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging',
            False, 
            [
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel bandwidth change messages
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all events for a tunnel
                ''',
                'all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('sub-lsp-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel sub-LSP state messages
                ''',
                'sub_lsp_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel rereoute messages
                ''',
                'reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('interface-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bandwidth of the interface in kbps
                ''',
                'interface_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
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
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute', 
                [], [], 
                '''                Specify MPLS tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2mpte-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes',
            False, 
            [
            _MetaInfoClassMember('p2mpte-attribute', REFERENCE_LIST, 'P2MpteAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute', 
                [], [], 
                '''                P2MP-TE Tunnel Attribute
                ''',
                'p2mpte_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2mpte-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index',
            False, 
            [
            _MetaInfoClassMember('index-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Index number
                ''',
                'index_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('prepend-type', REFERENCE_ENUM_CLASS, 'SrPrependEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'SrPrependEnum', 
                [], [], 
                '''                Prepend type
                ''',
                'prepend_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'index',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes',
            False, 
            [
            _MetaInfoClassMember('index', REFERENCE_LIST, 'Index' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index', 
                [], [], 
                '''                Prepend index information
                ''',
                'index',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend',
            False, 
            [
            _MetaInfoClassMember('indexes', REFERENCE_CLASS, 'Indexes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes', 
                [], [], 
                '''                Segment routing prepend index table
                ''',
                'indexes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter path selection segment routing
                prepend submode
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'segment-routing-prepend',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation',
            False, 
            [
            _MetaInfoClassMember('invalidation-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 60000)], [], 
                '''                Path selection invalidation timer value
                (milliseconds)
                ''',
                'invalidation_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('invalidation-timer-expire-type', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionInvalidationTimerExpireEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionInvalidationTimerExpireEnum', 
                [], [], 
                '''                Path selection invalidation timer expire
                type
                ''',
                'invalidation_timer_expire_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection-invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection',
            False, 
            [
            _MetaInfoClassMember('segment-routing-prepend', REFERENCE_CLASS, 'SegmentRoutingPrepend' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend', 
                [], [], 
                '''                Path selection segment routing prepend
                configuration
                ''',
                'segment_routing_prepend',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-invalidation', REFERENCE_CLASS, 'PathSelectionInvalidation' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation', 
                [], [], 
                '''                Path selection invalidation configuration
                ''',
                'path_selection_invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter path selection configuration
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Path selection metric to use in path
                calculation
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-segment-routing-adjacency-protection', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum', 
                [], [], 
                '''                Segment routing adjacency protection type
                to use in path calculation
                ''',
                'path_selection_segment_routing_adjacency_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging',
            False, 
            [
            _MetaInfoClassMember('lsp-switch-over-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for bandwidth change
                ''',
                'lsp_switch_over_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all events for a tunnel
                ''',
                'all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel record-route messages
                ''',
                'record_route_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BFD session state change alarm
                ''',
                'bfd_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
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
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('path-selection', REFERENCE_CLASS, 'PathSelection' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection', 
                [], [], 
                '''                Configure path selection properties
                ''',
                'path_selection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'logging',
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
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2p-te-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes',
            False, 
            [
            _MetaInfoClassMember('p2p-te-attribute', REFERENCE_LIST, 'P2PTeAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute', 
                [], [], 
                '''                P2P-TE Tunnel Attribute
                ''',
                'p2p_te_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'p2p-te-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Signalled name
                ''',
                'name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('source-type', REFERENCE_ENUM_CLASS, 'MplsTeSigNameOptionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSigNameOptionEnum', 
                [], [], 
                '''                Source address or name
                ''',
                'source_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protected-interface-type', REFERENCE_ENUM_CLASS, 'MplsTeSigNameOptionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSigNameOptionEnum', 
                [], [], 
                '''                Protected-interface address or name
                ''',
                'protected_interface_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mp-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set if merge-point address is to be
                appended
                ''',
                'mp_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'signalled-name',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-backup-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority',
            False, 
            [
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses',
            False, 
            [
            _MetaInfoClassMember('policy-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(1, 8)], [], 
                '''                Array of Policy class
                ''',
                'policy_class',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=7),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'policy-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('signalled-name', REFERENCE_CLASS, 'SignalledName' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName', 
                [], [], 
                '''                Signalled name
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-backup-logging', REFERENCE_CLASS, 'AutoBackupLogging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'auto_backup_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
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
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('policy-classes', REFERENCE_CLASS, 'PolicyClasses' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses', 
                [], [], 
                '''                Policy classes for PBTS
                ''',
                'policy_classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-backup-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-backup-attribute', REFERENCE_LIST, 'AutoBackupAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute', 
                [], [], 
                '''                Auto-backup Tunnel Attribute
                ''',
                'auto_backup_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-backup-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode',
            False, 
            [
            _MetaInfoClassMember('connection-mode', REFERENCE_ENUM_CLASS, 'MplsTeOtnSncModeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnSncModeEnum', 
                [], [], 
                '''                The sub-network connection mode
                ''',
                'connection_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('connection-monitoring-mode', ATTRIBUTE, 'int' , None, None, 
                [(1, 6)], [], 
                '''                Tandem Connection Monitoring ID for the
                interface
                ''',
                'connection_monitoring_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'sub-network-connection-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers',
            False, 
            [
            _MetaInfoClassMember('aps-wait-to-restore', ATTRIBUTE, 'int' , None, None, 
                [(0, 720)], [], 
                '''                G.709 OTN path protection wait to restore
                timer in seconds
                ''',
                'aps_wait_to_restore',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('aps-hold-off', ATTRIBUTE, 'int' , None, None, 
                [(100, 10000)], [], 
                '''                G.709 OTN path protection hold-off timer in
                milliseconds
                ''',
                'aps_hold_off',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('sub-network-connection-mode', REFERENCE_CLASS, 'SubNetworkConnectionMode' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode', 
                [], [], 
                '''                Sub-network connection mode
                ''',
                'sub_network_connection_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers', 
                [], [], 
                '''                Timers
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('aps-protection-mode', REFERENCE_ENUM_CLASS, 'MplsTeOtnApsProtectionModeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnApsProtectionModeEnum', 
                [], [], 
                '''                The APS protecion mode
                ''',
                'aps_protection_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('aps-protection-type', REFERENCE_ENUM_CLASS, 'MplsTeOtnApsProtectionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeOtnApsProtectionEnum', 
                [], [], 
                '''                The APS protecion type
                ''',
                'aps_protection_type',
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
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'otn-pp-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes',
            False, 
            [
            _MetaInfoClassMember('otn-pp-attribute', REFERENCE_LIST, 'OtnPpAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute', 
                [], [], 
                '''                OTN Path Protection Attribute
                ''',
                'otn_pp_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'otn-pp-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
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
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-mesh-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority',
            False, 
            [
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDsteEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDsteEnum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Class type for the bandwith allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses',
            False, 
            [
            _MetaInfoClassMember('policy-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(1, 8)], [], 
                '''                Array of Policy class
                ''',
                'policy_class',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=7),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'policy-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinityEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinityEnum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute',
            False, 
            [
            _MetaInfoClassMember('bandwidth-protection', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Bandwidth Protection
                ''',
                'bandwidth_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-protection', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Node Protection
                ''',
                'node_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('auto-mesh-logging', REFERENCE_CLASS, 'AutoMeshLogging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging', 
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
            _MetaInfoClassMember('interface-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bandwidth of the interface in kbps
                ''',
                'interface_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [(1, 7)], [], 
                '''                Forward class value
                ''',
                'forward_class',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
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
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth', 
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
            _MetaInfoClassMember('policy-classes', REFERENCE_CLASS, 'PolicyClasses' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses', 
                [], [], 
                '''                Policy classes for PBTS
                ''',
                'policy_classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soft-preemption', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the soft-preemption feature on the tunnel
                ''',
                'soft_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute', 
                [], [], 
                '''                Specify MPLS tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('load-share', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Tunnel loadsharing metric
                ''',
                'load_share',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-mesh-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-mesh-attribute', REFERENCE_LIST, 'AutoMeshAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute', 
                [], [], 
                '''                Auto-mesh Tunnel Attribute
                ''',
                'auto_mesh_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-mesh-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg',
            False, 
            [
            _MetaInfoClassMember('srlg', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                SRLG
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('conformance', REFERENCE_ENUM_CLASS, 'MplsTePathDiversityConformanceEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathDiversityConformanceEnum', 
                [], [], 
                '''                The diversity conformance requirements
                ''',
                'conformance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs',
            False, 
            [
            _MetaInfoClassMember('srlg', REFERENCE_LIST, 'Srlg' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg', 
                [], [], 
                '''                SRLG-based path-diversity element
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlgs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel id
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel-id
                ''',
                'extended_tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP id
                ''',
                'lsp_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('conformance', REFERENCE_ENUM_CLASS, 'MplsTePathDiversityConformanceEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathDiversityConformanceEnum', 
                [], [], 
                '''                The diversity conformance requirements
                ''',
                'conformance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fec',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs',
            False, 
            [
            _MetaInfoClassMember('fec', REFERENCE_LIST, 'Fec' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp',
            False, 
            [
            _MetaInfoClassMember('fecs', REFERENCE_CLASS, 'Fecs' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs', 
                [], [], 
                '''                FEC LSP-based path diversity
                ''',
                'fecs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity',
            False, 
            [
            _MetaInfoClassMember('srlgs', REFERENCE_CLASS, 'Srlgs' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs', 
                [], [], 
                '''                SRLG-based path diversity
                ''',
                'srlgs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp', REFERENCE_CLASS, 'Lsp' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp', 
                [], [], 
                '''                LSP-based path diversity
                ''',
                'lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-diversity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute',
            False, 
            [
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('path-diversity', REFERENCE_CLASS, 'PathDiversity' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity', 
                [], [], 
                '''                Path diversity
                ''',
                'path_diversity',
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
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'xro-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet.XroAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet.XroAttributes',
            False, 
            [
            _MetaInfoClassMember('xro-attribute', REFERENCE_LIST, 'XroAttribute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute', 
                [], [], 
                '''                XRO Attribute
                ''',
                'xro_attribute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'xro-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AttributeSet' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AttributeSet',
            False, 
            [
            _MetaInfoClassMember('path-option-attributes', REFERENCE_CLASS, 'PathOptionAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes', 
                [], [], 
                '''                Path Option Attribute-Set Table
                ''',
                'path_option_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2mpte-attributes', REFERENCE_CLASS, 'P2MpteAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes', 
                [], [], 
                '''                P2MP-TE Tunnel AttributeSets Table
                ''',
                'p2mpte_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('p2p-te-attributes', REFERENCE_CLASS, 'P2PTeAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes', 
                [], [], 
                '''                P2P-TE Tunnel AttributeSets Table
                ''',
                'p2p_te_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-backup-attributes', REFERENCE_CLASS, 'AutoBackupAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes', 
                [], [], 
                '''                Auto-backup Tunnel Attribute Table
                ''',
                'auto_backup_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('otn-pp-attributes', REFERENCE_CLASS, 'OtnPpAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes', 
                [], [], 
                '''                OTN Path Protection Attributes table
                ''',
                'otn_pp_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-mesh-attributes', REFERENCE_CLASS, 'AutoMeshAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes', 
                [], [], 
                '''                Auto-mesh Tunnel AttributeSets Table
                ''',
                'auto_mesh_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('xro-attributes', REFERENCE_CLASS, 'XroAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet.XroAttributes', 
                [], [], 
                '''                XRO Tunnel Attributes table
                ''',
                'xro_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'attribute-set',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.BfdOverLsp.Tail' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.BfdOverLsp.Tail',
            False, 
            [
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 10)], [], 
                '''                Specify BFD over LSP tail multiplier
                ''',
                'multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [(100, 30000)], [], 
                '''                Specify BFD over LSP tail minimum interval
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tail',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.BfdOverLsp.Head' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.BfdOverLsp.Head',
            False, 
            [
            _MetaInfoClassMember('reopt-timeout', ATTRIBUTE, 'int' , None, None, 
                [(120, 4294967295)], [], 
                '''                BFD session down reopt timeout
                ''',
                'reopt_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down-action', REFERENCE_ENUM_CLASS, 'MplsTeBfdSessionDownActionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBfdSessionDownActionEnum', 
                [], [], 
                '''                Specify BFD session down action
                ''',
                'down_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'head',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.BfdOverLsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.BfdOverLsp',
            False, 
            [
            _MetaInfoClassMember('tail', REFERENCE_CLASS, 'Tail' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.BfdOverLsp.Tail', 
                [], [], 
                '''                BFD over LSP Tail Global Configurations
                ''',
                'tail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('head', REFERENCE_CLASS, 'Head' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.BfdOverLsp.Head', 
                [], [], 
                '''                BFD over LSP Head Global Configurations
                ''',
                'head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd-over-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers',
            False, 
            [
            _MetaInfoClassMember('redelegation-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 3600)], [], 
                '''                Timer for static tunnel redelegation in
                seconds, default is 180 seconds
                ''',
                'redelegation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 3600)], [], 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.PceStateful' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.PceStateful',
            False, 
            [
            _MetaInfoClassMember('stateful-timers', REFERENCE_CLASS, 'StatefulTimers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers', 
                [], [], 
                '''                Configure Stateful PCE (Path Computation
                Element) timers
                ''',
                'stateful_timers',
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
            _MetaInfoClassMember('report', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Report all statically configured tunnels
                ''',
                'report',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PCE stateful capability
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce-stateful',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('pce-peer-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                MD5 password
                ''',
                'password',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Precedence order
                ''',
                'precedence',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Peers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Peers.Peer', 
                [], [], 
                '''                PCE peer
                ''',
                'peer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes.Logging' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes.Logging',
            False, 
            [
            _MetaInfoClassMember('events', REFERENCE_CLASS, 'Events' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Logging.Events', 
                [], [], 
                '''                Configure logging events
                ''',
                'events',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PceAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PceAttributes',
            False, 
            [
            _MetaInfoClassMember('pce-stateful', REFERENCE_CLASS, 'PceStateful' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.PceStateful', 
                [], [], 
                '''                PCE Stateful
                ''',
                'pce_stateful',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Timer', 
                [], [], 
                '''                Configure PCE (Path Computation Element)
                timers
                ''',
                'timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Peers', 
                [], [], 
                '''                Configure PCE peers
                ''',
                'peers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes.Logging', 
                [], [], 
                '''                Configure PCE (Path Computation Element)
                logging feature
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('request-timeout', ATTRIBUTE, 'int' , None, None, 
                [(5, 100)], [], 
                '''                Request timeout value in seconds
                ''',
                'request_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-period', ATTRIBUTE, 'int' , None, None, 
                [(60, 604800)], [], 
                '''                PCE reoptimization period for PCE-based paths
                ''',
                'reoptimize_period',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of this PCE
                ''',
                'address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('deadtimer', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Deadtimer interval in seconds
                ''',
                'deadtimer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keepalive', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Keepalive interval in seconds
                ''',
                'keepalive',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keepalive-tolerance', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Keepalive interval tolerance in seconds
                ''',
                'keepalive_tolerance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('peer-source-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCE Peer Source Address
                ''',
                'peer_source_addr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('speaker-entity-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                PCE speaker entity identifier
                ''',
                'speaker_entity_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                MD5 password
                ''',
                'password',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Precedence order
                ''',
                'precedence',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.SoftPreemption' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.SoftPreemption',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 300)], [], 
                '''                This object sets the timeout in seconds before
                hard preemption is triggered.
                ''',
                'timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('frr-rewrite', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object controls whether FRR rewrite
                during soft preemption is enabled.
                ''',
                'frr_rewrite',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object controls whether soft preemption
                is enabled. This object must be set before
                setting any other objects under the
                SoftPreemption class.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'soft-preemption',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathInvalidation' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathInvalidation',
            False, 
            [
            _MetaInfoClassMember('path-invalidation-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 60000)], [], 
                '''                Path Invalidation Timeout
                ''',
                'path_invalidation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation-action', REFERENCE_ENUM_CLASS, 'PathInvalidationActionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'PathInvalidationActionEnum', 
                [], [], 
                '''                Path Invalidation Action
                ''',
                'path_invalidation_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.FastReroute.Timers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.FastReroute.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-backup', ATTRIBUTE, 'int' , None, None, 
                [(0, 604800)], [], 
                '''                Seconds before backup declared UP (0 disables
                hold-timer)
                ''',
                'hold_backup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('promotion', ATTRIBUTE, 'int' , None, None, 
                [(0, 604800)], [], 
                '''                The value of the promotion timer in seconds
                ''',
                'promotion',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.FastReroute' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.FastReroute',
            False, 
            [
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.FastReroute.Timers', 
                [], [], 
                '''                Configure fast reroute timers
                ''',
                'timers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole',
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
            'path-selection-ignore-overload-role',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Affinity Name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('value-type', REFERENCE_ENUM_CLASS, 'MplsTeAffinityValueEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeAffinityValueEnum', 
                [], [], 
                '''                Affinity value type
                ''',
                'value_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity Value in Hex number or by Bit
                position
                ''',
                'value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes.AffinityMappings' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes.AffinityMappings',
            False, 
            [
            _MetaInfoClassMember('affinity-mapping', REFERENCE_LIST, 'AffinityMapping' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping', 
                [], [], 
                '''                Affinity Mapping configuration
                ''',
                'affinity_mapping',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GlobalAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.GlobalAttributes',
            False, 
            [
            _MetaInfoClassMember('path-selection-loose-affinities', REFERENCE_CLASS, 'PathSelectionLooseAffinities' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelectionLooseAffinities', 
                [], [], 
                '''                Path selection Loose ERO Affinity Class
                configuration
                ''',
                'path_selection_loose_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-tunnel', REFERENCE_CLASS, 'AutoTunnel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AutoTunnel', 
                [], [], 
                '''                Configure auto-tunnels feature
                ''',
                'auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('secondary-router-ids', REFERENCE_CLASS, 'SecondaryRouterIds' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.SecondaryRouterIds', 
                [], [], 
                '''                Configure MPLS TE Secondary Router ID
                ''',
                'secondary_router_ids',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('srlg', REFERENCE_CLASS, 'Srlg' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Srlg', 
                [], [], 
                '''                Configure SRLG values and MPLS-TE properties
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('queues', REFERENCE_CLASS, 'Queues' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Queues', 
                [], [], 
                '''                Configure MPLS TE route priority
                ''',
                'queues',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-loose-metrics', REFERENCE_CLASS, 'PathSelectionLooseMetrics' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelectionLooseMetrics', 
                [], [], 
                '''                Path selection Loose ERO Metric Class
                configuration
                ''',
                'path_selection_loose_metrics',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mib', REFERENCE_CLASS, 'Mib' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.Mib', 
                [], [], 
                '''                MPLS-TE MIB properties
                ''',
                'mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-set', REFERENCE_CLASS, 'AttributeSet' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AttributeSet', 
                [], [], 
                '''                Attribute AttributeSets
                ''',
                'attribute_set',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-over-lsp', REFERENCE_CLASS, 'BfdOverLsp' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.BfdOverLsp', 
                [], [], 
                '''                BFD over MPLS TE Global Configurations
                ''',
                'bfd_over_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce-attributes', REFERENCE_CLASS, 'PceAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PceAttributes', 
                [], [], 
                '''                Configuration MPLS TE PCE attributes
                ''',
                'pce_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soft-preemption', REFERENCE_CLASS, 'SoftPreemption' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.SoftPreemption', 
                [], [], 
                '''                Soft preemption configuration data
                ''',
                'soft_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation', REFERENCE_CLASS, 'PathInvalidation' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathInvalidation', 
                [], [], 
                '''                Path invalidation configuration for all tunnels
                ''',
                'path_invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.FastReroute', 
                [], [], 
                '''                Configure fast reroute attributes
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-ignore-overload-role', REFERENCE_CLASS, 'PathSelectionIgnoreOverloadRole' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole', 
                [], [], 
                '''                Path selection to ignore overload node during
                CSPF
                ''',
                'path_selection_ignore_overload_role',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('affinity-mappings', REFERENCE_CLASS, 'AffinityMappings' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes.AffinityMappings', 
                [], [], 
                '''                Affinity Mapping Table configuration
                ''',
                'affinity_mappings',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-nsr-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log NSR status messages
                ''',
                'log_nsr_status',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-tiebreaker', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionTiebreakerEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionTiebreakerEnum', 
                [], [], 
                '''                CSPF tiebreaker to use in path calculation
                ''',
                'path_selection_tiebreaker',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-issu-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log ISSU status messages
                ''',
                'log_issu_status',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-link-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable reoptimization based on link-up events
                ''',
                'reoptimize_link_up',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-cleanup-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 300)], [], 
                '''                Reoptimization Delay Cleanup Value (seconds)
                ''',
                'reoptimize_delay_cleanup_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('disable-reoptimize-affinity-failure', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable reoptimization after affinity failures
                ''',
                'disable_reoptimize_affinity_failure',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('maximum-tunnels', ATTRIBUTE, 'int' , None, None, 
                [(1, 65536)], [], 
                '''                The maximum number of tunnel heads that will be
                allowed.
                ''',
                'maximum_tunnels',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('link-holddown-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 300)], [], 
                '''                Holddown time for links which had Path Errors
                in seconds
                ''',
                'link_holddown_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetricEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetricEnum', 
                [], [], 
                '''                Metric to use in path calculation
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault-oam', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Fault-OAM functionality for
                bidirectional tunnels
                ''',
                'fault_oam',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable-unequal-load-balancing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable unequal load-balancing over tunnels to
                the same destination
                ''',
                'enable_unequal_load_balancing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-tail', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tail tunnel events
                ''',
                'log_tail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-after-frr-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 120)], [], 
                '''                Reoptimization Delay After FRR Value (seconds)
                ''',
                'reoptimize_delay_after_frr_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-bandwidth-collect-frequency', ATTRIBUTE, 'int' , None, None, 
                [(1, 10080)], [], 
                '''                Auto-bandwidth global collection frequency in
                minutes
                ''',
                'auto_bandwidth_collect_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reopt-delay-path-protect-switchover-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 604800)], [], 
                '''                Seconds between path protect switchover and
                tunnel re-optimization. Set to 0 to disable
                ''',
                'reopt_delay_path_protect_switchover_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'log_all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('loose-path-retry-period', ATTRIBUTE, 'int' , None, None, 
                [(30, 600)], [], 
                '''                Signalling retry for tunnels terminating
                outside the headend area
                ''',
                'loose_path_retry_period',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-load-balancing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Load balance bandwidth during reoptimization
                ''',
                'reoptimize_load_balancing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-head', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all head tunnel events
                ''',
                'log_head',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-ignore-overload', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Deprecated - do not use
                ''',
                'path_selection_ignore_overload',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('graceful-preemption-on-bandwidth-reduction', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable graceful preemption when there is a
                bandwidth reduction
                ''',
                'graceful_preemption_on_bandwidth_reduction',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('advertise-explicit-nulls', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable explicit-null advertising to PHOP
                ''',
                'advertise_explicit_nulls',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-install-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 3600)], [], 
                '''                Reoptimization Delay Install Value (seconds)
                ''',
                'reoptimize_delay_install_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-delay-after-affinity-failure-timer', ATTRIBUTE, 'int' , None, None, 
                [(1, 604800)], [], 
                '''                Delay reoptimizing current LSP after affinity
                failures
                ''',
                'reoptimize_delay_after_affinity_failure_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-frr-protection', REFERENCE_ENUM_CLASS, 'MplsTeLogFrrProtectionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeLogFrrProtectionEnum', 
                [], [], 
                '''                Log FRR Protection messages
                ''',
                'log_frr_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-timer-frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 604800)], [], 
                '''                Reoptimize timers period in seconds
                ''',
                'reoptimize_timer_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-mid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all mid tunnel events
                ''',
                'log_mid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('log-preemption', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel preemption messages
                ''',
                'log_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-cost-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Path selection cost limit configuration for all
                tunnels
                ''',
                'path_selection_cost_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'global-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Fault.ProtectionTrigger' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Fault.ProtectionTrigger',
            False, 
            [
            _MetaInfoClassMember('ldi', REFERENCE_CLASS, 'Ldi' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi', 
                [], [], 
                '''                Protection switching due to LDI event
                ''',
                'ldi',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lkr', REFERENCE_CLASS, 'Lkr' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr', 
                [], [], 
                '''                Protection switching due to LKR event
                ''',
                'lkr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ais', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable protection switching due to AIS event
                ''',
                'ais',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'protection-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Fault' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Fault',
            False, 
            [
            _MetaInfoClassMember('protection-trigger', REFERENCE_CLASS, 'ProtectionTrigger' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault.ProtectionTrigger', 
                [], [], 
                '''                OAM events that trigger protection switching
                ''',
                'protection_trigger',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('wait-to-restore-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Waiting time before restoring working LSP
                ''',
                'wait_to_restore_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('refresh-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 20)], [], 
                '''                Periodic refresh interval for fault OAM
                messages
                ''',
                'refresh_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fault',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Alarm' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Alarm',
            False, 
            [
            _MetaInfoClassMember('suppress-event', REFERENCE_CLASS, 'SuppressEvent' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Alarm.SuppressEvent', 
                [], [], 
                '''                Suppress all tunnel/LSP alarms
                ''',
                'suppress_event',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soak-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 10)], [], 
                '''                Duration of soaking alarms
                ''',
                'soak_time',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable-alarm', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Transport Profile Alarm
                ''',
                'enable_alarm',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'alarm',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Bfd.MinIntervalStandby' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Bfd.MinIntervalStandby',
            False, 
            [
            _MetaInfoClassMember('interval-standby-ms', ATTRIBUTE, 'int' , None, None, 
                [(3, 5000)], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval_standby_ms',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval-standby-us', ATTRIBUTE, 'int' , None, None, 
                [(3000, 5000000)], [], 
                '''                Hello interval in micro-seconds
                ''',
                'interval_standby_us',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'min-interval-standby',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Bfd.MinInterval' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Bfd.MinInterval',
            False, 
            [
            _MetaInfoClassMember('interval-ms', ATTRIBUTE, 'int' , None, None, 
                [(3, 5000)], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval_ms',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval-us', ATTRIBUTE, 'int' , None, None, 
                [(3000, 5000000)], [], 
                '''                Hello interval in micro-seconds
                ''',
                'interval_us',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'min-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Bfd' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Bfd',
            False, 
            [
            _MetaInfoClassMember('min-interval-standby', REFERENCE_CLASS, 'MinIntervalStandby' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Bfd.MinIntervalStandby', 
                [], [], 
                '''                Hello interval for standby transport profile
                LSPs, either in milli-seconds or in
                micro-seconds
                ''',
                'min_interval_standby',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-interval', REFERENCE_CLASS, 'MinInterval' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Bfd.MinInterval', 
                [], [], 
                '''                Hello interval, either in milli-seconds or in
                micro-seconds
                ''',
                'min_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('detection-multiplier-standby', ATTRIBUTE, 'int' , None, None, 
                [(2, 10)], [], 
                '''                Detect multiplier for standby transport
                profile LSP
                ''',
                'detection_multiplier_standby',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 10)], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.Source' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.Source',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel identifier in numeric value
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Global identifier in numeric value
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'source',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.Destination' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.Destination',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel identifier in numeric value
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Global identifier in numeric value
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 4015)], [], 
                '''                MPLS label
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                Outgoing MPLS label
                ''',
                'out_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-link', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Transport profile identifier of outgoing
                link
                ''',
                'out_link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'forward-io-map',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp',
            False, 
            [
            _MetaInfoClassMember('forward-io-map', REFERENCE_CLASS, 'ForwardIoMap' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap', 
                [], [], 
                '''                Label cross-connect of forward transport
                profile LSP
                ''',
                'forward_io_map',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Bandwidth of forward transport profile LSP
                ''',
                'forward_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'forward-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 4015)], [], 
                '''                MPLS label
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                Outgoing MPLS label
                ''',
                'out_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-link', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Transport profile identifier of outgoing
                link
                ''',
                'out_link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'reverse-io-map',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp',
            False, 
            [
            _MetaInfoClassMember('reverse-io-map', REFERENCE_CLASS, 'ReverseIoMap' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap', 
                [], [], 
                '''                Label cross-connect of reverse transport
                profile LSP
                ''',
                'reverse_io_map',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reverse-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Bandwidth of reverse transport profile LSP
                ''',
                'reverse_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'reverse-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints.Midpoint' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints.Midpoint',
            False, 
            [
            _MetaInfoClassMember('midpoint-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of mid-point
                ''',
                'midpoint_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.Source', 
                [], [], 
                '''                Node identifier, tunnel identifier and
                optional global identifier of the source of
                the LSP
                ''',
                'source',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.Destination', 
                [], [], 
                '''                Node identifier, tunnel identifier and
                optional global identifier of the destination
                of the LSP
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-lsp', REFERENCE_CLASS, 'ForwardLsp' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp', 
                [], [], 
                '''                Forward transport profile LSP
                ''',
                'forward_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reverse-lsp', REFERENCE_CLASS, 'ReverseLsp' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp', 
                [], [], 
                '''                none
                ''',
                'reverse_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel Name
                ''',
                'tunnel_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-protect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable LSP protection
                ''',
                'lsp_protect',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Numeric identifier
                ''',
                'lsp_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile.Midpoints' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile.Midpoints',
            False, 
            [
            _MetaInfoClassMember('midpoint', REFERENCE_LIST, 'Midpoint' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints.Midpoint', 
                [], [], 
                '''                Transport profile mid-point identifier
                ''',
                'midpoint',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'midpoints',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.TransportProfile' : {
        'meta_info' : _MetaInfoClass('MplsTe.TransportProfile',
            False, 
            [
            _MetaInfoClassMember('fault', REFERENCE_CLASS, 'Fault' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Fault', 
                [], [], 
                '''                Fault management
                ''',
                'fault',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('alarm', REFERENCE_CLASS, 'Alarm' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Alarm', 
                [], [], 
                '''                Alarm management
                ''',
                'alarm',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('midpoints', REFERENCE_CLASS, 'Midpoints' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile.Midpoints', 
                [], [], 
                '''                MPLS-TP tunnel mid-point table
                ''',
                'midpoints',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Transport profile global identifier
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'transport-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link',
            False, 
            [
            _MetaInfoClassMember('link-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Numeric link identifier
                ''',
                'link_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('next-hop-type', REFERENCE_ENUM_CLASS, 'LinkNextHopEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'LinkNextHopEnum', 
                [], [], 
                '''                Next hop type
                ''',
                'next_hop_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop address in IPv4 format
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'link',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.TransportProfileLink.Links' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.TransportProfileLink.Links',
            False, 
            [
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link', 
                [], [], 
                '''                Transport profile link
                ''',
                'link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'links',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.TransportProfileLink' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.TransportProfileLink',
            False, 
            [
            _MetaInfoClassMember('links', REFERENCE_CLASS, 'Links' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.TransportProfileLink.Links', 
                [], [], 
                '''                Transport profile link table
                ''',
                'links',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'transport-profile-link',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
                    _MetaInfoClassMember('switching-id', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingIndexEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingIndexEnum', 
                        [], [], 
                        '''                        Switching index
                        ''',
                        'switching_id',
                        'Cisco-IOS-XR-mpls-te-cfg', True),
                    _MetaInfoClassMember('switching-id', ATTRIBUTE, 'int' , None, None, 
                        [(1, 255)], [], 
                        '''                        Switching index
                        ''',
                        'switching_id',
                        'Cisco-IOS-XR-mpls-te-cfg', True),
                ]),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingEncodingEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingEncodingEnum', 
                [], [], 
                '''                Set the local encoding type
                ''',
                'encoding',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('capability', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingCapEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingCapEnum', 
                [], [], 
                '''                Set the local switching capability
                ''',
                'capability',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'switching',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Switchings' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Switchings',
            False, 
            [
            _MetaInfoClassMember('switching', REFERENCE_LIST, 'Switching' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Switchings.Switching', 
                [], [], 
                '''                The te-link switching attributes
                ''',
                'switching',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'switchings',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.FloodArea' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.FloodArea',
            False, 
            [
            _MetaInfoClassMember('igp-type', REFERENCE_ENUM_CLASS, 'MplsLcacFloodingIgpEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsLcacFloodingIgpEnum', 
                [], [], 
                '''                IGP type
                ''',
                'igp_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Area ID
                ''',
                'area_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'flood-area',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName',
            False, 
            [
            _MetaInfoClassMember('affinity-index', ATTRIBUTE, 'int' , None, None, 
                [(1, 9)], [], 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.AttributeNames' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.AttributeNames',
            False, 
            [
            _MetaInfoClassMember('attribute-name', REFERENCE_LIST, 'AttributeName' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName', 
                [], [], 
                '''                Set the interface attribute names
                ''',
                'attribute_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'attribute-names',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg',
            False, 
            [
            _MetaInfoClassMember('srlg-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                SRLG membership number
                ''',
                'srlg_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.Srlgs' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.Srlgs',
            False, 
            [
            _MetaInfoClassMember('srlg', REFERENCE_LIST, 'Srlg' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg', 
                [], [], 
                '''                SRLG membership number
                ''',
                'srlg',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'srlgs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.UpThresholds' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.UpThresholds',
            False, 
            [
            _MetaInfoClassMember('up-threshold', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Array of up threshold percentage
                ''',
                'up_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=14),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'up-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac.DownThresholds' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac.DownThresholds',
            False, 
            [
            _MetaInfoClassMember('down-threshold', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Array of down threshold percentage
                ''',
                'down_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=14),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'down-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.Lcac' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.Lcac',
            False, 
            [
            _MetaInfoClassMember('switchings', REFERENCE_CLASS, 'Switchings' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Switchings', 
                [], [], 
                '''                Set the te-link switching attributes
                ''',
                'switchings',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('flood-area', REFERENCE_CLASS, 'FloodArea' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.FloodArea', 
                [], [], 
                '''                Set the IGP instance into which this
                interface is to be flooded (GMPLS only)
                ''',
                'flood_area',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-name-xr', REFERENCE_CLASS, 'AttributeNameXr' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.AttributeNameXr', 
                [], [], 
                '''                Set the interface attribute names
                ''',
                'attribute_name_xr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-names', REFERENCE_CLASS, 'AttributeNames' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.AttributeNames', 
                [], [], 
                '''                Attribute name table
                ''',
                'attribute_names',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('srlgs', REFERENCE_CLASS, 'Srlgs' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.Srlgs', 
                [], [], 
                '''                Configure SRLG membership for the interface
                ''',
                'srlgs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('up-thresholds', REFERENCE_CLASS, 'UpThresholds' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.UpThresholds', 
                [], [], 
                '''                Set thresholds for increased resource
                availability in %
                ''',
                'up_thresholds',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down-thresholds', REFERENCE_CLASS, 'DownThresholds' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac.DownThresholds', 
                [], [], 
                '''                Set thresholds for decreased resource
                availability in %
                ''',
                'down_thresholds',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault-oam-lockout', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Lockout protection on the interface for Flex
                LSP
                ''',
                'fault_oam_lockout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-flags', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Set user defined interface attribute flags
                ''',
                'attribute_flags',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS-TE on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set administrative weight for the interface
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lcac',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude',
            False, 
            [
            _MetaInfoClassMember('srlg-mode', REFERENCE_ENUM_CLASS, 'MplsTesrlgExcludeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTesrlgExcludeEnum', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup',
            False, 
            [
            _MetaInfoClassMember('exclude', REFERENCE_CLASS, 'Exclude' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude', 
                [], [], 
                '''                Auto-tunnel backup exclusion criteria
                ''',
                'exclude',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable auto-tunnel backup on this TE link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('attribute-set', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The name of attribute set to be applied to
                this auto backup lsp
                ''',
                'attribute_set',
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel',
            False, 
            [
            _MetaInfoClassMember('backup', REFERENCE_CLASS, 'Backup' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup', 
                [], [], 
                '''                Auto tunnel backup configuration
                ''',
                'backup',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath',
            False, 
            [
            _MetaInfoClassMember('tunnel-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel interface number
                ''',
                'tunnel_number',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths',
            False, 
            [
            _MetaInfoClassMember('backup-path', REFERENCE_LIST, 'BackupPath' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath', 
                [], [], 
                '''                Tunnel interface number
                ''',
                'backup_path',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface.GlobalAttributes' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface.GlobalAttributes',
            False, 
            [
            _MetaInfoClassMember('auto-tunnel', REFERENCE_CLASS, 'AutoTunnel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel', 
                [], [], 
                '''                Auto tunnel configuration
                ''',
                'auto_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('backup-paths', REFERENCE_CLASS, 'BackupPaths' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths', 
                [], [], 
                '''                Configure MPLS TE backup tunnels for this
                interface
                ''',
                'backup_paths',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'global-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('transport-profile-link', REFERENCE_CLASS, 'TransportProfileLink' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.TransportProfileLink', 
                [], [], 
                '''                MPLS transport profile capable link
                ''',
                'transport_profile_link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lcac', REFERENCE_CLASS, 'Lcac' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.Lcac', 
                [], [], 
                '''                LCAC specific MPLS interface configuration
                ''',
                'lcac',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-attributes', REFERENCE_CLASS, 'GlobalAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface.GlobalAttributes', 
                [], [], 
                '''                MPLS TE global interface configuration
                ''',
                'global_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsTe.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces.Interface', 
                [], [], 
                '''                Configure an MPLS TE interface
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode',
            False, 
            [
            _MetaInfoClassMember('tti-mode-type', REFERENCE_ENUM_CLASS, 'GmplsttiModeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'GmplsttiModeEnum', 
                [], [], 
                '''                Type of Trail Trace Identifier
                ''',
                'tti_mode_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tcmid', ATTRIBUTE, 'int' , None, None, 
                [(1, 6)], [], 
                '''                Tandem Connection Monitoring ID for the
                interface
                ''',
                'tcmid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tti-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('tti-mode', REFERENCE_CLASS, 'TtiMode' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode', 
                [], [], 
                '''                Set tandem connection monitoring for the
                interface
                ''',
                'tti_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Set administrative weight for the
                interface
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GMPLS-NNI on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller', 
                [], [], 
                '''                Configure a GMPLS NNI controller
                ''',
                'controller',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt',
            False, 
            [
            _MetaInfoClassMember('igp-area', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                IGP area
                ''',
                'igp_area',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers', 
                [], [], 
                '''                GMPLS-NNI controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ospf-int',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode',
            False, 
            [
            _MetaInfoClassMember('tti-mode-type', REFERENCE_ENUM_CLASS, 'GmplsttiModeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'GmplsttiModeEnum', 
                [], [], 
                '''                Type of Trail Trace Identifier
                ''',
                'tti_mode_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tcmid', ATTRIBUTE, 'int' , None, None, 
                [(1, 6)], [], 
                '''                Tandem Connection Monitoring ID for the
                interface
                ''',
                'tcmid',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tti-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('tti-mode', REFERENCE_CLASS, 'TtiMode' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode', 
                [], [], 
                '''                Set tandem connection monitoring for the
                interface
                ''',
                'tti_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Set administrative weight for the
                interface
                ''',
                'admin_weight',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GMPLS-NNI on the link
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller', 
                [], [], 
                '''                Configure a GMPLS NNI controller
                ''',
                'controller',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID if in IP address format
                ''',
                'address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers', 
                [], [], 
                '''                GMPLS-NNI controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'ospfip-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances.TopologyInstance' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances.TopologyInstance',
            False, 
            [
            _MetaInfoClassMember('igp-type', REFERENCE_ENUM_CLASS, 'MplsTeIgpProtocolEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeIgpProtocolEnum', 
                [], [], 
                '''                IGP type
                ''',
                'igp_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('igp-instance-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 40)], [], 
                '''                Name of IGP instance
                ''',
                'igp_instance_name',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('ospf-area-type', REFERENCE_ENUM_CLASS, 'OspfAreaModeEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OspfAreaModeEnum', 
                [], [], 
                '''                OSPF area format
                ''',
                'ospf_area_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('ospf-int', REFERENCE_LIST, 'OspfInt' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt', 
                [], [], 
                '''                ospf int
                ''',
                'ospf_int',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ospfip-addr', REFERENCE_LIST, 'OspfipAddr' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr', 
                [], [], 
                '''                ospfip addr
                ''',
                'ospfip_addr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'topology-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TopologyInstances' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TopologyInstances',
            False, 
            [
            _MetaInfoClassMember('topology-instance', REFERENCE_LIST, 'TopologyInstance' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances.TopologyInstance', 
                [], [], 
                '''                GMPLS-NNI topology instance configuration
                ''',
                'topology_instance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'topology-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth',
            False, 
            [
            _MetaInfoClassMember('signalled-bandwidth-type', REFERENCE_ENUM_CLASS, 'OtnSignaledBandwidthEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OtnSignaledBandwidthEnum', 
                [], [], 
                '''                The g.709 signal type requested
                ''',
                'signalled_bandwidth_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bitrate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Bitrate value in Kbps for ODUflex framing
                type
                ''',
                'bitrate',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('od-uflex-framing-type', REFERENCE_ENUM_CLASS, 'OtnSignaledBandwidthFlexFramingEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OtnSignaledBandwidthFlexFramingEnum', 
                [], [], 
                '''                Framing type in case of ODUflex signal type
                ''',
                'od_uflex_framing_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'signalled-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 tunnel destination
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-type', REFERENCE_ENUM_CLASS, 'OtnDestinationEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OtnDestinationEnum', 
                [], [], 
                '''                Destination type whether it is unicast or
                unnumbered
                ''',
                'destination_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interface-if-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Interface index of port
                ''',
                'interface_if_index',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
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
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient
                bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption',
            False, 
            [
            _MetaInfoClassMember('preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Preference level for this path option
                ''',
                'preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsTePathOptionEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionEnum', 
                [], [], 
                '''                The type of the path option
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
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
            _MetaInfoClassMember('protected-by-preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1001)], [], 
                '''                Preference level of the protecting explicit
                path. 
                ''',
                'protected_by_preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('restore-by-preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Preference level of the restore path. 
                ''',
                'restore_by_preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lockdown', REFERENCE_ENUM_CLASS, 'MplsTePathOptionPropertyEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionPropertyEnum', 
                [], [], 
                '''                Lockdown properties
                ''',
                'lockdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions',
            False, 
            [
            _MetaInfoClassMember('path-option', REFERENCE_LIST, 'PathOption' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni',
            False, 
            [
            _MetaInfoClassMember('ingress-controller-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Name of  ingress controller
                ''',
                'ingress_controller_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('egress-controller-if-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Interface index of Egress controller
                ''',
                'egress_controller_if_index',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ingress-type', REFERENCE_ENUM_CLASS, 'OtnStaticUniEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OtnStaticUniEnum', 
                [], [], 
                '''                Ingress type whether it is xconnect or
                terminated
                ''',
                'ingress_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('egress-type', REFERENCE_ENUM_CLASS, 'OtnStaticUniEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OtnStaticUniEnum', 
                [], [], 
                '''                Egress type whether it is xconnect or
                terminated
                ''',
                'egress_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'static-uni',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads.TunnelHead' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads.TunnelHead',
            False, 
            [
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('signalled-bandwidth', REFERENCE_CLASS, 'SignalledBandwidth' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth', 
                [], [], 
                '''                The existence of this configuration indicates
                the signalled bandwidth has been set for the
                tunnel
                ''',
                'signalled_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination', 
                [], [], 
                '''                The existence of this configuration indicates
                the destination has been set for the tunnel
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging', 
                [], [], 
                '''                Tunnel event logging
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-options', REFERENCE_CLASS, 'PathOptions' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions', 
                [], [], 
                '''                GMPLS NNI path options
                ''',
                'path_options',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('static-uni', REFERENCE_CLASS, 'StaticUni' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni', 
                [], [], 
                '''                The existence of this configuration indicates
                the static UNI endpoints have been set for
                the tunnel
                ''',
                'static_uni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the a new GMPLS NNI tunnel has been enabled
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('restore-lsp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the restore LSP of tunnel is shutdown
                ''',
                'restore_lsp_shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('current-lsp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the current/working LSP of tunnel is shutdown
                ''',
                'current_lsp_shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('payload', REFERENCE_ENUM_CLASS, 'OtnPayloadEnum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'OtnPayloadEnum', 
                [], [], 
                '''                The existence of this configuration indicates
                the Payload type have been set for the tunnel
                ''',
                'payload',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('standby-lsp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the standby/protect LSP of tunnel is shutdown
                ''',
                'standby_lsp_shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the tunnel is shutdown
                ''',
                'shutdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-protection-attribute-set-profile', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The name of the path-protection profile to be
                included in signalling messages
                ''',
                'path_protection_attribute_set_profile',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 254)], [], 
                '''                The name of the tunnel to be included in
                signalling messages
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-head',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni.TunnelHeads' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni.TunnelHeads',
            False, 
            [
            _MetaInfoClassMember('tunnel-head', REFERENCE_LIST, 'TunnelHead' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads.TunnelHead', 
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
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.GmplsNni' : {
        'meta_info' : _MetaInfoClass('MplsTe.GmplsNni',
            False, 
            [
            _MetaInfoClassMember('topology-instances', REFERENCE_CLASS, 'TopologyInstances' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TopologyInstances', 
                [], [], 
                '''                GMPLS-NNI topology instance table
                ''',
                'topology_instances',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-heads', REFERENCE_CLASS, 'TunnelHeads' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni.TunnelHeads', 
                [], [], 
                '''                GMPLS-NNI tunnel-head table
                ''',
                'tunnel_heads',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable-gmpls-nni', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS Traffic Engineering GMPLS-NNI
                ''',
                'enable_gmpls_nni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'gmpls-nni',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Lcac.Bfd' : {
        'meta_info' : _MetaInfoClass('MplsTe.Lcac.Bfd',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(15, 200)], [], 
                '''                Hello interval for BFD sessions created by TE
                ''',
                'interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 10)], [], 
                '''                Detection multiplier for BFD sessions created
                by TE
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Lcac.FloodingThreshold' : {
        'meta_info' : _MetaInfoClass('MplsTe.Lcac.FloodingThreshold',
            False, 
            [
            _MetaInfoClassMember('up-stream', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Upward flooding Threshold in percentages of
                total bandwidth
                ''',
                'up_stream',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down-stream', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Downward flooding Threshold in percentages of
                total bandwidth
                ''',
                'down_stream',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'flooding-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe.Lcac' : {
        'meta_info' : _MetaInfoClass('MplsTe.Lcac',
            False, 
            [
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Lcac.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('flooding-threshold', REFERENCE_CLASS, 'FloodingThreshold' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Lcac.FloodingThreshold', 
                [], [], 
                '''                Configure flooding threshold as percentage of
                total link bandwidth.
                ''',
                'flooding_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-hold-timer', ATTRIBUTE, 'int' , None, None, 
                [(1, 300)], [], 
                '''                Bandwidth hold timer value (seconds)
                ''',
                'bandwidth_hold_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('delay-preempt-bundle-capacity-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 300)], [], 
                '''                Bundle capacity preemption timer value
                (seconds)
                ''',
                'delay_preempt_bundle_capacity_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('periodic-flooding-timer', ATTRIBUTE, 'int' , None, None, 
                [(0, 3600)], [], 
                '''                Periodic flooding value (seconds)
                ''',
                'periodic_flooding_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'lcac',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
    'MplsTe' : {
        'meta_info' : _MetaInfoClass('MplsTe',
            False, 
            [
            _MetaInfoClassMember('diff-serv-traffic-engineering', REFERENCE_CLASS, 'DiffServTrafficEngineering' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.DiffServTrafficEngineering', 
                [], [], 
                '''                Configure Diff-Serv Traffic-Engineering
                ''',
                'diff_serv_traffic_engineering',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('gmpls-uni', REFERENCE_CLASS, 'GmplsUni' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsUni', 
                [], [], 
                '''                GMPLS-UNI configuration
                ''',
                'gmpls_uni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('global-attributes', REFERENCE_CLASS, 'GlobalAttributes' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GlobalAttributes', 
                [], [], 
                '''                Configure MPLS TE global attributes
                ''',
                'global_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('transport-profile', REFERENCE_CLASS, 'TransportProfile' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.TransportProfile', 
                [], [], 
                '''                MPLS transport profile configuration data
                ''',
                'transport_profile',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Interfaces', 
                [], [], 
                '''                Configure MPLS TE interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('gmpls-nni', REFERENCE_CLASS, 'GmplsNni' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.GmplsNni', 
                [], [], 
                '''                GMPLS-NNI configuration
                ''',
                'gmpls_nni',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lcac', REFERENCE_CLASS, 'Lcac' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTe.Lcac', 
                [], [], 
                '''                LCAC specific MPLS global configuration
                ''',
                'lcac',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable-traffic-engineering', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS Traffic Engineering
                ''',
                'enable_traffic_engineering',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg'
        ),
    },
}
_meta_table['MplsTe.DiffServTrafficEngineering.Classes.Class']['meta_info'].parent =_meta_table['MplsTe.DiffServTrafficEngineering.Classes']['meta_info']
_meta_table['MplsTe.DiffServTrafficEngineering.Classes']['meta_info'].parent =_meta_table['MplsTe.DiffServTrafficEngineering']['meta_info']
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
_meta_table['MplsTe.GlobalAttributes.PathSelectionLooseAffinities.PathSelectionLooseAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelectionLooseAffinities']['meta_info']
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
_meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Names']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg.Values']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Names']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg.Values']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Queues.Queue']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.Queues']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelectionLooseMetrics.PathSelectionLooseMetric']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.PathSelectionLooseMetrics']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute']['meta_info']
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
_meta_table['MplsTe.GlobalAttributes.FastReroute.Timers']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.FastReroute']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes.AffinityMappings']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelectionLooseAffinities']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Queues']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelectionLooseMetrics']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.Mib']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.BfdOverLsp']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.SoftPreemption']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathInvalidation']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.FastReroute']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
_meta_table['MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole']['meta_info'].parent =_meta_table['MplsTe.GlobalAttributes']['meta_info']
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
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel']['meta_info']
_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath']['meta_info'].parent =_meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths']['meta_info']
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
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info'].parent =_meta_table['MplsTe.GmplsNni.TunnelHeads']['meta_info']
_meta_table['MplsTe.GmplsNni.TopologyInstances']['meta_info'].parent =_meta_table['MplsTe.GmplsNni']['meta_info']
_meta_table['MplsTe.GmplsNni.TunnelHeads']['meta_info'].parent =_meta_table['MplsTe.GmplsNni']['meta_info']
_meta_table['MplsTe.Lcac.Bfd']['meta_info'].parent =_meta_table['MplsTe.Lcac']['meta_info']
_meta_table['MplsTe.Lcac.FloodingThreshold']['meta_info'].parent =_meta_table['MplsTe.Lcac']['meta_info']
_meta_table['MplsTe.DiffServTrafficEngineering']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.GmplsUni']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.GlobalAttributes']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.TransportProfile']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.Interfaces']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.GmplsNni']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
_meta_table['MplsTe.Lcac']['meta_info'].parent =_meta_table['MplsTe']['meta_info']
