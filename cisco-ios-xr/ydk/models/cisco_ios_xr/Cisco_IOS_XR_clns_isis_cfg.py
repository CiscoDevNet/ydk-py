""" Cisco_IOS_XR_clns_isis_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR clns\-isis package configuration.

This module contains definitions
for the following management objects\:
  isis\: IS\-IS configuration for all instances

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IsisAdjCheckEnum(Enum):
    """
    IsisAdjCheckEnum

    Isis adj check

    .. data:: disabled = 0

    	Disabled

    """

    disabled = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAdjCheckEnum']


class IsisAdvTypeExternalEnum(Enum):
    """
    IsisAdvTypeExternalEnum

    Isis adv type external

    .. data:: external = 1

    	External

    """

    external = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAdvTypeExternalEnum']


class IsisAdvTypeInterLevelEnum(Enum):
    """
    IsisAdvTypeInterLevelEnum

    Isis adv type inter level

    .. data:: inter_level = 1

    	InterLevel

    """

    inter_level = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAdvTypeInterLevelEnum']


class IsisApplyWeightEnum(Enum):
    """
    IsisApplyWeightEnum

    Isis apply weight

    .. data:: ecmp_only = 1

    	Apply weight to ECMP prefixes

    .. data:: ucmp_only = 2

    	Apply weight to UCMP prefixes

    """

    ecmp_only = 1

    ucmp_only = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisApplyWeightEnum']


class IsisAttachedBitEnum(Enum):
    """
    IsisAttachedBitEnum

    Isis attached bit

    .. data:: area = 0

    	Computed from the attached areas

    .. data:: on = 1

    	Forced ON

    .. data:: off = 2

    	Forced OFF

    """

    area = 0

    on = 1

    off = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAttachedBitEnum']


class IsisAuthenticationAlgorithmEnum(Enum):
    """
    IsisAuthenticationAlgorithmEnum

    Isis authentication algorithm

    .. data:: cleartext = 1

    	Cleartext password

    .. data:: hmac_md5 = 2

    	HMAC-MD5 checksum

    .. data:: keychain = 3

    	Key Chain authentication

    """

    cleartext = 1

    hmac_md5 = 2

    keychain = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAuthenticationAlgorithmEnum']


class IsisAuthenticationFailureModeEnum(Enum):
    """
    IsisAuthenticationFailureModeEnum

    Isis authentication failure mode

    .. data:: drop = 0

    	Drop non-authenticating PDUs

    .. data:: send_only = 1

    	Accept non-authenticating PDUs

    """

    drop = 0

    send_only = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAuthenticationFailureModeEnum']


class IsisConfigurableLevelsEnum(Enum):
    """
    IsisConfigurableLevelsEnum

    Isis configurable levels

    .. data:: level1 = 1

    	Level1

    .. data:: level2 = 2

    	Level2

    .. data:: level1_and2 = 3

    	Both Levels

    """

    level1 = 1

    level2 = 2

    level1_and2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisConfigurableLevelsEnum']


class IsisHelloPaddingEnum(Enum):
    """
    IsisHelloPaddingEnum

    Isis hello padding

    .. data:: never = 0

    	Never pad Hellos

    .. data:: sometimes = 1

    	Pad Hellos during adjacency formation only

    """

    never = 0

    sometimes = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisHelloPaddingEnum']


class IsisInterfaceAfStateEnum(Enum):
    """
    IsisInterfaceAfStateEnum

    Isis interface af state

    .. data:: disable = 0

    	Disable

    """

    disable = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisInterfaceAfStateEnum']


class IsisInterfaceFrrTiebreakerEnum(Enum):
    """
    IsisInterfaceFrrTiebreakerEnum

    Isis interface frr tiebreaker

    .. data:: node_protecting = 3

    	Prefer node protecting backup path

    .. data:: srlg_disjoint = 6

    	Prefer SRLG disjoint backup path

    """

    node_protecting = 3

    srlg_disjoint = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisInterfaceFrrTiebreakerEnum']


class IsisInterfaceStateEnum(Enum):
    """
    IsisInterfaceStateEnum

    Isis interface state

    .. data:: shutdown = 0

    	Shutdown

    .. data:: suppressed = 1

    	Suppressed

    .. data:: passive = 2

    	Passive

    """

    shutdown = 0

    suppressed = 1

    passive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisInterfaceStateEnum']


class IsisLabelPreferenceEnum(Enum):
    """
    IsisLabelPreferenceEnum

    Isis label preference

    .. data:: ldp = 0

    	Label Distribution Protocol

    .. data:: segment_routing = 1

    	Segment Routing

    """

    ldp = 0

    segment_routing = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisLabelPreferenceEnum']


class IsisMetricEnum(Enum):
    """
    IsisMetricEnum

    Isis metric

    .. data:: internal = 0

    	Internal metric

    .. data:: external = 1

    	External metric

    """

    internal = 0

    external = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMetricEnum']


class IsisMetricStyleEnum(Enum):
    """
    IsisMetricStyleEnum

    Isis metric style

    .. data:: old_metric_style = 0

    	ISO 10589 metric style (old-style)

    .. data:: new_metric_style = 1

    	32-bit metric style (new-style)

    .. data:: both_metric_style = 2

    	Both forms of metric style

    """

    old_metric_style = 0

    new_metric_style = 1

    both_metric_style = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMetricStyleEnum']


class IsisMetricStyleTransitionEnum(Enum):
    """
    IsisMetricStyleTransitionEnum

    Isis metric style transition

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMetricStyleTransitionEnum']


class IsisMibAdjacencyChangeBooleanEnum(Enum):
    """
    IsisMibAdjacencyChangeBooleanEnum

    Isis mib adjacency change boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 17

    	Enable

    """

    false = 0

    true = 17


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAdjacencyChangeBooleanEnum']


class IsisMibAllBooleanEnum(Enum):
    """
    IsisMibAllBooleanEnum

    Isis mib all boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 19

    	Enable

    """

    false = 0

    true = 19


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAllBooleanEnum']


class IsisMibAreaMismatchBooleanEnum(Enum):
    """
    IsisMibAreaMismatchBooleanEnum

    Isis mib area mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 12

    	Enable

    """

    false = 0

    true = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAreaMismatchBooleanEnum']


class IsisMibAttemptToExceedMaxSequenceBooleanEnum(Enum):
    """
    IsisMibAttemptToExceedMaxSequenceBooleanEnum

    Isis mib attempt to exceed max sequence boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 4

    	Enable

    """

    false = 0

    true = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAttemptToExceedMaxSequenceBooleanEnum']


class IsisMibAuthenticationFailureBooleanEnum(Enum):
    """
    IsisMibAuthenticationFailureBooleanEnum

    Isis mib authentication failure boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 10

    	Enable

    """

    false = 0

    true = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAuthenticationFailureBooleanEnum']


class IsisMibAuthenticationTypeFailureBooleanEnum(Enum):
    """
    IsisMibAuthenticationTypeFailureBooleanEnum

    Isis mib authentication type failure boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 9

    	Enable

    """

    false = 0

    true = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAuthenticationTypeFailureBooleanEnum']


class IsisMibCorruptedLspDetectedBooleanEnum(Enum):
    """
    IsisMibCorruptedLspDetectedBooleanEnum

    Isis mib corrupted lsp detected boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 3

    	Enable

    """

    false = 0

    true = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibCorruptedLspDetectedBooleanEnum']


class IsisMibDatabaseOverFlowBooleanEnum(Enum):
    """
    IsisMibDatabaseOverFlowBooleanEnum

    Isis mib database over flow boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 1

    	Enable

    """

    false = 0

    true = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibDatabaseOverFlowBooleanEnum']


class IsisMibIdLengthMismatchBooleanEnum(Enum):
    """
    IsisMibIdLengthMismatchBooleanEnum

    Isis mib id length mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 5

    	Enable

    """

    false = 0

    true = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibIdLengthMismatchBooleanEnum']


class IsisMibLspErrorDetectedBooleanEnum(Enum):
    """
    IsisMibLspErrorDetectedBooleanEnum

    Isis mib lsp error detected boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 18

    	Enable

    """

    false = 0

    true = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibLspErrorDetectedBooleanEnum']


class IsisMibLspTooLargeToPropagateBooleanEnum(Enum):
    """
    IsisMibLspTooLargeToPropagateBooleanEnum

    Isis mib lsp too large to propagate boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 14

    	Enable

    """

    false = 0

    true = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibLspTooLargeToPropagateBooleanEnum']


class IsisMibManualAddressDropsBooleanEnum(Enum):
    """
    IsisMibManualAddressDropsBooleanEnum

    Isis mib manual address drops boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 2

    	Enable

    """

    false = 0

    true = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibManualAddressDropsBooleanEnum']


class IsisMibMaxAreaAddressMismatchBooleanEnum(Enum):
    """
    IsisMibMaxAreaAddressMismatchBooleanEnum

    Isis mib max area address mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 6

    	Enable

    """

    false = 0

    true = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibMaxAreaAddressMismatchBooleanEnum']


class IsisMibOriginatedLspBufferSizeMismatchBooleanEnum(Enum):
    """
    IsisMibOriginatedLspBufferSizeMismatchBooleanEnum

    Isis mib originated lsp buffer size mismatch

    boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 15

    	Enable

    """

    false = 0

    true = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibOriginatedLspBufferSizeMismatchBooleanEnum']


class IsisMibOwnLspPurgeBooleanEnum(Enum):
    """
    IsisMibOwnLspPurgeBooleanEnum

    Isis mib own lsp purge boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 7

    	Enable

    """

    false = 0

    true = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibOwnLspPurgeBooleanEnum']


class IsisMibProtocolsSupportedMismatchBooleanEnum(Enum):
    """
    IsisMibProtocolsSupportedMismatchBooleanEnum

    Isis mib protocols supported mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 16

    	Enable

    """

    false = 0

    true = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibProtocolsSupportedMismatchBooleanEnum']


class IsisMibRejectedAdjacencyBooleanEnum(Enum):
    """
    IsisMibRejectedAdjacencyBooleanEnum

    Isis mib rejected adjacency boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 13

    	Enable

    """

    false = 0

    true = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibRejectedAdjacencyBooleanEnum']


class IsisMibSequenceNumberSkipBooleanEnum(Enum):
    """
    IsisMibSequenceNumberSkipBooleanEnum

    Isis mib sequence number skip boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 8

    	Enable

    """

    false = 0

    true = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibSequenceNumberSkipBooleanEnum']


class IsisMibVersionSkewBooleanEnum(Enum):
    """
    IsisMibVersionSkewBooleanEnum

    Isis mib version skew boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 11

    	Enable

    """

    false = 0

    true = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibVersionSkewBooleanEnum']


class IsisMicroLoopAvoidanceEnum(Enum):
    """
    IsisMicroLoopAvoidanceEnum

    Isis micro loop avoidance

    .. data:: not_set = 0

    	No Avoidance type set

    .. data:: micro_loop_avoidance_all = 1

    	Provide mirco loop avoidance for all prefixes

    .. data:: micro_loop_avoidance_protected = 2

    	Provide mirco loop avoidance only for protected

    	prefixes

    .. data:: micro_loop_avoidance_segement_routing = 3

    	Provide segment-routing mirco loop avoidance

    """

    not_set = 0

    micro_loop_avoidance_all = 1

    micro_loop_avoidance_protected = 2

    micro_loop_avoidance_segement_routing = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMicroLoopAvoidanceEnum']


class IsisNsfFlavorEnum(Enum):
    """
    IsisNsfFlavorEnum

    Isis nsf flavor

    .. data:: cisco_proprietary_nsf = 1

    	Cisco proprietary NSF

    .. data:: ietf_standard_nsf = 2

    	IETF standard NSF

    """

    cisco_proprietary_nsf = 1

    ietf_standard_nsf = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisNsfFlavorEnum']


class IsisOverloadBitModeEnum(Enum):
    """
    IsisOverloadBitModeEnum

    Isis overload bit mode

    .. data:: permanently_set = 1

    	Set always

    .. data:: startup_period = 2

    	Set during the startup period

    .. data:: wait_for_bgp = 3

    	Set until BGP comverges

    """

    permanently_set = 1

    startup_period = 2

    wait_for_bgp = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisOverloadBitModeEnum']


class IsisPrefixPriorityEnum(Enum):
    """
    IsisPrefixPriorityEnum

    Isis prefix priority

    .. data:: critical_priority = 0

    	Critical prefix priority

    .. data:: high_priority = 1

    	High prefix priority

    .. data:: medium_priority = 2

    	Medium prefix priority

    """

    critical_priority = 0

    high_priority = 1

    medium_priority = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisPrefixPriorityEnum']


class IsisRedistProtoEnum(Enum):
    """
    IsisRedistProtoEnum

    Isis redist proto

    .. data:: connected = 0

    	Connected

    .. data:: static = 1

    	Static

    .. data:: ospf = 2

    	OSPF

    .. data:: bgp = 3

    	BGP

    .. data:: isis = 4

    	ISIS

    .. data:: ospfv3 = 5

    	OSPFv3

    .. data:: rip = 6

    	RIP

    .. data:: eigrp = 7

    	EIGRP

    .. data:: subscriber = 8

    	Subscriber

    .. data:: application = 9

    	Application

    .. data:: mobile = 10

    	Mobile

    """

    connected = 0

    static = 1

    ospf = 2

    bgp = 3

    isis = 4

    ospfv3 = 5

    rip = 6

    eigrp = 7

    subscriber = 8

    application = 9

    mobile = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisRedistProtoEnum']


class IsisRemoteLfaEnum(Enum):
    """
    IsisRemoteLfaEnum

    Isis remote lfa

    .. data:: remote_lfa_none = 0

    	No remote LFA option set

    .. data:: remote_lfa_tunnel_ldp = 1

    	Construct remote LFA tunnel using MPLS LDP

    """

    remote_lfa_none = 0

    remote_lfa_tunnel_ldp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisRemoteLfaEnum']


class IsisSnpAuthEnum(Enum):
    """
    IsisSnpAuthEnum

    Isis snp auth

    .. data:: send_only = 0

    	Authenticate SNP send only

    .. data:: full = 1

    	Authenticate SNP send and recv

    """

    send_only = 0

    full = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisSnpAuthEnum']


class IsisTracingModeEnum(Enum):
    """
    IsisTracingModeEnum

    Isis tracing mode

    .. data:: off = 0

    	No tracing

    .. data:: basic = 1

    	Basic tracing (less overhead)

    .. data:: enhanced = 2

    	Enhanced tracing (more overhead)

    """

    off = 0

    basic = 1

    enhanced = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisTracingModeEnum']


class IsisexplicitNullFlagEnum(Enum):
    """
    IsisexplicitNullFlagEnum

    Isisexplicit null flag

    .. data:: disable = 0

    	Disable EXPLICITNULL

    .. data:: enable = 1

    	Enable EXPLICITNULL

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisexplicitNullFlagEnum']


class IsisfrrEnum(Enum):
    """
    IsisfrrEnum

    Isisfrr

    .. data:: per_link = 1

    	Prefix independent per-link computation

    .. data:: per_prefix = 2

    	Prefix dependent computation

    """

    per_link = 1

    per_prefix = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisfrrEnum']


class IsisfrrLoadSharingEnum(Enum):
    """
    IsisfrrLoadSharingEnum

    Isisfrr load sharing

    .. data:: disable = 1

    	Disable load sharing of prefixes across

    	multiple backups

    """

    disable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisfrrLoadSharingEnum']


class IsisfrrTiebreakerEnum(Enum):
    """
    IsisfrrTiebreakerEnum

    Isisfrr tiebreaker

    .. data:: downstream = 0

    	Prefer backup path via downstream node

    .. data:: lc_disjoint = 1

    	Prefer line card disjoint backup path

    .. data:: lowest_backup_metric = 2

    	Prefer backup path with lowest total metric

    .. data:: node_protecting = 3

    	Prefer node protecting backup path

    .. data:: primary_path = 4

    	Prefer backup path from ECMP set

    .. data:: secondary_path = 5

    	Prefer non-ECMP backup path

    .. data:: srlg_disjoint = 6

    	Prefer SRLG disjoint backup path

    """

    downstream = 0

    lc_disjoint = 1

    lowest_backup_metric = 2

    node_protecting = 3

    primary_path = 4

    secondary_path = 5

    srlg_disjoint = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisfrrTiebreakerEnum']


class IsisispfStateEnum(Enum):
    """
    IsisispfStateEnum

    Isisispf state

    .. data:: enabled = 1

    	Enabled

    """

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisispfStateEnum']


class IsisphpFlagEnum(Enum):
    """
    IsisphpFlagEnum

    Isisphp flag

    .. data:: enable = 0

    	Enable PHP

    .. data:: disable = 1

    	Disable PHP

    """

    enable = 0

    disable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisphpFlagEnum']


class IsissidEnum(Enum):
    """
    IsissidEnum

    Isissid

    .. data:: index = 1

    	SID as an index

    .. data:: absolute = 2

    	SID as an absolute label

    """

    index = 1

    absolute = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsissidEnum']


class NflagClearEnum(Enum):
    """
    NflagClearEnum

    Nflag clear

    .. data:: disable = 0

    	Disable N-flag-clear

    .. data:: enable = 1

    	Enable N-flag-clear

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['NflagClearEnum']



