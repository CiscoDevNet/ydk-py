


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IfoperstatusreasonEnum' : _MetaInfoEnum('IfoperstatusreasonEnum', 'ydk.models.cisco_ios_xe.CISCO_TC',
        {
            'other':'other',
            'none':'none',
            'hwFailure':'hwFailure',
            'loopbackDiagFailure':'loopbackDiagFailure',
            'errorDisabled':'errorDisabled',
            'swFailure':'swFailure',
            'linkFailure':'linkFailure',
            'offline':'offline',
            'nonParticipating':'nonParticipating',
            'initializing':'initializing',
            'vsanInactive':'vsanInactive',
            'adminDown':'adminDown',
            'channelAdminDown':'channelAdminDown',
            'channelOperSuspended':'channelOperSuspended',
            'channelConfigurationInProgress':'channelConfigurationInProgress',
            'rcfInProgress':'rcfInProgress',
            'elpFailureIsolation':'elpFailureIsolation',
            'escFailureIsolation':'escFailureIsolation',
            'domainOverlapIsolation':'domainOverlapIsolation',
            'domainAddrAssignFailureIsolation':'domainAddrAssignFailureIsolation',
            'domainOtherSideEportIsolation':'domainOtherSideEportIsolation',
            'domainInvalidRcfReceived':'domainInvalidRcfReceived',
            'domainManagerDisabled':'domainManagerDisabled',
            'zoneMergeFailureIsolation':'zoneMergeFailureIsolation',
            'vsanMismatchIsolation':'vsanMismatchIsolation',
            'parentDown':'parentDown',
            'srcPortNotBound':'srcPortNotBound',
            'interfaceRemoved':'interfaceRemoved',
            'fcotNotPresent':'fcotNotPresent',
            'fcotVendorNotSupported':'fcotVendorNotSupported',
            'incompatibleAdminMode':'incompatibleAdminMode',
            'incompatibleAdminSpeed':'incompatibleAdminSpeed',
            'suspendedByMode':'suspendedByMode',
            'suspendedBySpeed':'suspendedBySpeed',
            'suspendedByWWN':'suspendedByWWN',
            'domainMaxReTxFailure':'domainMaxReTxFailure',
            'eppFailure':'eppFailure',
            'portVsanMismatchIsolation':'portVsanMismatchIsolation',
            'loopbackIsolation':'loopbackIsolation',
            'upgradeInProgress':'upgradeInProgress',
            'incompatibleAdminRxBbCredit':'incompatibleAdminRxBbCredit',
            'incompatibleAdminRxBufferSize':'incompatibleAdminRxBufferSize',
            'portChannelMembersDown':'portChannelMembersDown',
            'zoneRemoteNoRespIsolation':'zoneRemoteNoRespIsolation',
            'firstPortUpAsEport':'firstPortUpAsEport',
            'firstPortNotUp':'firstPortNotUp',
            'peerFCIPPortClosedConnection':'peerFCIPPortClosedConnection',
            'peerFCIPPortResetConnection':'peerFCIPPortResetConnection',
            'fcipPortMaxReTx':'fcipPortMaxReTx',
            'fcipPortKeepAliveTimerExpire':'fcipPortKeepAliveTimerExpire',
            'fcipPortPersistTimerExpire':'fcipPortPersistTimerExpire',
            'fcipPortSrcLinkDown':'fcipPortSrcLinkDown',
            'fcipPortSrcAdminDown':'fcipPortSrcAdminDown',
            'fcipPortAdminCfgChange':'fcipPortAdminCfgChange',
            'fcipSrcPortRemoved':'fcipSrcPortRemoved',
            'fcipSrcModuleNotOnline':'fcipSrcModuleNotOnline',
            'invalidConfig':'invalidConfig',
            'portBindFailure':'portBindFailure',
            'portFabricBindFailure':'portFabricBindFailure',
            'noCommonVsanIsolation':'noCommonVsanIsolation',
            'ficonVsanDown':'ficonVsanDown',
            'invalidAttachment':'invalidAttachment',
            'portBlocked':'portBlocked',
            'incomAdminRxBbCreditPerBuf':'incomAdminRxBbCreditPerBuf',
            'tooManyInvalidFlogis':'tooManyInvalidFlogis',
            'deniedDueToPortBinding':'deniedDueToPortBinding',
            'elpFailureRevMismatch':'elpFailureRevMismatch',
            'elpFailureClassFParamErr':'elpFailureClassFParamErr',
            'elpFailureClassNParamErr':'elpFailureClassNParamErr',
            'elpFailureUnknownFlowCtlCode':'elpFailureUnknownFlowCtlCode',
            'elpFailureInvalidFlowCtlParam':'elpFailureInvalidFlowCtlParam',
            'elpFailureInvalidPortName':'elpFailureInvalidPortName',
            'elpFailureInvalidSwitchName':'elpFailureInvalidSwitchName',
            'elpFailureRatovEdtovMismatch':'elpFailureRatovEdtovMismatch',
            'elpFailureLoopbackDetected':'elpFailureLoopbackDetected',
            'elpFailureInvalidTxBbCredit':'elpFailureInvalidTxBbCredit',
            'elpFailureInvalidPayloadSize':'elpFailureInvalidPayloadSize',
            'bundleMisCfg':'bundleMisCfg',
            'bitErrRuntimeThreshExceeded':'bitErrRuntimeThreshExceeded',
            'linkFailLinkReset':'linkFailLinkReset',
            'linkFailPortInitFail':'linkFailPortInitFail',
            'linkFailPortUnusable':'linkFailPortUnusable',
            'linkFailLossOfSignal':'linkFailLossOfSignal',
            'linkFailLossOfSync':'linkFailLossOfSync',
            'linkFailNosRcvd':'linkFailNosRcvd',
            'linkFailOLSRcvd':'linkFailOLSRcvd',
            'linkFailDebounceTimeout':'linkFailDebounceTimeout',
            'linkFailLrRcvd':'linkFailLrRcvd',
            'linkFailCreditLoss':'linkFailCreditLoss',
            'linkFailRxQOverflow':'linkFailRxQOverflow',
            'linkFailTooManyInterrupts':'linkFailTooManyInterrupts',
            'linkFailLipRcvdBb':'linkFailLipRcvdBb',
            'linkFailBbCreditLoss':'linkFailBbCreditLoss',
            'linkFailOpenPrimSignalTimeout':'linkFailOpenPrimSignalTimeout',
            'linkFailOpenPrimSignalReturned':'linkFailOpenPrimSignalReturned',
            'linkFailLipF8Rcvd':'linkFailLipF8Rcvd',
            'linkFailLineCardPortShutdown':'linkFailLineCardPortShutdown',
            'fcspAuthenfailure':'fcspAuthenfailure',
            'fcotChecksumError':'fcotChecksumError',
            'ohmsExtLoopbackTest':'ohmsExtLoopbackTest',
            'invalidFabricBindExchange':'invalidFabricBindExchange',
            'tovMismatch':'tovMismatch',
            'ficonNotEnabled':'ficonNotEnabled',
            'ficonNoPortNumber':'ficonNoPortNumber',
            'ficonBeingEnabled':'ficonBeingEnabled',
            'ePortProhibited':'ePortProhibited',
            'portGracefulShutdown':'portGracefulShutdown',
            'trunkNotFullyActive':'trunkNotFullyActive',
            'fabricBindingSwitchWwnNotFound':'fabricBindingSwitchWwnNotFound',
            'fabricBindingDomainInvalid':'fabricBindingDomainInvalid',
            'fabricBindingDbMismatch':'fabricBindingDbMismatch',
            'fabricBindingNoRspFromPeer':'fabricBindingNoRspFromPeer',
            'dpvmVsanSuspended':'dpvmVsanSuspended',
            'dpvmVsanNotFound':'dpvmVsanNotFound',
            'trackedPortDown':'trackedPortDown',
            'ecSuspendedOnLoop':'ecSuspendedOnLoop',
            'isolateBundleMisCfg':'isolateBundleMisCfg',
            'noPeerBundleSupport':'noPeerBundleSupport',
            'portBringupIsolation':'portBringupIsolation',
            'domainNotAllowedIsolated':'domainNotAllowedIsolated',
            'virtualIvrDomainOverlapIsolation':'virtualIvrDomainOverlapIsolation',
            'outOfService':'outOfService',
            'portAuthFailed':'portAuthFailed',
            'bundleStandby':'bundleStandby',
            'portConnectorTypeErr':'portConnectorTypeErr',
            'errorDisabledReInitLmtReached':'errorDisabledReInitLmtReached',
            'ficonDupPortNum':'ficonDupPortNum',
            'localRcf':'localRcf',
            'twoSwitchesWithSameWWN':'twoSwitchesWithSameWWN',
            'invalidOtherSidePrincEFPReqRecd':'invalidOtherSidePrincEFPReqRecd',
            'domainOther':'domainOther',
            'elpFailureAllZeroPeerWWNRcvd':'elpFailureAllZeroPeerWWNRcvd',
            'preferredPathIsolation':'preferredPathIsolation',
            'fcRedirectIsolation':'fcRedirectIsolation',
            'portActLicenseNotAvailable':'portActLicenseNotAvailable',
            'sdmIsolation':'sdmIsolation',
            'fcidAllocationFailed':'fcidAllocationFailed',
            'externallyDisabled':'externallyDisabled',
            'unavailableNPVUpstreamPort':'unavailableNPVUpstreamPort',
            'unavailableNPVPrefUpstreamPort':'unavailableNPVPrefUpstreamPort',
            'sfpReadError':'sfpReadError',
            'stickyDownOnLinkFailure':'stickyDownOnLinkFailure',
            'tooManyLinkFlapsErr':'tooManyLinkFlapsErr',
            'unidirectionalUDLD':'unidirectionalUDLD',
            'txRxLoopUDLD':'txRxLoopUDLD',
            'neighborMismatchUDLD':'neighborMismatchUDLD',
            'authzPending':'authzPending',
            'hotStdbyInBundle':'hotStdbyInBundle',
            'incompleteConfig':'incompleteConfig',
            'incompleteTunnelCfg':'incompleteTunnelCfg',
            'hwProgrammingFailed':'hwProgrammingFailed',
            'tunnelDstUnreachable':'tunnelDstUnreachable',
            'suspendByMtu':'suspendByMtu',
            'sfpInvalid':'sfpInvalid',
            'sfpAbsent':'sfpAbsent',
            'portCapabilitiesUnknown':'portCapabilitiesUnknown',
            'channelErrDisabled':'channelErrDisabled',
            'vrfMismatch':'vrfMismatch',
            'vrfForwardReferencing':'vrfForwardReferencing',
            'dupTunnelConfigDetected':'dupTunnelConfigDetected',
            'primaryVLANDown':'primaryVLANDown',
            'vrfUnusable':'vrfUnusable',
            'errDisableHandShkFailure':'errDisableHandShkFailure',
            'errDisabledBPDUGuard':'errDisabledBPDUGuard',
            'dot1xSecViolationErrDisabled':'dot1xSecViolationErrDisabled',
            'emptyEchoUDLD':'emptyEchoUDLD',
            'vfTaggingCapErr':'vfTaggingCapErr',
            'portDisabled':'portDisabled',
            'tunnelModeNotConfigured':'tunnelModeNotConfigured',
            'tunnelSrcNotConfigured':'tunnelSrcNotConfigured',
            'tunnelDstNotConfigured':'tunnelDstNotConfigured',
            'tunnelUnableToResolveSrcIP':'tunnelUnableToResolveSrcIP',
            'tunnelUnableToResolveDstIP':'tunnelUnableToResolveDstIP',
            'tunnelVrfDown':'tunnelVrfDown',
            'sifAdminDown':'sifAdminDown',
            'phyIntfDown':'phyIntfDown',
            'ifSifLimitExceeded':'ifSifLimitExceeded',
            'sifHoldDown':'sifHoldDown',
            'noFcoe':'noFcoe',
            'dcxCompatMismatch':'dcxCompatMismatch',
            'isolateBundleLimitExceeded':'isolateBundleLimitExceeded',
            'sifNotBound':'sifNotBound',
            'errDisabledLacpMiscfg':'errDisabledLacpMiscfg',
            'satFabricIfDown':'satFabricIfDown',
            'invalidSatFabricIf':'invalidSatFabricIf',
            'noRemoteChassis':'noRemoteChassis',
            'vicEnableNotReceived':'vicEnableNotReceived',
            'vicDisableReceived':'vicDisableReceived',
            'vlanVsanMappingNotEnabled':'vlanVsanMappingNotEnabled',
            'stpNotFwdingInFcoeMappedVlan':'stpNotFwdingInFcoeMappedVlan',
            'moduleOffline':'moduleOffline',
            'udldAggModeLinkFailure':'udldAggModeLinkFailure',
            'stpInconsVpcPeerDisabled':'stpInconsVpcPeerDisabled',
            'setPortStateFailed':'setPortStateFailed',
            'suspendedByVpc':'suspendedByVpc',
            'vpcCfgInProgress':'vpcCfgInProgress',
            'vpcPeerLinkDown':'vpcPeerLinkDown',
            'vpcNoRspFromPeer':'vpcNoRspFromPeer',
            'protoPortSuspend':'protoPortSuspend',
            'tunnelSrcDown':'tunnelSrcDown',
            'cdpInfoUnavailable':'cdpInfoUnavailable',
            'fexSfpInvalid':'fexSfpInvalid',
            'errDisabledIpConflict':'errDisabledIpConflict',
            'fcotClkRateMismatch':'fcotClkRateMismatch',
            'portGuardTrustSecViolation':'portGuardTrustSecViolation',
            'sdpTimeout':'sdpTimeout',
            'satIncompatTopo':'satIncompatTopo',
            'waitForFlogi':'waitForFlogi',
            'satNotConfigured':'satNotConfigured',
            'npivNotEnabledInUpstream':'npivNotEnabledInUpstream',
            'vsanMismatchWithUpstreamSwPort':'vsanMismatchWithUpstreamSwPort',
            'portGuardBitErrRate':'portGuardBitErrRate',
            'portGuardSigLoss':'portGuardSigLoss',
            'portGuardSyncLoss':'portGuardSyncLoss',
            'portGuardLinkReset':'portGuardLinkReset',
            'portGuardCreditLoss':'portGuardCreditLoss',
            'ipQosMgrPolicyAppFailure':'ipQosMgrPolicyAppFailure',
            'pauseRateLimitErrDisabled':'pauseRateLimitErrDisabled',
            'lstGrpUplinkDown':'lstGrpUplinkDown',
            'stickyDnLinkFailure':'stickyDnLinkFailure',
            'routerMacFailure':'routerMacFailure',
            'dcxMultipleMsapIds':'dcxMultipleMsapIds',
            'dcxHundredPdusRcvdNoAck':'dcxHundredPdusRcvdNoAck',
            'enmSatIncompatibleUplink':'enmSatIncompatibleUplink',
            'enmLoopDetected':'enmLoopDetected',
            'nonStickyExternallyDisabled':'nonStickyExternallyDisabled',
            'subGroupIdNotAssigned':'subGroupIdNotAssigned',
            'vemUnlicensed':'vemUnlicensed',
            'profileNotFound':'profileNotFound',
            'nonExistentVlan':'nonExistentVlan',
            'vlanInvalidType':'vlanInvalidType',
            'vlanDown':'vlanDown',
            'vpcPeerUpgrade':'vpcPeerUpgrade',
            'ipQosDcbxpCompatFailure':'ipQosDcbxpCompatFailure',
            'nonCiscoHbaVfTag':'nonCiscoHbaVfTag',
            'domainIdConfigMismatch':'domainIdConfigMismatch',
            'sfpSpeedMismatch':'sfpSpeedMismatch',
            'xcvrInitializing':'xcvrInitializing',
            'xcvrAbsent':'xcvrAbsent',
            'xcvrInvalid':'xcvrInvalid',
            'vfcBindingInvalid':'vfcBindingInvalid',
            'vlanNotFcoeEnabled':'vlanNotFcoeEnabled',
            'pvlanNativeVlanErr':'pvlanNativeVlanErr',
            'ethL2VlanDown':'ethL2VlanDown',
            'ethIntfInvalidBinding':'ethIntfInvalidBinding',
            'pmonFailure':'pmonFailure',
            'l3NotReady':'l3NotReady',
            'speedMismatch':'speedMismatch',
            'flowControlMismatch':'flowControlMismatch',
            'vdcMode':'vdcMode',
            'suspendedDueToMinLinks':'suspendedDueToMinLinks',
            'enmPinFailLinkDown':'enmPinFailLinkDown',
            'inactiveM1PortFpathActiveVlan':'inactiveM1PortFpathActiveVlan',
            'parentPortDown':'parentPortDown',
            'moduleRemoved':'moduleRemoved',
            'corePortMct':'corePortMct',
            'nonCorePortMct':'nonCorePortMct',
            'ficonInorderNotActive':'ficonInorderNotActive',
            'invalidEncapsulation':'invalidEncapsulation',
            'modemLineDeasserted':'modemLineDeasserted',
            'ipSecHndshkInProgress':'ipSecHndshkInProgress',
            'sfpEthCompliantErr':'sfpEthCompliantErr',
            'cellularModemUnattached':'cellularModemUnattached',
            'outOfGlblRxBuffers':'outOfGlblRxBuffers',
            'sfpFcCompliantErr':'sfpFcCompliantErr',
            'ethIntfNotLicensed':'ethIntfNotLicensed',
            'domainIdsInvalid':'domainIdsInvalid',
            'fabricNameInvalid':'fabricNameInvalid',
        }, 'CISCO-TC', _yang_ns._namespaces['CISCO-TC']),
    'CisconetworkprotocolEnum' : _MetaInfoEnum('CisconetworkprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_TC',
        {
            'ip':'ip',
            'decnet':'decnet',
            'pup':'pup',
            'chaos':'chaos',
            'xns':'xns',
            'x121':'x121',
            'appletalk':'appletalk',
            'clns':'clns',
            'lat':'lat',
            'vines':'vines',
            'cons':'cons',
            'apollo':'apollo',
            'stun':'stun',
            'novell':'novell',
            'qllc':'qllc',
            'snapshot':'snapshot',
            'atmIlmi':'atmIlmi',
            'bstun':'bstun',
            'x25pvc':'x25pvc',
            'ipv6':'ipv6',
            'cdm':'cdm',
            'nbf':'nbf',
            'bpxIgx':'bpxIgx',
            'clnsPfx':'clnsPfx',
            'http':'http',
            'unknown':'unknown',
        }, 'CISCO-TC', _yang_ns._namespaces['CISCO-TC']),
    'CiscoalarmseverityEnum' : _MetaInfoEnum('CiscoalarmseverityEnum', 'ydk.models.cisco_ios_xe.CISCO_TC',
        {
            'cleared':'cleared',
            'indeterminate':'indeterminate',
            'critical':'critical',
            'major':'major',
            'minor':'minor',
            'warning':'warning',
            'info':'info',
        }, 'CISCO-TC', _yang_ns._namespaces['CISCO-TC']),
    'CiscoportlistrangeEnum' : _MetaInfoEnum('CiscoportlistrangeEnum', 'ydk.models.cisco_ios_xe.CISCO_TC',
        {
            'oneto2k':'oneto2k',
            'twoKto4K':'twoKto4K',
            'fourKto6K':'fourKto6K',
            'sixKto8K':'sixKto8K',
            'eightKto10K':'eightKto10K',
            'tenKto12K':'tenKto12K',
            'twelveKto14K':'twelveKto14K',
            'fourteenKto16K':'fourteenKto16K',
        }, 'CISCO-TC', _yang_ns._namespaces['CISCO-TC']),
    'CiscolocationclassEnum' : _MetaInfoEnum('CiscolocationclassEnum', 'ydk.models.cisco_ios_xe.CISCO_TC',
        {
            'chassis':'chassis',
            'shelf':'shelf',
            'slot':'slot',
            'subSlot':'subSlot',
            'port':'port',
            'subPort':'subPort',
            'channel':'channel',
            'subChannel':'subChannel',
        }, 'CISCO-TC', _yang_ns._namespaces['CISCO-TC']),
    'CiscorowoperstatusEnum' : _MetaInfoEnum('CiscorowoperstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_TC',
        {
            'active':'active',
            'activeDependencies':'activeDependencies',
            'inactiveDependency':'inactiveDependency',
            'missingDependency':'missingDependency',
        }, 'CISCO-TC', _yang_ns._namespaces['CISCO-TC']),
}
