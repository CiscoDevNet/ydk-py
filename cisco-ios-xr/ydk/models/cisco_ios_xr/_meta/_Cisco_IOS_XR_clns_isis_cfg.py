


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IsisexplicitNullFlagEnum' : _MetaInfoEnum('IsisexplicitNullFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsissidEnum' : _MetaInfoEnum('IsissidEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'index':'index',
            'absolute':'absolute',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibDatabaseOverFlowBooleanEnum' : _MetaInfoEnum('IsisMibDatabaseOverFlowBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisOverloadBitModeEnum' : _MetaInfoEnum('IsisOverloadBitModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'permanently-set':'permanently_set',
            'startup-period':'startup_period',
            'wait-for-bgp':'wait_for_bgp',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisPrefixPriorityEnum' : _MetaInfoEnum('IsisPrefixPriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'critical-priority':'critical_priority',
            'high-priority':'high_priority',
            'medium-priority':'medium_priority',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisfrrEnum' : _MetaInfoEnum('IsisfrrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'per-link':'per_link',
            'per-prefix':'per_prefix',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibManualAddressDropsBooleanEnum' : _MetaInfoEnum('IsisMibManualAddressDropsBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisTracingModeEnum' : _MetaInfoEnum('IsisTracingModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'off':'off',
            'basic':'basic',
            'enhanced':'enhanced',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisApplyWeightEnum' : _MetaInfoEnum('IsisApplyWeightEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'ecmp-only':'ecmp_only',
            'ucmp-only':'ucmp_only',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAuthenticationFailureBooleanEnum' : _MetaInfoEnum('IsisMibAuthenticationFailureBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisphpFlagEnum' : _MetaInfoEnum('IsisphpFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMetricStyleEnum' : _MetaInfoEnum('IsisMetricStyleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'old-metric-style':'old_metric_style',
            'new-metric-style':'new_metric_style',
            'both-metric-style':'both_metric_style',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAuthenticationAlgorithmEnum' : _MetaInfoEnum('IsisAuthenticationAlgorithmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'cleartext':'cleartext',
            'hmac-md5':'hmac_md5',
            'keychain':'keychain',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibVersionSkewBooleanEnum' : _MetaInfoEnum('IsisMibVersionSkewBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisfrrTiebreakerEnum' : _MetaInfoEnum('IsisfrrTiebreakerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'downstream':'downstream',
            'lc-disjoint':'lc_disjoint',
            'lowest-backup-metric':'lowest_backup_metric',
            'node-protecting':'node_protecting',
            'primary-path':'primary_path',
            'secondary-path':'secondary_path',
            'srlg-disjoint':'srlg_disjoint',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisConfigurableLevelsEnum' : _MetaInfoEnum('IsisConfigurableLevelsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'level1':'level1',
            'level2':'level2',
            'level1-and2':'level1_and2',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAllBooleanEnum' : _MetaInfoEnum('IsisMibAllBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAreaMismatchBooleanEnum' : _MetaInfoEnum('IsisMibAreaMismatchBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibSequenceNumberSkipBooleanEnum' : _MetaInfoEnum('IsisMibSequenceNumberSkipBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibRejectedAdjacencyBooleanEnum' : _MetaInfoEnum('IsisMibRejectedAdjacencyBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAdjCheckEnum' : _MetaInfoEnum('IsisAdjCheckEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibIdLengthMismatchBooleanEnum' : _MetaInfoEnum('IsisMibIdLengthMismatchBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibProtocolsSupportedMismatchBooleanEnum' : _MetaInfoEnum('IsisMibProtocolsSupportedMismatchBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisInterfaceFrrTiebreakerEnum' : _MetaInfoEnum('IsisInterfaceFrrTiebreakerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'node-protecting':'node_protecting',
            'srlg-disjoint':'srlg_disjoint',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisLabelPreferenceEnum' : _MetaInfoEnum('IsisLabelPreferenceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'ldp':'ldp',
            'segment-routing':'segment_routing',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisHelloPaddingEnum' : _MetaInfoEnum('IsisHelloPaddingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'never':'never',
            'sometimes':'sometimes',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibOriginatedLspBufferSizeMismatchBooleanEnum' : _MetaInfoEnum('IsisMibOriginatedLspBufferSizeMismatchBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibOwnLspPurgeBooleanEnum' : _MetaInfoEnum('IsisMibOwnLspPurgeBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAttachedBitEnum' : _MetaInfoEnum('IsisAttachedBitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'area':'area',
            'on':'on',
            'off':'off',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAdvTypeInterLevelEnum' : _MetaInfoEnum('IsisAdvTypeInterLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'inter-level':'inter_level',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMicroLoopAvoidanceEnum' : _MetaInfoEnum('IsisMicroLoopAvoidanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'not-set':'not_set',
            'micro-loop-avoidance-all':'micro_loop_avoidance_all',
            'micro-loop-avoidance-protected':'micro_loop_avoidance_protected',
            'micro-loop-avoidance-segement-routing':'micro_loop_avoidance_segement_routing',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAuthenticationFailureModeEnum' : _MetaInfoEnum('IsisAuthenticationFailureModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'drop':'drop',
            'send-only':'send_only',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMetricStyleTransitionEnum' : _MetaInfoEnum('IsisMetricStyleTransitionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisInterfaceStateEnum' : _MetaInfoEnum('IsisInterfaceStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'shutdown':'shutdown',
            'suppressed':'suppressed',
            'passive':'passive',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibLspTooLargeToPropagateBooleanEnum' : _MetaInfoEnum('IsisMibLspTooLargeToPropagateBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisRedistProtoEnum' : _MetaInfoEnum('IsisRedistProtoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'connected':'connected',
            'static':'static',
            'ospf':'ospf',
            'bgp':'bgp',
            'isis':'isis',
            'ospfv3':'ospfv3',
            'rip':'rip',
            'eigrp':'eigrp',
            'subscriber':'subscriber',
            'application':'application',
            'mobile':'mobile',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisSnpAuthEnum' : _MetaInfoEnum('IsisSnpAuthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'send-only':'send_only',
            'full':'full',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisispfStateEnum' : _MetaInfoEnum('IsisispfStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisfrrLoadSharingEnum' : _MetaInfoEnum('IsisfrrLoadSharingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibLspErrorDetectedBooleanEnum' : _MetaInfoEnum('IsisMibLspErrorDetectedBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisInterfaceAfStateEnum' : _MetaInfoEnum('IsisInterfaceAfStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAdjacencyChangeBooleanEnum' : _MetaInfoEnum('IsisMibAdjacencyChangeBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'NflagClearEnum' : _MetaInfoEnum('NflagClearEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisNsfFlavorEnum' : _MetaInfoEnum('IsisNsfFlavorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'cisco-proprietary-nsf':'cisco_proprietary_nsf',
            'ietf-standard-nsf':'ietf_standard_nsf',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAttemptToExceedMaxSequenceBooleanEnum' : _MetaInfoEnum('IsisMibAttemptToExceedMaxSequenceBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAdvTypeExternalEnum' : _MetaInfoEnum('IsisAdvTypeExternalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'external':'external',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMetricEnum' : _MetaInfoEnum('IsisMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'internal':'internal',
            'external':'external',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibMaxAreaAddressMismatchBooleanEnum' : _MetaInfoEnum('IsisMibMaxAreaAddressMismatchBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisRemoteLfaEnum' : _MetaInfoEnum('IsisRemoteLfaEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'remote-lfa-none':'remote_lfa_none',
            'remote-lfa-tunnel-ldp':'remote_lfa_tunnel_ldp',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibCorruptedLspDetectedBooleanEnum' : _MetaInfoEnum('IsisMibCorruptedLspDetectedBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAuthenticationTypeFailureBooleanEnum' : _MetaInfoEnum('IsisMibAuthenticationTypeFailureBooleanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Srgb' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Srgb',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [('16000', '1048574')], [], 
                '''                The lower bound of the SRGB
                ''',
                'lower_bound',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [('16001', '1048575')], [], 
                '''                The upper bound of the SRGB
                ''',
                'upper_bound',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Initial wait before generating local LSP in
                milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Maximum wait before generating local LSP in
                milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Secondary wait before generating local LSP
                in milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-generation-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspGenerationIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspGenerationIntervals',
            False, 
            [
            _MetaInfoClassMember('lsp-generation-interval', REFERENCE_LIST, 'LspGenerationInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval', 
                [], [], 
                '''                LSP generation scheduling parameters
                ''',
                'lsp_generation_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-generation-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Initial delay expected to take since last
                LSPin milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Maximum delay expected to take since last
                LSPin milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Secondary delay expected to take since last
                LSPin milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-arrival-time',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspArrivalTimes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspArrivalTimes',
            False, 
            [
            _MetaInfoClassMember('lsp-arrival-time', REFERENCE_LIST, 'LspArrivalTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime', 
                [], [], 
                '''                Minimum LSP arrival time
                ''',
                'lsp_arrival_time',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-arrival-times',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.TraceBufferSize' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.TraceBufferSize',
            False, 
            [
            _MetaInfoClassMember('detailed', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000000')], [], 
                '''                Buffer size for detailed traces
                ''',
                'detailed',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000000')], [], 
                '''                Buffer size for hello trace
                ''',
                'hello',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000000')], [], 
                '''                Buffer size for severe trace
                ''',
                'severe',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('standard', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000000')], [], 
                '''                Buffer size for standard traces
                ''',
                'standard',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'trace-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-link-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.MaxLinkMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.MaxLinkMetrics',
            False, 
            [
            _MetaInfoClassMember('max-link-metric', REFERENCE_LIST, 'MaxLinkMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric', 
                [], [], 
                '''                Max Link Metric
                ''',
                'max_link_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-link-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.AdjacencyStagger' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.AdjacencyStagger',
            False, 
            [
            _MetaInfoClassMember('initial-nbr', ATTRIBUTE, 'int' , None, None, 
                [('2', '65000')], [], 
                '''                Adjacency Stagger: Initial number of
                neighbors to bring up per area
                ''',
                'initial_nbr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-nbr', ATTRIBUTE, 'int' , None, None, 
                [('2', '65000')], [], 
                '''                Adjacency Stagger: Subsequent simultaneous
                number of neighbors to bring up
                ''',
                'max_nbr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'adjacency-stagger',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap',
            False, 
            [
            _MetaInfoClassMember('advertise-local', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Segment Routing prefix SID map
                advertise local
                ''',
                'advertise_local',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, remote prefix SID map
                advertisements will be used. If FALSE,
                they will not be used.
                ''',
                'receive',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid-map',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting',
            False, 
            [
            _MetaInfoClassMember('mpls', REFERENCE_ENUM_CLASS, 'IsisLabelPreferenceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreferenceEnum', 
                [], [], 
                '''                Prefer segment routing labels over LDP
                labels
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sid-map', REFERENCE_CLASS, 'PrefixSidMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap', 
                [], [], 
                '''                Enable Segment Routing prefix SID map
                configuration
                ''',
                'prefix_sid_map',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'segment-routing',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('style', REFERENCE_ENUM_CLASS, 'IsisMetricStyleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyleEnum', 
                [], [], 
                '''                Metric Style
                ''',
                'style',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('transition-state', REFERENCE_ENUM_CLASS, 'IsisMetricStyleTransitionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyleTransitionEnum', 
                [], [], 
                '''                Transition state
                ''',
                'transition_state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-style',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MetricStyles',
            False, 
            [
            _MetaInfoClassMember('metric-style', REFERENCE_LIST, 'MetricStyle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle', 
                [], [], 
                '''                Configuration of metric style in LSPs
                ''',
                'metric_style',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-styles',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('load-sharing', REFERENCE_ENUM_CLASS, 'IsisfrrLoadSharingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharingEnum', 
                [], [], 
                '''                Load sharing
                ''',
                'load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharing',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharing', REFERENCE_LIST, 'FrrLoadSharing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing', 
                [], [], 
                '''                Disable load sharing
                ''',
                'frr_load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharings',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'IsisPrefixPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriorityEnum', 
                [], [], 
                '''                Compute for all prefixes upto the
                specified priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits',
            False, 
            [
            _MetaInfoClassMember('priority-limit', REFERENCE_LIST, 'PriorityLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit', 
                [], [], 
                '''                Limit backup computation upto the prefix
                priority
                ''',
                'priority_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limits',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-prefix', REFERENCE_LIST, 'FrrRemoteLfaPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix', 
                [], [], 
                '''                Filter remote LFA router IDs using
                prefix-list
                ''',
                'frr_remote_lfa_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisfrrTiebreakerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreakerEnum', 
                [], [], 
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers',
            False, 
            [
            _MetaInfoClassMember('frr-tiebreaker', REFERENCE_LIST, 'FrrTiebreaker' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker', 
                [], [], 
                '''                Configure tiebreaker for multiple backups
                ''',
                'frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-only',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies',
            False, 
            [
            _MetaInfoClassMember('frr-use-cand-only', REFERENCE_LIST, 'FrrUseCandOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly', 
                [], [], 
                '''                Configure use candidate only to exclude
                interfaces as backup
                ''',
                'frr_use_cand_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-onlies',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharings', REFERENCE_CLASS, 'FrrLoadSharings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings', 
                [], [], 
                '''                Load share prefixes across multiple
                backups
                ''',
                'frr_load_sharings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-prefixes', REFERENCE_CLASS, 'FrrRemoteLfaPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes', 
                [], [], 
                '''                FRR remote LFA prefix list filter
                configuration
                ''',
                'frr_remote_lfa_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-tiebreakers', REFERENCE_CLASS, 'FrrTiebreakers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers', 
                [], [], 
                '''                FRR tiebreakers configuration
                ''',
                'frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-use-cand-onlies', REFERENCE_CLASS, 'FrrUseCandOnlies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies', 
                [], [], 
                '''                FRR use candidate only configuration
                ''',
                'frr_use_cand_onlies',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priority-limits', REFERENCE_CLASS, 'PriorityLimits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits', 
                [], [], 
                '''                FRR prefix-limit configuration
                ''',
                'priority_limits',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-table',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.RouterId',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4/IPv6 address to be used as a router
                ID. Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                SPF Level for prefix prioritization
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-priority-type', REFERENCE_ENUM_CLASS, 'IsisPrefixPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriorityEnum', 
                [], [], 
                '''                SPF Priority to assign matching prefixes
                ''',
                'prefix_priority_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access List to determine prefixes for
                this priority
                ''',
                'access_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tag value to determine prefixes for this
                priority
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priority',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities',
            False, 
            [
            _MetaInfoClassMember('spf-prefix-priority', REFERENCE_LIST, 'SpfPrefixPriority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority', 
                [], [], 
                '''                Determine SPF priority for prefixes
                ''',
                'spf_prefix_priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priorities',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP summary address prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                Level in which to summarize routes
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The tag value
                ''',
                'tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes',
            False, 
            [
            _MetaInfoClassMember('summary-prefix', REFERENCE_LIST, 'SummaryPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix', 
                [], [], 
                '''                Configure IP address prefixes to advertise
                ''',
                'summary_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'IsisMicroLoopAvoidanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidanceEnum', 
                [], [], 
                '''                MicroLoop avoidance enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('rib-update-delay', ATTRIBUTE, 'int' , None, None, 
                [('1000', '65535')], [], 
                '''                Value of delay in msecs in updating RIB
                ''',
                'rib_update_delay',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'micro-loop-avoidance',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('variance', ATTRIBUTE, 'int' , None, None, 
                [('101', '10000')], [], 
                '''                Value of variance
                ''',
                'variance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'enable',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface to be excluded
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude this interface from UCMP path
                computation
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp',
            False, 
            [
            _MetaInfoClassMember('delay-interval', ATTRIBUTE, 'int' , None, None, 
                [('100', '65535')], [], 
                '''                Delay in msecs between primary SPF and
                UCMP computation
                ''',
                'delay_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable', 
                [], [], 
                '''                UCMP feature enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces', 
                [], [], 
                '''                Interfaces excluded from UCMP path
                computation
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ucmp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '28000')], [], 
                '''                Max number of prefixes
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes',
            False, 
            [
            _MetaInfoClassMember('max-redist-prefix', REFERENCE_LIST, 'MaxRedistPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix', 
                [], [], 
                '''                An upper limit on the number of
                redistributed prefixes which may be
                included in the local system's LSP
                ''',
                'max_redist_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation',
            False, 
            [
            _MetaInfoClassMember('source-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Source level for routes
                ''',
                'source_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('destination-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Destination level for routes.  Must
                differ from SourceLevel
                ''',
                'destination_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy limiting routes to be
                propagated
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagation',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Propagations' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Propagations',
            False, 
            [
            _MetaInfoClassMember('propagation', REFERENCE_LIST, 'Propagation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation', 
                [], [], 
                '''                Propagate routes between IS-IS levels
                ''',
                'propagation',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagations',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile',
            False, 
            [
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-or-static-or-rip-or-subscriber-or-mobile',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Protocol Instance Identifier.  Mandatory
                for ISIS, OSPF and application, must not
                be specified otherwise.
                ''',
                'instance_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ospf-or-ospfv3-or-isis-or-application',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First half of BGP AS number in XX.YY
                format.  Mandatory if Protocol is BGP
                and must not be specified otherwise.
                Must be a non-zero value if second half
                is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Second half of BGP AS number in XX.YY
                format. Mandatory if Protocol is BGP and
                must not be specified otherwise. Must be
                a non-zero value if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as-zz', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Eigrp as number.
                ''',
                'as_zz',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'IsisRedistProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProtoEnum', 
                [], [], 
                '''                The protocol to be redistributed.  OSPFv3
                may not be specified for an IPv4 topology
                and OSPF may not be specified for an IPv6
                topology.
                ''',
                'protocol_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp', 
                [], [], 
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('connected-or-static-or-rip-or-subscriber-or-mobile', REFERENCE_CLASS, 'ConnectedOrStaticOrRipOrSubscriberOrMobile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile', 
                [], [], 
                '''                connected or static or rip or subscriber
                or mobile
                ''',
                'connected_or_static_or_rip_or_subscriber_or_mobile',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp', 
                [], [], 
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-or-ospfv3-or-isis-or-application', REFERENCE_LIST, 'OspfOrOspfv3OrIsisOrApplication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication', 
                [], [], 
                '''                ospf or ospfv3 or isis or application
                ''',
                'ospf_or_ospfv3_or_isis_or_application',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions',
            False, 
            [
            _MetaInfoClassMember('redistribution', REFERENCE_LIST, 'Redistribution' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution', 
                [], [], 
                '''                Redistribution of other protocols into
                this IS-IS instance
                ''',
                'redistribution',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistributions',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Maximum interval in between SPF runs in
                seconds
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals',
            False, 
            [
            _MetaInfoClassMember('spf-periodic-interval', REFERENCE_LIST, 'SpfPeriodicInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval', 
                [], [], 
                '''                Maximum interval between spf runs
                ''',
                'spf_periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Initial wait before running a route
                calculation in milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Maximum wait before running a route
                calculation in milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Secondary wait before running a route
                calculation in milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals',
            False, 
            [
            _MetaInfoClassMember('spf-interval', REFERENCE_LIST, 'SpfInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval', 
                [], [], 
                '''                Route calculation scheduling parameters
                ''',
                'spf_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable convergence monitoring
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable the monitoring of individual
                prefixes (prefix list name)
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('track-ip-frr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the Tracking of IP-Frr Convergence
                ''',
                'track_ip_frr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'monitor-convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('external', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Flag to indicate that the default prefix
                should be originated as an external route
                ''',
                'external',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('use-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate whether default
                origination is controlled using a policy
                ''',
                'use_policy',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP route source prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                List of prefixes to which this distance
                applies
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.AdminDistances',
            False, 
            [
            _MetaInfoClassMember('admin-distance', REFERENCE_LIST, 'AdminDistance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance', 
                [], [], 
                '''                Administrative distance configuration. The
                supplied distance is applied to all routes
                discovered from the specified source, or
                only those that match the supplied prefix
                list if this is specified
                ''',
                'admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distances',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsisispfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ispf.States',
            False, 
            [
            _MetaInfoClassMember('state', REFERENCE_LIST, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State', 
                [], [], 
                '''                Enable/disable ISPF
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'states',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ispf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ispf',
            False, 
            [
            _MetaInfoClassMember('states', REFERENCE_CLASS, 'States' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States', 
                [], [], 
                '''                ISPF state (enable/disable)
                ''',
                'states',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ispf',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal',
            False, 
            [
            _MetaInfoClassMember('auto-config', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, LDP will be enabled onall IS-IS
                interfaces enabled for this address-family
                ''',
                'auto_config',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp-global',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address to be used as a router ID.
                Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Mpls' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Mpls',
            False, 
            [
            _MetaInfoClassMember('igp-intact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Install TE and non-TE nexthops in the RIB
                ''',
                'igp_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Enable MPLS for an IS-IS at the given
                levels
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('multicast-intact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Install non-TE nexthops in the RIB for use
                by multicast
                ''',
                'multicast_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId', 
                [], [], 
                '''                Traffic Engineering stable IP address for
                system
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric.MetricEnum' : _MetaInfoEnum('MetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum', 
                        [], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                        [('1', '16777215')], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Metrics',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric', 
                [], [], 
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Weights',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight', 
                [], [], 
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData',
            False, 
            [
            _MetaInfoClassMember('adjacency-check', REFERENCE_ENUM_CLASS, 'IsisAdjCheckEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheckEnum', 
                [], [], 
                '''                Suppress check for consistent AF support on
                received IIHs
                ''',
                'adjacency_check',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-distances', REFERENCE_CLASS, 'AdminDistances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances', 
                [], [], 
                '''                Per-route administrative
                distanceconfiguration
                ''',
                'admin_distances',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-link-attributes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, advertise additional link
                attributes in our LSP
                ''',
                'advertise_link_attributes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-passive-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If enabled, advertise prefixes of passive
                interfaces only
                ''',
                'advertise_passive_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('apply-weight', REFERENCE_ENUM_CLASS, 'IsisApplyWeightEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeightEnum', 
                [], [], 
                '''                Apply weights to UCMP or ECMP only
                ''',
                'apply_weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('attached-bit', REFERENCE_ENUM_CLASS, 'IsisAttachedBitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBitEnum', 
                [], [], 
                '''                Set the attached bit in this router's level
                1 System LSP
                ''',
                'attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-admin-distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Default IS-IS administrative distance
                configuration.
                ''',
                'default_admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation', 
                [], [], 
                '''                Control origination of a default route with
                the option of using a policy.  If no policy
                is specified the default route is
                advertised with zero cost in level 2 only.
                ''',
                'default_information',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-table', REFERENCE_CLASS, 'FrrTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable', 
                [], [], 
                '''                Fast-ReRoute configuration
                ''',
                'frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ignore-attached-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, Ignore other routers attached bit
                ''',
                'ignore_attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ispf', REFERENCE_CLASS, 'Ispf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ispf', 
                [], [], 
                '''                ISPF configuration
                ''',
                'ispf',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-redist-prefixes', REFERENCE_CLASS, 'MaxRedistPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes', 
                [], [], 
                '''                Maximum number of redistributed
                prefixesconfiguration
                ''',
                'max_redist_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Maximum number of active parallel paths per
                route
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-styles', REFERENCE_CLASS, 'MetricStyles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles', 
                [], [], 
                '''                Metric-style configuration
                ''',
                'metric_styles',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Metrics', 
                [], [], 
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('micro-loop-avoidance', REFERENCE_CLASS, 'MicroLoopAvoidance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance', 
                [], [], 
                '''                Micro Loop Avoidance configuration
                ''',
                'micro_loop_avoidance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('monitor-convergence', REFERENCE_CLASS, 'MonitorConvergence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence', 
                [], [], 
                '''                Enable convergence monitoring
                ''',
                'monitor_convergence',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Mpls', 
                [], [], 
                '''                MPLS configuration. MPLS configuration will
                only be applied for the IPv4-unicast
                address-family.
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp-global', REFERENCE_CLASS, 'MplsLdpGlobal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal', 
                [], [], 
                '''                MPLS LDP configuration. MPLS LDP
                configuration will only be applied for the
                IPv4-unicast address-family.
                ''',
                'mpls_ldp_global',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('propagations', REFERENCE_CLASS, 'Propagations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Propagations', 
                [], [], 
                '''                Route propagation configuration
                ''',
                'propagations',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('redistributions', REFERENCE_CLASS, 'Redistributions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions', 
                [], [], 
                '''                Protocol redistribution configuration
                ''',
                'redistributions',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-source-first-hop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, routes will be installed with the
                IP address of the first-hop node as the
                source instead of the originating node
                ''',
                'route_source_first_hop',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.RouterId', 
                [], [], 
                '''                Stable IP address for system. Will only be
                applied for the unicast sub-address-family.
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting', 
                [], [], 
                '''                Enable Segment Routing configuration
                ''',
                'segment_routing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('single-topology', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Run IPv6 Unicast using the standard (IPv4
                Unicast) topology
                ''',
                'single_topology',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-intervals', REFERENCE_CLASS, 'SpfIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals', 
                [], [], 
                '''                SPF-interval configuration
                ''',
                'spf_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-periodic-intervals', REFERENCE_CLASS, 'SpfPeriodicIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals', 
                [], [], 
                '''                Peoridic SPF configuration
                ''',
                'spf_periodic_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-prefix-priorities', REFERENCE_CLASS, 'SpfPrefixPriorities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities', 
                [], [], 
                '''                SPF Prefix Priority configuration
                ''',
                'spf_prefix_priorities',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes', 
                [], [], 
                '''                Summary-prefix configuration
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-id', ATTRIBUTE, 'int' , None, None, 
                [('6', '4095')], [], 
                '''                Set the topology ID for a named
                (non-default) topology. This object must be
                set before any other configuration is
                supplied for a named (non-default) topology
                , and must be the last configuration object
                to be removed. This item should not be
                supplied for the non-named default
                topologies.
                ''',
                'topology_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ucmp', REFERENCE_CLASS, 'Ucmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp', 
                [], [], 
                '''                UCMP (UnEqual Cost MultiPath) configuration
                ''',
                'ucmp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Weights', 
                [], [], 
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'af-data',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap',
            False, 
            [
            _MetaInfoClassMember('advertise-local', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Segment Routing prefix SID map
                advertise local
                ''',
                'advertise_local',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, remote prefix SID map
                advertisements will be used. If FALSE,
                they will not be used.
                ''',
                'receive',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid-map',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting',
            False, 
            [
            _MetaInfoClassMember('mpls', REFERENCE_ENUM_CLASS, 'IsisLabelPreferenceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreferenceEnum', 
                [], [], 
                '''                Prefer segment routing labels over LDP
                labels
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sid-map', REFERENCE_CLASS, 'PrefixSidMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap', 
                [], [], 
                '''                Enable Segment Routing prefix SID map
                configuration
                ''',
                'prefix_sid_map',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'segment-routing',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('style', REFERENCE_ENUM_CLASS, 'IsisMetricStyleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyleEnum', 
                [], [], 
                '''                Metric Style
                ''',
                'style',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('transition-state', REFERENCE_ENUM_CLASS, 'IsisMetricStyleTransitionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyleTransitionEnum', 
                [], [], 
                '''                Transition state
                ''',
                'transition_state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-style',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles',
            False, 
            [
            _MetaInfoClassMember('metric-style', REFERENCE_LIST, 'MetricStyle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle', 
                [], [], 
                '''                Configuration of metric style in LSPs
                ''',
                'metric_style',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-styles',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('load-sharing', REFERENCE_ENUM_CLASS, 'IsisfrrLoadSharingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharingEnum', 
                [], [], 
                '''                Load sharing
                ''',
                'load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharing',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharing', REFERENCE_LIST, 'FrrLoadSharing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing', 
                [], [], 
                '''                Disable load sharing
                ''',
                'frr_load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharings',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'IsisPrefixPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriorityEnum', 
                [], [], 
                '''                Compute for all prefixes upto the
                specified priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits',
            False, 
            [
            _MetaInfoClassMember('priority-limit', REFERENCE_LIST, 'PriorityLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit', 
                [], [], 
                '''                Limit backup computation upto the prefix
                priority
                ''',
                'priority_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limits',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-prefix', REFERENCE_LIST, 'FrrRemoteLfaPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix', 
                [], [], 
                '''                Filter remote LFA router IDs using
                prefix-list
                ''',
                'frr_remote_lfa_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisfrrTiebreakerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreakerEnum', 
                [], [], 
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers',
            False, 
            [
            _MetaInfoClassMember('frr-tiebreaker', REFERENCE_LIST, 'FrrTiebreaker' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker', 
                [], [], 
                '''                Configure tiebreaker for multiple backups
                ''',
                'frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-only',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies',
            False, 
            [
            _MetaInfoClassMember('frr-use-cand-only', REFERENCE_LIST, 'FrrUseCandOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly', 
                [], [], 
                '''                Configure use candidate only to exclude
                interfaces as backup
                ''',
                'frr_use_cand_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-onlies',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharings', REFERENCE_CLASS, 'FrrLoadSharings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings', 
                [], [], 
                '''                Load share prefixes across multiple
                backups
                ''',
                'frr_load_sharings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-prefixes', REFERENCE_CLASS, 'FrrRemoteLfaPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes', 
                [], [], 
                '''                FRR remote LFA prefix list filter
                configuration
                ''',
                'frr_remote_lfa_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-tiebreakers', REFERENCE_CLASS, 'FrrTiebreakers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers', 
                [], [], 
                '''                FRR tiebreakers configuration
                ''',
                'frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-use-cand-onlies', REFERENCE_CLASS, 'FrrUseCandOnlies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies', 
                [], [], 
                '''                FRR use candidate only configuration
                ''',
                'frr_use_cand_onlies',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priority-limits', REFERENCE_CLASS, 'PriorityLimits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits', 
                [], [], 
                '''                FRR prefix-limit configuration
                ''',
                'priority_limits',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-table',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.RouterId',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4/IPv6 address to be used as a router
                ID. Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                SPF Level for prefix prioritization
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-priority-type', REFERENCE_ENUM_CLASS, 'IsisPrefixPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriorityEnum', 
                [], [], 
                '''                SPF Priority to assign matching prefixes
                ''',
                'prefix_priority_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access List to determine prefixes for
                this priority
                ''',
                'access_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tag value to determine prefixes for this
                priority
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priority',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities',
            False, 
            [
            _MetaInfoClassMember('spf-prefix-priority', REFERENCE_LIST, 'SpfPrefixPriority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority', 
                [], [], 
                '''                Determine SPF priority for prefixes
                ''',
                'spf_prefix_priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priorities',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP summary address prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                Level in which to summarize routes
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The tag value
                ''',
                'tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes',
            False, 
            [
            _MetaInfoClassMember('summary-prefix', REFERENCE_LIST, 'SummaryPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix', 
                [], [], 
                '''                Configure IP address prefixes to advertise
                ''',
                'summary_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'IsisMicroLoopAvoidanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidanceEnum', 
                [], [], 
                '''                MicroLoop avoidance enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('rib-update-delay', ATTRIBUTE, 'int' , None, None, 
                [('1000', '65535')], [], 
                '''                Value of delay in msecs in updating RIB
                ''',
                'rib_update_delay',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'micro-loop-avoidance',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('variance', ATTRIBUTE, 'int' , None, None, 
                [('101', '10000')], [], 
                '''                Value of variance
                ''',
                'variance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'enable',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface to be excluded
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude this interface from UCMP path
                computation
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp',
            False, 
            [
            _MetaInfoClassMember('delay-interval', ATTRIBUTE, 'int' , None, None, 
                [('100', '65535')], [], 
                '''                Delay in msecs between primary SPF and
                UCMP computation
                ''',
                'delay_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable', 
                [], [], 
                '''                UCMP feature enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces', 
                [], [], 
                '''                Interfaces excluded from UCMP path
                computation
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ucmp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '28000')], [], 
                '''                Max number of prefixes
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes',
            False, 
            [
            _MetaInfoClassMember('max-redist-prefix', REFERENCE_LIST, 'MaxRedistPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix', 
                [], [], 
                '''                An upper limit on the number of
                redistributed prefixes which may be
                included in the local system's LSP
                ''',
                'max_redist_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation',
            False, 
            [
            _MetaInfoClassMember('source-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Source level for routes
                ''',
                'source_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('destination-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Destination level for routes.  Must
                differ from SourceLevel
                ''',
                'destination_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy limiting routes to be
                propagated
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagation',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Propagations',
            False, 
            [
            _MetaInfoClassMember('propagation', REFERENCE_LIST, 'Propagation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation', 
                [], [], 
                '''                Propagate routes between IS-IS levels
                ''',
                'propagation',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagations',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile',
            False, 
            [
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-or-static-or-rip-or-subscriber-or-mobile',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Protocol Instance Identifier.  Mandatory
                for ISIS, OSPF and application, must not
                be specified otherwise.
                ''',
                'instance_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ospf-or-ospfv3-or-isis-or-application',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First half of BGP AS number in XX.YY
                format.  Mandatory if Protocol is BGP
                and must not be specified otherwise.
                Must be a non-zero value if second half
                is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Second half of BGP AS number in XX.YY
                format. Mandatory if Protocol is BGP and
                must not be specified otherwise. Must be
                a non-zero value if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as-zz', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Eigrp as number.
                ''',
                'as_zz',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricEnum', 
                [], [], 
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'IsisRedistProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProtoEnum', 
                [], [], 
                '''                The protocol to be redistributed.  OSPFv3
                may not be specified for an IPv4 topology
                and OSPF may not be specified for an IPv6
                topology.
                ''',
                'protocol_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp', 
                [], [], 
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('connected-or-static-or-rip-or-subscriber-or-mobile', REFERENCE_CLASS, 'ConnectedOrStaticOrRipOrSubscriberOrMobile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile', 
                [], [], 
                '''                connected or static or rip or subscriber
                or mobile
                ''',
                'connected_or_static_or_rip_or_subscriber_or_mobile',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp', 
                [], [], 
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-or-ospfv3-or-isis-or-application', REFERENCE_LIST, 'OspfOrOspfv3OrIsisOrApplication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication', 
                [], [], 
                '''                ospf or ospfv3 or isis or application
                ''',
                'ospf_or_ospfv3_or_isis_or_application',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions',
            False, 
            [
            _MetaInfoClassMember('redistribution', REFERENCE_LIST, 'Redistribution' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution', 
                [], [], 
                '''                Redistribution of other protocols into
                this IS-IS instance
                ''',
                'redistribution',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistributions',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Maximum interval in between SPF runs in
                seconds
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals',
            False, 
            [
            _MetaInfoClassMember('spf-periodic-interval', REFERENCE_LIST, 'SpfPeriodicInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval', 
                [], [], 
                '''                Maximum interval between spf runs
                ''',
                'spf_periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Initial wait before running a route
                calculation in milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Maximum wait before running a route
                calculation in milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '120000')], [], 
                '''                Secondary wait before running a route
                calculation in milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals',
            False, 
            [
            _MetaInfoClassMember('spf-interval', REFERENCE_LIST, 'SpfInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval', 
                [], [], 
                '''                Route calculation scheduling parameters
                ''',
                'spf_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable convergence monitoring
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable the monitoring of individual
                prefixes (prefix list name)
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('track-ip-frr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the Tracking of IP-Frr Convergence
                ''',
                'track_ip_frr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'monitor-convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('external', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Flag to indicate that the default prefix
                should be originated as an external route
                ''',
                'external',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('use-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to indicate whether default
                origination is controlled using a policy
                ''',
                'use_policy',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP route source prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                List of prefixes to which this distance
                applies
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances',
            False, 
            [
            _MetaInfoClassMember('admin-distance', REFERENCE_LIST, 'AdminDistance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance', 
                [], [], 
                '''                Administrative distance configuration. The
                supplied distance is applied to all routes
                discovered from the specified source, or
                only those that match the supplied prefix
                list if this is specified
                ''',
                'admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distances',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsisispfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States',
            False, 
            [
            _MetaInfoClassMember('state', REFERENCE_LIST, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State', 
                [], [], 
                '''                Enable/disable ISPF
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'states',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ispf',
            False, 
            [
            _MetaInfoClassMember('states', REFERENCE_CLASS, 'States' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States', 
                [], [], 
                '''                ISPF state (enable/disable)
                ''',
                'states',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ispf',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal',
            False, 
            [
            _MetaInfoClassMember('auto-config', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, LDP will be enabled onall IS-IS
                interfaces enabled for this address-family
                ''',
                'auto_config',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp-global',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address to be used as a router ID.
                Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Mpls',
            False, 
            [
            _MetaInfoClassMember('igp-intact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Install TE and non-TE nexthops in the RIB
                ''',
                'igp_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Enable MPLS for an IS-IS at the given
                levels
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('multicast-intact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Install non-TE nexthops in the RIB for use
                by multicast
                ''',
                'multicast_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId', 
                [], [], 
                '''                Traffic Engineering stable IP address for
                system
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric.MetricEnum' : _MetaInfoEnum('MetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum', 
                        [], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                        [('1', '16777215')], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Metrics',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric', 
                [], [], 
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Weights',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight', 
                [], [], 
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName',
            False, 
            [
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Topology Name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('adjacency-check', REFERENCE_ENUM_CLASS, 'IsisAdjCheckEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheckEnum', 
                [], [], 
                '''                Suppress check for consistent AF support on
                received IIHs
                ''',
                'adjacency_check',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-distances', REFERENCE_CLASS, 'AdminDistances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances', 
                [], [], 
                '''                Per-route administrative
                distanceconfiguration
                ''',
                'admin_distances',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-link-attributes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, advertise additional link
                attributes in our LSP
                ''',
                'advertise_link_attributes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-passive-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If enabled, advertise prefixes of passive
                interfaces only
                ''',
                'advertise_passive_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('apply-weight', REFERENCE_ENUM_CLASS, 'IsisApplyWeightEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeightEnum', 
                [], [], 
                '''                Apply weights to UCMP or ECMP only
                ''',
                'apply_weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('attached-bit', REFERENCE_ENUM_CLASS, 'IsisAttachedBitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBitEnum', 
                [], [], 
                '''                Set the attached bit in this router's level
                1 System LSP
                ''',
                'attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-admin-distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Default IS-IS administrative distance
                configuration.
                ''',
                'default_admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation', 
                [], [], 
                '''                Control origination of a default route with
                the option of using a policy.  If no policy
                is specified the default route is
                advertised with zero cost in level 2 only.
                ''',
                'default_information',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-table', REFERENCE_CLASS, 'FrrTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable', 
                [], [], 
                '''                Fast-ReRoute configuration
                ''',
                'frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ignore-attached-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, Ignore other routers attached bit
                ''',
                'ignore_attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ispf', REFERENCE_CLASS, 'Ispf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf', 
                [], [], 
                '''                ISPF configuration
                ''',
                'ispf',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-redist-prefixes', REFERENCE_CLASS, 'MaxRedistPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes', 
                [], [], 
                '''                Maximum number of redistributed
                prefixesconfiguration
                ''',
                'max_redist_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Maximum number of active parallel paths per
                route
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-styles', REFERENCE_CLASS, 'MetricStyles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles', 
                [], [], 
                '''                Metric-style configuration
                ''',
                'metric_styles',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics', 
                [], [], 
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('micro-loop-avoidance', REFERENCE_CLASS, 'MicroLoopAvoidance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance', 
                [], [], 
                '''                Micro Loop Avoidance configuration
                ''',
                'micro_loop_avoidance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('monitor-convergence', REFERENCE_CLASS, 'MonitorConvergence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence', 
                [], [], 
                '''                Enable convergence monitoring
                ''',
                'monitor_convergence',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls', 
                [], [], 
                '''                MPLS configuration. MPLS configuration will
                only be applied for the IPv4-unicast
                address-family.
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp-global', REFERENCE_CLASS, 'MplsLdpGlobal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal', 
                [], [], 
                '''                MPLS LDP configuration. MPLS LDP
                configuration will only be applied for the
                IPv4-unicast address-family.
                ''',
                'mpls_ldp_global',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('propagations', REFERENCE_CLASS, 'Propagations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations', 
                [], [], 
                '''                Route propagation configuration
                ''',
                'propagations',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('redistributions', REFERENCE_CLASS, 'Redistributions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions', 
                [], [], 
                '''                Protocol redistribution configuration
                ''',
                'redistributions',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-source-first-hop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, routes will be installed with the
                IP address of the first-hop node as the
                source instead of the originating node
                ''',
                'route_source_first_hop',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.RouterId', 
                [], [], 
                '''                Stable IP address for system. Will only be
                applied for the unicast sub-address-family.
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting', 
                [], [], 
                '''                Enable Segment Routing configuration
                ''',
                'segment_routing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('single-topology', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Run IPv6 Unicast using the standard (IPv4
                Unicast) topology
                ''',
                'single_topology',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-intervals', REFERENCE_CLASS, 'SpfIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals', 
                [], [], 
                '''                SPF-interval configuration
                ''',
                'spf_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-periodic-intervals', REFERENCE_CLASS, 'SpfPeriodicIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals', 
                [], [], 
                '''                Peoridic SPF configuration
                ''',
                'spf_periodic_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-prefix-priorities', REFERENCE_CLASS, 'SpfPrefixPriorities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities', 
                [], [], 
                '''                SPF Prefix Priority configuration
                ''',
                'spf_prefix_priorities',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes', 
                [], [], 
                '''                Summary-prefix configuration
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-id', ATTRIBUTE, 'int' , None, None, 
                [('6', '4095')], [], 
                '''                Set the topology ID for a named
                (non-default) topology. This object must be
                set before any other configuration is
                supplied for a named (non-default) topology
                , and must be the last configuration object
                to be removed. This item should not be
                supplied for the non-named default
                topologies.
                ''',
                'topology_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ucmp', REFERENCE_CLASS, 'Ucmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp', 
                [], [], 
                '''                UCMP (UnEqual Cost MultiPath) configuration
                ''',
                'ucmp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Weights', 
                [], [], 
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'topology-name',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs.Af' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'IsisAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'IsisSubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamilyEnum', 
                [], [], 
                '''                Sub address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('af-data', REFERENCE_CLASS, 'AfData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData', 
                [], [], 
                '''                Data container.
                ''',
                'af_data',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-name', REFERENCE_LIST, 'TopologyName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName', 
                [], [], 
                '''                keys: topology-name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Afs' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af', 
                [], [], 
                '''                Configuration for an IS-IS address-family. If
                a named (non-default) topology is being
                created it must be multicast.
                ''',
                'af',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-refresh-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspRefreshIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspRefreshIntervals',
            False, 
            [
            _MetaInfoClassMember('lsp-refresh-interval', REFERENCE_LIST, 'LspRefreshInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval', 
                [], [], 
                '''                Interval between re-flooding of unchanged
                LSPs
                ''',
                'lsp_refresh_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-refresh-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Distribute' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Distribute',
            False, 
            [
            _MetaInfoClassMember('dist-inst-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Instance ID
                ''',
                'dist_inst_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('dist-throttle', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                Seconds
                ''',
                'dist_throttle',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'distribute',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-accept-password',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspAcceptPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspAcceptPasswords',
            False, 
            [
            _MetaInfoClassMember('lsp-accept-password', REFERENCE_LIST, 'LspAcceptPassword' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword', 
                [], [], 
                '''                LSP/SNP accept passwords. This requires the
                existence of an LSPPassword of the same level
                .
                ''',
                'lsp_accept_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-accept-passwords',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspMtus.LspMtu' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspMtus.LspMtu',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('128', '4352')], [], 
                '''                Bytes
                ''',
                'mtu',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-mtu',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspMtus' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspMtus',
            False, 
            [
            _MetaInfoClassMember('lsp-mtu', REFERENCE_LIST, 'LspMtu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspMtus.LspMtu', 
                [], [], 
                '''                LSP MTU
                ''',
                'lsp_mtu',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-mtus',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Nsf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Nsf',
            False, 
            [
            _MetaInfoClassMember('flavor', REFERENCE_ENUM_CLASS, 'IsisNsfFlavorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisNsfFlavorEnum', 
                [], [], 
                '''                NSF not configured if item is deleted
                ''',
                'flavor',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                Per-interface time period to wait for a
                restart ACK during an IETF-NSF restart. This
                configuration has no effect if IETF-NSF is
                not configured
                ''',
                'interface_timer',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Maximum route lifetime following restart.
                When this lifetime expires, old routes will
                be purged from the RIB.
                ''',
                'lifetime',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-interface-timer-expiry', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Maximum number of times an interface timer
                may expire during an IETF-NSF restart before
                the NSF restart is aborted. This
                configuration has no effect if IETF NSF is
                not configured.
                ''',
                'max_interface_timer_expiry',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LinkGroups.LinkGroup' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LinkGroups.LinkGroup',
            False, 
            [
            _MetaInfoClassMember('link-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Link Group Name
                ''',
                'link_group_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Flag to indicate that linkgroup should be
                running.  This must be the first object
                created when a linkgroup is configured, and
                the last object deleted when it is
                deconfigured.  When this object is deleted,
                the IS-IS linkgroup will be removed.
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for redistributed routes: <0-63> for
                narrow, <0-16777215> for wide
                ''',
                'metric_offset',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('minimum-members', ATTRIBUTE, 'int' , None, None, 
                [('2', '64')], [], 
                '''                Minimum Members
                ''',
                'minimum_members',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('revert-members', ATTRIBUTE, 'int' , None, None, 
                [('2', '64')], [], 
                '''                Revert Members
                ''',
                'revert_members',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'link-group',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LinkGroups' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LinkGroups',
            False, 
            [
            _MetaInfoClassMember('link-group', REFERENCE_LIST, 'LinkGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LinkGroups.LinkGroup', 
                [], [], 
                '''                Configuration for link group name
                ''',
                'link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'link-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '65535')], [], 
                '''                LSP checksum check interval time in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-check-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspCheckIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspCheckIntervals',
            False, 
            [
            _MetaInfoClassMember('lsp-check-interval', REFERENCE_LIST, 'LspCheckInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval', 
                [], [], 
                '''                LSP checksum check interval parameters
                ''',
                'lsp_check_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-check-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspPasswords.LspPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspPasswords.LspPassword',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'IsisAuthenticationAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithmEnum', 
                [], [], 
                '''                Algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'IsisSnpAuthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisSnpAuthEnum', 
                [], [], 
                '''                SNP packet authentication mode
                ''',
                'authentication_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('failure-mode', REFERENCE_ENUM_CLASS, 'IsisAuthenticationFailureModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureModeEnum', 
                [], [], 
                '''                Failure Mode
                ''',
                'failure_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Password or unencrypted Key Chain name
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-password',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspPasswords',
            False, 
            [
            _MetaInfoClassMember('lsp-password', REFERENCE_LIST, 'LspPassword' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspPasswords.LspPassword', 
                [], [], 
                '''                LSP/SNP passwords. This must exist if an
                LSPAcceptPassword of the same level exists.
                ''',
                'lsp_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-passwords',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Nets.Net' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Nets.Net',
            False, 
            [
            _MetaInfoClassMember('net-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}'], 
                '''                Network Entity Title
                ''',
                'net_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'net',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Nets' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Nets',
            False, 
            [
            _MetaInfoClassMember('net', REFERENCE_LIST, 'Net' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Nets.Net', 
                [], [], 
                '''                Network Entity Title (NET)
                ''',
                'net',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'nets',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspLifetimes.LspLifetime' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspLifetimes.LspLifetime',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Seconds
                ''',
                'lifetime',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-lifetime',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.LspLifetimes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspLifetimes',
            False, 
            [
            _MetaInfoClassMember('lsp-lifetime', REFERENCE_LIST, 'LspLifetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspLifetimes.LspLifetime', 
                [], [], 
                '''                Maximum LSP lifetime
                ''',
                'lsp_lifetime',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-lifetimes',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.OverloadBits.OverloadBit' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.OverloadBits.OverloadBit',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('external-adv-type', REFERENCE_ENUM_CLASS, 'IsisAdvTypeExternalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeExternalEnum', 
                [], [], 
                '''                Advertise prefixes from other protocols
                ''',
                'external_adv_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hippity-period', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time in seconds to advertise ourself as
                overloaded after process startup
                ''',
                'hippity_period',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('inter-level-adv-type', REFERENCE_ENUM_CLASS, 'IsisAdvTypeInterLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeInterLevelEnum', 
                [], [], 
                '''                Advertise prefixes across ISIS levels
                ''',
                'inter_level_adv_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('overload-bit-mode', REFERENCE_ENUM_CLASS, 'IsisOverloadBitModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisOverloadBitModeEnum', 
                [], [], 
                '''                Circumstances under which the overload bit
                is set in the system LSP
                ''',
                'overload_bit_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'overload-bit',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.OverloadBits' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.OverloadBits',
            False, 
            [
            _MetaInfoClassMember('overload-bit', REFERENCE_LIST, 'OverloadBit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.OverloadBits.OverloadBit', 
                [], [], 
                '''                Set the overload bit in the System LSP so
                that other routers avoid this one in SPF
                calculations. This may be done either
                unconditionally, or on startup until either a
                set time has passed or IS-IS is informed that
                BGP has converged. This is an Object with a
                union discriminated on an integer value of
                the ISISOverloadBitModeType.
                ''',
                'overload_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'overload-bits',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Milliseconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-throttle-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals',
            False, 
            [
            _MetaInfoClassMember('lsp-retransmit-throttle-interval', REFERENCE_LIST, 'LspRetransmitThrottleInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval', 
                [], [], 
                '''                Minimum interval betwen retransissions of
                different LSPs
                ''',
                'lsp_retransmit_throttle_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-throttle-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals',
            False, 
            [
            _MetaInfoClassMember('lsp-retransmit-interval', REFERENCE_LIST, 'LspRetransmitInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval', 
                [], [], 
                '''                Interval between retransmissions of the
                same LSP
                ''',
                'lsp_retransmit_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions
                created by isis
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('enable-ipv4', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable_ipv4',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('enable-ipv6', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable_ipv6',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by
                isis
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('priority-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Priority
                ''',
                'priority_value',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.Priorities' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.Priorities',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority', 
                [], [], 
                '''                DIS-election priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priorities',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-accept-password',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords',
            False, 
            [
            _MetaInfoClassMember('hello-accept-password', REFERENCE_LIST, 'HelloAcceptPassword' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword', 
                [], [], 
                '''                IIH accept passwords. This requires the
                existence of a HelloPassword of the same
                level.
                ''',
                'hello_accept_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-accept-passwords',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'IsisAuthenticationAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithmEnum', 
                [], [], 
                '''                Algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('failure-mode', REFERENCE_ENUM_CLASS, 'IsisAuthenticationFailureModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureModeEnum', 
                [], [], 
                '''                Failure Mode
                ''',
                'failure_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Password or unencrypted Key Chain name
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-password',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPasswords',
            False, 
            [
            _MetaInfoClassMember('hello-password', REFERENCE_LIST, 'HelloPassword' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword', 
                [], [], 
                '''                IIH passwords. This must exist if a
                HelloAcceptPassword of the same level
                exists.
                ''',
                'hello_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-passwords',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('padding-type', REFERENCE_ENUM_CLASS, 'IsisHelloPaddingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisHelloPaddingEnum', 
                [], [], 
                '''                Hello padding type value
                ''',
                'padding_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-padding',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPaddings',
            False, 
            [
            _MetaInfoClassMember('hello-padding', REFERENCE_LIST, 'HelloPadding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding', 
                [], [], 
                '''                Pad IIHs to the interface MTU
                ''',
                'hello_padding',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-paddings',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [('3', '1000')], [], 
                '''                Hello multiplier value
                ''',
                'multiplier',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers',
            False, 
            [
            _MetaInfoClassMember('hello-multiplier', REFERENCE_LIST, 'HelloMultiplier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier', 
                [], [], 
                '''                Hello-multiplier configuration. The number
                of successive IIHs that may be missed on an
                adjacency before it is considered down.
                ''',
                'hello_multiplier',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-multipliers',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Count
                ''',
                'count',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-fast-flood-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds',
            False, 
            [
            _MetaInfoClassMember('lsp-fast-flood-threshold', REFERENCE_LIST, 'LspFastFloodThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold', 
                [], [], 
                '''                Number of LSPs to send back to back on an
                interface.
                ''',
                'lsp_fast_flood_threshold',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-fast-flood-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-attribute-n-flag-clear',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears',
            False, 
            [
            _MetaInfoClassMember('prefix-attribute-n-flag-clear', REFERENCE_LIST, 'PrefixAttributeNFlagClear' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear', 
                [], [], 
                '''                Clear the N flag in prefix attribute flags
                sub-TLV
                ''',
                'prefix_attribute_n_flag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-attribute-n-flag-clears',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloIntervals',
            False, 
            [
            _MetaInfoClassMember('hello-interval', REFERENCE_LIST, 'HelloInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval', 
                [], [], 
                '''                Hello-interval configuration. The interval
                at which IIH packets will be sent. This
                will be three times quicker on a LAN
                interface which has been electted DIS.
                ''',
                'hello_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlagEnum', 
                [], [], 
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClearEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClearEnum', 
                [], [], 
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlagEnum', 
                [], [], 
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsissidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidEnum', 
                [], [], 
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('frrlfa-candidate-interface', REFERENCE_LIST, 'FrrlfaCandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface', 
                [], [], 
                '''                Include an interface to LFA candidate
                in computation
                ''',
                'frrlfa_candidate_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('max-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Value of the metric
                ''',
                'max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-max-metric', REFERENCE_LIST, 'FrrRemoteLfaMaxMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric', 
                [], [], 
                '''                Configure the maximum metric for
                selecting a remote LFA node
                ''',
                'frr_remote_lfa_max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-type',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes',
            False, 
            [
            _MetaInfoClassMember('frr-type', REFERENCE_LIST, 'FrrType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType', 
                [], [], 
                '''                Type of computation for prefixes
                reachable via interface
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-types',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsisRemoteLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfaEnum', 
                [], [], 
                '''                Remote LFA Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-type',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-type', REFERENCE_LIST, 'FrrRemoteLfaType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType', 
                [], [], 
                '''                Enable remote lfa for a particular
                level
                ''',
                'frr_remote_lfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-types',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-default',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker-default', REFERENCE_LIST, 'InterfaceFrrTiebreakerDefault' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault', 
                [], [], 
                '''                Configure default tiebreaker
                ''',
                'interface_frr_tiebreaker_default',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-type',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes',
            False, 
            [
            _MetaInfoClassMember('frrtilfa-type', REFERENCE_LIST, 'FrrtilfaType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType', 
                [], [], 
                '''                Enable TI lfa for a particular level
                ''',
                'frrtilfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-types',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('frr-exclude-interface', REFERENCE_LIST, 'FrrExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface', 
                [], [], 
                '''                Exclude an interface from computation
                ''',
                'frr_exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisInterfaceFrrTiebreakerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreakerEnum', 
                [], [], 
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker', REFERENCE_LIST, 'InterfaceFrrTiebreaker' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker', 
                [], [], 
                '''                Configure tiebreaker for multiple
                backups
                ''',
                'interface_frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable',
            False, 
            [
            _MetaInfoClassMember('frr-exclude-interfaces', REFERENCE_CLASS, 'FrrExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces', 
                [], [], 
                '''                FRR exclusion configuration
                ''',
                'frr_exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-max-metrics', REFERENCE_CLASS, 'FrrRemoteLfaMaxMetrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics', 
                [], [], 
                '''                Remote LFA maxmimum metric
                ''',
                'frr_remote_lfa_max_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-types', REFERENCE_CLASS, 'FrrRemoteLfaTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes', 
                [], [], 
                '''                Remote LFA Enable
                ''',
                'frr_remote_lfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-types', REFERENCE_CLASS, 'FrrTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes', 
                [], [], 
                '''                Type of FRR computation per level
                ''',
                'frr_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrlfa-candidate-interfaces', REFERENCE_CLASS, 'FrrlfaCandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces', 
                [], [], 
                '''                FRR LFA candidate configuration
                ''',
                'frrlfa_candidate_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrtilfa-types', REFERENCE_CLASS, 'FrrtilfaTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes', 
                [], [], 
                '''                TI LFA Enable
                ''',
                'frrtilfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreaker-defaults', REFERENCE_CLASS, 'InterfaceFrrTiebreakerDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults', 
                [], [], 
                '''                Interface FRR Default tiebreaker
                configuration
                ''',
                'interface_frr_tiebreaker_defaults',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreakers', REFERENCE_CLASS, 'InterfaceFrrTiebreakers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers', 
                [], [], 
                '''                Interface FRR tiebreakers configuration
                ''',
                'interface_frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-table',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp',
            False, 
            [
            _MetaInfoClassMember('sync-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Enable MPLS LDP Synchronization for an
                IS-IS level
                ''',
                'sync_level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlagEnum', 
                [], [], 
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClearEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClearEnum', 
                [], [], 
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlagEnum', 
                [], [], 
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsissidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidEnum', 
                [], [], 
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sspfsid',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('proactive-protect', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Allowed auto metric:<1-63> for narrow
                ,<1-16777214> for wide
                ''',
                'proactive_protect',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics',
            False, 
            [
            _MetaInfoClassMember('auto-metric', REFERENCE_LIST, 'AutoMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric', 
                [], [], 
                '''                AutoMetric Proactive-Protect
                configuration. Legal value depends on
                the metric-style specified for the
                topology. If the metric-style defined is
                narrow, then only a value between <1-63>
                is allowed and if the metric-style is
                defined as wide, then a value between
                <1-16777214> is allowed as the
                auto-metric value.
                ''',
                'auto_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tag to associate with connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags',
            False, 
            [
            _MetaInfoClassMember('admin-tag', REFERENCE_LIST, 'AdminTag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag', 
                [], [], 
                '''                Admin tag for advertised interface
                connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tags',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Level in which link group will be
                effective
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('link-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Link Group
                ''',
                'link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-link-group',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric.MetricEnum' : _MetaInfoEnum('MetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum', 
                        [], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                        [('1', '16777215')], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric', 
                [], [], 
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight', 
                [], [], 
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData',
            False, 
            [
            _MetaInfoClassMember('admin-tags', REFERENCE_CLASS, 'AdminTags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags', 
                [], [], 
                '''                admin-tag configuration
                ''',
                'admin_tags',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('auto-metrics', REFERENCE_CLASS, 'AutoMetrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics', 
                [], [], 
                '''                AutoMetric configuration
                ''',
                'auto_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-af-state', REFERENCE_ENUM_CLASS, 'IsisInterfaceAfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'interface_af_state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-table', REFERENCE_CLASS, 'InterfaceFrrTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable', 
                [], [], 
                '''                Fast-ReRoute configuration
                ''',
                'interface_frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-link-group', REFERENCE_CLASS, 'InterfaceLinkGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup', 
                [], [], 
                '''                Provide link group name and level
                ''',
                'interface_link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics', 
                [], [], 
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp', 
                [], [], 
                '''                MPLS LDP configuration
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid', 
                [], [], 
                '''                Assign prefix SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sspfsid', REFERENCE_CLASS, 'PrefixSspfsid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid', 
                [], [], 
                '''                Assign prefix SSPF SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sspfsid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The presence of this object allows an
                address-family to be run over the
                interface in question.This must be the
                first object created under the
                InterfaceAddressFamily container, and the
                last one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights', 
                [], [], 
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-af-data',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlagEnum', 
                [], [], 
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClearEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClearEnum', 
                [], [], 
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlagEnum', 
                [], [], 
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsissidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidEnum', 
                [], [], 
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('frrlfa-candidate-interface', REFERENCE_LIST, 'FrrlfaCandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface', 
                [], [], 
                '''                Include an interface to LFA candidate
                in computation
                ''',
                'frrlfa_candidate_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('max-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Value of the metric
                ''',
                'max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-max-metric', REFERENCE_LIST, 'FrrRemoteLfaMaxMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric', 
                [], [], 
                '''                Configure the maximum metric for
                selecting a remote LFA node
                ''',
                'frr_remote_lfa_max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-type',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes',
            False, 
            [
            _MetaInfoClassMember('frr-type', REFERENCE_LIST, 'FrrType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType', 
                [], [], 
                '''                Type of computation for prefixes
                reachable via interface
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-types',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsisRemoteLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfaEnum', 
                [], [], 
                '''                Remote LFA Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-type',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-type', REFERENCE_LIST, 'FrrRemoteLfaType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType', 
                [], [], 
                '''                Enable remote lfa for a particular
                level
                ''',
                'frr_remote_lfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-types',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-default',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker-default', REFERENCE_LIST, 'InterfaceFrrTiebreakerDefault' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault', 
                [], [], 
                '''                Configure default tiebreaker
                ''',
                'interface_frr_tiebreaker_default',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-type',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes',
            False, 
            [
            _MetaInfoClassMember('frrtilfa-type', REFERENCE_LIST, 'FrrtilfaType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType', 
                [], [], 
                '''                Enable TI lfa for a particular level
                ''',
                'frrtilfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-types',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'IsisfrrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrEnum', 
                [], [], 
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('frr-exclude-interface', REFERENCE_LIST, 'FrrExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface', 
                [], [], 
                '''                Exclude an interface from computation
                ''',
                'frr_exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisInterfaceFrrTiebreakerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreakerEnum', 
                [], [], 
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker', REFERENCE_LIST, 'InterfaceFrrTiebreaker' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker', 
                [], [], 
                '''                Configure tiebreaker for multiple
                backups
                ''',
                'interface_frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable',
            False, 
            [
            _MetaInfoClassMember('frr-exclude-interfaces', REFERENCE_CLASS, 'FrrExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces', 
                [], [], 
                '''                FRR exclusion configuration
                ''',
                'frr_exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-max-metrics', REFERENCE_CLASS, 'FrrRemoteLfaMaxMetrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics', 
                [], [], 
                '''                Remote LFA maxmimum metric
                ''',
                'frr_remote_lfa_max_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-types', REFERENCE_CLASS, 'FrrRemoteLfaTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes', 
                [], [], 
                '''                Remote LFA Enable
                ''',
                'frr_remote_lfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-types', REFERENCE_CLASS, 'FrrTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes', 
                [], [], 
                '''                Type of FRR computation per level
                ''',
                'frr_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrlfa-candidate-interfaces', REFERENCE_CLASS, 'FrrlfaCandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces', 
                [], [], 
                '''                FRR LFA candidate configuration
                ''',
                'frrlfa_candidate_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrtilfa-types', REFERENCE_CLASS, 'FrrtilfaTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes', 
                [], [], 
                '''                TI LFA Enable
                ''',
                'frrtilfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreaker-defaults', REFERENCE_CLASS, 'InterfaceFrrTiebreakerDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults', 
                [], [], 
                '''                Interface FRR Default tiebreaker
                configuration
                ''',
                'interface_frr_tiebreaker_defaults',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreakers', REFERENCE_CLASS, 'InterfaceFrrTiebreakers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers', 
                [], [], 
                '''                Interface FRR tiebreakers configuration
                ''',
                'interface_frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-table',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp',
            False, 
            [
            _MetaInfoClassMember('sync-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Enable MPLS LDP Synchronization for an
                IS-IS level
                ''',
                'sync_level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlagEnum', 
                [], [], 
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClearEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClearEnum', 
                [], [], 
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlagEnum', 
                [], [], 
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsissidEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidEnum', 
                [], [], 
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sspfsid',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('proactive-protect', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Allowed auto metric:<1-63> for narrow
                ,<1-16777214> for wide
                ''',
                'proactive_protect',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics',
            False, 
            [
            _MetaInfoClassMember('auto-metric', REFERENCE_LIST, 'AutoMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric', 
                [], [], 
                '''                AutoMetric Proactive-Protect
                configuration. Legal value depends on
                the metric-style specified for the
                topology. If the metric-style defined is
                narrow, then only a value between <1-63>
                is allowed and if the metric-style is
                defined as wide, then a value between
                <1-16777214> is allowed as the
                auto-metric value.
                ''',
                'auto_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tag to associate with connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags',
            False, 
            [
            _MetaInfoClassMember('admin-tag', REFERENCE_LIST, 'AdminTag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag', 
                [], [], 
                '''                Admin tag for advertised interface
                connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tags',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                Level in which link group will be
                effective
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('link-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Link Group
                ''',
                'link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-link-group',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum' : _MetaInfoEnum('MetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum', 
                        [], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                        [('1', '16777215')], [], 
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric', 
                [], [], 
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight', 
                [], [], 
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName',
            False, 
            [
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Topology Name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tags', REFERENCE_CLASS, 'AdminTags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags', 
                [], [], 
                '''                admin-tag configuration
                ''',
                'admin_tags',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('auto-metrics', REFERENCE_CLASS, 'AutoMetrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics', 
                [], [], 
                '''                AutoMetric configuration
                ''',
                'auto_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-af-state', REFERENCE_ENUM_CLASS, 'IsisInterfaceAfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'interface_af_state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-table', REFERENCE_CLASS, 'InterfaceFrrTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable', 
                [], [], 
                '''                Fast-ReRoute configuration
                ''',
                'interface_frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-link-group', REFERENCE_CLASS, 'InterfaceLinkGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup', 
                [], [], 
                '''                Provide link group name and level
                ''',
                'interface_link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics', 
                [], [], 
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp', 
                [], [], 
                '''                MPLS LDP configuration
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid', 
                [], [], 
                '''                Assign prefix SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sspfsid', REFERENCE_CLASS, 'PrefixSspfsid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid', 
                [], [], 
                '''                Assign prefix SSPF SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sspfsid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The presence of this object allows an
                address-family to be run over the
                interface in question.This must be the
                first object created under the
                InterfaceAddressFamily container, and the
                last one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights', 
                [], [], 
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'topology-name',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'IsisAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'IsisSubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamilyEnum', 
                [], [], 
                '''                Sub address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interface-af-data', REFERENCE_CLASS, 'InterfaceAfData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData', 
                [], [], 
                '''                Data container.
                ''',
                'interface_af_data',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-name', REFERENCE_LIST, 'TopologyName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName', 
                [], [], 
                '''                keys: topology-name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-af',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs',
            False, 
            [
            _MetaInfoClassMember('interface-af', REFERENCE_LIST, 'InterfaceAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf', 
                [], [], 
                '''                Configuration for an IS-IS address-family
                on a single interface. If a named
                (non-default) topology is being created it
                must be multicast. Also the topology ID
                mustbe set first and delete last in the
                router configuration.
                ''',
                'interface_af',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'csnp-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals',
            False, 
            [
            _MetaInfoClassMember('csnp-interval', REFERENCE_LIST, 'CsnpInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval', 
                [], [], 
                '''                CSNP-interval configuration. No fixed
                default value as this depends on the media
                type of the interface.
                ''',
                'csnp_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'csnp-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevelEnum', 
                [], [], 
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Milliseconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspIntervals',
            False, 
            [
            _MetaInfoClassMember('lsp-interval', REFERENCE_LIST, 'LspInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval', 
                [], [], 
                '''                Interval between transmission of LSPs on
                interface.
                ''',
                'lsp_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-intervals',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.MeshGroupEnum' : _MetaInfoEnum('MeshGroupEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        {
            'blocked':'blocked',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('circuit-type', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                Configure circuit type for interface
                ''',
                'circuit_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('csnp-intervals', REFERENCE_CLASS, 'CsnpIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals', 
                [], [], 
                '''                CSNP-interval configuration
                ''',
                'csnp_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-accept-passwords', REFERENCE_CLASS, 'HelloAcceptPasswords' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords', 
                [], [], 
                '''                IIH accept password configuration
                ''',
                'hello_accept_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-intervals', REFERENCE_CLASS, 'HelloIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals', 
                [], [], 
                '''                Hello-interval configuration
                ''',
                'hello_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-multipliers', REFERENCE_CLASS, 'HelloMultipliers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers', 
                [], [], 
                '''                Hello-multiplier configuration
                ''',
                'hello_multipliers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-paddings', REFERENCE_CLASS, 'HelloPaddings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings', 
                [], [], 
                '''                Hello-padding configuration
                ''',
                'hello_paddings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-passwords', REFERENCE_CLASS, 'HelloPasswords' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords', 
                [], [], 
                '''                IIH password configuration
                ''',
                'hello_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-afs', REFERENCE_CLASS, 'InterfaceAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs', 
                [], [], 
                '''                Per-interface address-family configuration
                ''',
                'interface_afs',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure high priority detection of
                interface down event
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-fast-flood-thresholds', REFERENCE_CLASS, 'LspFastFloodThresholds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds', 
                [], [], 
                '''                LSP fast flood threshold configuration
                ''',
                'lsp_fast_flood_thresholds',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-intervals', REFERENCE_CLASS, 'LspIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspIntervals', 
                [], [], 
                '''                LSP-interval configuration
                ''',
                'lsp_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-retransmit-intervals', REFERENCE_CLASS, 'LspRetransmitIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals', 
                [], [], 
                '''                LSP-retransmission-interval configuration
                ''',
                'lsp_retransmit_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-retransmit-throttle-intervals', REFERENCE_CLASS, 'LspRetransmitThrottleIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals', 
                [], [], 
                '''                LSP-retransmission-throttle-interval
                configuration
                ''',
                'lsp_retransmit_throttle_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mesh-group', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mesh-group configuration
                ''',
                'mesh_group',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('mesh-group', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.MeshGroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.MeshGroupEnum', 
                        [], [], 
                        '''                        Mesh-group configuration
                        ''',
                        'mesh_group',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                    _MetaInfoClassMember('mesh-group', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Mesh-group configuration
                        ''',
                        'mesh_group',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                ]),
            _MetaInfoClassMember('point-to-point', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                IS-IS will attempt to form point-to-point
                over LAN adjacencies over this interface.
                ''',
                'point_to_point',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-attribute-n-flag-clears', REFERENCE_CLASS, 'PrefixAttributeNFlagClears' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears', 
                [], [], 
                '''                Prefix attribute N flag clear configuration
                ''',
                'prefix_attribute_n_flag_clears',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priorities', REFERENCE_CLASS, 'Priorities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.Priorities', 
                [], [], 
                '''                DIS-election priority configuration
                ''',
                'priorities',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object must be set before any other
                configuration is supplied for an interface,
                and must be the last per-interface
                configuration object to be removed.
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsisInterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceStateEnum', 
                [], [], 
                '''                Enable/Disable routing
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance.Interfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface', 
                [], [], 
                '''                Configuration for an IS-IS interface
                ''',
                'interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Instance identifier
                ''',
                'instance_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('adjacency-stagger', REFERENCE_CLASS, 'AdjacencyStagger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.AdjacencyStagger', 
                [], [], 
                '''                Stagger ISIS adjacency bring up
                ''',
                'adjacency_stagger',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs', 
                [], [], 
                '''                Per-address-family configuration
                ''',
                'afs',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('distribute', REFERENCE_CLASS, 'Distribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Distribute', 
                [], [], 
                '''                IS-IS Distribute BGP-LS configuration
                ''',
                'distribute',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('dynamic-host-name', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, dynamic hostname resolution is
                disabled, and system IDs will always be
                displayed by show and debug output.
                ''',
                'dynamic_host_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ignore-lsp-errors', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, LSPs recieved with bad checksums will
                result in the purging of that LSP from the LSP
                DB. If FALSE or not set, the received LSP will
                just be ignored.
                ''',
                'ignore_lsp_errors',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('instance-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Instance ID of the IS-IS process
                ''',
                'instance_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces', 
                [], [], 
                '''                Per-interface configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('is-type', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevelsEnum', 
                [], [], 
                '''                IS type of the IS-IS process
                ''',
                'is_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('link-groups', REFERENCE_CLASS, 'LinkGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LinkGroups', 
                [], [], 
                '''                Link Group
                ''',
                'link_groups',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('log-adjacency-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log changes in adjacency state
                ''',
                'log_adjacency_changes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('log-pdu-drops', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log PDU drops
                ''',
                'log_pdu_drops',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-accept-passwords', REFERENCE_CLASS, 'LspAcceptPasswords' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspAcceptPasswords', 
                [], [], 
                '''                LSP/SNP accept password configuration
                ''',
                'lsp_accept_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-arrival-times', REFERENCE_CLASS, 'LspArrivalTimes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspArrivalTimes', 
                [], [], 
                '''                LSP arrival time configuration
                ''',
                'lsp_arrival_times',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-check-intervals', REFERENCE_CLASS, 'LspCheckIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspCheckIntervals', 
                [], [], 
                '''                LSP checksum check interval configuration
                ''',
                'lsp_check_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-generation-intervals', REFERENCE_CLASS, 'LspGenerationIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspGenerationIntervals', 
                [], [], 
                '''                LSP generation-interval configuration
                ''',
                'lsp_generation_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-lifetimes', REFERENCE_CLASS, 'LspLifetimes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspLifetimes', 
                [], [], 
                '''                LSP lifetime configuration
                ''',
                'lsp_lifetimes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-mtus', REFERENCE_CLASS, 'LspMtus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspMtus', 
                [], [], 
                '''                LSP MTU configuration
                ''',
                'lsp_mtus',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-passwords', REFERENCE_CLASS, 'LspPasswords' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspPasswords', 
                [], [], 
                '''                LSP/SNP password configuration
                ''',
                'lsp_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-refresh-intervals', REFERENCE_CLASS, 'LspRefreshIntervals' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspRefreshIntervals', 
                [], [], 
                '''                LSP refresh-interval configuration
                ''',
                'lsp_refresh_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-link-metrics', REFERENCE_CLASS, 'MaxLinkMetrics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.MaxLinkMetrics', 
                [], [], 
                '''                Max Link Metric configuration
                ''',
                'max_link_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nets', REFERENCE_CLASS, 'Nets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Nets', 
                [], [], 
                '''                NET configuration
                ''',
                'nets',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Nsf', 
                [], [], 
                '''                IS-IS NSF configuration
                ''',
                'nsf',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nsr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                IS-IS NSR configuration
                ''',
                'nsr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('overload-bits', REFERENCE_CLASS, 'OverloadBits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.OverloadBits', 
                [], [], 
                '''                LSP overload-bit configuration
                ''',
                'overload_bits',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Flag to indicate that instance should be
                running.  This must be the first object
                created when an IS-IS instance is configured,
                and the last object deleted when it is
                deconfigured.  When this object is deleted,
                the IS-IS instance will exit.
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('srgb', REFERENCE_CLASS, 'Srgb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Srgb', 
                [], [], 
                '''                Segment Routing Global Block configuration
                ''',
                'srgb',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('trace-buffer-size', REFERENCE_CLASS, 'TraceBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.TraceBufferSize', 
                [], [], 
                '''                Trace buffer size configuration
                ''',
                'trace_buffer_size',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('tracing-mode', REFERENCE_ENUM_CLASS, 'IsisTracingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisTracingModeEnum', 
                [], [], 
                '''                Tracing mode configuration
                ''',
                'tracing_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis.Instances' : {
        'meta_info' : _MetaInfoClass('Isis.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance', 
                [], [], 
                '''                Configuration for a single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
    'Isis' : {
        'meta_info' : _MetaInfoClass('Isis',
            False, 
            [
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances', 
                [], [], 
                '''                IS-IS instance configuration
                ''',
                'instances',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg'
        ),
    },
}
_meta_table['Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspGenerationIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspArrivalTimes']['meta_info']
_meta_table['Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.MaxLinkMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs']['meta_info']
_meta_table['Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspRefreshIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspAcceptPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.LspMtus.LspMtu']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspMtus']['meta_info']
_meta_table['Isis.Instances.Instance.LinkGroups.LinkGroup']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LinkGroups']['meta_info']
_meta_table['Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspCheckIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.LspPasswords.LspPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.Nets.Net']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Nets']['meta_info']
_meta_table['Isis.Instances.Instance.LspLifetimes.LspLifetime']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspLifetimes']['meta_info']
_meta_table['Isis.Instances.Instance.OverloadBits.OverloadBit']['meta_info'].parent =_meta_table['Isis.Instances.Instance.OverloadBits']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Srgb']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspGenerationIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspArrivalTimes']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.TraceBufferSize']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.MaxLinkMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.AdjacencyStagger']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Afs']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspRefreshIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Distribute']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspAcceptPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspMtus']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Nsf']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LinkGroups']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspCheckIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Nets']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspLifetimes']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.OverloadBits']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance']['meta_info'].parent =_meta_table['Isis.Instances']['meta_info']
_meta_table['Isis.Instances']['meta_info'].parent =_meta_table['Isis']['meta_info']