class Isis(object):
    """
    IS\-IS configuration for all instances
    
    .. attribute:: instances
    
    	IS\-IS instance configuration
    	**type**\:   :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances>`
    
    

    """

    _prefix = 'clns-isis-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.instances = Isis.Instances()
        self.instances.parent = self


    class Instances(object):
        """
        IS\-IS instance configuration
        
        .. attribute:: instance
        
        	Configuration for a single IS\-IS instance
        	**type**\: list of    :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance>`
        
        

        """

        _prefix = 'clns-isis-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.instance = YList()
            self.instance.parent = self
            self.instance.name = 'instance'


        class Instance(object):
            """
            Configuration for a single IS\-IS instance
            
            .. attribute:: instance_name  <key>
            
            	Instance identifier
            	**type**\:  str
            
            	**length:** 1..40
            
            .. attribute:: adjacency_stagger
            
            	Stagger ISIS adjacency bring up
            	**type**\:   :py:class:`AdjacencyStagger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.AdjacencyStagger>`
            
            	**presence node**\: True
            
            .. attribute:: afs
            
            	Per\-address\-family configuration
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs>`
            
            .. attribute:: distribute
            
            	IS\-IS Distribute BGP\-LS configuration
            	**type**\:   :py:class:`Distribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Distribute>`
            
            	**presence node**\: True
            
            .. attribute:: dynamic_host_name
            
            	If TRUE, dynamic hostname resolution is disabled, and system IDs will always be displayed by show and debug output
            	**type**\:  bool
            
            .. attribute:: ignore_lsp_errors
            
            	If TRUE, LSPs recieved with bad checksums will result in the purging of that LSP from the LSP DB. If FALSE or not set, the received LSP will just be ignored
            	**type**\:  bool
            
            .. attribute:: instance_id
            
            	Instance ID of the IS\-IS process
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: interfaces
            
            	Per\-interface configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces>`
            
            .. attribute:: is_type
            
            	IS type of the IS\-IS process
            	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
            
            	**default value**\: level1-and2
            
            .. attribute:: link_groups
            
            	Link Group
            	**type**\:   :py:class:`LinkGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups>`
            
            .. attribute:: log_adjacency_changes
            
            	Log changes in adjacency state
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_pdu_drops
            
            	Log PDU drops
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lsp_accept_passwords
            
            	LSP/SNP accept password configuration
            	**type**\:   :py:class:`LspAcceptPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords>`
            
            .. attribute:: lsp_arrival_times
            
            	LSP arrival time configuration
            	**type**\:   :py:class:`LspArrivalTimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes>`
            
            .. attribute:: lsp_check_intervals
            
            	LSP checksum check interval configuration
            	**type**\:   :py:class:`LspCheckIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals>`
            
            .. attribute:: lsp_generation_intervals
            
            	LSP generation\-interval configuration
            	**type**\:   :py:class:`LspGenerationIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals>`
            
            .. attribute:: lsp_lifetimes
            
            	LSP lifetime configuration
            	**type**\:   :py:class:`LspLifetimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes>`
            
            .. attribute:: lsp_mtus
            
            	LSP MTU configuration
            	**type**\:   :py:class:`LspMtus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus>`
            
            .. attribute:: lsp_passwords
            
            	LSP/SNP password configuration
            	**type**\:   :py:class:`LspPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords>`
            
            .. attribute:: lsp_refresh_intervals
            
            	LSP refresh\-interval configuration
            	**type**\:   :py:class:`LspRefreshIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals>`
            
            .. attribute:: max_link_metrics
            
            	Max Link Metric configuration
            	**type**\:   :py:class:`MaxLinkMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics>`
            
            .. attribute:: nets
            
            	NET configuration
            	**type**\:   :py:class:`Nets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets>`
            
            .. attribute:: nsf
            
            	IS\-IS NSF configuration
            	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nsf>`
            
            .. attribute:: nsr
            
            	IS\-IS NSR configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: overload_bits
            
            	LSP overload\-bit configuration
            	**type**\:   :py:class:`OverloadBits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits>`
            
            .. attribute:: running
            
            	Flag to indicate that instance should be running.  This must be the first object created when an IS\-IS instance is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS instance will exit
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: srgb
            
            	Segment Routing Global Block configuration
            	**type**\:   :py:class:`Srgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Srgb>`
            
            	**presence node**\: True
            
            .. attribute:: trace_buffer_size
            
            	Trace buffer size configuration
            	**type**\:   :py:class:`TraceBufferSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.TraceBufferSize>`
            
            .. attribute:: tracing_mode
            
            	Tracing mode configuration
            	**type**\:   :py:class:`IsisTracingModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisTracingModeEnum>`
            
            	**default value**\: basic
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.instance_name = None
                self.adjacency_stagger = None
                self.afs = Isis.Instances.Instance.Afs()
                self.afs.parent = self
                self.distribute = None
                self.dynamic_host_name = None
                self.ignore_lsp_errors = None
                self.instance_id = None
                self.interfaces = Isis.Instances.Instance.Interfaces()
                self.interfaces.parent = self
                self.is_type = None
                self.link_groups = Isis.Instances.Instance.LinkGroups()
                self.link_groups.parent = self
                self.log_adjacency_changes = None
                self.log_pdu_drops = None
                self.lsp_accept_passwords = Isis.Instances.Instance.LspAcceptPasswords()
                self.lsp_accept_passwords.parent = self
                self.lsp_arrival_times = Isis.Instances.Instance.LspArrivalTimes()
                self.lsp_arrival_times.parent = self
                self.lsp_check_intervals = Isis.Instances.Instance.LspCheckIntervals()
                self.lsp_check_intervals.parent = self
                self.lsp_generation_intervals = Isis.Instances.Instance.LspGenerationIntervals()
                self.lsp_generation_intervals.parent = self
                self.lsp_lifetimes = Isis.Instances.Instance.LspLifetimes()
                self.lsp_lifetimes.parent = self
                self.lsp_mtus = Isis.Instances.Instance.LspMtus()
                self.lsp_mtus.parent = self
                self.lsp_passwords = Isis.Instances.Instance.LspPasswords()
                self.lsp_passwords.parent = self
                self.lsp_refresh_intervals = Isis.Instances.Instance.LspRefreshIntervals()
                self.lsp_refresh_intervals.parent = self
                self.max_link_metrics = Isis.Instances.Instance.MaxLinkMetrics()
                self.max_link_metrics.parent = self
                self.nets = Isis.Instances.Instance.Nets()
                self.nets.parent = self
                self.nsf = Isis.Instances.Instance.Nsf()
                self.nsf.parent = self
                self.nsr = None
                self.overload_bits = Isis.Instances.Instance.OverloadBits()
                self.overload_bits.parent = self
                self.running = None
                self.srgb = None
                self.trace_buffer_size = Isis.Instances.Instance.TraceBufferSize()
                self.trace_buffer_size.parent = self
                self.tracing_mode = None


            class Srgb(object):
                """
                Segment Routing Global Block configuration
                
                .. attribute:: lower_bound
                
                	The lower bound of the SRGB
                	**type**\:  int
                
                	**range:** 16000..1048574
                
                	**mandatory**\: True
                
                .. attribute:: upper_bound
                
                	The upper bound of the SRGB
                	**type**\:  int
                
                	**range:** 16001..1048575
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.lower_bound = None
                    self.upper_bound = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:srgb'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.lower_bound is not None:
                        return True

                    if self.upper_bound is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Srgb']['meta_info']


            class LspGenerationIntervals(object):
                """
                LSP generation\-interval configuration
                
                .. attribute:: lsp_generation_interval
                
                	LSP generation scheduling parameters
                	**type**\: list of    :py:class:`LspGenerationInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_generation_interval = YList()
                    self.lsp_generation_interval.parent = self
                    self.lsp_generation_interval.name = 'lsp_generation_interval'


                class LspGenerationInterval(object):
                    """
                    LSP generation scheduling parameters
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: initial_wait
                    
                    	Initial wait before generating local LSP in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum wait before generating local LSP in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary wait before generating local LSP in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.initial_wait = None
                        self.maximum_wait = None
                        self.secondary_wait = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-generation-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.initial_wait is not None:
                            return True

                        if self.maximum_wait is not None:
                            return True

                        if self.secondary_wait is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-generation-intervals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_generation_interval is not None:
                        for child_ref in self.lsp_generation_interval:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspGenerationIntervals']['meta_info']


            class LspArrivalTimes(object):
                """
                LSP arrival time configuration
                
                .. attribute:: lsp_arrival_time
                
                	Minimum LSP arrival time
                	**type**\: list of    :py:class:`LspArrivalTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_arrival_time = YList()
                    self.lsp_arrival_time.parent = self
                    self.lsp_arrival_time.name = 'lsp_arrival_time'


                class LspArrivalTime(object):
                    """
                    Minimum LSP arrival time
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: initial_wait
                    
                    	Initial delay expected to take since last LSPin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum delay expected to take since last LSPin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary delay expected to take since last LSPin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.initial_wait = None
                        self.maximum_wait = None
                        self.secondary_wait = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-arrival-time[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.initial_wait is not None:
                            return True

                        if self.maximum_wait is not None:
                            return True

                        if self.secondary_wait is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-arrival-times'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_arrival_time is not None:
                        for child_ref in self.lsp_arrival_time:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspArrivalTimes']['meta_info']


            class TraceBufferSize(object):
                """
                Trace buffer size configuration
                
                .. attribute:: detailed
                
                	Buffer size for detailed traces
                	**type**\:  int
                
                	**range:** 1..1000000
                
                .. attribute:: hello
                
                	Buffer size for hello trace
                	**type**\:  int
                
                	**range:** 1..1000000
                
                .. attribute:: severe
                
                	Buffer size for severe trace
                	**type**\:  int
                
                	**range:** 1..1000000
                
                .. attribute:: standard
                
                	Buffer size for standard traces
                	**type**\:  int
                
                	**range:** 1..1000000
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detailed = None
                    self.hello = None
                    self.severe = None
                    self.standard = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:trace-buffer-size'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.detailed is not None:
                        return True

                    if self.hello is not None:
                        return True

                    if self.severe is not None:
                        return True

                    if self.standard is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.TraceBufferSize']['meta_info']


            class MaxLinkMetrics(object):
                """
                Max Link Metric configuration
                
                .. attribute:: max_link_metric
                
                	Max Link Metric
                	**type**\: list of    :py:class:`MaxLinkMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.max_link_metric = YList()
                    self.max_link_metric.parent = self
                    self.max_link_metric.name = 'max_link_metric'


                class MaxLinkMetric(object):
                    """
                    Max Link Metric
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-link-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-link-metrics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.max_link_metric is not None:
                        for child_ref in self.max_link_metric:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.MaxLinkMetrics']['meta_info']


            class AdjacencyStagger(object):
                """
                Stagger ISIS adjacency bring up
                
                .. attribute:: initial_nbr
                
                	Adjacency Stagger\: Initial number of neighbors to bring up per area
                	**type**\:  int
                
                	**range:** 2..65000
                
                	**default value**\: 2
                
                .. attribute:: max_nbr
                
                	Adjacency Stagger\: Subsequent simultaneous number of neighbors to bring up
                	**type**\:  int
                
                	**range:** 2..65000
                
                	**default value**\: 64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.initial_nbr = None
                    self.max_nbr = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:adjacency-stagger'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.initial_nbr is not None:
                        return True

                    if self.max_nbr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.AdjacencyStagger']['meta_info']


            class Afs(object):
                """
                Per\-address\-family configuration
                
                .. attribute:: af
                
                	Configuration for an IS\-IS address\-family. If a named (non\-default) topology is being created it must be multicast
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af = YList()
                    self.af.parent = self
                    self.af.name = 'af'


                class Af(object):
                    """
                    Configuration for an IS\-IS address\-family. If
                    a named (non\-default) topology is being
                    created it must be multicast.
                    
                    .. attribute:: af_name  <key>
                    
                    	Address family
                    	**type**\:   :py:class:`IsisAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamilyEnum>`
                    
                    .. attribute:: saf_name  <key>
                    
                    	Sub address family
                    	**type**\:   :py:class:`IsisSubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamilyEnum>`
                    
                    .. attribute:: af_data
                    
                    	Data container
                    	**type**\:   :py:class:`AfData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: topology_name
                    
                    	keys\: topology\-name
                    	**type**\: list of    :py:class:`TopologyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.saf_name = None
                        self.af_data = None
                        self.topology_name = YList()
                        self.topology_name.parent = self
                        self.topology_name.name = 'topology_name'


                    class AfData(object):
                        """
                        Data container.
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\:   :py:class:`IsisAdjCheckEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheckEnum>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\:   :py:class:`AdminDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances>`
                        
                        .. attribute:: advertise_link_attributes
                        
                        	If TRUE, advertise additional link attributes in our LSP
                        	**type**\:  bool
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\:   :py:class:`IsisApplyWeightEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeightEnum>`
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\:   :py:class:`IsisAttachedBitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBitEnum>`
                        
                        	**default value**\: area
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 115
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\:   :py:class:`FrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\:  bool
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\:   :py:class:`Ispf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\:   :py:class:`MaxRedistPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\:  int
                        
                        	**range:** 1..64
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\:   :py:class:`MetricStyles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\:   :py:class:`MicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\:   :py:class:`MonitorConvergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`MplsLdpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\:   :py:class:`Propagations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\:   :py:class:`Redistributions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions>`
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\:  bool
                        
                        .. attribute:: router_id
                        
                        	Stable IP address for system. Will only be applied for the unicast sub\-address\-family
                        	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.RouterId>`
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\:   :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting>`
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\:   :py:class:`SpfIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\:   :py:class:`SpfPeriodicIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\:   :py:class:`SpfPrefixPriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\:   :py:class:`SummaryPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes>`
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\:  int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\:   :py:class:`Ucmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.adjacency_check = None
                            self.admin_distances = Isis.Instances.Instance.Afs.Af.AfData.AdminDistances()
                            self.admin_distances.parent = self
                            self.advertise_link_attributes = None
                            self.advertise_passive_only = None
                            self.apply_weight = None
                            self.attached_bit = None
                            self.default_admin_distance = None
                            self.default_information = Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation()
                            self.default_information.parent = self
                            self.frr_table = Isis.Instances.Instance.Afs.Af.AfData.FrrTable()
                            self.frr_table.parent = self
                            self.ignore_attached_bit = None
                            self.ispf = Isis.Instances.Instance.Afs.Af.AfData.Ispf()
                            self.ispf.parent = self
                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self.maximum_paths = None
                            self.metric_styles = Isis.Instances.Instance.Afs.Af.AfData.MetricStyles()
                            self.metric_styles.parent = self
                            self.metrics = Isis.Instances.Instance.Afs.Af.AfData.Metrics()
                            self.metrics.parent = self
                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self.mpls = Isis.Instances.Instance.Afs.Af.AfData.Mpls()
                            self.mpls.parent = self
                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self.propagations = Isis.Instances.Instance.Afs.Af.AfData.Propagations()
                            self.propagations.parent = self
                            self.redistributions = Isis.Instances.Instance.Afs.Af.AfData.Redistributions()
                            self.redistributions.parent = self
                            self.route_source_first_hop = None
                            self.router_id = Isis.Instances.Instance.Afs.Af.AfData.RouterId()
                            self.router_id.parent = self
                            self.segment_routing = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting()
                            self.segment_routing.parent = self
                            self.single_topology = None
                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals()
                            self.spf_intervals.parent = self
                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self.topology_id = None
                            self.ucmp = Isis.Instances.Instance.Afs.Af.AfData.Ucmp()
                            self.ucmp.parent = self
                            self.weights = Isis.Instances.Instance.Afs.Af.AfData.Weights()
                            self.weights.parent = self


                        class SegmentRouting(object):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\:   :py:class:`IsisLabelPreferenceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreferenceEnum>`
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\:   :py:class:`PrefixSidMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mpls = None
                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self


                            class PrefixSidMap(object):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.advertise_local = None
                                    self.receive = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid-map'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.advertise_local is not None:
                                        return True

                                    if self.receive is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:segment-routing'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.mpls is not None:
                                    return True

                                if self.prefix_sid_map is not None and self.prefix_sid_map._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info']


                        class MetricStyles(object):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of    :py:class:`MetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric_style = YList()
                                self.metric_style.parent = self
                                self.metric_style.name = 'metric_style'


                            class MetricStyle(object):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\:   :py:class:`IsisMetricStyleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleEnum>`
                                
                                	**default value**\: old-metric-style
                                
                                .. attribute:: transition_state
                                
                                	Transition state
                                	**type**\:   :py:class:`IsisMetricStyleTransitionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleTransitionEnum>`
                                
                                	**default value**\: disabled
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.style = None
                                    self.transition_state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-style[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.style is not None:
                                        return True

                                    if self.transition_state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-styles'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.metric_style is not None:
                                    for child_ref in self.metric_style:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles']['meta_info']


                        class FrrTable(object):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\:   :py:class:`FrrLoadSharings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\:   :py:class:`FrrRemoteLfaPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\:   :py:class:`FrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\:   :py:class:`FrrUseCandOnlies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\:   :py:class:`PriorityLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self.priority_limits = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self


                            class FrrLoadSharings(object):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of    :py:class:`FrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_load_sharing = YList()
                                    self.frr_load_sharing.parent = self
                                    self.frr_load_sharing.name = 'frr_load_sharing'


                                class FrrLoadSharing(object):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\:   :py:class:`IsisfrrLoadSharingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharingEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.load_sharing = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharing[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.load_sharing is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharings'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_load_sharing is not None:
                                        for child_ref in self.frr_load_sharing:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings']['meta_info']


                            class PriorityLimits(object):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of    :py:class:`PriorityLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.priority_limit = YList()
                                    self.priority_limit.parent = self
                                    self.priority_limit.name = 'priority_limit'


                                class PriorityLimit(object):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                    
                                    .. attribute:: priority
                                    
                                    	Compute for all prefixes upto the specified priority
                                    	**type**\:   :py:class:`IsisPrefixPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriorityEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.frr_type = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')
                                        if self.frr_type is None:
                                            raise YPYModelError('Key property frr_type is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limit[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.frr_type is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limits'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.priority_limit is not None:
                                        for child_ref in self.priority_limit:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits']['meta_info']


                            class FrrRemoteLfaPrefixes(object):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of    :py:class:`FrrRemoteLfaPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_remote_lfa_prefix = YList()
                                    self.frr_remote_lfa_prefix.parent = self
                                    self.frr_remote_lfa_prefix.name = 'frr_remote_lfa_prefix'


                                class FrrRemoteLfaPrefix(object):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\:  str
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.prefix_list_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.prefix_list_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefixes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_remote_lfa_prefix is not None:
                                        for child_ref in self.frr_remote_lfa_prefix:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes']['meta_info']


                            class FrrTiebreakers(object):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of    :py:class:`FrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_tiebreaker = YList()
                                    self.frr_tiebreaker.parent = self
                                    self.frr_tiebreaker.name = 'frr_tiebreaker'


                                class FrrTiebreaker(object):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: tiebreaker  <key>
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\:   :py:class:`IsisfrrTiebreakerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreakerEnum>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.tiebreaker = None
                                        self.index = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')
                                        if self.tiebreaker is None:
                                            raise YPYModelError('Key property tiebreaker is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreaker[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:tiebreaker = ' + str(self.tiebreaker) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.tiebreaker is not None:
                                            return True

                                        if self.index is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreakers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_tiebreaker is not None:
                                        for child_ref in self.frr_tiebreaker:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers']['meta_info']


                            class FrrUseCandOnlies(object):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of    :py:class:`FrrUseCandOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_use_cand_only = YList()
                                    self.frr_use_cand_only.parent = self
                                    self.frr_use_cand_only.name = 'frr_use_cand_only'


                                class FrrUseCandOnly(object):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.frr_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')
                                        if self.frr_type is None:
                                            raise YPYModelError('Key property frr_type is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-only[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.frr_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-onlies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_use_cand_only is not None:
                                        for child_ref in self.frr_use_cand_only:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-table'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.frr_load_sharings is not None and self.frr_load_sharings._has_data():
                                    return True

                                if self.frr_remote_lfa_prefixes is not None and self.frr_remote_lfa_prefixes._has_data():
                                    return True

                                if self.frr_tiebreakers is not None and self.frr_tiebreakers._has_data():
                                    return True

                                if self.frr_use_cand_onlies is not None and self.frr_use_cand_onlies._has_data():
                                    return True

                                if self.priority_limits is not None and self.priority_limits._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']


                        class RouterId(object):
                            """
                            Stable IP address for system. Will only be
                            applied for the unicast sub\-address\-family.
                            
                            .. attribute:: address
                            
                            	IPv4/IPv6 address to be used as a router ID. Precisely one of Address and Interface must be specified
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:router-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.RouterId']['meta_info']


                        class SpfPrefixPriorities(object):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of    :py:class:`SpfPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_prefix_priority = YList()
                                self.spf_prefix_priority.parent = self
                                self.spf_prefix_priority.name = 'spf_prefix_priority'


                            class SpfPrefixPriority(object):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level  <key>
                                
                                	SPF Level for prefix prioritization
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: prefix_priority_type  <key>
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\:   :py:class:`IsisPrefixPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriorityEnum>`
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\:  str
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_priority_type = None
                                    self.access_list_name = None
                                    self.admin_tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')
                                    if self.prefix_priority_type is None:
                                        raise YPYModelError('Key property prefix_priority_type is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priority[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:prefix-priority-type = ' + str(self.prefix_priority_type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.prefix_priority_type is not None:
                                        return True

                                    if self.access_list_name is not None:
                                        return True

                                    if self.admin_tag is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priorities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.spf_prefix_priority is not None:
                                    for child_ref in self.spf_prefix_priority:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities']['meta_info']


                        class SummaryPrefixes(object):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of    :py:class:`SummaryPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.summary_prefix = YList()
                                self.summary_prefix.parent = self
                                self.summary_prefix.name = 'summary_prefix'


                            class SummaryPrefix(object):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP summary address prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\:  int
                                
                                	**range:** 1..2
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.level = None
                                    self.tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYModelError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefix[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address_prefix is not None:
                                        return True

                                    if self.level is not None:
                                        return True

                                    if self.tag is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.summary_prefix is not None:
                                    for child_ref in self.summary_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes']['meta_info']


                        class MicroLoopAvoidance(object):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\:   :py:class:`IsisMicroLoopAvoidanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidanceEnum>`
                            
                            	**default value**\: micro-loop-avoidance-all
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\:  int
                            
                            	**range:** 1000..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 5000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.rib_update_delay = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:micro-loop-avoidance'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.rib_update_delay is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance']['meta_info']


                        class Ucmp(object):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\:  int
                            
                            	**range:** 100..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 100
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\:   :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\:   :py:class:`ExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay_interval = None
                                self.enable = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable()
                                self.enable.parent = self
                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self


                            class Enable(object):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\:  str
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\:  int
                                
                                	**range:** 101..10000
                                
                                	**default value**\: 200
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix_list_name = None
                                    self.variance = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:enable'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix_list_name is not None:
                                        return True

                                    if self.variance is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable']['meta_info']


                            class ExcludeInterfaces(object):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of    :py:class:`ExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_interface = YList()
                                    self.exclude_interface.parent = self
                                    self.exclude_interface.name = 'exclude_interface'


                                class ExcludeInterface(object):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Name of the interface to be excluded
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.exclude_interface is not None:
                                        for child_ref in self.exclude_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ucmp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.delay_interval is not None:
                                    return True

                                if self.enable is not None and self.enable._has_data():
                                    return True

                                if self.exclude_interfaces is not None and self.exclude_interfaces._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info']


                        class MaxRedistPrefixes(object):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of    :py:class:`MaxRedistPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_redist_prefix = YList()
                                self.max_redist_prefix.parent = self
                                self.max_redist_prefix.name = 'max_redist_prefix'


                            class MaxRedistPrefix(object):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\:  int
                                
                                	**range:** 1..28000
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_limit = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.prefix_limit is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.max_redist_prefix is not None:
                                    for child_ref in self.max_redist_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes']['meta_info']


                        class Propagations(object):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of    :py:class:`Propagation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.propagation = YList()
                                self.propagation.parent = self
                                self.propagation.name = 'propagation'


                            class Propagation(object):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: source_level  <key>
                                
                                	Source level for routes
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: destination_level  <key>
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.source_level = None
                                    self.destination_level = None
                                    self.route_policy_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.source_level is None:
                                        raise YPYModelError('Key property source_level is None')
                                    if self.destination_level is None:
                                        raise YPYModelError('Key property destination_level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagation[Cisco-IOS-XR-clns-isis-cfg:source-level = ' + str(self.source_level) + '][Cisco-IOS-XR-clns-isis-cfg:destination-level = ' + str(self.destination_level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.source_level is not None:
                                        return True

                                    if self.destination_level is not None:
                                        return True

                                    if self.route_policy_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.propagation is not None:
                                    for child_ref in self.propagation:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations']['meta_info']


                        class Redistributions(object):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of    :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.redistribution = YList()
                                self.redistribution.parent = self
                                self.redistribution.name = 'redistribution'


                            class Redistribution(object):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name  <key>
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\:   :py:class:`IsisRedistProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProtoEnum>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\:   :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp>`
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of    :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.protocol_name = None
                                    self.bgp = YList()
                                    self.bgp.parent = self
                                    self.bgp.name = 'bgp'
                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self.eigrp = YList()
                                    self.eigrp.parent = self
                                    self.eigrp.name = 'eigrp'
                                    self.ospf_or_ospfv3_or_isis_or_application = YList()
                                    self.ospf_or_ospfv3_or_isis_or_application.parent = self
                                    self.ospf_or_ospfv3_or_isis_or_application.name = 'ospf_or_ospfv3_or_isis_or_application'


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(object):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:connected-or-static-or-rip-or-subscriber-or-mobile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info']


                                class OspfOrOspfv3OrIsisOrApplication(object):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name  <key>
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.instance_name = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.instance_name is None:
                                            raise YPYModelError('Key property instance_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ospf-or-ospfv3-or-isis-or-application[Cisco-IOS-XR-clns-isis-cfg:instance-name = ' + str(self.instance_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.instance_name is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info']


                                class Bgp(object):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  <key>
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.as_xx is None:
                                            raise YPYModelError('Key property as_xx is None')
                                        if self.as_yy is None:
                                            raise YPYModelError('Key property as_yy is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:bgp[Cisco-IOS-XR-clns-isis-cfg:as-xx = ' + str(self.as_xx) + '][Cisco-IOS-XR-clns-isis-cfg:as-yy = ' + str(self.as_yy) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.as_xx is not None:
                                            return True

                                        if self.as_yy is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp']['meta_info']


                                class Eigrp(object):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz  <key>
                                    
                                    	Eigrp as number
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_zz = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.as_zz is None:
                                            raise YPYModelError('Key property as_zz is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:eigrp[Cisco-IOS-XR-clns-isis-cfg:as-zz = ' + str(self.as_zz) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.as_zz is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.protocol_name is None:
                                        raise YPYModelError('Key property protocol_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistribution[Cisco-IOS-XR-clns-isis-cfg:protocol-name = ' + str(self.protocol_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.protocol_name is not None:
                                        return True

                                    if self.bgp is not None:
                                        for child_ref in self.bgp:
                                            if child_ref._has_data():
                                                return True

                                    if self.connected_or_static_or_rip_or_subscriber_or_mobile is not None and self.connected_or_static_or_rip_or_subscriber_or_mobile._has_data():
                                        return True

                                    if self.eigrp is not None:
                                        for child_ref in self.eigrp:
                                            if child_ref._has_data():
                                                return True

                                    if self.ospf_or_ospfv3_or_isis_or_application is not None:
                                        for child_ref in self.ospf_or_ospfv3_or_isis_or_application:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistributions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.redistribution is not None:
                                    for child_ref in self.redistribution:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions']['meta_info']


                        class SpfPeriodicIntervals(object):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of    :py:class:`SpfPeriodicInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_periodic_interval = YList()
                                self.spf_periodic_interval.parent = self
                                self.spf_periodic_interval.name = 'spf_periodic_interval'


                            class SpfPeriodicInterval(object):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**mandatory**\: True
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.periodic_interval = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.periodic_interval is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.spf_periodic_interval is not None:
                                    for child_ref in self.spf_periodic_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals']['meta_info']


                        class SpfIntervals(object):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of    :py:class:`SpfInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_interval = YList()
                                self.spf_interval.parent = self
                                self.spf_interval.name = 'spf_interval'


                            class SpfInterval(object):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.initial_wait = None
                                    self.maximum_wait = None
                                    self.secondary_wait = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.initial_wait is not None:
                                        return True

                                    if self.maximum_wait is not None:
                                        return True

                                    if self.secondary_wait is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.spf_interval is not None:
                                    for child_ref in self.spf_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals']['meta_info']


                        class MonitorConvergence(object):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\:  str
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.prefix_list = None
                                self.track_ip_frr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:monitor-convergence'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.prefix_list is not None:
                                    return True

                                if self.track_ip_frr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence']['meta_info']


                        class DefaultInformation(object):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\:  str
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.external = None
                                self.policy_name = None
                                self.use_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:default-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.external is not None:
                                    return True

                                if self.policy_name is not None:
                                    return True

                                if self.use_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation']['meta_info']


                        class AdminDistances(object):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of    :py:class:`AdminDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_distance = YList()
                                self.admin_distance.parent = self
                                self.admin_distance.name = 'admin_distance'


                            class AdminDistance(object):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP route source prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**mandatory**\: True
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.distance = None
                                    self.prefix_list = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYModelError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distance[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address_prefix is not None:
                                        return True

                                    if self.distance is not None:
                                        return True

                                    if self.prefix_list is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distances'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.admin_distance is not None:
                                    for child_ref in self.admin_distance:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances']['meta_info']


                        class Ispf(object):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\:   :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.states = Isis.Instances.Instance.Afs.Af.AfData.Ispf.States()
                                self.states.parent = self


                            class States(object):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of    :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.state = YList()
                                    self.state.parent = self
                                    self.state.name = 'state'


                                class State(object):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:   :py:class:`IsisispfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisispfStateEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:state[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:states'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.state is not None:
                                        for child_ref in self.state:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ispf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.states is not None and self.states._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf']['meta_info']


                        class MplsLdpGlobal(object):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_config = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp-global'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.auto_config is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal']['meta_info']


                        class Mpls(object):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.igp_intact = None
                                self.level = None
                                self.multicast_intact = None
                                self.router_id = Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId()
                                self.router_id.parent = self


                            class RouterId(object):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:router-id'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.igp_intact is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.multicast_intact is not None:
                                    return True

                                if self.router_id is not None and self.router_id._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info']


                        class Metrics(object):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric = YList()
                                self.metric.parent = self
                                self.metric.name = 'metric'


                            class Metric(object):
                                """
                                Metric configuration. Legal value depends on
                                the metric\-style specified for the topology. If
                                the metric\-style defined is narrow, then only a
                                value between <1\-63> is allowed and if the
                                metric\-style is defined as wide, then a value
                                between <1\-16777215> is allowed as the metric
                                value.  All routers exclude links with the
                                maximum wide metric (16777215) from their SPF
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: one of the below types:
                                
                                	**type**\:   :py:class:`MetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum>`
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.metric = None

                                class MetricEnum(Enum):
                                    """
                                    MetricEnum

                                    Allowed metric\: <1\-63> for narrow,

                                    <1\-16777215> for wide

                                    .. data:: maximum = 16777215

                                    	Maximum wide metric.  All routers will

                                    	exclude this link from their SPF

                                    """

                                    maximum = 16777215


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric.MetricEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.metric is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.metric is not None:
                                    for child_ref in self.metric:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics']['meta_info']


                        class Weights(object):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.weight = YList()
                                self.weight.parent = self
                                self.weight.name = 'weight'


                            class Weight(object):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\:  int
                                
                                	**range:** 1..16777214
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.weight = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.weight is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.weight is not None:
                                    for child_ref in self.weight:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:af-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.adjacency_check is not None:
                                return True

                            if self.admin_distances is not None and self.admin_distances._has_data():
                                return True

                            if self.advertise_link_attributes is not None:
                                return True

                            if self.advertise_passive_only is not None:
                                return True

                            if self.apply_weight is not None:
                                return True

                            if self.attached_bit is not None:
                                return True

                            if self.default_admin_distance is not None:
                                return True

                            if self.default_information is not None and self.default_information._has_data():
                                return True

                            if self.frr_table is not None and self.frr_table._has_data():
                                return True

                            if self.ignore_attached_bit is not None:
                                return True

                            if self.ispf is not None and self.ispf._has_data():
                                return True

                            if self.max_redist_prefixes is not None and self.max_redist_prefixes._has_data():
                                return True

                            if self.maximum_paths is not None:
                                return True

                            if self.metric_styles is not None and self.metric_styles._has_data():
                                return True

                            if self.metrics is not None and self.metrics._has_data():
                                return True

                            if self.micro_loop_avoidance is not None and self.micro_loop_avoidance._has_data():
                                return True

                            if self.monitor_convergence is not None and self.monitor_convergence._has_data():
                                return True

                            if self.mpls is not None and self.mpls._has_data():
                                return True

                            if self.mpls_ldp_global is not None and self.mpls_ldp_global._has_data():
                                return True

                            if self.propagations is not None and self.propagations._has_data():
                                return True

                            if self.redistributions is not None and self.redistributions._has_data():
                                return True

                            if self.route_source_first_hop is not None:
                                return True

                            if self.router_id is not None and self.router_id._has_data():
                                return True

                            if self.segment_routing is not None and self.segment_routing._has_data():
                                return True

                            if self.single_topology is not None:
                                return True

                            if self.spf_intervals is not None and self.spf_intervals._has_data():
                                return True

                            if self.spf_periodic_intervals is not None and self.spf_periodic_intervals._has_data():
                                return True

                            if self.spf_prefix_priorities is not None and self.spf_prefix_priorities._has_data():
                                return True

                            if self.summary_prefixes is not None and self.summary_prefixes._has_data():
                                return True

                            if self.topology_id is not None:
                                return True

                            if self.ucmp is not None and self.ucmp._has_data():
                                return True

                            if self.weights is not None and self.weights._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']


                    class TopologyName(object):
                        """
                        keys\: topology\-name
                        
                        .. attribute:: topology_name  <key>
                        
                        	Topology Name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\:   :py:class:`IsisAdjCheckEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheckEnum>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\:   :py:class:`AdminDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances>`
                        
                        .. attribute:: advertise_link_attributes
                        
                        	If TRUE, advertise additional link attributes in our LSP
                        	**type**\:  bool
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\:   :py:class:`IsisApplyWeightEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeightEnum>`
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\:   :py:class:`IsisAttachedBitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBitEnum>`
                        
                        	**default value**\: area
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 115
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\:   :py:class:`FrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\:  bool
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\:   :py:class:`Ispf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\:   :py:class:`MaxRedistPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\:  int
                        
                        	**range:** 1..64
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\:   :py:class:`MetricStyles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\:   :py:class:`MicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\:   :py:class:`MonitorConvergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`MplsLdpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\:   :py:class:`Propagations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\:   :py:class:`Redistributions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions>`
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\:  bool
                        
                        .. attribute:: router_id
                        
                        	Stable IP address for system. Will only be applied for the unicast sub\-address\-family
                        	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.RouterId>`
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\:   :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting>`
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\:   :py:class:`SpfIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\:   :py:class:`SpfPeriodicIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\:   :py:class:`SpfPrefixPriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\:   :py:class:`SummaryPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes>`
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\:  int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\:   :py:class:`Ucmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.topology_name = None
                            self.adjacency_check = None
                            self.admin_distances = Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances()
                            self.admin_distances.parent = self
                            self.advertise_link_attributes = None
                            self.advertise_passive_only = None
                            self.apply_weight = None
                            self.attached_bit = None
                            self.default_admin_distance = None
                            self.default_information = Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation()
                            self.default_information.parent = self
                            self.frr_table = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable()
                            self.frr_table.parent = self
                            self.ignore_attached_bit = None
                            self.ispf = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf()
                            self.ispf.parent = self
                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self.maximum_paths = None
                            self.metric_styles = Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles()
                            self.metric_styles.parent = self
                            self.metrics = Isis.Instances.Instance.Afs.Af.TopologyName.Metrics()
                            self.metrics.parent = self
                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self.mpls = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls()
                            self.mpls.parent = self
                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self.propagations = Isis.Instances.Instance.Afs.Af.TopologyName.Propagations()
                            self.propagations.parent = self
                            self.redistributions = Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions()
                            self.redistributions.parent = self
                            self.route_source_first_hop = None
                            self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.RouterId()
                            self.router_id.parent = self
                            self.segment_routing = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting()
                            self.segment_routing.parent = self
                            self.single_topology = None
                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals()
                            self.spf_intervals.parent = self
                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self.topology_id = None
                            self.ucmp = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp()
                            self.ucmp.parent = self
                            self.weights = Isis.Instances.Instance.Afs.Af.TopologyName.Weights()
                            self.weights.parent = self


                        class SegmentRouting(object):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\:   :py:class:`IsisLabelPreferenceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreferenceEnum>`
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\:   :py:class:`PrefixSidMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mpls = None
                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self


                            class PrefixSidMap(object):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.advertise_local = None
                                    self.receive = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid-map'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.advertise_local is not None:
                                        return True

                                    if self.receive is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:segment-routing'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.mpls is not None:
                                    return True

                                if self.prefix_sid_map is not None and self.prefix_sid_map._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info']


                        class MetricStyles(object):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of    :py:class:`MetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric_style = YList()
                                self.metric_style.parent = self
                                self.metric_style.name = 'metric_style'


                            class MetricStyle(object):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\:   :py:class:`IsisMetricStyleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleEnum>`
                                
                                	**default value**\: old-metric-style
                                
                                .. attribute:: transition_state
                                
                                	Transition state
                                	**type**\:   :py:class:`IsisMetricStyleTransitionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleTransitionEnum>`
                                
                                	**default value**\: disabled
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.style = None
                                    self.transition_state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-style[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.style is not None:
                                        return True

                                    if self.transition_state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-styles'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.metric_style is not None:
                                    for child_ref in self.metric_style:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles']['meta_info']


                        class FrrTable(object):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\:   :py:class:`FrrLoadSharings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\:   :py:class:`FrrRemoteLfaPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\:   :py:class:`FrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\:   :py:class:`FrrUseCandOnlies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\:   :py:class:`PriorityLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self.priority_limits = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self


                            class FrrLoadSharings(object):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of    :py:class:`FrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_load_sharing = YList()
                                    self.frr_load_sharing.parent = self
                                    self.frr_load_sharing.name = 'frr_load_sharing'


                                class FrrLoadSharing(object):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\:   :py:class:`IsisfrrLoadSharingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharingEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.load_sharing = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharing[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.load_sharing is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharings'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_load_sharing is not None:
                                        for child_ref in self.frr_load_sharing:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings']['meta_info']


                            class PriorityLimits(object):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of    :py:class:`PriorityLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.priority_limit = YList()
                                    self.priority_limit.parent = self
                                    self.priority_limit.name = 'priority_limit'


                                class PriorityLimit(object):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                    
                                    .. attribute:: priority
                                    
                                    	Compute for all prefixes upto the specified priority
                                    	**type**\:   :py:class:`IsisPrefixPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriorityEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.frr_type = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')
                                        if self.frr_type is None:
                                            raise YPYModelError('Key property frr_type is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limit[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.frr_type is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limits'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.priority_limit is not None:
                                        for child_ref in self.priority_limit:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits']['meta_info']


                            class FrrRemoteLfaPrefixes(object):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of    :py:class:`FrrRemoteLfaPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_remote_lfa_prefix = YList()
                                    self.frr_remote_lfa_prefix.parent = self
                                    self.frr_remote_lfa_prefix.name = 'frr_remote_lfa_prefix'


                                class FrrRemoteLfaPrefix(object):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\:  str
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.prefix_list_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.prefix_list_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefixes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_remote_lfa_prefix is not None:
                                        for child_ref in self.frr_remote_lfa_prefix:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes']['meta_info']


                            class FrrTiebreakers(object):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of    :py:class:`FrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_tiebreaker = YList()
                                    self.frr_tiebreaker.parent = self
                                    self.frr_tiebreaker.name = 'frr_tiebreaker'


                                class FrrTiebreaker(object):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: tiebreaker  <key>
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\:   :py:class:`IsisfrrTiebreakerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreakerEnum>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.tiebreaker = None
                                        self.index = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')
                                        if self.tiebreaker is None:
                                            raise YPYModelError('Key property tiebreaker is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreaker[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:tiebreaker = ' + str(self.tiebreaker) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.tiebreaker is not None:
                                            return True

                                        if self.index is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreakers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_tiebreaker is not None:
                                        for child_ref in self.frr_tiebreaker:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers']['meta_info']


                            class FrrUseCandOnlies(object):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of    :py:class:`FrrUseCandOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_use_cand_only = YList()
                                    self.frr_use_cand_only.parent = self
                                    self.frr_use_cand_only.name = 'frr_use_cand_only'


                                class FrrUseCandOnly(object):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.frr_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')
                                        if self.frr_type is None:
                                            raise YPYModelError('Key property frr_type is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-only[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.frr_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-onlies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.frr_use_cand_only is not None:
                                        for child_ref in self.frr_use_cand_only:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-table'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.frr_load_sharings is not None and self.frr_load_sharings._has_data():
                                    return True

                                if self.frr_remote_lfa_prefixes is not None and self.frr_remote_lfa_prefixes._has_data():
                                    return True

                                if self.frr_tiebreakers is not None and self.frr_tiebreakers._has_data():
                                    return True

                                if self.frr_use_cand_onlies is not None and self.frr_use_cand_onlies._has_data():
                                    return True

                                if self.priority_limits is not None and self.priority_limits._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']


                        class RouterId(object):
                            """
                            Stable IP address for system. Will only be
                            applied for the unicast sub\-address\-family.
                            
                            .. attribute:: address
                            
                            	IPv4/IPv6 address to be used as a router ID. Precisely one of Address and Interface must be specified
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:router-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.RouterId']['meta_info']


                        class SpfPrefixPriorities(object):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of    :py:class:`SpfPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_prefix_priority = YList()
                                self.spf_prefix_priority.parent = self
                                self.spf_prefix_priority.name = 'spf_prefix_priority'


                            class SpfPrefixPriority(object):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level  <key>
                                
                                	SPF Level for prefix prioritization
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: prefix_priority_type  <key>
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\:   :py:class:`IsisPrefixPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriorityEnum>`
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\:  str
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_priority_type = None
                                    self.access_list_name = None
                                    self.admin_tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')
                                    if self.prefix_priority_type is None:
                                        raise YPYModelError('Key property prefix_priority_type is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priority[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:prefix-priority-type = ' + str(self.prefix_priority_type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.prefix_priority_type is not None:
                                        return True

                                    if self.access_list_name is not None:
                                        return True

                                    if self.admin_tag is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priorities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.spf_prefix_priority is not None:
                                    for child_ref in self.spf_prefix_priority:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities']['meta_info']


                        class SummaryPrefixes(object):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of    :py:class:`SummaryPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.summary_prefix = YList()
                                self.summary_prefix.parent = self
                                self.summary_prefix.name = 'summary_prefix'


                            class SummaryPrefix(object):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP summary address prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\:  int
                                
                                	**range:** 1..2
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.level = None
                                    self.tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYModelError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefix[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address_prefix is not None:
                                        return True

                                    if self.level is not None:
                                        return True

                                    if self.tag is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.summary_prefix is not None:
                                    for child_ref in self.summary_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes']['meta_info']


                        class MicroLoopAvoidance(object):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\:   :py:class:`IsisMicroLoopAvoidanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidanceEnum>`
                            
                            	**default value**\: micro-loop-avoidance-all
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\:  int
                            
                            	**range:** 1000..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 5000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.rib_update_delay = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:micro-loop-avoidance'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.rib_update_delay is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance']['meta_info']


                        class Ucmp(object):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\:  int
                            
                            	**range:** 100..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 100
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\:   :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\:   :py:class:`ExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay_interval = None
                                self.enable = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable()
                                self.enable.parent = self
                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self


                            class Enable(object):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\:  str
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\:  int
                                
                                	**range:** 101..10000
                                
                                	**default value**\: 200
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix_list_name = None
                                    self.variance = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:enable'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix_list_name is not None:
                                        return True

                                    if self.variance is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable']['meta_info']


                            class ExcludeInterfaces(object):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of    :py:class:`ExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_interface = YList()
                                    self.exclude_interface.parent = self
                                    self.exclude_interface.name = 'exclude_interface'


                                class ExcludeInterface(object):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Name of the interface to be excluded
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.exclude_interface is not None:
                                        for child_ref in self.exclude_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ucmp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.delay_interval is not None:
                                    return True

                                if self.enable is not None and self.enable._has_data():
                                    return True

                                if self.exclude_interfaces is not None and self.exclude_interfaces._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info']


                        class MaxRedistPrefixes(object):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of    :py:class:`MaxRedistPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_redist_prefix = YList()
                                self.max_redist_prefix.parent = self
                                self.max_redist_prefix.name = 'max_redist_prefix'


                            class MaxRedistPrefix(object):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\:  int
                                
                                	**range:** 1..28000
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_limit = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.prefix_limit is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.max_redist_prefix is not None:
                                    for child_ref in self.max_redist_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes']['meta_info']


                        class Propagations(object):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of    :py:class:`Propagation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.propagation = YList()
                                self.propagation.parent = self
                                self.propagation.name = 'propagation'


                            class Propagation(object):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: source_level  <key>
                                
                                	Source level for routes
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: destination_level  <key>
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.source_level = None
                                    self.destination_level = None
                                    self.route_policy_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.source_level is None:
                                        raise YPYModelError('Key property source_level is None')
                                    if self.destination_level is None:
                                        raise YPYModelError('Key property destination_level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagation[Cisco-IOS-XR-clns-isis-cfg:source-level = ' + str(self.source_level) + '][Cisco-IOS-XR-clns-isis-cfg:destination-level = ' + str(self.destination_level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.source_level is not None:
                                        return True

                                    if self.destination_level is not None:
                                        return True

                                    if self.route_policy_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.propagation is not None:
                                    for child_ref in self.propagation:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations']['meta_info']


                        class Redistributions(object):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of    :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.redistribution = YList()
                                self.redistribution.parent = self
                                self.redistribution.name = 'redistribution'


                            class Redistribution(object):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name  <key>
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\:   :py:class:`IsisRedistProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProtoEnum>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\:   :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp>`
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of    :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.protocol_name = None
                                    self.bgp = YList()
                                    self.bgp.parent = self
                                    self.bgp.name = 'bgp'
                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self.eigrp = YList()
                                    self.eigrp.parent = self
                                    self.eigrp.name = 'eigrp'
                                    self.ospf_or_ospfv3_or_isis_or_application = YList()
                                    self.ospf_or_ospfv3_or_isis_or_application.parent = self
                                    self.ospf_or_ospfv3_or_isis_or_application.name = 'ospf_or_ospfv3_or_isis_or_application'


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(object):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:connected-or-static-or-rip-or-subscriber-or-mobile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info']


                                class OspfOrOspfv3OrIsisOrApplication(object):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name  <key>
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.instance_name = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.instance_name is None:
                                            raise YPYModelError('Key property instance_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ospf-or-ospfv3-or-isis-or-application[Cisco-IOS-XR-clns-isis-cfg:instance-name = ' + str(self.instance_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.instance_name is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info']


                                class Bgp(object):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  <key>
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.as_xx is None:
                                            raise YPYModelError('Key property as_xx is None')
                                        if self.as_yy is None:
                                            raise YPYModelError('Key property as_yy is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:bgp[Cisco-IOS-XR-clns-isis-cfg:as-xx = ' + str(self.as_xx) + '][Cisco-IOS-XR-clns-isis-cfg:as-yy = ' + str(self.as_yy) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.as_xx is not None:
                                            return True

                                        if self.as_yy is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp']['meta_info']


                                class Eigrp(object):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz  <key>
                                    
                                    	Eigrp as number
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricEnum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_zz = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.as_zz is None:
                                            raise YPYModelError('Key property as_zz is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:eigrp[Cisco-IOS-XR-clns-isis-cfg:as-zz = ' + str(self.as_zz) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.as_zz is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.protocol_name is None:
                                        raise YPYModelError('Key property protocol_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistribution[Cisco-IOS-XR-clns-isis-cfg:protocol-name = ' + str(self.protocol_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.protocol_name is not None:
                                        return True

                                    if self.bgp is not None:
                                        for child_ref in self.bgp:
                                            if child_ref._has_data():
                                                return True

                                    if self.connected_or_static_or_rip_or_subscriber_or_mobile is not None and self.connected_or_static_or_rip_or_subscriber_or_mobile._has_data():
                                        return True

                                    if self.eigrp is not None:
                                        for child_ref in self.eigrp:
                                            if child_ref._has_data():
                                                return True

                                    if self.ospf_or_ospfv3_or_isis_or_application is not None:
                                        for child_ref in self.ospf_or_ospfv3_or_isis_or_application:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistributions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.redistribution is not None:
                                    for child_ref in self.redistribution:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions']['meta_info']


                        class SpfPeriodicIntervals(object):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of    :py:class:`SpfPeriodicInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_periodic_interval = YList()
                                self.spf_periodic_interval.parent = self
                                self.spf_periodic_interval.name = 'spf_periodic_interval'


                            class SpfPeriodicInterval(object):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**mandatory**\: True
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.periodic_interval = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.periodic_interval is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.spf_periodic_interval is not None:
                                    for child_ref in self.spf_periodic_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals']['meta_info']


                        class SpfIntervals(object):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of    :py:class:`SpfInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_interval = YList()
                                self.spf_interval.parent = self
                                self.spf_interval.name = 'spf_interval'


                            class SpfInterval(object):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.initial_wait = None
                                    self.maximum_wait = None
                                    self.secondary_wait = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.initial_wait is not None:
                                        return True

                                    if self.maximum_wait is not None:
                                        return True

                                    if self.secondary_wait is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.spf_interval is not None:
                                    for child_ref in self.spf_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals']['meta_info']


                        class MonitorConvergence(object):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\:  str
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.prefix_list = None
                                self.track_ip_frr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:monitor-convergence'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.prefix_list is not None:
                                    return True

                                if self.track_ip_frr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence']['meta_info']


                        class DefaultInformation(object):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\:  str
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.external = None
                                self.policy_name = None
                                self.use_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:default-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.external is not None:
                                    return True

                                if self.policy_name is not None:
                                    return True

                                if self.use_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation']['meta_info']


                        class AdminDistances(object):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of    :py:class:`AdminDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_distance = YList()
                                self.admin_distance.parent = self
                                self.admin_distance.name = 'admin_distance'


                            class AdminDistance(object):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP route source prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**mandatory**\: True
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.distance = None
                                    self.prefix_list = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYModelError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distance[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address_prefix is not None:
                                        return True

                                    if self.distance is not None:
                                        return True

                                    if self.prefix_list is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distances'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.admin_distance is not None:
                                    for child_ref in self.admin_distance:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances']['meta_info']


                        class Ispf(object):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\:   :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.states = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States()
                                self.states.parent = self


                            class States(object):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of    :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.state = YList()
                                    self.state.parent = self
                                    self.state.name = 'state'


                                class State(object):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:   :py:class:`IsisispfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisispfStateEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYModelError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:state[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.level is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:states'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.state is not None:
                                        for child_ref in self.state:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ispf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.states is not None and self.states._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf']['meta_info']


                        class MplsLdpGlobal(object):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_config = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp-global'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.auto_config is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal']['meta_info']


                        class Mpls(object):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.igp_intact = None
                                self.level = None
                                self.multicast_intact = None
                                self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId()
                                self.router_id.parent = self


                            class RouterId(object):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:router-id'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.igp_intact is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.multicast_intact is not None:
                                    return True

                                if self.router_id is not None and self.router_id._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info']


                        class Metrics(object):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric = YList()
                                self.metric.parent = self
                                self.metric.name = 'metric'


                            class Metric(object):
                                """
                                Metric configuration. Legal value depends on
                                the metric\-style specified for the topology. If
                                the metric\-style defined is narrow, then only a
                                value between <1\-63> is allowed and if the
                                metric\-style is defined as wide, then a value
                                between <1\-16777215> is allowed as the metric
                                value.  All routers exclude links with the
                                maximum wide metric (16777215) from their SPF
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: one of the below types:
                                
                                	**type**\:   :py:class:`MetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum>`
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.metric = None

                                class MetricEnum(Enum):
                                    """
                                    MetricEnum

                                    Allowed metric\: <1\-63> for narrow,

                                    <1\-16777215> for wide

                                    .. data:: maximum = 16777215

                                    	Maximum wide metric.  All routers will

                                    	exclude this link from their SPF

                                    """

                                    maximum = 16777215


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric.MetricEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.metric is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.metric is not None:
                                    for child_ref in self.metric:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics']['meta_info']


                        class Weights(object):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.weight = YList()
                                self.weight.parent = self
                                self.weight.name = 'weight'


                            class Weight(object):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\:  int
                                
                                	**range:** 1..16777214
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.weight = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYModelError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.level is not None:
                                        return True

                                    if self.weight is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.weight is not None:
                                    for child_ref in self.weight:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.topology_name is None:
                                raise YPYModelError('Key property topology_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:topology-name[Cisco-IOS-XR-clns-isis-cfg:topology-name = ' + str(self.topology_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.topology_name is not None:
                                return True

                            if self.adjacency_check is not None:
                                return True

                            if self.admin_distances is not None and self.admin_distances._has_data():
                                return True

                            if self.advertise_link_attributes is not None:
                                return True

                            if self.advertise_passive_only is not None:
                                return True

                            if self.apply_weight is not None:
                                return True

                            if self.attached_bit is not None:
                                return True

                            if self.default_admin_distance is not None:
                                return True

                            if self.default_information is not None and self.default_information._has_data():
                                return True

                            if self.frr_table is not None and self.frr_table._has_data():
                                return True

                            if self.ignore_attached_bit is not None:
                                return True

                            if self.ispf is not None and self.ispf._has_data():
                                return True

                            if self.max_redist_prefixes is not None and self.max_redist_prefixes._has_data():
                                return True

                            if self.maximum_paths is not None:
                                return True

                            if self.metric_styles is not None and self.metric_styles._has_data():
                                return True

                            if self.metrics is not None and self.metrics._has_data():
                                return True

                            if self.micro_loop_avoidance is not None and self.micro_loop_avoidance._has_data():
                                return True

                            if self.monitor_convergence is not None and self.monitor_convergence._has_data():
                                return True

                            if self.mpls is not None and self.mpls._has_data():
                                return True

                            if self.mpls_ldp_global is not None and self.mpls_ldp_global._has_data():
                                return True

                            if self.propagations is not None and self.propagations._has_data():
                                return True

                            if self.redistributions is not None and self.redistributions._has_data():
                                return True

                            if self.route_source_first_hop is not None:
                                return True

                            if self.router_id is not None and self.router_id._has_data():
                                return True

                            if self.segment_routing is not None and self.segment_routing._has_data():
                                return True

                            if self.single_topology is not None:
                                return True

                            if self.spf_intervals is not None and self.spf_intervals._has_data():
                                return True

                            if self.spf_periodic_intervals is not None and self.spf_periodic_intervals._has_data():
                                return True

                            if self.spf_prefix_priorities is not None and self.spf_prefix_priorities._has_data():
                                return True

                            if self.summary_prefixes is not None and self.summary_prefixes._has_data():
                                return True

                            if self.topology_id is not None:
                                return True

                            if self.ucmp is not None and self.ucmp._has_data():
                                return True

                            if self.weights is not None and self.weights._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.af_name is None:
                            raise YPYModelError('Key property af_name is None')
                        if self.saf_name is None:
                            raise YPYModelError('Key property saf_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:af[Cisco-IOS-XR-clns-isis-cfg:af-name = ' + str(self.af_name) + '][Cisco-IOS-XR-clns-isis-cfg:saf-name = ' + str(self.saf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.saf_name is not None:
                            return True

                        if self.af_data is not None and self.af_data._has_data():
                            return True

                        if self.topology_name is not None:
                            for child_ref in self.topology_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.Afs.Af']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af is not None:
                        for child_ref in self.af:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Afs']['meta_info']


            class LspRefreshIntervals(object):
                """
                LSP refresh\-interval configuration
                
                .. attribute:: lsp_refresh_interval
                
                	Interval between re\-flooding of unchanged LSPs
                	**type**\: list of    :py:class:`LspRefreshInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_refresh_interval = YList()
                    self.lsp_refresh_interval.parent = self
                    self.lsp_refresh_interval.name = 'lsp_refresh_interval'


                class LspRefreshInterval(object):
                    """
                    Interval between re\-flooding of unchanged
                    LSPs
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: interval
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-refresh-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-refresh-intervals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_refresh_interval is not None:
                        for child_ref in self.lsp_refresh_interval:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspRefreshIntervals']['meta_info']


            class Distribute(object):
                """
                IS\-IS Distribute BGP\-LS configuration
                
                .. attribute:: dist_inst_id
                
                	Instance ID
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: dist_throttle
                
                	Seconds
                	**type**\:  int
                
                	**range:** 1..20
                
                	**units**\: second
                
                .. attribute:: level
                
                	Level
                	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.dist_inst_id = None
                    self.dist_throttle = None
                    self.level = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:distribute'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.dist_inst_id is not None:
                        return True

                    if self.dist_throttle is not None:
                        return True

                    if self.level is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Distribute']['meta_info']


            class LspAcceptPasswords(object):
                """
                LSP/SNP accept password configuration
                
                .. attribute:: lsp_accept_password
                
                	LSP/SNP accept passwords. This requires the existence of an LSPPassword of the same level 
                	**type**\: list of    :py:class:`LspAcceptPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_accept_password = YList()
                    self.lsp_accept_password.parent = self
                    self.lsp_accept_password.name = 'lsp_accept_password'


                class LspAcceptPassword(object):
                    """
                    LSP/SNP accept passwords. This requires the
                    existence of an LSPPassword of the same level
                    .
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: password
                    
                    	Password
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.password = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-accept-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.password is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-accept-passwords'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_accept_password is not None:
                        for child_ref in self.lsp_accept_password:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspAcceptPasswords']['meta_info']


            class LspMtus(object):
                """
                LSP MTU configuration
                
                .. attribute:: lsp_mtu
                
                	LSP MTU
                	**type**\: list of    :py:class:`LspMtu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus.LspMtu>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_mtu = YList()
                    self.lsp_mtu.parent = self
                    self.lsp_mtu.name = 'lsp_mtu'


                class LspMtu(object):
                    """
                    LSP MTU
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: mtu
                    
                    	Bytes
                    	**type**\:  int
                    
                    	**range:** 128..4352
                    
                    	**mandatory**\: True
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-mtu[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspMtus.LspMtu']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-mtus'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_mtu is not None:
                        for child_ref in self.lsp_mtu:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspMtus']['meta_info']


            class Nsf(object):
                """
                IS\-IS NSF configuration
                
                .. attribute:: flavor
                
                	NSF not configured if item is deleted
                	**type**\:   :py:class:`IsisNsfFlavorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisNsfFlavorEnum>`
                
                .. attribute:: interface_timer
                
                	Per\-interface time period to wait for a restart ACK during an IETF\-NSF restart. This configuration has no effect if IETF\-NSF is not configured
                	**type**\:  int
                
                	**range:** 1..20
                
                	**units**\: second
                
                	**default value**\: 1
                
                .. attribute:: lifetime
                
                	Maximum route lifetime following restart. When this lifetime expires, old routes will be purged from the RIB
                	**type**\:  int
                
                	**range:** 5..300
                
                	**units**\: second
                
                	**default value**\: 90
                
                .. attribute:: max_interface_timer_expiry
                
                	Maximum number of times an interface timer may expire during an IETF\-NSF restart before the NSF restart is aborted. This configuration has no effect if IETF NSF is not configured
                	**type**\:  int
                
                	**range:** 1..10
                
                	**default value**\: 10
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flavor = None
                    self.interface_timer = None
                    self.lifetime = None
                    self.max_interface_timer_expiry = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:nsf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.flavor is not None:
                        return True

                    if self.interface_timer is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.max_interface_timer_expiry is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Nsf']['meta_info']


            class LinkGroups(object):
                """
                Link Group
                
                .. attribute:: link_group
                
                	Configuration for link group name
                	**type**\: list of    :py:class:`LinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups.LinkGroup>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.link_group = YList()
                    self.link_group.parent = self
                    self.link_group.name = 'link_group'


                class LinkGroup(object):
                    """
                    Configuration for link group name
                    
                    .. attribute:: link_group_name  <key>
                    
                    	Link Group Name
                    	**type**\:  str
                    
                    	**length:** 1..40
                    
                    .. attribute:: enable
                    
                    	Flag to indicate that linkgroup should be running.  This must be the first object created when a linkgroup is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS linkgroup will be removed
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: metric_offset
                    
                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                    	**type**\:  int
                    
                    	**range:** 0..16777215
                    
                    .. attribute:: minimum_members
                    
                    	Minimum Members
                    	**type**\:  int
                    
                    	**range:** 2..64
                    
                    	**default value**\: 2
                    
                    .. attribute:: revert_members
                    
                    	Revert Members
                    	**type**\:  int
                    
                    	**range:** 2..64
                    
                    	**default value**\: 2
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.link_group_name = None
                        self.enable = None
                        self.metric_offset = None
                        self.minimum_members = None
                        self.revert_members = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.link_group_name is None:
                            raise YPYModelError('Key property link_group_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:link-group[Cisco-IOS-XR-clns-isis-cfg:link-group-name = ' + str(self.link_group_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.link_group_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.metric_offset is not None:
                            return True

                        if self.minimum_members is not None:
                            return True

                        if self.revert_members is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LinkGroups.LinkGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:link-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.link_group is not None:
                        for child_ref in self.link_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LinkGroups']['meta_info']


            class LspCheckIntervals(object):
                """
                LSP checksum check interval configuration
                
                .. attribute:: lsp_check_interval
                
                	LSP checksum check interval parameters
                	**type**\: list of    :py:class:`LspCheckInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_check_interval = YList()
                    self.lsp_check_interval.parent = self
                    self.lsp_check_interval.name = 'lsp_check_interval'


                class LspCheckInterval(object):
                    """
                    LSP checksum check interval parameters
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: interval
                    
                    	LSP checksum check interval time in seconds
                    	**type**\:  int
                    
                    	**range:** 10..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-check-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-check-intervals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_check_interval is not None:
                        for child_ref in self.lsp_check_interval:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspCheckIntervals']['meta_info']


            class LspPasswords(object):
                """
                LSP/SNP password configuration
                
                .. attribute:: lsp_password
                
                	LSP/SNP passwords. This must exist if an LSPAcceptPassword of the same level exists
                	**type**\: list of    :py:class:`LspPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords.LspPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_password = YList()
                    self.lsp_password.parent = self
                    self.lsp_password.name = 'lsp_password'


                class LspPassword(object):
                    """
                    LSP/SNP passwords. This must exist if an
                    LSPAcceptPassword of the same level exists.
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: algorithm
                    
                    	Algorithm
                    	**type**\:   :py:class:`IsisAuthenticationAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithmEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: authentication_type
                    
                    	SNP packet authentication mode
                    	**type**\:   :py:class:`IsisSnpAuthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisSnpAuthEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: failure_mode
                    
                    	Failure Mode
                    	**type**\:   :py:class:`IsisAuthenticationFailureModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureModeEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: password
                    
                    	Password or unencrypted Key Chain name
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.algorithm = None
                        self.authentication_type = None
                        self.failure_mode = None
                        self.password = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.algorithm is not None:
                            return True

                        if self.authentication_type is not None:
                            return True

                        if self.failure_mode is not None:
                            return True

                        if self.password is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspPasswords.LspPassword']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-passwords'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_password is not None:
                        for child_ref in self.lsp_password:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspPasswords']['meta_info']


            class Nets(object):
                """
                NET configuration
                
                .. attribute:: net
                
                	Network Entity Title (NET)
                	**type**\: list of    :py:class:`Net <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets.Net>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.net = YList()
                    self.net.parent = self
                    self.net.name = 'net'


                class Net(object):
                    """
                    Network Entity Title (NET)
                    
                    .. attribute:: net_name  <key>
                    
                    	Network Entity Title
                    	**type**\:  str
                    
                    	**pattern:** [a\-fA\-F0\-9]{2}(\\.[a\-fA\-F0\-9]{4}){3,9}\\.[a\-fA\-F0\-9]{2}
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.net_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.net_name is None:
                            raise YPYModelError('Key property net_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:net[Cisco-IOS-XR-clns-isis-cfg:net-name = ' + str(self.net_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.net_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.Nets.Net']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:nets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.net is not None:
                        for child_ref in self.net:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Nets']['meta_info']


            class LspLifetimes(object):
                """
                LSP lifetime configuration
                
                .. attribute:: lsp_lifetime
                
                	Maximum LSP lifetime
                	**type**\: list of    :py:class:`LspLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes.LspLifetime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_lifetime = YList()
                    self.lsp_lifetime.parent = self
                    self.lsp_lifetime.name = 'lsp_lifetime'


                class LspLifetime(object):
                    """
                    Maximum LSP lifetime
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: lifetime
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.lifetime = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-lifetime[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspLifetimes.LspLifetime']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-lifetimes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_lifetime is not None:
                        for child_ref in self.lsp_lifetime:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspLifetimes']['meta_info']


            class OverloadBits(object):
                """
                LSP overload\-bit configuration
                
                .. attribute:: overload_bit
                
                	Set the overload bit in the System LSP so that other routers avoid this one in SPF calculations. This may be done either unconditionally, or on startup until either a set time has passed or IS\-IS is informed that BGP has converged. This is an Object with a union discriminated on an integer value of the ISISOverloadBitModeType
                	**type**\: list of    :py:class:`OverloadBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits.OverloadBit>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.overload_bit = YList()
                    self.overload_bit.parent = self
                    self.overload_bit.name = 'overload_bit'


                class OverloadBit(object):
                    """
                    Set the overload bit in the System LSP so
                    that other routers avoid this one in SPF
                    calculations. This may be done either
                    unconditionally, or on startup until either a
                    set time has passed or IS\-IS is informed that
                    BGP has converged. This is an Object with a
                    union discriminated on an integer value of
                    the ISISOverloadBitModeType.
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                    
                    .. attribute:: external_adv_type
                    
                    	Advertise prefixes from other protocols
                    	**type**\:   :py:class:`IsisAdvTypeExternalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeExternalEnum>`
                    
                    .. attribute:: hippity_period
                    
                    	Time in seconds to advertise ourself as overloaded after process startup
                    	**type**\:  int
                    
                    	**range:** 5..86400
                    
                    	**units**\: second
                    
                    .. attribute:: inter_level_adv_type
                    
                    	Advertise prefixes across ISIS levels
                    	**type**\:   :py:class:`IsisAdvTypeInterLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeInterLevelEnum>`
                    
                    .. attribute:: overload_bit_mode
                    
                    	Circumstances under which the overload bit is set in the system LSP
                    	**type**\:   :py:class:`IsisOverloadBitModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisOverloadBitModeEnum>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.external_adv_type = None
                        self.hippity_period = None
                        self.inter_level_adv_type = None
                        self.overload_bit_mode = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYModelError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:overload-bit[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.level is not None:
                            return True

                        if self.external_adv_type is not None:
                            return True

                        if self.hippity_period is not None:
                            return True

                        if self.inter_level_adv_type is not None:
                            return True

                        if self.overload_bit_mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.OverloadBits.OverloadBit']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:overload-bits'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.overload_bit is not None:
                        for child_ref in self.overload_bit:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.OverloadBits']['meta_info']


            class Interfaces(object):
                """
                Per\-interface configuration
                
                .. attribute:: interface
                
                	Configuration for an IS\-IS interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Configuration for an IS\-IS interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: circuit_type
                    
                    	Configure circuit type for interface
                    	**type**\:   :py:class:`IsisConfigurableLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevelsEnum>`
                    
                    	**default value**\: level1-and2
                    
                    .. attribute:: csnp_intervals
                    
                    	CSNP\-interval configuration
                    	**type**\:   :py:class:`CsnpIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals>`
                    
                    .. attribute:: hello_accept_passwords
                    
                    	IIH accept password configuration
                    	**type**\:   :py:class:`HelloAcceptPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords>`
                    
                    .. attribute:: hello_intervals
                    
                    	Hello\-interval configuration
                    	**type**\:   :py:class:`HelloIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals>`
                    
                    .. attribute:: hello_multipliers
                    
                    	Hello\-multiplier configuration
                    	**type**\:   :py:class:`HelloMultipliers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers>`
                    
                    .. attribute:: hello_paddings
                    
                    	Hello\-padding configuration
                    	**type**\:   :py:class:`HelloPaddings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings>`
                    
                    .. attribute:: hello_passwords
                    
                    	IIH password configuration
                    	**type**\:   :py:class:`HelloPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords>`
                    
                    .. attribute:: interface_afs
                    
                    	Per\-interface address\-family configuration
                    	**type**\:   :py:class:`InterfaceAfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs>`
                    
                    .. attribute:: link_down_fast_detect
                    
                    	Configure high priority detection of interface down event
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lsp_fast_flood_thresholds
                    
                    	LSP fast flood threshold configuration
                    	**type**\:   :py:class:`LspFastFloodThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds>`
                    
                    .. attribute:: lsp_intervals
                    
                    	LSP\-interval configuration
                    	**type**\:   :py:class:`LspIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals>`
                    
                    .. attribute:: lsp_retransmit_intervals
                    
                    	LSP\-retransmission\-interval configuration
                    	**type**\:   :py:class:`LspRetransmitIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals>`
                    
                    .. attribute:: lsp_retransmit_throttle_intervals
                    
                    	LSP\-retransmission\-throttle\-interval configuration
                    	**type**\:   :py:class:`LspRetransmitThrottleIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals>`
                    
                    .. attribute:: mesh_group
                    
                    	Mesh\-group configuration
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`MeshGroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.MeshGroupEnum>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    .. attribute:: point_to_point
                    
                    	IS\-IS will attempt to form point\-to\-point over LAN adjacencies over this interface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: prefix_attribute_n_flag_clears
                    
                    	Prefix attribute N flag clear configuration
                    	**type**\:   :py:class:`PrefixAttributeNFlagClears <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears>`
                    
                    .. attribute:: priorities
                    
                    	DIS\-election priority configuration
                    	**type**\:   :py:class:`Priorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities>`
                    
                    .. attribute:: running
                    
                    	This object must be set before any other configuration is supplied for an interface, and must be the last per\-interface configuration object to be removed
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: state
                    
                    	Enable/Disable routing
                    	**type**\:   :py:class:`IsisInterfaceStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceStateEnum>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.bfd = Isis.Instances.Instance.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self.circuit_type = None
                        self.csnp_intervals = Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals()
                        self.csnp_intervals.parent = self
                        self.hello_accept_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords()
                        self.hello_accept_passwords.parent = self
                        self.hello_intervals = Isis.Instances.Instance.Interfaces.Interface.HelloIntervals()
                        self.hello_intervals.parent = self
                        self.hello_multipliers = Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers()
                        self.hello_multipliers.parent = self
                        self.hello_paddings = Isis.Instances.Instance.Interfaces.Interface.HelloPaddings()
                        self.hello_paddings.parent = self
                        self.hello_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloPasswords()
                        self.hello_passwords.parent = self
                        self.interface_afs = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs()
                        self.interface_afs.parent = self
                        self.link_down_fast_detect = None
                        self.lsp_fast_flood_thresholds = Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds()
                        self.lsp_fast_flood_thresholds.parent = self
                        self.lsp_intervals = Isis.Instances.Instance.Interfaces.Interface.LspIntervals()
                        self.lsp_intervals.parent = self
                        self.lsp_retransmit_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals()
                        self.lsp_retransmit_intervals.parent = self
                        self.lsp_retransmit_throttle_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals()
                        self.lsp_retransmit_throttle_intervals.parent = self
                        self.mesh_group = None
                        self.point_to_point = None
                        self.prefix_attribute_n_flag_clears = Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears()
                        self.prefix_attribute_n_flag_clears.parent = self
                        self.priorities = Isis.Instances.Instance.Interfaces.Interface.Priorities()
                        self.priorities.parent = self
                        self.running = None
                        self.state = None

                    class MeshGroupEnum(Enum):
                        """
                        MeshGroupEnum

                        Mesh\-group configuration

                        .. data:: blocked = 0

                        	Blocked mesh group.  Changed LSPs are not

                        	flooded over blocked interfaces

                        """

                        blocked = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.MeshGroupEnum']



                    class LspRetransmitThrottleIntervals(object):
                        """
                        LSP\-retransmission\-throttle\-interval
                        configuration
                        
                        .. attribute:: lsp_retransmit_throttle_interval
                        
                        	Minimum interval betwen retransissions of different LSPs
                        	**type**\: list of    :py:class:`LspRetransmitThrottleInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_retransmit_throttle_interval = YList()
                            self.lsp_retransmit_throttle_interval.parent = self
                            self.lsp_retransmit_throttle_interval.name = 'lsp_retransmit_throttle_interval'


                        class LspRetransmitThrottleInterval(object):
                            """
                            Minimum interval betwen retransissions of
                            different LSPs
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-throttle-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-throttle-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.lsp_retransmit_throttle_interval is not None:
                                for child_ref in self.lsp_retransmit_throttle_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals']['meta_info']


                    class LspRetransmitIntervals(object):
                        """
                        LSP\-retransmission\-interval configuration
                        
                        .. attribute:: lsp_retransmit_interval
                        
                        	Interval between retransmissions of the same LSP
                        	**type**\: list of    :py:class:`LspRetransmitInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_retransmit_interval = YList()
                            self.lsp_retransmit_interval.parent = self
                            self.lsp_retransmit_interval.name = 'lsp_retransmit_interval'


                        class LspRetransmitInterval(object):
                            """
                            Interval between retransmissions of the
                            same LSP
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.lsp_retransmit_interval is not None:
                                for child_ref in self.lsp_retransmit_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals']['meta_info']


                    class Bfd(object):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by isis
                        	**type**\:  int
                        
                        	**range:** 2..50
                        
                        .. attribute:: enable_ipv4
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\:  bool
                        
                        .. attribute:: enable_ipv6
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\:  bool
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by isis
                        	**type**\:  int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.detection_multiplier = None
                            self.enable_ipv4 = None
                            self.enable_ipv6 = None
                            self.interval = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:bfd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.detection_multiplier is not None:
                                return True

                            if self.enable_ipv4 is not None:
                                return True

                            if self.enable_ipv6 is not None:
                                return True

                            if self.interval is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.Bfd']['meta_info']


                    class Priorities(object):
                        """
                        DIS\-election priority configuration
                        
                        .. attribute:: priority
                        
                        	DIS\-election priority
                        	**type**\: list of    :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.priority = YList()
                            self.priority.parent = self
                            self.priority.name = 'priority'


                        class Priority(object):
                            """
                            DIS\-election priority
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: priority_value
                            
                            	Priority
                            	**type**\:  int
                            
                            	**range:** 0..127
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.priority_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.priority_value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priorities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.priority is not None:
                                for child_ref in self.priority:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities']['meta_info']


                    class HelloAcceptPasswords(object):
                        """
                        IIH accept password configuration
                        
                        .. attribute:: hello_accept_password
                        
                        	IIH accept passwords. This requires the existence of a HelloPassword of the same level
                        	**type**\: list of    :py:class:`HelloAcceptPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_accept_password = YList()
                            self.hello_accept_password.parent = self
                            self.hello_accept_password.name = 'hello_accept_password'


                        class HelloAcceptPassword(object):
                            """
                            IIH accept passwords. This requires the
                            existence of a HelloPassword of the same
                            level.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: password
                            
                            	Password
                            	**type**\:  str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.password = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-accept-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.password is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-accept-passwords'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.hello_accept_password is not None:
                                for child_ref in self.hello_accept_password:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords']['meta_info']


                    class HelloPasswords(object):
                        """
                        IIH password configuration
                        
                        .. attribute:: hello_password
                        
                        	IIH passwords. This must exist if a HelloAcceptPassword of the same level exists
                        	**type**\: list of    :py:class:`HelloPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_password = YList()
                            self.hello_password.parent = self
                            self.hello_password.name = 'hello_password'


                        class HelloPassword(object):
                            """
                            IIH passwords. This must exist if a
                            HelloAcceptPassword of the same level
                            exists.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: algorithm
                            
                            	Algorithm
                            	**type**\:   :py:class:`IsisAuthenticationAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithmEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: failure_mode
                            
                            	Failure Mode
                            	**type**\:   :py:class:`IsisAuthenticationFailureModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureModeEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: password
                            
                            	Password or unencrypted Key Chain name
                            	**type**\:  str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.algorithm = None
                                self.failure_mode = None
                                self.password = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.algorithm is not None:
                                    return True

                                if self.failure_mode is not None:
                                    return True

                                if self.password is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-passwords'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.hello_password is not None:
                                for child_ref in self.hello_password:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords']['meta_info']


                    class HelloPaddings(object):
                        """
                        Hello\-padding configuration
                        
                        .. attribute:: hello_padding
                        
                        	Pad IIHs to the interface MTU
                        	**type**\: list of    :py:class:`HelloPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_padding = YList()
                            self.hello_padding.parent = self
                            self.hello_padding.name = 'hello_padding'


                        class HelloPadding(object):
                            """
                            Pad IIHs to the interface MTU
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: padding_type
                            
                            	Hello padding type value
                            	**type**\:   :py:class:`IsisHelloPaddingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisHelloPaddingEnum>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.padding_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-padding[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.padding_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-paddings'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.hello_padding is not None:
                                for child_ref in self.hello_padding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings']['meta_info']


                    class HelloMultipliers(object):
                        """
                        Hello\-multiplier configuration
                        
                        .. attribute:: hello_multiplier
                        
                        	Hello\-multiplier configuration. The number of successive IIHs that may be missed on an adjacency before it is considered down
                        	**type**\: list of    :py:class:`HelloMultiplier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_multiplier = YList()
                            self.hello_multiplier.parent = self
                            self.hello_multiplier.name = 'hello_multiplier'


                        class HelloMultiplier(object):
                            """
                            Hello\-multiplier configuration. The number
                            of successive IIHs that may be missed on an
                            adjacency before it is considered down.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: multiplier
                            
                            	Hello multiplier value
                            	**type**\:  int
                            
                            	**range:** 3..1000
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.multiplier = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-multiplier[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.multiplier is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-multipliers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.hello_multiplier is not None:
                                for child_ref in self.hello_multiplier:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers']['meta_info']


                    class LspFastFloodThresholds(object):
                        """
                        LSP fast flood threshold configuration
                        
                        .. attribute:: lsp_fast_flood_threshold
                        
                        	Number of LSPs to send back to back on an interface
                        	**type**\: list of    :py:class:`LspFastFloodThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_fast_flood_threshold = YList()
                            self.lsp_fast_flood_threshold.parent = self
                            self.lsp_fast_flood_threshold.name = 'lsp_fast_flood_threshold'


                        class LspFastFloodThreshold(object):
                            """
                            Number of LSPs to send back to back on an
                            interface.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: count
                            
                            	Count
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.count = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-fast-flood-threshold[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-fast-flood-thresholds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.lsp_fast_flood_threshold is not None:
                                for child_ref in self.lsp_fast_flood_threshold:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds']['meta_info']


                    class PrefixAttributeNFlagClears(object):
                        """
                        Prefix attribute N flag clear configuration
                        
                        .. attribute:: prefix_attribute_n_flag_clear
                        
                        	Clear the N flag in prefix attribute flags sub\-TLV
                        	**type**\: list of    :py:class:`PrefixAttributeNFlagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.prefix_attribute_n_flag_clear = YList()
                            self.prefix_attribute_n_flag_clear.parent = self
                            self.prefix_attribute_n_flag_clear.name = 'prefix_attribute_n_flag_clear'


                        class PrefixAttributeNFlagClear(object):
                            """
                            Clear the N flag in prefix attribute flags
                            sub\-TLV
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-attribute-n-flag-clear[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-attribute-n-flag-clears'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.prefix_attribute_n_flag_clear is not None:
                                for child_ref in self.prefix_attribute_n_flag_clear:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears']['meta_info']


                    class HelloIntervals(object):
                        """
                        Hello\-interval configuration
                        
                        .. attribute:: hello_interval
                        
                        	Hello\-interval configuration. The interval at which IIH packets will be sent. This will be three times quicker on a LAN interface which has been electted DIS
                        	**type**\: list of    :py:class:`HelloInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_interval = YList()
                            self.hello_interval.parent = self
                            self.hello_interval.name = 'hello_interval'


                        class HelloInterval(object):
                            """
                            Hello\-interval configuration. The interval
                            at which IIH packets will be sent. This
                            will be three times quicker on a LAN
                            interface which has been electted DIS.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.hello_interval is not None:
                                for child_ref in self.hello_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals']['meta_info']


                    class InterfaceAfs(object):
                        """
                        Per\-interface address\-family configuration
                        
                        .. attribute:: interface_af
                        
                        	Configuration for an IS\-IS address\-family on a single interface. If a named (non\-default) topology is being created it must be multicast. Also the topology ID mustbe set first and delete last in the router configuration
                        	**type**\: list of    :py:class:`InterfaceAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_af = YList()
                            self.interface_af.parent = self
                            self.interface_af.name = 'interface_af'


                        class InterfaceAf(object):
                            """
                            Configuration for an IS\-IS address\-family
                            on a single interface. If a named
                            (non\-default) topology is being created it
                            must be multicast. Also the topology ID
                            mustbe set first and delete last in the
                            router configuration.
                            
                            .. attribute:: af_name  <key>
                            
                            	Address family
                            	**type**\:   :py:class:`IsisAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamilyEnum>`
                            
                            .. attribute:: saf_name  <key>
                            
                            	Sub address family
                            	**type**\:   :py:class:`IsisSubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamilyEnum>`
                            
                            .. attribute:: interface_af_data
                            
                            	Data container
                            	**type**\:   :py:class:`InterfaceAfData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData>`
                            
                            .. attribute:: topology_name
                            
                            	keys\: topology\-name
                            	**type**\: list of    :py:class:`TopologyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.saf_name = None
                                self.interface_af_data = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData()
                                self.interface_af_data.parent = self
                                self.topology_name = YList()
                                self.topology_name.parent = self
                                self.topology_name.name = 'topology_name'


                            class InterfaceAfData(object):
                                """
                                Data container.
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\:   :py:class:`AdminTags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\:   :py:class:`AutoMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics>`
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\:   :py:class:`IsisInterfaceAfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfStateEnum>`
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\:   :py:class:`InterfaceFrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\:   :py:class:`InterfaceLinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp>`
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: prefix_sspfsid
                                
                                	Assign prefix SSPF SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSspfsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags()
                                    self.admin_tags.parent = self
                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self.interface_af_state = None
                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self.interface_link_group = None
                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics()
                                    self.metrics.parent = self
                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self.prefix_sid = None
                                    self.prefix_sspfsid = None
                                    self.running = None
                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights()
                                    self.weights.parent = self


                                class PrefixSid(object):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClearEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClearEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`IsissidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self.php = None
                                        self.type = None
                                        self.value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.explicit_null is not None:
                                            return True

                                        if self.nflag_clear is not None:
                                            return True

                                        if self.php is not None:
                                            return True

                                        if self.type is not None:
                                            return True

                                        if self.value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid']['meta_info']


                                class InterfaceFrrTable(object):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\:   :py:class:`FrrExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\:   :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\:   :py:class:`FrrRemoteLfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\:   :py:class:`FrrTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\:   :py:class:`FrrlfaCandidateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\:   :py:class:`FrrtilfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    .. attribute:: interface_frr_tiebreaker_defaults
                                    
                                    	Interface FRR Default tiebreaker configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakerDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults>`
                                    
                                    .. attribute:: interface_frr_tiebreakers
                                    
                                    	Interface FRR tiebreakers configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self
                                        self.interface_frr_tiebreaker_defaults = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults()
                                        self.interface_frr_tiebreaker_defaults.parent = self
                                        self.interface_frr_tiebreakers = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers()
                                        self.interface_frr_tiebreakers.parent = self


                                    class FrrlfaCandidateInterfaces(object):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of    :py:class:`FrrlfaCandidateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrlfa_candidate_interface = YList()
                                            self.frrlfa_candidate_interface.parent = self
                                            self.frrlfa_candidate_interface.name = 'frrlfa_candidate_interface'


                                        class FrrlfaCandidateInterface(object):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.interface_name is None:
                                                    raise YPYModelError('Key property interface_name is None')
                                                if self.frr_type is None:
                                                    raise YPYModelError('Key property frr_type is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.interface_name is not None:
                                                    return True

                                                if self.frr_type is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frrlfa_candidate_interface is not None:
                                                for child_ref in self.frrlfa_candidate_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']


                                    class FrrRemoteLfaMaxMetrics(object):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of    :py:class:`FrrRemoteLfaMaxMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_max_metric = YList()
                                            self.frr_remote_lfa_max_metric.parent = self
                                            self.frr_remote_lfa_max_metric.name = 'frr_remote_lfa_max_metric'


                                        class FrrRemoteLfaMaxMetric(object):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\:  int
                                            
                                            	**range:** 1..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.max_metric = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.max_metric is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metrics'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_remote_lfa_max_metric is not None:
                                                for child_ref in self.frr_remote_lfa_max_metric:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']


                                    class FrrTypes(object):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of    :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_type = YList()
                                            self.frr_type.parent = self
                                            self.frr_type.name = 'frr_type'


                                        class FrrType(object):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_type is not None:
                                                for child_ref in self.frr_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes']['meta_info']


                                    class FrrRemoteLfaTypes(object):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrRemoteLfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_type = YList()
                                            self.frr_remote_lfa_type.parent = self
                                            self.frr_remote_lfa_type.name = 'frr_remote_lfa_type'


                                        class FrrRemoteLfaType(object):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\:   :py:class:`IsisRemoteLfaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfaEnum>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_remote_lfa_type is not None:
                                                for child_ref in self.frr_remote_lfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']


                                    class InterfaceFrrTiebreakerDefaults(object):
                                        """
                                        Interface FRR Default tiebreaker
                                        configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker_default
                                        
                                        	Configure default tiebreaker
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreakerDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_frr_tiebreaker_default = YList()
                                            self.interface_frr_tiebreaker_default.parent = self
                                            self.interface_frr_tiebreaker_default.name = 'interface_frr_tiebreaker_default'


                                        class InterfaceFrrTiebreakerDefault(object):
                                            """
                                            Configure default tiebreaker
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreaker-default[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreaker-defaults'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_frr_tiebreaker_default is not None:
                                                for child_ref in self.interface_frr_tiebreaker_default:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info']


                                    class FrrtilfaTypes(object):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrtilfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrtilfa_type = YList()
                                            self.frrtilfa_type.parent = self
                                            self.frrtilfa_type.name = 'frrtilfa_type'


                                        class FrrtilfaType(object):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frrtilfa_type is not None:
                                                for child_ref in self.frrtilfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes']['meta_info']


                                    class FrrExcludeInterfaces(object):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of    :py:class:`FrrExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_exclude_interface = YList()
                                            self.frr_exclude_interface.parent = self
                                            self.frr_exclude_interface.name = 'frr_exclude_interface'


                                        class FrrExcludeInterface(object):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.interface_name is None:
                                                    raise YPYModelError('Key property interface_name is None')
                                                if self.frr_type is None:
                                                    raise YPYModelError('Key property frr_type is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.interface_name is not None:
                                                    return True

                                                if self.frr_type is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_exclude_interface is not None:
                                                for child_ref in self.frr_exclude_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']


                                    class InterfaceFrrTiebreakers(object):
                                        """
                                        Interface FRR tiebreakers configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker
                                        
                                        	Configure tiebreaker for multiple backups
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_frr_tiebreaker = YList()
                                            self.interface_frr_tiebreaker.parent = self
                                            self.interface_frr_tiebreaker.name = 'interface_frr_tiebreaker'


                                        class InterfaceFrrTiebreaker(object):
                                            """
                                            Configure tiebreaker for multiple
                                            backups
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: tiebreaker  <key>
                                            
                                            	Tiebreaker for which configuration applies
                                            	**type**\:   :py:class:`IsisInterfaceFrrTiebreakerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceFrrTiebreakerEnum>`
                                            
                                            .. attribute:: index
                                            
                                            	Preference order among tiebreakers
                                            	**type**\:  int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.tiebreaker = None
                                                self.index = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')
                                                if self.tiebreaker is None:
                                                    raise YPYModelError('Key property tiebreaker is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreaker[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:tiebreaker = ' + str(self.tiebreaker) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.tiebreaker is not None:
                                                    return True

                                                if self.index is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreakers'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_frr_tiebreaker is not None:
                                                for child_ref in self.interface_frr_tiebreaker:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-table'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.frr_exclude_interfaces is not None and self.frr_exclude_interfaces._has_data():
                                            return True

                                        if self.frr_remote_lfa_max_metrics is not None and self.frr_remote_lfa_max_metrics._has_data():
                                            return True

                                        if self.frr_remote_lfa_types is not None and self.frr_remote_lfa_types._has_data():
                                            return True

                                        if self.frr_types is not None and self.frr_types._has_data():
                                            return True

                                        if self.frrlfa_candidate_interfaces is not None and self.frrlfa_candidate_interfaces._has_data():
                                            return True

                                        if self.frrtilfa_types is not None and self.frrtilfa_types._has_data():
                                            return True

                                        if self.interface_frr_tiebreaker_defaults is not None and self.interface_frr_tiebreaker_defaults._has_data():
                                            return True

                                        if self.interface_frr_tiebreakers is not None and self.interface_frr_tiebreakers._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']


                                class MplsLdp(object):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sync_level = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.sync_level is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp']['meta_info']


                                class PrefixSspfsid(object):
                                    """
                                    Assign prefix SSPF SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClearEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClearEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`IsissidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self.php = None
                                        self.type = None
                                        self.value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sspfsid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.explicit_null is not None:
                                            return True

                                        if self.nflag_clear is not None:
                                            return True

                                        if self.php is not None:
                                            return True

                                        if self.type is not None:
                                            return True

                                        if self.value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid']['meta_info']


                                class AutoMetrics(object):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of    :py:class:`AutoMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.auto_metric = YList()
                                        self.auto_metric.parent = self
                                        self.auto_metric.name = 'auto_metric'


                                    class AutoMetric(object):
                                        """
                                        AutoMetric Proactive\-Protect
                                        configuration. Legal value depends on
                                        the metric\-style specified for the
                                        topology. If the metric\-style defined is
                                        narrow, then only a value between <1\-63>
                                        is allowed and if the metric\-style is
                                        defined as wide, then a value between
                                        <1\-16777214> is allowed as the
                                        auto\-metric value.
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.proactive_protect = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.proactive_protect is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.auto_metric is not None:
                                            for child_ref in self.auto_metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics']['meta_info']


                                class AdminTags(object):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of    :py:class:`AdminTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.admin_tag = YList()
                                        self.admin_tag.parent = self
                                        self.admin_tag.name = 'admin_tag'


                                    class AdminTag(object):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.admin_tag = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tag[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.admin_tag is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tags'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.admin_tag is not None:
                                            for child_ref in self.admin_tag:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags']['meta_info']


                                class InterfaceLinkGroup(object):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\:  str
                                    
                                    	**length:** 1..40
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.level = None
                                        self.link_group = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-link-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.link_group is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup']['meta_info']


                                class Metrics(object):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.metric = YList()
                                        self.metric.parent = self
                                        self.metric.name = 'metric'


                                    class Metric(object):
                                        """
                                        Metric configuration. Legal value depends on
                                        the metric\-style specified for the topology. If
                                        the metric\-style defined is narrow, then only a
                                        value between <1\-63> is allowed and if the
                                        metric\-style is defined as wide, then a value
                                        between <1\-16777215> is allowed as the metric
                                        value.  All routers exclude links with the
                                        maximum wide metric (16777215) from their SPF
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:   :py:class:`MetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum>`
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.metric = None

                                        class MetricEnum(Enum):
                                            """
                                            MetricEnum

                                            Allowed metric\: <1\-63> for narrow,

                                            <1\-16777215> for wide

                                            .. data:: maximum = 16777215

                                            	Maximum wide metric.  All routers will

                                            	exclude this link from their SPF

                                            """

                                            maximum = 16777215


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric.MetricEnum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.metric is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.metric is not None:
                                            for child_ref in self.metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics']['meta_info']


                                class Weights(object):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.weight = YList()
                                        self.weight.parent = self
                                        self.weight.name = 'weight'


                                    class Weight(object):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.weight = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.weight is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.weight is not None:
                                            for child_ref in self.weight:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-af-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.admin_tags is not None and self.admin_tags._has_data():
                                        return True

                                    if self.auto_metrics is not None and self.auto_metrics._has_data():
                                        return True

                                    if self.interface_af_state is not None:
                                        return True

                                    if self.interface_frr_table is not None and self.interface_frr_table._has_data():
                                        return True

                                    if self.interface_link_group is not None and self.interface_link_group._has_data():
                                        return True

                                    if self.metrics is not None and self.metrics._has_data():
                                        return True

                                    if self.mpls_ldp is not None and self.mpls_ldp._has_data():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid._has_data():
                                        return True

                                    if self.prefix_sspfsid is not None and self.prefix_sspfsid._has_data():
                                        return True

                                    if self.running is not None:
                                        return True

                                    if self.weights is not None and self.weights._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']


                            class TopologyName(object):
                                """
                                keys\: topology\-name
                                
                                .. attribute:: topology_name  <key>
                                
                                	Topology Name
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\:   :py:class:`AdminTags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\:   :py:class:`AutoMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics>`
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\:   :py:class:`IsisInterfaceAfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfStateEnum>`
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\:   :py:class:`InterfaceFrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\:   :py:class:`InterfaceLinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp>`
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: prefix_sspfsid
                                
                                	Assign prefix SSPF SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSspfsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.topology_name = None
                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags()
                                    self.admin_tags.parent = self
                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self.interface_af_state = None
                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self.interface_link_group = None
                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics()
                                    self.metrics.parent = self
                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self.prefix_sid = None
                                    self.prefix_sspfsid = None
                                    self.running = None
                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights()
                                    self.weights.parent = self


                                class PrefixSid(object):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClearEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClearEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`IsissidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self.php = None
                                        self.type = None
                                        self.value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.explicit_null is not None:
                                            return True

                                        if self.nflag_clear is not None:
                                            return True

                                        if self.php is not None:
                                            return True

                                        if self.type is not None:
                                            return True

                                        if self.value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid']['meta_info']


                                class InterfaceFrrTable(object):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\:   :py:class:`FrrExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\:   :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\:   :py:class:`FrrRemoteLfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\:   :py:class:`FrrTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\:   :py:class:`FrrlfaCandidateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\:   :py:class:`FrrtilfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    .. attribute:: interface_frr_tiebreaker_defaults
                                    
                                    	Interface FRR Default tiebreaker configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakerDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults>`
                                    
                                    .. attribute:: interface_frr_tiebreakers
                                    
                                    	Interface FRR tiebreakers configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self
                                        self.interface_frr_tiebreaker_defaults = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults()
                                        self.interface_frr_tiebreaker_defaults.parent = self
                                        self.interface_frr_tiebreakers = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers()
                                        self.interface_frr_tiebreakers.parent = self


                                    class FrrlfaCandidateInterfaces(object):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of    :py:class:`FrrlfaCandidateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrlfa_candidate_interface = YList()
                                            self.frrlfa_candidate_interface.parent = self
                                            self.frrlfa_candidate_interface.name = 'frrlfa_candidate_interface'


                                        class FrrlfaCandidateInterface(object):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.interface_name is None:
                                                    raise YPYModelError('Key property interface_name is None')
                                                if self.frr_type is None:
                                                    raise YPYModelError('Key property frr_type is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.interface_name is not None:
                                                    return True

                                                if self.frr_type is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frrlfa_candidate_interface is not None:
                                                for child_ref in self.frrlfa_candidate_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']


                                    class FrrRemoteLfaMaxMetrics(object):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of    :py:class:`FrrRemoteLfaMaxMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_max_metric = YList()
                                            self.frr_remote_lfa_max_metric.parent = self
                                            self.frr_remote_lfa_max_metric.name = 'frr_remote_lfa_max_metric'


                                        class FrrRemoteLfaMaxMetric(object):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\:  int
                                            
                                            	**range:** 1..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.max_metric = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.max_metric is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metrics'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_remote_lfa_max_metric is not None:
                                                for child_ref in self.frr_remote_lfa_max_metric:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']


                                    class FrrTypes(object):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of    :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_type = YList()
                                            self.frr_type.parent = self
                                            self.frr_type.name = 'frr_type'


                                        class FrrType(object):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_type is not None:
                                                for child_ref in self.frr_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes']['meta_info']


                                    class FrrRemoteLfaTypes(object):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrRemoteLfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_type = YList()
                                            self.frr_remote_lfa_type.parent = self
                                            self.frr_remote_lfa_type.name = 'frr_remote_lfa_type'


                                        class FrrRemoteLfaType(object):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\:   :py:class:`IsisRemoteLfaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfaEnum>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_remote_lfa_type is not None:
                                                for child_ref in self.frr_remote_lfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']


                                    class InterfaceFrrTiebreakerDefaults(object):
                                        """
                                        Interface FRR Default tiebreaker
                                        configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker_default
                                        
                                        	Configure default tiebreaker
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreakerDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_frr_tiebreaker_default = YList()
                                            self.interface_frr_tiebreaker_default.parent = self
                                            self.interface_frr_tiebreaker_default.name = 'interface_frr_tiebreaker_default'


                                        class InterfaceFrrTiebreakerDefault(object):
                                            """
                                            Configure default tiebreaker
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreaker-default[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreaker-defaults'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_frr_tiebreaker_default is not None:
                                                for child_ref in self.interface_frr_tiebreaker_default:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info']


                                    class FrrtilfaTypes(object):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrtilfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrtilfa_type = YList()
                                            self.frrtilfa_type.parent = self
                                            self.frrtilfa_type.name = 'frrtilfa_type'


                                        class FrrtilfaType(object):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frrtilfa_type is not None:
                                                for child_ref in self.frrtilfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes']['meta_info']


                                    class FrrExcludeInterfaces(object):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of    :py:class:`FrrExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_exclude_interface = YList()
                                            self.frr_exclude_interface.parent = self
                                            self.frr_exclude_interface.name = 'frr_exclude_interface'


                                        class FrrExcludeInterface(object):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`IsisfrrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrEnum>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.interface_name is None:
                                                    raise YPYModelError('Key property interface_name is None')
                                                if self.frr_type is None:
                                                    raise YPYModelError('Key property frr_type is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.interface_name is not None:
                                                    return True

                                                if self.frr_type is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.frr_exclude_interface is not None:
                                                for child_ref in self.frr_exclude_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']


                                    class InterfaceFrrTiebreakers(object):
                                        """
                                        Interface FRR tiebreakers configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker
                                        
                                        	Configure tiebreaker for multiple backups
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_frr_tiebreaker = YList()
                                            self.interface_frr_tiebreaker.parent = self
                                            self.interface_frr_tiebreaker.name = 'interface_frr_tiebreaker'


                                        class InterfaceFrrTiebreaker(object):
                                            """
                                            Configure tiebreaker for multiple
                                            backups
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                            
                                            .. attribute:: tiebreaker  <key>
                                            
                                            	Tiebreaker for which configuration applies
                                            	**type**\:   :py:class:`IsisInterfaceFrrTiebreakerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceFrrTiebreakerEnum>`
                                            
                                            .. attribute:: index
                                            
                                            	Preference order among tiebreakers
                                            	**type**\:  int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.tiebreaker = None
                                                self.index = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYModelError('Key property level is None')
                                                if self.tiebreaker is None:
                                                    raise YPYModelError('Key property tiebreaker is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreaker[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:tiebreaker = ' + str(self.tiebreaker) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.level is not None:
                                                    return True

                                                if self.tiebreaker is not None:
                                                    return True

                                                if self.index is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-tiebreakers'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_frr_tiebreaker is not None:
                                                for child_ref in self.interface_frr_tiebreaker:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-table'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.frr_exclude_interfaces is not None and self.frr_exclude_interfaces._has_data():
                                            return True

                                        if self.frr_remote_lfa_max_metrics is not None and self.frr_remote_lfa_max_metrics._has_data():
                                            return True

                                        if self.frr_remote_lfa_types is not None and self.frr_remote_lfa_types._has_data():
                                            return True

                                        if self.frr_types is not None and self.frr_types._has_data():
                                            return True

                                        if self.frrlfa_candidate_interfaces is not None and self.frrlfa_candidate_interfaces._has_data():
                                            return True

                                        if self.frrtilfa_types is not None and self.frrtilfa_types._has_data():
                                            return True

                                        if self.interface_frr_tiebreaker_defaults is not None and self.interface_frr_tiebreaker_defaults._has_data():
                                            return True

                                        if self.interface_frr_tiebreakers is not None and self.interface_frr_tiebreakers._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']


                                class MplsLdp(object):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sync_level = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.sync_level is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp']['meta_info']


                                class PrefixSspfsid(object):
                                    """
                                    Assign prefix SSPF SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClearEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClearEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlagEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`IsissidEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self.php = None
                                        self.type = None
                                        self.value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sspfsid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.explicit_null is not None:
                                            return True

                                        if self.nflag_clear is not None:
                                            return True

                                        if self.php is not None:
                                            return True

                                        if self.type is not None:
                                            return True

                                        if self.value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid']['meta_info']


                                class AutoMetrics(object):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of    :py:class:`AutoMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.auto_metric = YList()
                                        self.auto_metric.parent = self
                                        self.auto_metric.name = 'auto_metric'


                                    class AutoMetric(object):
                                        """
                                        AutoMetric Proactive\-Protect
                                        configuration. Legal value depends on
                                        the metric\-style specified for the
                                        topology. If the metric\-style defined is
                                        narrow, then only a value between <1\-63>
                                        is allowed and if the metric\-style is
                                        defined as wide, then a value between
                                        <1\-16777214> is allowed as the
                                        auto\-metric value.
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.proactive_protect = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.proactive_protect is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.auto_metric is not None:
                                            for child_ref in self.auto_metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics']['meta_info']


                                class AdminTags(object):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of    :py:class:`AdminTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.admin_tag = YList()
                                        self.admin_tag.parent = self
                                        self.admin_tag.name = 'admin_tag'


                                    class AdminTag(object):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.admin_tag = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tag[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.admin_tag is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tags'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.admin_tag is not None:
                                            for child_ref in self.admin_tag:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags']['meta_info']


                                class InterfaceLinkGroup(object):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\:  str
                                    
                                    	**length:** 1..40
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: _is_presence
                                    
                                    	Is present if this instance represents presence container else not
                                    	**type**\: bool
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self._is_presence = True
                                        self.level = None
                                        self.link_group = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-link-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self._is_presence:
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.link_group is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup']['meta_info']


                                class Metrics(object):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.metric = YList()
                                        self.metric.parent = self
                                        self.metric.name = 'metric'


                                    class Metric(object):
                                        """
                                        Metric configuration. Legal value depends on
                                        the metric\-style specified for the topology. If
                                        the metric\-style defined is narrow, then only a
                                        value between <1\-63> is allowed and if the
                                        metric\-style is defined as wide, then a value
                                        between <1\-16777215> is allowed as the metric
                                        value.  All routers exclude links with the
                                        maximum wide metric (16777215) from their SPF
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:   :py:class:`MetricEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum>`
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.metric = None

                                        class MetricEnum(Enum):
                                            """
                                            MetricEnum

                                            Allowed metric\: <1\-63> for narrow,

                                            <1\-16777215> for wide

                                            .. data:: maximum = 16777215

                                            	Maximum wide metric.  All routers will

                                            	exclude this link from their SPF

                                            """

                                            maximum = 16777215


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.MetricEnum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.metric is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.metric is not None:
                                            for child_ref in self.metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics']['meta_info']


                                class Weights(object):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.weight = YList()
                                        self.weight.parent = self
                                        self.weight.name = 'weight'


                                    class Weight(object):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.weight = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYModelError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.level is not None:
                                                return True

                                            if self.weight is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.weight is not None:
                                            for child_ref in self.weight:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.topology_name is None:
                                        raise YPYModelError('Key property topology_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:topology-name[Cisco-IOS-XR-clns-isis-cfg:topology-name = ' + str(self.topology_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.topology_name is not None:
                                        return True

                                    if self.admin_tags is not None and self.admin_tags._has_data():
                                        return True

                                    if self.auto_metrics is not None and self.auto_metrics._has_data():
                                        return True

                                    if self.interface_af_state is not None:
                                        return True

                                    if self.interface_frr_table is not None and self.interface_frr_table._has_data():
                                        return True

                                    if self.interface_link_group is not None and self.interface_link_group._has_data():
                                        return True

                                    if self.metrics is not None and self.metrics._has_data():
                                        return True

                                    if self.mpls_ldp is not None and self.mpls_ldp._has_data():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid._has_data():
                                        return True

                                    if self.prefix_sspfsid is not None and self.prefix_sspfsid._has_data():
                                        return True

                                    if self.running is not None:
                                        return True

                                    if self.weights is not None and self.weights._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.af_name is None:
                                    raise YPYModelError('Key property af_name is None')
                                if self.saf_name is None:
                                    raise YPYModelError('Key property saf_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-af[Cisco-IOS-XR-clns-isis-cfg:af-name = ' + str(self.af_name) + '][Cisco-IOS-XR-clns-isis-cfg:saf-name = ' + str(self.saf_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.interface_af_data is not None and self.interface_af_data._has_data():
                                    return True

                                if self.topology_name is not None:
                                    for child_ref in self.topology_name:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-afs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_af is not None:
                                for child_ref in self.interface_af:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs']['meta_info']


                    class CsnpIntervals(object):
                        """
                        CSNP\-interval configuration
                        
                        .. attribute:: csnp_interval
                        
                        	CSNP\-interval configuration. No fixed default value as this depends on the media type of the interface
                        	**type**\: list of    :py:class:`CsnpInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.csnp_interval = YList()
                            self.csnp_interval.parent = self
                            self.csnp_interval.name = 'csnp_interval'


                        class CsnpInterval(object):
                            """
                            CSNP\-interval configuration. No fixed
                            default value as this depends on the media
                            type of the interface.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:csnp-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:csnp-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.csnp_interval is not None:
                                for child_ref in self.csnp_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals']['meta_info']


                    class LspIntervals(object):
                        """
                        LSP\-interval configuration
                        
                        .. attribute:: lsp_interval
                        
                        	Interval between transmission of LSPs on interface
                        	**type**\: list of    :py:class:`LspInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_interval = YList()
                            self.lsp_interval.parent = self
                            self.lsp_interval.name = 'lsp_interval'


                        class LspInterval(object):
                            """
                            Interval between transmission of LSPs on
                            interface.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevelEnum>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYModelError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.lsp_interval is not None:
                                for child_ref in self.lsp_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.bfd is not None and self.bfd._has_data():
                            return True

                        if self.circuit_type is not None:
                            return True

                        if self.csnp_intervals is not None and self.csnp_intervals._has_data():
                            return True

                        if self.hello_accept_passwords is not None and self.hello_accept_passwords._has_data():
                            return True

                        if self.hello_intervals is not None and self.hello_intervals._has_data():
                            return True

                        if self.hello_multipliers is not None and self.hello_multipliers._has_data():
                            return True

                        if self.hello_paddings is not None and self.hello_paddings._has_data():
                            return True

                        if self.hello_passwords is not None and self.hello_passwords._has_data():
                            return True

                        if self.interface_afs is not None and self.interface_afs._has_data():
                            return True

                        if self.link_down_fast_detect is not None:
                            return True

                        if self.lsp_fast_flood_thresholds is not None and self.lsp_fast_flood_thresholds._has_data():
                            return True

                        if self.lsp_intervals is not None and self.lsp_intervals._has_data():
                            return True

                        if self.lsp_retransmit_intervals is not None and self.lsp_retransmit_intervals._has_data():
                            return True

                        if self.lsp_retransmit_throttle_intervals is not None and self.lsp_retransmit_throttle_intervals._has_data():
                            return True

                        if self.mesh_group is not None:
                            return True

                        if self.point_to_point is not None:
                            return True

                        if self.prefix_attribute_n_flag_clears is not None and self.prefix_attribute_n_flag_clears._has_data():
                            return True

                        if self.priorities is not None and self.priorities._has_data():
                            return True

                        if self.running is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.instance_name is None:
                    raise YPYModelError('Key property instance_name is None')

                return '/Cisco-IOS-XR-clns-isis-cfg:isis/Cisco-IOS-XR-clns-isis-cfg:instances/Cisco-IOS-XR-clns-isis-cfg:instance[Cisco-IOS-XR-clns-isis-cfg:instance-name = ' + str(self.instance_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.instance_name is not None:
                    return True

                if self.adjacency_stagger is not None and self.adjacency_stagger._has_data():
                    return True

                if self.afs is not None and self.afs._has_data():
                    return True

                if self.distribute is not None and self.distribute._has_data():
                    return True

                if self.dynamic_host_name is not None:
                    return True

                if self.ignore_lsp_errors is not None:
                    return True

                if self.instance_id is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.is_type is not None:
                    return True

                if self.link_groups is not None and self.link_groups._has_data():
                    return True

                if self.log_adjacency_changes is not None:
                    return True

                if self.log_pdu_drops is not None:
                    return True

                if self.lsp_accept_passwords is not None and self.lsp_accept_passwords._has_data():
                    return True

                if self.lsp_arrival_times is not None and self.lsp_arrival_times._has_data():
                    return True

                if self.lsp_check_intervals is not None and self.lsp_check_intervals._has_data():
                    return True

                if self.lsp_generation_intervals is not None and self.lsp_generation_intervals._has_data():
                    return True

                if self.lsp_lifetimes is not None and self.lsp_lifetimes._has_data():
                    return True

                if self.lsp_mtus is not None and self.lsp_mtus._has_data():
                    return True

                if self.lsp_passwords is not None and self.lsp_passwords._has_data():
                    return True

                if self.lsp_refresh_intervals is not None and self.lsp_refresh_intervals._has_data():
                    return True

                if self.max_link_metrics is not None and self.max_link_metrics._has_data():
                    return True

                if self.nets is not None and self.nets._has_data():
                    return True

                if self.nsf is not None and self.nsf._has_data():
                    return True

                if self.nsr is not None:
                    return True

                if self.overload_bits is not None and self.overload_bits._has_data():
                    return True

                if self.running is not None:
                    return True

                if self.srgb is not None and self.srgb._has_data():
                    return True

                if self.trace_buffer_size is not None and self.trace_buffer_size._has_data():
                    return True

                if self.tracing_mode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                return meta._meta_table['Isis.Instances.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-clns-isis-cfg:isis/Cisco-IOS-XR-clns-isis-cfg:instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.instance is not None:
                for child_ref in self.instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
            return meta._meta_table['Isis.Instances']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-clns-isis-cfg:isis'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.instances is not None and self.instances._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['Isis']['meta_info']


