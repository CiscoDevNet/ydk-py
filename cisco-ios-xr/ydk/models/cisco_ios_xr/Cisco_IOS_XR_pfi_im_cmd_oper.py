""" Cisco_IOS_XR_pfi_im_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pfi\-im\-cmd package operational data.

This module contains definitions
for the following management objects\:
  interfaces\: Interface operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BmMbrStateReasonEnum(Enum):
    """
    BmMbrStateReasonEnum

    Bm mbr state reason

    .. data:: bm_mbr_state_reason_unknown = 0

    	Reason unavailable (diagnostics error)

    .. data:: bm_mbr_state_reason_unselectable_unknown = 1

    	Link cannot be used (unknown reason)

    .. data:: bm_mbr_state_reason_link_down = 2

    	Link is down

    .. data:: bm_mbr_state_reason_link_deleting = 3

    	Link is being removed from the bundle

    .. data:: bm_mbr_state_reason_creating = 4

    	Link is in the process of being created

    .. data:: bm_mbr_state_reason_bundle_creating = 5

    	Bundle is in the process of being created

    .. data:: bm_mbr_state_reason_bundle_deleting = 6

    	Bundle is in the process of being deleted

    .. data:: bm_mbr_state_reason_bundle_admin_down = 7

    	Bundle has been shut down

    .. data:: bm_mbr_state_reason_replicating = 8

    	Bundle is in the process of being replicated to

    	this location

    .. data:: bm_mbr_state_reason_bandwidth = 9

    	Incompatible with other links in the bundle

    	(bandwidth out of range)

    .. data:: bm_mbr_state_reason_loop_back = 10

    	Loopback: Actor and Partner have the same

    	System ID and Key

    .. data:: bm_mbr_state_reason_activity_type = 11

    	Incompatible with other links in the bundle

    	(LACP vs non-LACP)

    .. data:: bm_mbr_state_reason_bundle_shutdown = 12

    	Bundle shutdown is configured for the bundle

    .. data:: bm_mbr_state_reason_min_selected = 13

    	Not enough links available to meet

    	minimum-active threshold

    .. data:: bm_mbr_state_reason_max_selected = 14

    	Link is Standby due to maximum-active links

    	configuration

    .. data:: bm_mbr_state_reason_link_limit = 15

    	Bundle has too many member links configured

    .. data:: bm_mbr_state_reason_active_limit = 16

    	Bundle has reached maximum supported number of

    	active links

    .. data:: bm_mbr_state_reason_standby_unknown = 17

    	Link is Standby (unknown reason)

    .. data:: bm_mbr_state_reason_expired = 18

    	Link is Expired; LACPDUs are not being received

    	from the partner

    .. data:: bm_mbr_state_reason_defaulted = 19

    	Link is Defaulted; LACPDUs are not being

    	received from the partner

    .. data:: bm_mbr_state_reason_act_or_not_agg = 20

    	Link is Not Aggregatable (unknown reason)

    .. data:: bm_mbr_state_reason_partner_not_agg = 21

    	Partner has marked the link as Not Aggregatable

    .. data:: bm_mbr_state_reason_lagid = 22

    	Partner System ID/Key do not match that of the

    	Selected links

    .. data:: bm_mbr_state_reason_bundle_not_cfgd = 23

    	Bundle interface is not present in

    	configuration

    .. data:: bm_mbr_state_reason_bundle_not_ready = 24

    	Wait-while timer is running

    .. data:: bm_mbr_state_reason_partner_ood = 25

    	Partner has not echoed the correct parameters

    	for this link

    .. data:: bm_mbr_state_reason_partner_not_in_sync = 26

    	Partner is not Synchronized (Waiting, Standby,

    	or LAG ID mismatch)

    .. data:: bm_mbr_state_reason_foreign_partner_oos = 27

    	Partner is not Synchronized (Waiting, not

    	Selected, or out-of-date)

    .. data:: bm_mbr_state_reason_attach_unknown = 28

    	Link is Attached and has not gone Collecting

    	(unknown reason)

    .. data:: bm_mbr_state_reason_partner_not_collecting = 29

    	Partner has not advertized that it is

    	Collecting

    .. data:: bm_mbr_state_reason_collect_unknown = 30

    	Link is Collecting and has not gone

    	Distributing (unknown reason)

    .. data:: bm_mbr_state_reason_standby_foreign = 31

    	Link is marked as Standby by mLACP peer

    .. data:: bm_mbr_state_reason_bfd_starting = 32

    	Link is waiting for BFD session to start

    .. data:: bm_mbr_state_reason_bfd_down = 33

    	BFD state of this link is Down

    .. data:: bm_mbr_state_reason_bfd_nbr_unconfig = 34

    	BFD session is unconfigured on the remote end

    .. data:: bm_mbr_state_reason_mlacp = 35

    	Link is not operational as a result of mLACP

    	negotiations

    .. data:: bm_mbr_state_reason_pe_isolated = 36

    	ICCP group is isolated from the core network

    .. data:: bm_mbr_state_reason_forced_switchover = 37

    	Forced switchover to the mLACP peer

    .. data:: bm_mbr_state_reason_errdis_unknown = 38

    	Link is error disabled (unknown reason)

    .. data:: bm_mbr_state_reason_mlacp_no_mbr_state_info = 39

    	Waiting for member state information from mLACP

    	peer

    .. data:: bm_mbr_state_reason_active = 40

    	Link is Active

    .. data:: bm_mbr_state_reason_mlacp_no_bdl_state_info = 41

    	Waiting for bundle state information from mLACP

    	peer

    .. data:: bm_mbr_state_reason_mlacp_no_bdl_config_info = 42

    	Waiting for bundle configuration information

    	from mLACP peer

    .. data:: bm_mbr_state_reason_mlacp_no_bdl_sync = 43

    	Waiting for bundle to complete initial

    	synchronization with mLACP peer

    .. data:: bm_mbr_state_reason_mlacp_bdl_has_no_peer = 44

    	mLACP bundle does not have a peer device

    .. data:: bm_mbr_state_reason_mlacp_nak = 45

    	Link is being ignored due to an inconsistency

    	with mLACP peer

    .. data:: bm_mbr_state_reason_mlacp_transport_unavailable = 46

    	ICCP transport is unavailable

    .. data:: bm_mbr_state_reason_mlacp_not_configured = 47

    	ICCP Group is not fully configured

    .. data:: bm_mbr_state_reason_recovery_timer = 48

    	mLACP recovery delay timer is running

    .. data:: bm_mbr_state_reason_mlacp_standby = 49

    	mLACP peer is active

    .. data:: bm_mbr_state_reason_maximized_out = 50

    	mLACP peer has more links/bandwidth available

    .. data:: bm_mbr_state_reason_mlacp_peer_selected = 51

    	mLACP peer has one or more links Selected

    .. data:: bm_mbr_state_reason_mlacp_connect_timer_running = 52

    	mLACP bundle does not have a peer device

    	(connect timer running)

    .. data:: bm_mbr_state_reason_bundle_not_mlacp = 53

    	Bundle is not configured to run mLACP

    .. data:: bm_mbr_state_reason_no_lon = 54

    	Bundle has too many working links configured

    	(more than the maximum-active limit)

    .. data:: bm_mbr_state_reason_cumul_rel_bw_limit = 55

    	Additional bandwidth from link would exceed

    	load balancing capabilities

    .. data:: bm_mbr_state_reason_no_mac = 56

    	No MAC address available for the bundle

    .. data:: bm_mbr_state_reason_no_system_id = 57

    	No system ID available for use by this bundle

    .. data:: bm_mbr_state_reason_link_shutdown = 58

    	Link is shutdown

    .. data:: bm_mbr_state_reason_activity_mlacp = 59

    	Non-LACP link in mLACP bundle

    .. data:: bm_mbr_state_reason_activity_iccp = 60

    	LACP link in inter-chassis bundle

    .. data:: bm_mbr_state_reason_bundle_icpe_mlacp = 61

    	Parent bundle is both inter-chassis and

    	configured for mLACP

    .. data:: bm_mbr_state_reason_no_link_num = 62

    	Too many bundle members in system; no link

    	number available

    .. data:: bm_mbr_state_reason_standby_peer_higher_prio = 63

    	mLACP peer has a higher priority link

    .. data:: bm_mbr_state_reason_red_state_standby = 64

    	Link is in standby redundancy state

    .. data:: bm_mbr_state_reason_other_red_state_standby = 65

    	One or more links in the bundle are in standby

    	redundancy state

    .. data:: bm_mbr_state_reason_hold_ing = 66

    	Holding down temporary to avoid churn after

    	restart

    .. data:: bm_mbr_state_reason_bundle_error_disabled = 67

    	Bundle has been error-disabled

    .. data:: bm_mbr_state_reason_bundle_efd_disabled = 68

    	Bundle has been disabled by EFD

    .. data:: bm_mbr_state_reason_singleton_pe_isolated = 69

    	Singleton ICCP group is isolated from the core

    	network

    .. data:: bm_mbr_state_reason_bfd_ipv6_starting = 70

    	Link is waiting for BFDv6 session to start

    .. data:: bm_mbr_state_reason_bfd_ipv6_down = 71

    	BFDv6 state of this link is Down

    .. data:: bm_mbr_state_reason_bfd_ipv6_nbr_unconfig = 72

    	BFDv6 session is unconfigured on the remote end

    .. data:: bm_mbr_state_reason_timer_running = 73

    	LACP delay timer is running

    .. data:: bm_mbr_state_reason_client_bundle_ctrl = 74

    	Client has configured the bundle state Down

    .. data:: bm_mbr_state_reason_count = 75

    	Enumeration maximum value

    """

    bm_mbr_state_reason_unknown = 0

    bm_mbr_state_reason_unselectable_unknown = 1

    bm_mbr_state_reason_link_down = 2

    bm_mbr_state_reason_link_deleting = 3

    bm_mbr_state_reason_creating = 4

    bm_mbr_state_reason_bundle_creating = 5

    bm_mbr_state_reason_bundle_deleting = 6

    bm_mbr_state_reason_bundle_admin_down = 7

    bm_mbr_state_reason_replicating = 8

    bm_mbr_state_reason_bandwidth = 9

    bm_mbr_state_reason_loop_back = 10

    bm_mbr_state_reason_activity_type = 11

    bm_mbr_state_reason_bundle_shutdown = 12

    bm_mbr_state_reason_min_selected = 13

    bm_mbr_state_reason_max_selected = 14

    bm_mbr_state_reason_link_limit = 15

    bm_mbr_state_reason_active_limit = 16

    bm_mbr_state_reason_standby_unknown = 17

    bm_mbr_state_reason_expired = 18

    bm_mbr_state_reason_defaulted = 19

    bm_mbr_state_reason_act_or_not_agg = 20

    bm_mbr_state_reason_partner_not_agg = 21

    bm_mbr_state_reason_lagid = 22

    bm_mbr_state_reason_bundle_not_cfgd = 23

    bm_mbr_state_reason_bundle_not_ready = 24

    bm_mbr_state_reason_partner_ood = 25

    bm_mbr_state_reason_partner_not_in_sync = 26

    bm_mbr_state_reason_foreign_partner_oos = 27

    bm_mbr_state_reason_attach_unknown = 28

    bm_mbr_state_reason_partner_not_collecting = 29

    bm_mbr_state_reason_collect_unknown = 30

    bm_mbr_state_reason_standby_foreign = 31

    bm_mbr_state_reason_bfd_starting = 32

    bm_mbr_state_reason_bfd_down = 33

    bm_mbr_state_reason_bfd_nbr_unconfig = 34

    bm_mbr_state_reason_mlacp = 35

    bm_mbr_state_reason_pe_isolated = 36

    bm_mbr_state_reason_forced_switchover = 37

    bm_mbr_state_reason_errdis_unknown = 38

    bm_mbr_state_reason_mlacp_no_mbr_state_info = 39

    bm_mbr_state_reason_active = 40

    bm_mbr_state_reason_mlacp_no_bdl_state_info = 41

    bm_mbr_state_reason_mlacp_no_bdl_config_info = 42

    bm_mbr_state_reason_mlacp_no_bdl_sync = 43

    bm_mbr_state_reason_mlacp_bdl_has_no_peer = 44

    bm_mbr_state_reason_mlacp_nak = 45

    bm_mbr_state_reason_mlacp_transport_unavailable = 46

    bm_mbr_state_reason_mlacp_not_configured = 47

    bm_mbr_state_reason_recovery_timer = 48

    bm_mbr_state_reason_mlacp_standby = 49

    bm_mbr_state_reason_maximized_out = 50

    bm_mbr_state_reason_mlacp_peer_selected = 51

    bm_mbr_state_reason_mlacp_connect_timer_running = 52

    bm_mbr_state_reason_bundle_not_mlacp = 53

    bm_mbr_state_reason_no_lon = 54

    bm_mbr_state_reason_cumul_rel_bw_limit = 55

    bm_mbr_state_reason_no_mac = 56

    bm_mbr_state_reason_no_system_id = 57

    bm_mbr_state_reason_link_shutdown = 58

    bm_mbr_state_reason_activity_mlacp = 59

    bm_mbr_state_reason_activity_iccp = 60

    bm_mbr_state_reason_bundle_icpe_mlacp = 61

    bm_mbr_state_reason_no_link_num = 62

    bm_mbr_state_reason_standby_peer_higher_prio = 63

    bm_mbr_state_reason_red_state_standby = 64

    bm_mbr_state_reason_other_red_state_standby = 65

    bm_mbr_state_reason_hold_ing = 66

    bm_mbr_state_reason_bundle_error_disabled = 67

    bm_mbr_state_reason_bundle_efd_disabled = 68

    bm_mbr_state_reason_singleton_pe_isolated = 69

    bm_mbr_state_reason_bfd_ipv6_starting = 70

    bm_mbr_state_reason_bfd_ipv6_down = 71

    bm_mbr_state_reason_bfd_ipv6_nbr_unconfig = 72

    bm_mbr_state_reason_timer_running = 73

    bm_mbr_state_reason_client_bundle_ctrl = 74

    bm_mbr_state_reason_count = 75


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmMbrStateReasonEnum']


class BmMuxreasonEnum(Enum):
    """
    BmMuxreasonEnum

    Bm muxreason

    .. data:: bm_mux_reason_no_reason = 0

    	Selection logic has not yet been run for the

    	bundle this link is a member of

    .. data:: bm_mux_reason_link_down = 1

    	Link is down

    .. data:: bm_mux_reason_link_deleted = 2

    	Link is being removed from the bundle

    .. data:: bm_mux_reason_duplex = 3

    	Link has wrong duplexity

    .. data:: bm_mux_reason_bandwidth = 4

    	Link has wrong bandwidth

    .. data:: bm_mux_reason_loop_back = 5

    	Link is a loopback interface

    .. data:: bm_mux_reason_activity_type = 6

    	Link has wrong activity type

    .. data:: bm_mux_reason_link_limit = 7

    	Link's bundle already has maximum number of

    	members allowed

    .. data:: bm_mux_reason_shared = 8

    	Link is attached to a shared medium

    .. data:: bm_mux_reason_lagid = 9

    	Link has wrong LAG ID

    .. data:: bm_mux_reason_no_bundle = 10

    	Link's bundle does not exist

    .. data:: bm_mux_reason_no_primary = 11

    	Link's bundle has no primary link

    .. data:: bm_mux_reason_bundle_down = 12

    	Link's bundle is shut down

    .. data:: bm_mux_reason_individual = 13

    	Link is marked individual by partner

    .. data:: bm_mux_reason_defaulted = 14

    	Link is Defaulted, suggesting it is not

    	receiving LACPDUs from the peer

    .. data:: bm_mux_reason_in_sync = 15

    	Link is in InSync state

    .. data:: bm_mux_reason_collecting = 16

    	Link is in Collecting state

    .. data:: bm_mux_reason_active_link_limit = 17

    	Link exceeds maximum active limit

    .. data:: bm_mux_reason_distributing = 18

    	Link is in Distributing state

    .. data:: bm_mux_reason_count = 19

    	Enumeration maximum value

    """

    bm_mux_reason_no_reason = 0

    bm_mux_reason_link_down = 1

    bm_mux_reason_link_deleted = 2

    bm_mux_reason_duplex = 3

    bm_mux_reason_bandwidth = 4

    bm_mux_reason_loop_back = 5

    bm_mux_reason_activity_type = 6

    bm_mux_reason_link_limit = 7

    bm_mux_reason_shared = 8

    bm_mux_reason_lagid = 9

    bm_mux_reason_no_bundle = 10

    bm_mux_reason_no_primary = 11

    bm_mux_reason_bundle_down = 12

    bm_mux_reason_individual = 13

    bm_mux_reason_defaulted = 14

    bm_mux_reason_in_sync = 15

    bm_mux_reason_collecting = 16

    bm_mux_reason_active_link_limit = 17

    bm_mux_reason_distributing = 18

    bm_mux_reason_count = 19


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmMuxreasonEnum']


class BmMuxstateEnum(Enum):
    """
    BmMuxstateEnum

    Bm muxstate

    .. data:: detached = 1

    	Port is not attached to a bundle

    .. data:: waiting = 2

    	Port has chosen bundle and is waiting to join

    .. data:: attached = 3

    	Port is attached to the bundle but not active

    .. data:: collecting = 4

    	Port is ready to receive data

    .. data:: distributing = 5

    	Port is distributing data

    .. data:: collecting_distributing = 6

    	Port is active and can send and receive data

    """

    detached = 1

    waiting = 2

    attached = 3

    collecting = 4

    distributing = 5

    collecting_distributing = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmMuxstateEnum']


class BmSeverityEnum(Enum):
    """
    BmSeverityEnum

    Severity of the member state reason

    .. data:: ok = 0

    	OK

    .. data:: information = 1

    	Information

    .. data:: misconfiguration = 2

    	Misconfiguration

    .. data:: warning = 3

    	Warning

    .. data:: error = 5

    	Error

    """

    ok = 0

    information = 1

    misconfiguration = 2

    warning = 3

    error = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmSeverityEnum']


class BmStateReasonTargetEnum(Enum):
    """
    BmStateReasonTargetEnum

    Scope of the state reason

    .. data:: member_reason = 0

    	Member applicable reason

    .. data:: bundle_reason = 1

    	Bundle applicable reason

    """

    member_reason = 0

    bundle_reason = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmStateReasonTargetEnum']


class BmdMemberStateEnum(Enum):
    """
    BmdMemberStateEnum

    Bmd member state

    .. data:: bmd_mbr_state_configured = 1

    	Member is configured

    .. data:: bmd_mbr_state_standby = 2

    	Member is standby

    .. data:: bmd_mbr_state_hot_standby = 3

    	Member is hot standby

    .. data:: bmd_mbr_state_negotiating = 4

    	Member is negotiating

    .. data:: bmd_mbr_state_bfd_running = 5

    	Member has a BFD session running

    .. data:: bmd_mbr_state_active = 6

    	Member is active

    """

    bmd_mbr_state_configured = 1

    bmd_mbr_state_standby = 2

    bmd_mbr_state_hot_standby = 3

    bmd_mbr_state_negotiating = 4

    bmd_mbr_state_bfd_running = 5

    bmd_mbr_state_active = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmdMemberStateEnum']


class BmdMemberTypeEnumEnum(Enum):
    """
    BmdMemberTypeEnumEnum

    Bmd member type enum

    .. data:: bmd_mbr_local = 0

    	Member has been configured on the local device

    .. data:: bmd_mbr_foreign = 1

    	Member has been configured on an mLACP peer

    	device

    .. data:: bmd_mbr_unknown = 2

    	Member's type is unknown

    """

    bmd_mbr_local = 0

    bmd_mbr_foreign = 1

    bmd_mbr_unknown = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmdMemberTypeEnumEnum']


class EfpPayloadEtypeEnum(Enum):
    """
    EfpPayloadEtypeEnum

    Payload ethertype match

    .. data:: payload_ethertype_any = 0

    	Any

    .. data:: payload_ethertype_ip = 1

    	IP

    .. data:: payload_ethertype_pppoe = 2

    	PPPoE

    """

    payload_ethertype_any = 0

    payload_ethertype_ip = 1

    payload_ethertype_pppoe = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['EfpPayloadEtypeEnum']


class EfpTagEtypeEnum(Enum):
    """
    EfpTagEtypeEnum

    Tag ethertype

    .. data:: untagged = 0

    	Untagged

    .. data:: dot1q = 33024

    	Dot1Q

    .. data:: dot1ad = 34984

    	Dot1ad

    """

    untagged = 0

    dot1q = 33024

    dot1ad = 34984


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['EfpTagEtypeEnum']


class EfpTagPriorityEnum(Enum):
    """
    EfpTagPriorityEnum

    Priority

    .. data:: priority0 = 0

    	Priority 0

    .. data:: priority1 = 1

    	Priority 1

    .. data:: priority2 = 2

    	Priority 2

    .. data:: priority3 = 3

    	Priority 3

    .. data:: priority4 = 4

    	Priority 4

    .. data:: priority5 = 5

    	Priority 5

    .. data:: priority6 = 6

    	Priority 6

    .. data:: priority7 = 7

    	Priority 7

    .. data:: priority_any = 8

    	Any priority

    """

    priority0 = 0

    priority1 = 1

    priority2 = 2

    priority3 = 3

    priority4 = 4

    priority5 = 5

    priority6 = 6

    priority7 = 7

    priority_any = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['EfpTagPriorityEnum']


class GccDerStateEnum(Enum):
    """
    GccDerStateEnum

    Gcc der state

    .. data:: in_service = 0

    	In Service

    .. data:: out_of_service = 1

    	Out Of Service

    .. data:: maintainance = 2

    	Maintainance

    .. data:: ais = 3

    	Automatic In Service

    """

    in_service = 0

    out_of_service = 1

    maintainance = 2

    ais = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['GccDerStateEnum']


class GccSecStateEnum(Enum):
    """
    GccSecStateEnum

    Gcc sec state

    .. data:: normal = 0

    	Normal

    .. data:: maintainance = 1

    	Maintainance

    .. data:: ais = 2

    	Automatic In Service

    """

    normal = 0

    maintainance = 1

    ais = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['GccSecStateEnum']


class ImAttrDuplexEnum(Enum):
    """
    ImAttrDuplexEnum

    Im attr duplex

    .. data:: im_attr_duplex_unknown = 0

    	im attr duplex unknown

    .. data:: im_attr_duplex_half = 1

    	im attr duplex half

    .. data:: im_attr_duplex_full = 2

    	im attr duplex full

    """

    im_attr_duplex_unknown = 0

    im_attr_duplex_half = 1

    im_attr_duplex_full = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrDuplexEnum']


class ImAttrFlowControlEnum(Enum):
    """
    ImAttrFlowControlEnum

    Im attr flow control

    .. data:: im_attr_flow_control_off = 0

    	im attr flow control off

    .. data:: im_attr_flow_control_on = 1

    	im attr flow control on

    .. data:: im_attr_flow_control_not_sup = 2

    	im attr flow control not sup

    .. data:: im_attr_flow_control_priority = 3

    	im attr flow control priority

    """

    im_attr_flow_control_off = 0

    im_attr_flow_control_on = 1

    im_attr_flow_control_not_sup = 2

    im_attr_flow_control_priority = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrFlowControlEnum']


class ImAttrLinkEnum(Enum):
    """
    ImAttrLinkEnum

    Im attr link

    .. data:: im_attr_link_type_auto = 0

    	im attr link type auto

    .. data:: im_attr_link_type_force = 1

    	im attr link type force

    """

    im_attr_link_type_auto = 0

    im_attr_link_type_force = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrLinkEnum']


class ImAttrMediaEnum(Enum):
    """
    ImAttrMediaEnum

    Im attr media

    .. data:: im_attr_media_other = 0

    	im attr media other

    .. data:: im_attr_media_unknown = 1

    	im attr media unknown

    .. data:: im_attr_media_aui = 2

    	im attr media aui

    .. data:: im_attr_media_10base5 = 3

    	im attr media 10base5

    .. data:: im_attr_media_foirl = 4

    	im attr media foirl

    .. data:: im_attr_media_10base2 = 5

    	im attr media 10base2

    .. data:: im_attr_media_10broad36 = 6

    	im attr media 10broad36

    .. data:: im_attr_media_10base = 7

    	im attr media 10base

    .. data:: im_attr_media_10base_thd = 8

    	im attr media 10base thd

    .. data:: im_attr_media_10base_tfd = 9

    	im attr media 10base tfd

    .. data:: im_attr_media_10base_fp = 10

    	im attr media 10base fp

    .. data:: im_attr_media_10base_fb = 11

    	im attr media 10base fb

    .. data:: im_attr_media_10base_fl = 12

    	im attr media 10base fl

    .. data:: im_attr_media_10base_flhd = 13

    	im attr media 10base flhd

    .. data:: im_attr_media_10base_flfd = 14

    	im attr media 10base flfd

    .. data:: im_attr_media_100base_t4 = 15

    	im attr media 100base t4

    .. data:: im_attr_media_100base_tx = 16

    	im attr media 100base tx

    .. data:: im_attr_media_100base_txhd = 17

    	im attr media 100base txhd

    .. data:: im_attr_media_100base_txfd = 18

    	im attr media 100base txfd

    .. data:: im_attr_media_100base_fx = 19

    	im attr media 100base fx

    .. data:: im_attr_media_100base_fxhd = 20

    	im attr media 100base fxhd

    .. data:: im_attr_media_100base_fxfd = 21

    	im attr media 100base fxfd

    .. data:: im_attr_media_100base_ex = 22

    	im attr media 100base ex

    .. data:: im_attr_media_100base_exhd = 23

    	im attr media 100base exhd

    .. data:: im_attr_media_100base_exfd = 24

    	im attr media 100base exfd

    .. data:: im_attr_media_100base_t2 = 25

    	im attr media 100base t2

    .. data:: im_attr_media_100base_t2hd = 26

    	im attr media 100base t2hd

    .. data:: im_attr_media_100base_t2fd = 27

    	im attr media 100base t2fd

    .. data:: im_attr_media_1000base_x = 28

    	im attr media 1000base x

    .. data:: im_attr_media_1000base_xhdx = 29

    	im attr media 1000base xhdx

    .. data:: im_attr_media_1000base_xfd = 30

    	im attr media 1000base xfd

    .. data:: im_attr_media_1000base_lx = 31

    	im attr media 1000base lx

    .. data:: im_attr_media_1000base_lxhd = 32

    	im attr media 1000base lxhd

    .. data:: im_attr_media_1000base_lxfdx = 33

    	im attr media 1000base lxfdx

    .. data:: im_attr_media_1000base_sx = 34

    	im attr media 1000base sx

    .. data:: im_attr_media_1000base_sxhd = 35

    	im attr media 1000base sxhd

    .. data:: im_attr_media_1000base_sxfd = 36

    	im attr media 1000base sxfd

    .. data:: im_attr_media_1000base_cx = 37

    	im attr media 1000base cx

    .. data:: im_attr_media_1000base_cxhdx = 38

    	im attr media 1000base cxhdx

    .. data:: im_attr_media_1000base_cxfd = 39

    	im attr media 1000base cxfd

    .. data:: im_attr_media_1000base = 40

    	im attr media 1000base

    .. data:: im_attr_media_1000base_thd = 41

    	im attr media 1000base thd

    .. data:: im_attr_media_1000base_tfd = 42

    	im attr media 1000base tfd

    .. data:: im_attr_media_10gbase_x = 43

    	im attr media 10gbase x

    .. data:: im_attr_media_10gbase_lx4 = 44

    	im attr media 10gbase lx4

    .. data:: im_attr_media_10gbase_r = 45

    	im attr media 10gbase r

    .. data:: im_attr_media_10gbase_er = 46

    	im attr media 10gbase er

    .. data:: im_attr_media_10gbase_lr = 47

    	im attr media 10gbase lr

    .. data:: im_attr_media_10gbase_sr = 48

    	im attr media 10gbase sr

    .. data:: im_attr_media_10gbase_w = 49

    	im attr media 10gbase w

    .. data:: im_attr_media_10gbase_ew = 50

    	im attr media 10gbase ew

    .. data:: im_attr_media_10gbase_lw = 51

    	im attr media 10gbase lw

    .. data:: im_attr_media_10gbase_sw = 52

    	im attr media 10gbase sw

    .. data:: im_attr_media_10gbase_zr = 53

    	im attr media 10gbase zr

    .. data:: im_attr_media_802_9a = 54

    	im attr media 802 9a

    .. data:: im_attr_media_rj45 = 55

    	im attr media rj45

    .. data:: im_attr_media_1000base_zx = 56

    	im attr media 1000base zx

    .. data:: im_attr_media_1000base_cwdm = 57

    	im attr media 1000base cwdm

    .. data:: im_attr_media_1000base_cwdm_1470 = 58

    	im attr media 1000base cwdm 1470

    .. data:: im_attr_media_1000base_cwdm_1490 = 59

    	im attr media 1000base cwdm 1490

    .. data:: im_attr_media_1000base_cwdm_1510 = 60

    	im attr media 1000base cwdm 1510

    .. data:: im_attr_media_1000base_cwdm_1530 = 61

    	im attr media 1000base cwdm 1530

    .. data:: im_attr_media_1000base_cwdm_1550 = 62

    	im attr media 1000base cwdm 1550

    .. data:: im_attr_media_1000base_cwdm_1570 = 63

    	im attr media 1000base cwdm 1570

    .. data:: im_attr_media_1000base_cwdm_1590 = 64

    	im attr media 1000base cwdm 1590

    .. data:: im_attr_media_1000base_cwdm_1610 = 65

    	im attr media 1000base cwdm 1610

    .. data:: im_attr_media_10gbase_dwdm = 66

    	im attr media 10gbase dwdm

    .. data:: im_attr_media_100gbase_lr4 = 67

    	im attr media 100gbase lr4

    .. data:: im_attr_media_1000base_dwdm = 68

    	im attr media 1000base dwdm

    .. data:: im_attr_media_1000base_dwdm_1533 = 69

    	im attr media 1000base dwdm 1533

    .. data:: im_attr_media_1000base_dwdm_1537 = 70

    	im attr media 1000base dwdm 1537

    .. data:: im_attr_media_1000base_dwdm_1541 = 71

    	im attr media 1000base dwdm 1541

    .. data:: im_attr_media_1000base_dwdm_1545 = 72

    	im attr media 1000base dwdm 1545

    .. data:: im_attr_media_1000base_dwdm_1549 = 73

    	im attr media 1000base dwdm 1549

    .. data:: im_attr_media_1000base_dwdm_1553 = 74

    	im attr media 1000base dwdm 1553

    .. data:: im_attr_media_1000base_dwdm_1557 = 75

    	im attr media 1000base dwdm 1557

    .. data:: im_attr_media_1000base_dwdm_1561 = 76

    	im attr media 1000base dwdm 1561

    .. data:: im_attr_media_40gbase_lr4 = 77

    	im attr media 40gbase lr4

    .. data:: im_attr_media_40gbase_er4 = 78

    	im attr media 40gbase er4

    .. data:: im_attr_media_100gbase_er4 = 79

    	im attr media 100gbase er4

    .. data:: im_attr_media_1000base_ex = 80

    	im attr media 1000base ex

    .. data:: im_attr_media_1000base_bx10_d = 81

    	im attr media 1000base bx10 d

    .. data:: im_attr_media_1000base_bx10_u = 82

    	im attr media 1000base bx10 u

    .. data:: im_attr_media_1000base_dwdm_1561_42 = 83

    	im attr media 1000base dwdm 1561 42

    .. data:: im_attr_media_1000base_dwdm_1560_61 = 84

    	im attr media 1000base dwdm 1560 61

    .. data:: im_attr_media_1000base_dwdm_1559_79 = 85

    	im attr media 1000base dwdm 1559 79

    .. data:: im_attr_media_1000base_dwdm_1558_98 = 86

    	im attr media 1000base dwdm 1558 98

    .. data:: im_attr_media_1000base_dwdm_1558_17 = 87

    	im attr media 1000base dwdm 1558 17

    .. data:: im_attr_media_1000base_dwdm_1557_36 = 88

    	im attr media 1000base dwdm 1557 36

    .. data:: im_attr_media_1000base_dwdm_1556_55 = 89

    	im attr media 1000base dwdm 1556 55

    .. data:: im_attr_media_1000base_dwdm_1555_75 = 90

    	im attr media 1000base dwdm 1555 75

    .. data:: im_attr_media_1000base_dwdm_1554_94 = 91

    	im attr media 1000base dwdm 1554 94

    .. data:: im_attr_media_1000base_dwdm_1554_13 = 92

    	im attr media 1000base dwdm 1554 13

    .. data:: im_attr_media_1000base_dwdm_1553_33 = 93

    	im attr media 1000base dwdm 1553 33

    .. data:: im_attr_media_1000base_dwdm_1552_52 = 94

    	im attr media 1000base dwdm 1552 52

    .. data:: im_attr_media_1000base_dwdm_1551_72 = 95

    	im attr media 1000base dwdm 1551 72

    .. data:: im_attr_media_1000base_dwdm_1550_92 = 96

    	im attr media 1000base dwdm 1550 92

    .. data:: im_attr_media_1000base_dwdm_1550_12 = 97

    	im attr media 1000base dwdm 1550 12

    .. data:: im_attr_media_1000base_dwdm_1549_32 = 98

    	im attr media 1000base dwdm 1549 32

    .. data:: im_attr_media_1000base_dwdm_1548_51 = 99

    	im attr media 1000base dwdm 1548 51

    .. data:: im_attr_media_1000base_dwdm_1547_72 = 100

    	im attr media 1000base dwdm 1547 72

    .. data:: im_attr_media_1000base_dwdm_1546_92 = 101

    	im attr media 1000base dwdm 1546 92

    .. data:: im_attr_media_1000base_dwdm_1546_12 = 102

    	im attr media 1000base dwdm 1546 12

    .. data:: im_attr_media_1000base_dwdm_1545_32 = 103

    	im attr media 1000base dwdm 1545 32

    .. data:: im_attr_media_1000base_dwdm_1544_53 = 104

    	im attr media 1000base dwdm 1544 53

    .. data:: im_attr_media_1000base_dwdm_1543_73 = 105

    	im attr media 1000base dwdm 1543 73

    .. data:: im_attr_media_1000base_dwdm_1542_94 = 106

    	im attr media 1000base dwdm 1542 94

    .. data:: im_attr_media_1000base_dwdm_1542_14 = 107

    	im attr media 1000base dwdm 1542 14

    .. data:: im_attr_media_1000base_dwdm_1541_35 = 108

    	im attr media 1000base dwdm 1541 35

    .. data:: im_attr_media_1000base_dwdm_1540_56 = 109

    	im attr media 1000base dwdm 1540 56

    .. data:: im_attr_media_1000base_dwdm_1539_77 = 110

    	im attr media 1000base dwdm 1539 77

    .. data:: im_attr_media_1000base_dwdm_1538_98 = 111

    	im attr media 1000base dwdm 1538 98

    .. data:: im_attr_media_1000base_dwdm_1538_19 = 112

    	im attr media 1000base dwdm 1538 19

    .. data:: im_attr_media_1000base_dwdm_1537_40 = 113

    	im attr media 1000base dwdm 1537 40

    .. data:: im_attr_media_1000base_dwdm_1536_61 = 114

    	im attr media 1000base dwdm 1536 61

    .. data:: im_attr_media_1000base_dwdm_1535_82 = 115

    	im attr media 1000base dwdm 1535 82

    .. data:: im_attr_media_1000base_dwdm_1535_04 = 116

    	im attr media 1000base dwdm 1535 04

    .. data:: im_attr_media_1000base_dwdm_1534_25 = 117

    	im attr media 1000base dwdm 1534 25

    .. data:: im_attr_media_1000base_dwdm_1533_47 = 118

    	im attr media 1000base dwdm 1533 47

    .. data:: im_attr_media_1000base_dwdm_1532_68 = 119

    	im attr media 1000base dwdm 1532 68

    .. data:: im_attr_media_1000base_dwdm_1531_90 = 120

    	im attr media 1000base dwdm 1531 90

    .. data:: im_attr_media_1000base_dwdm_1531_12 = 121

    	im attr media 1000base dwdm 1531 12

    .. data:: im_attr_media_1000base_dwdm_1530_33 = 122

    	im attr media 1000base dwdm 1530 33

    .. data:: im_attr_media_1000base_dwdm_tunable = 123

    	im attr media 1000base dwdm tunable

    .. data:: im_attr_media_10gbase_dwdm_1561_42 = 124

    	im attr media 10gbase dwdm 1561 42

    .. data:: im_attr_media_10gbase_dwdm_1560_61 = 125

    	im attr media 10gbase dwdm 1560 61

    .. data:: im_attr_media_10gbase_dwdm_1559_79 = 126

    	im attr media 10gbase dwdm 1559 79

    .. data:: im_attr_media_10gbase_dwdm_1558_98 = 127

    	im attr media 10gbase dwdm 1558 98

    .. data:: im_attr_media_10gbase_dwdm_1558_17 = 128

    	im attr media 10gbase dwdm 1558 17

    .. data:: im_attr_media_10gbase_dwdm_1557_36 = 129

    	im attr media 10gbase dwdm 1557 36

    .. data:: im_attr_media_10gbase_dwdm_1556_55 = 130

    	im attr media 10gbase dwdm 1556 55

    .. data:: im_attr_media_10gbase_dwdm_1555_75 = 131

    	im attr media 10gbase dwdm 1555 75

    .. data:: im_attr_media_10gbase_dwdm_1554_94 = 132

    	im attr media 10gbase dwdm 1554 94

    .. data:: im_attr_media_10gbase_dwdm_1554_13 = 133

    	im attr media 10gbase dwdm 1554 13

    .. data:: im_attr_media_10gbase_dwdm_1553_33 = 134

    	im attr media 10gbase dwdm 1553 33

    .. data:: im_attr_media_10gbase_dwdm_1552_52 = 135

    	im attr media 10gbase dwdm 1552 52

    .. data:: im_attr_media_10gbase_dwdm_1551_72 = 136

    	im attr media 10gbase dwdm 1551 72

    .. data:: im_attr_media_10gbase_dwdm_1550_92 = 137

    	im attr media 10gbase dwdm 1550 92

    .. data:: im_attr_media_10gbase_dwdm_1550_12 = 138

    	im attr media 10gbase dwdm 1550 12

    .. data:: im_attr_media_10gbase_dwdm_1549_32 = 139

    	im attr media 10gbase dwdm 1549 32

    .. data:: im_attr_media_10gbase_dwdm_1548_51 = 140

    	im attr media 10gbase dwdm 1548 51

    .. data:: im_attr_media_10gbase_dwdm_1547_72 = 141

    	im attr media 10gbase dwdm 1547 72

    .. data:: im_attr_media_10gbase_dwdm_1546_92 = 142

    	im attr media 10gbase dwdm 1546 92

    .. data:: im_attr_media_10gbase_dwdm_1546_12 = 143

    	im attr media 10gbase dwdm 1546 12

    .. data:: im_attr_media_10gbase_dwdm_1545_32 = 144

    	im attr media 10gbase dwdm 1545 32

    .. data:: im_attr_media_10gbase_dwdm_1544_53 = 145

    	im attr media 10gbase dwdm 1544 53

    .. data:: im_attr_media_10gbase_dwdm_1543_73 = 146

    	im attr media 10gbase dwdm 1543 73

    .. data:: im_attr_media_10gbase_dwdm_1542_94 = 147

    	im attr media 10gbase dwdm 1542 94

    .. data:: im_attr_media_10gbase_dwdm_1542_14 = 148

    	im attr media 10gbase dwdm 1542 14

    .. data:: im_attr_media_10gbase_dwdm_1541_35 = 149

    	im attr media 10gbase dwdm 1541 35

    .. data:: im_attr_media_10gbase_dwdm_1540_56 = 150

    	im attr media 10gbase dwdm 1540 56

    .. data:: im_attr_media_10gbase_dwdm_1539_77 = 151

    	im attr media 10gbase dwdm 1539 77

    .. data:: im_attr_media_10gbase_dwdm_1538_98 = 152

    	im attr media 10gbase dwdm 1538 98

    .. data:: im_attr_media_10gbase_dwdm_1538_19 = 153

    	im attr media 10gbase dwdm 1538 19

    .. data:: im_attr_media_10gbase_dwdm_1537_40 = 154

    	im attr media 10gbase dwdm 1537 40

    .. data:: im_attr_media_10gbase_dwdm_1536_61 = 155

    	im attr media 10gbase dwdm 1536 61

    .. data:: im_attr_media_10gbase_dwdm_1535_82 = 156

    	im attr media 10gbase dwdm 1535 82

    .. data:: im_attr_media_10gbase_dwdm_1535_04 = 157

    	im attr media 10gbase dwdm 1535 04

    .. data:: im_attr_media_10gbase_dwdm_1534_25 = 158

    	im attr media 10gbase dwdm 1534 25

    .. data:: im_attr_media_10gbase_dwdm_1533_47 = 159

    	im attr media 10gbase dwdm 1533 47

    .. data:: im_attr_media_10gbase_dwdm_1532_68 = 160

    	im attr media 10gbase dwdm 1532 68

    .. data:: im_attr_media_10gbase_dwdm_1531_90 = 161

    	im attr media 10gbase dwdm 1531 90

    .. data:: im_attr_media_10gbase_dwdm_1531_12 = 162

    	im attr media 10gbase dwdm 1531 12

    .. data:: im_attr_media_10gbase_dwdm_1530_33 = 163

    	im attr media 10gbase dwdm 1530 33

    .. data:: im_attr_media_10gbase_dwdm_tunable = 164

    	im attr media 10gbase dwdm tunable

    .. data:: im_attr_media_40gbase_dwdm_1561_42 = 165

    	im attr media 40gbase dwdm 1561 42

    .. data:: im_attr_media_40gbase_dwdm_1560_61 = 166

    	im attr media 40gbase dwdm 1560 61

    .. data:: im_attr_media_40gbase_dwdm_1559_79 = 167

    	im attr media 40gbase dwdm 1559 79

    .. data:: im_attr_media_40gbase_dwdm_1558_98 = 168

    	im attr media 40gbase dwdm 1558 98

    .. data:: im_attr_media_40gbase_dwdm_1558_17 = 169

    	im attr media 40gbase dwdm 1558 17

    .. data:: im_attr_media_40gbase_dwdm_1557_36 = 170

    	im attr media 40gbase dwdm 1557 36

    .. data:: im_attr_media_40gbase_dwdm_1556_55 = 171

    	im attr media 40gbase dwdm 1556 55

    .. data:: im_attr_media_40gbase_dwdm_1555_75 = 172

    	im attr media 40gbase dwdm 1555 75

    .. data:: im_attr_media_40gbase_dwdm_1554_94 = 173

    	im attr media 40gbase dwdm 1554 94

    .. data:: im_attr_media_40gbase_dwdm_1554_13 = 174

    	im attr media 40gbase dwdm 1554 13

    .. data:: im_attr_media_40gbase_dwdm_1553_33 = 175

    	im attr media 40gbase dwdm 1553 33

    .. data:: im_attr_media_40gbase_dwdm_1552_52 = 176

    	im attr media 40gbase dwdm 1552 52

    .. data:: im_attr_media_40gbase_dwdm_1551_72 = 177

    	im attr media 40gbase dwdm 1551 72

    .. data:: im_attr_media_40gbase_dwdm_1550_92 = 178

    	im attr media 40gbase dwdm 1550 92

    .. data:: im_attr_media_40gbase_dwdm_1550_12 = 179

    	im attr media 40gbase dwdm 1550 12

    .. data:: im_attr_media_40gbase_dwdm_1549_32 = 180

    	im attr media 40gbase dwdm 1549 32

    .. data:: im_attr_media_40gbase_dwdm_1548_51 = 181

    	im attr media 40gbase dwdm 1548 51

    .. data:: im_attr_media_40gbase_dwdm_1547_72 = 182

    	im attr media 40gbase dwdm 1547 72

    .. data:: im_attr_media_40gbase_dwdm_1546_92 = 183

    	im attr media 40gbase dwdm 1546 92

    .. data:: im_attr_media_40gbase_dwdm_1546_12 = 184

    	im attr media 40gbase dwdm 1546 12

    .. data:: im_attr_media_40gbase_dwdm_1545_32 = 185

    	im attr media 40gbase dwdm 1545 32

    .. data:: im_attr_media_40gbase_dwdm_1544_53 = 186

    	im attr media 40gbase dwdm 1544 53

    .. data:: im_attr_media_40gbase_dwdm_1543_73 = 187

    	im attr media 40gbase dwdm 1543 73

    .. data:: im_attr_media_40gbase_dwdm_1542_94 = 188

    	im attr media 40gbase dwdm 1542 94

    .. data:: im_attr_media_40gbase_dwdm_1542_14 = 189

    	im attr media 40gbase dwdm 1542 14

    .. data:: im_attr_media_40gbase_dwdm_1541_35 = 190

    	im attr media 40gbase dwdm 1541 35

    .. data:: im_attr_media_40gbase_dwdm_1540_56 = 191

    	im attr media 40gbase dwdm 1540 56

    .. data:: im_attr_media_40gbase_dwdm_1539_77 = 192

    	im attr media 40gbase dwdm 1539 77

    .. data:: im_attr_media_40gbase_dwdm_1538_98 = 193

    	im attr media 40gbase dwdm 1538 98

    .. data:: im_attr_media_40gbase_dwdm_1538_19 = 194

    	im attr media 40gbase dwdm 1538 19

    .. data:: im_attr_media_40gbase_dwdm_1537_40 = 195

    	im attr media 40gbase dwdm 1537 40

    .. data:: im_attr_media_40gbase_dwdm_1536_61 = 196

    	im attr media 40gbase dwdm 1536 61

    .. data:: im_attr_media_40gbase_dwdm_1535_82 = 197

    	im attr media 40gbase dwdm 1535 82

    .. data:: im_attr_media_40gbase_dwdm_1535_04 = 198

    	im attr media 40gbase dwdm 1535 04

    .. data:: im_attr_media_40gbase_dwdm_1534_25 = 199

    	im attr media 40gbase dwdm 1534 25

    .. data:: im_attr_media_40gbase_dwdm_1533_47 = 200

    	im attr media 40gbase dwdm 1533 47

    .. data:: im_attr_media_40gbase_dwdm_1532_68 = 201

    	im attr media 40gbase dwdm 1532 68

    .. data:: im_attr_media_40gbase_dwdm_1531_90 = 202

    	im attr media 40gbase dwdm 1531 90

    .. data:: im_attr_media_40gbase_dwdm_1531_12 = 203

    	im attr media 40gbase dwdm 1531 12

    .. data:: im_attr_media_40gbase_dwdm_1530_33 = 204

    	im attr media 40gbase dwdm 1530 33

    .. data:: im_attr_media_40gbase_dwdm_tunable = 205

    	im attr media 40gbase dwdm tunable

    .. data:: im_attr_media_100gbase_dwdm_1561_42 = 206

    	im attr media 100gbase dwdm 1561 42

    .. data:: im_attr_media_100gbase_dwdm_1560_61 = 207

    	im attr media 100gbase dwdm 1560 61

    .. data:: im_attr_media_100gbase_dwdm_1559_79 = 208

    	im attr media 100gbase dwdm 1559 79

    .. data:: im_attr_media_100gbase_dwdm_1558_98 = 209

    	im attr media 100gbase dwdm 1558 98

    .. data:: im_attr_media_100gbase_dwdm_1558_17 = 210

    	im attr media 100gbase dwdm 1558 17

    .. data:: im_attr_media_100gbase_dwdm_1557_36 = 211

    	im attr media 100gbase dwdm 1557 36

    .. data:: im_attr_media_100gbase_dwdm_1556_55 = 212

    	im attr media 100gbase dwdm 1556 55

    .. data:: im_attr_media_100gbase_dwdm_1555_75 = 213

    	im attr media 100gbase dwdm 1555 75

    .. data:: im_attr_media_100gbase_dwdm_1554_94 = 214

    	im attr media 100gbase dwdm 1554 94

    .. data:: im_attr_media_100gbase_dwdm_1554_13 = 215

    	im attr media 100gbase dwdm 1554 13

    .. data:: im_attr_media_100gbase_dwdm_1553_33 = 216

    	im attr media 100gbase dwdm 1553 33

    .. data:: im_attr_media_100gbase_dwdm_1552_52 = 217

    	im attr media 100gbase dwdm 1552 52

    .. data:: im_attr_media_100gbase_dwdm_1551_72 = 218

    	im attr media 100gbase dwdm 1551 72

    .. data:: im_attr_media_100gbase_dwdm_1550_92 = 219

    	im attr media 100gbase dwdm 1550 92

    .. data:: im_attr_media_100gbase_dwdm_1550_12 = 220

    	im attr media 100gbase dwdm 1550 12

    .. data:: im_attr_media_100gbase_dwdm_1549_32 = 221

    	im attr media 100gbase dwdm 1549 32

    .. data:: im_attr_media_100gbase_dwdm_1548_51 = 222

    	im attr media 100gbase dwdm 1548 51

    .. data:: im_attr_media_100gbase_dwdm_1547_72 = 223

    	im attr media 100gbase dwdm 1547 72

    .. data:: im_attr_media_100gbase_dwdm_1546_92 = 224

    	im attr media 100gbase dwdm 1546 92

    .. data:: im_attr_media_100gbase_dwdm_1546_12 = 225

    	im attr media 100gbase dwdm 1546 12

    .. data:: im_attr_media_100gbase_dwdm_1545_32 = 226

    	im attr media 100gbase dwdm 1545 32

    .. data:: im_attr_media_100gbase_dwdm_1544_53 = 227

    	im attr media 100gbase dwdm 1544 53

    .. data:: im_attr_media_100gbase_dwdm_1543_73 = 228

    	im attr media 100gbase dwdm 1543 73

    .. data:: im_attr_media_100gbase_dwdm_1542_94 = 229

    	im attr media 100gbase dwdm 1542 94

    .. data:: im_attr_media_100gbase_dwdm_1542_14 = 230

    	im attr media 100gbase dwdm 1542 14

    .. data:: im_attr_media_100gbase_dwdm_1541_35 = 231

    	im attr media 100gbase dwdm 1541 35

    .. data:: im_attr_media_100gbase_dwdm_1540_56 = 232

    	im attr media 100gbase dwdm 1540 56

    .. data:: im_attr_media_100gbase_dwdm_1539_77 = 233

    	im attr media 100gbase dwdm 1539 77

    .. data:: im_attr_media_100gbase_dwdm_1538_98 = 234

    	im attr media 100gbase dwdm 1538 98

    .. data:: im_attr_media_100gbase_dwdm_1538_19 = 235

    	im attr media 100gbase dwdm 1538 19

    .. data:: im_attr_media_100gbase_dwdm_1537_40 = 236

    	im attr media 100gbase dwdm 1537 40

    .. data:: im_attr_media_100gbase_dwdm_1536_61 = 237

    	im attr media 100gbase dwdm 1536 61

    .. data:: im_attr_media_100gbase_dwdm_1535_82 = 238

    	im attr media 100gbase dwdm 1535 82

    .. data:: im_attr_media_100gbase_dwdm_1535_04 = 239

    	im attr media 100gbase dwdm 1535 04

    .. data:: im_attr_media_100gbase_dwdm_1534_25 = 240

    	im attr media 100gbase dwdm 1534 25

    .. data:: im_attr_media_100gbase_dwdm_1533_47 = 241

    	im attr media 100gbase dwdm 1533 47

    .. data:: im_attr_media_100gbase_dwdm_1532_68 = 242

    	im attr media 100gbase dwdm 1532 68

    .. data:: im_attr_media_100gbase_dwdm_1531_90 = 243

    	im attr media 100gbase dwdm 1531 90

    .. data:: im_attr_media_100gbase_dwdm_1531_12 = 244

    	im attr media 100gbase dwdm 1531 12

    .. data:: im_attr_media_100gbase_dwdm_1530_33 = 245

    	im attr media 100gbase dwdm 1530 33

    .. data:: im_attr_media_100gbase_dwdm_tunable = 246

    	im attr media 100gbase dwdm tunable

    .. data:: im_attr_media_40gbase_kr4 = 247

    	im attr media 40gbase kr4

    .. data:: im_attr_media_40gbase_cr4 = 248

    	im attr media 40gbase cr4

    .. data:: im_attr_media_40gbase_sr4 = 249

    	im attr media 40gbase sr4

    .. data:: im_attr_media_40gbase_fr = 250

    	im attr media 40gbase fr

    .. data:: im_attr_media_100gbase_cr10 = 251

    	im attr media 100gbase cr10

    .. data:: im_attr_media_100gbase_sr10 = 252

    	im attr media 100gbase sr10

    .. data:: im_attr_media_40gbase_csr4 = 253

    	im attr media 40gbase csr4

    .. data:: im_attr_media_10gbase_cwdm = 254

    	im attr media 10gbase cwdm

    .. data:: im_attr_media_10gbase_cwdm_tunable = 255

    	im attr media 10gbase cwdm tunable

    .. data:: im_attr_media_10gbase_cwdm_1470 = 256

    	im attr media 10gbase cwdm 1470

    .. data:: im_attr_media_10gbase_cwdm_1490 = 257

    	im attr media 10gbase cwdm 1490

    .. data:: im_attr_media_10gbase_cwdm_1510 = 258

    	im attr media 10gbase cwdm 1510

    .. data:: im_attr_media_10gbase_cwdm_1530 = 259

    	im attr media 10gbase cwdm 1530

    .. data:: im_attr_media_10gbase_cwdm_1550 = 260

    	im attr media 10gbase cwdm 1550

    .. data:: im_attr_media_10gbase_cwdm_1570 = 261

    	im attr media 10gbase cwdm 1570

    .. data:: im_attr_media_10gbase_cwdm_1590 = 262

    	im attr media 10gbase cwdm 1590

    .. data:: im_attr_media_10gbase_cwdm_1610 = 263

    	im attr media 10gbase cwdm 1610

    .. data:: im_attr_media_40gbase_cwdm = 264

    	im attr media 40gbase cwdm

    .. data:: im_attr_media_40gbase_cwdm_tunable = 265

    	im attr media 40gbase cwdm tunable

    .. data:: im_attr_media_40gbase_cwdm_1470 = 266

    	im attr media 40gbase cwdm 1470

    .. data:: im_attr_media_40gbase_cwdm_1490 = 267

    	im attr media 40gbase cwdm 1490

    .. data:: im_attr_media_40gbase_cwdm_1510 = 268

    	im attr media 40gbase cwdm 1510

    .. data:: im_attr_media_40gbase_cwdm_1530 = 269

    	im attr media 40gbase cwdm 1530

    .. data:: im_attr_media_40gbase_cwdm_1550 = 270

    	im attr media 40gbase cwdm 1550

    .. data:: im_attr_media_40gbase_cwdm_1570 = 271

    	im attr media 40gbase cwdm 1570

    .. data:: im_attr_media_40gbase_cwdm_1590 = 272

    	im attr media 40gbase cwdm 1590

    .. data:: im_attr_media_40gbase_cwdm_1610 = 273

    	im attr media 40gbase cwdm 1610

    .. data:: im_attr_media_100gbase_cwdm = 274

    	im attr media 100gbase cwdm

    .. data:: im_attr_media_100gbase_cwdm_tunable = 275

    	im attr media 100gbase cwdm tunable

    .. data:: im_attr_media_100gbase_cwdm_1470 = 276

    	im attr media 100gbase cwdm 1470

    .. data:: im_attr_media_100gbase_cwdm_1490 = 277

    	im attr media 100gbase cwdm 1490

    .. data:: im_attr_media_100gbase_cwdm_1510 = 278

    	im attr media 100gbase cwdm 1510

    .. data:: im_attr_media_100gbase_cwdm_1530 = 279

    	im attr media 100gbase cwdm 1530

    .. data:: im_attr_media_100gbase_cwdm_1550 = 280

    	im attr media 100gbase cwdm 1550

    .. data:: im_attr_media_100gbase_cwdm_1570 = 281

    	im attr media 100gbase cwdm 1570

    .. data:: im_attr_media_100gbase_cwdm_1590 = 282

    	im attr media 100gbase cwdm 1590

    .. data:: im_attr_media_100gbase_cwdm_1610 = 283

    	im attr media 100gbase cwdm 1610

    .. data:: im_attr_media_40gbase_elpb = 284

    	im attr media 40gbase elpb

    .. data:: im_attr_media_100gbase_elpb = 285

    	im attr media 100gbase elpb

    .. data:: im_attr_media_100gbase_lr10 = 286

    	im attr media 100gbase lr10

    .. data:: im_attr_media_40gbase = 287

    	im attr media 40gbase

    .. data:: im_attr_media_100gbase_kp4 = 288

    	im attr media 100gbase kp4

    .. data:: im_attr_media_100gbase_kr4 = 289

    	im attr media 100gbase kr4

    .. data:: im_attr_media_10gbase_lrm = 290

    	im attr media 10gbase lrm

    .. data:: im_attr_media_10gbase_cx4 = 291

    	im attr media 10gbase cx4

    .. data:: im_attr_media_10gbase = 292

    	im attr media 10gbase

    .. data:: im_attr_media_10gbase_kx4 = 293

    	im attr media 10gbase kx4

    .. data:: im_attr_media_10gbase_kr = 294

    	im attr media 10gbase kr

    .. data:: im_attr_media_10gbase_pr = 295

    	im attr media 10gbase pr

    .. data:: im_attr_media_100base_lx = 296

    	im attr media 100base lx

    .. data:: im_attr_media_100base_zx = 297

    	im attr media 100base zx

    .. data:: im_attr_media_1000base_bx_d = 298

    	im attr media 1000base bx d

    .. data:: im_attr_media_1000base_bx_u = 299

    	im attr media 1000base bx u

    .. data:: im_attr_media_1000base_bx20_d = 300

    	im attr media 1000base bx20 d

    .. data:: im_attr_media_1000base_bx20_u = 301

    	im attr media 1000base bx20 u

    .. data:: im_attr_media_1000base_bx40_d = 302

    	im attr media 1000base bx40 d

    .. data:: im_attr_media_1000base_bx40_da = 303

    	im attr media 1000base bx40 da

    .. data:: im_attr_media_1000base_bx40_u = 304

    	im attr media 1000base bx40 u

    .. data:: im_attr_media_1000base_bx80_d = 305

    	im attr media 1000base bx80 d

    .. data:: im_attr_media_1000base_bx80_u = 306

    	im attr media 1000base bx80 u

    .. data:: im_attr_media_1000base_bx120_d = 307

    	im attr media 1000base bx120 d

    .. data:: im_attr_media_1000base_bx120_u = 308

    	im attr media 1000base bx120 u

    .. data:: im_attr_media_10gbase_bx_d = 309

    	im attr media 10gbase bx d

    .. data:: im_attr_media_10gbase_bx_u = 310

    	im attr media 10gbase bx u

    .. data:: im_attr_media_10gbase_bx10_d = 311

    	im attr media 10gbase bx10 d

    .. data:: im_attr_media_10gbase_bx10_u = 312

    	im attr media 10gbase bx10 u

    .. data:: im_attr_media_10gbase_bx20_d = 313

    	im attr media 10gbase bx20 d

    .. data:: im_attr_media_10gbase_bx20_u = 314

    	im attr media 10gbase bx20 u

    .. data:: im_attr_media_10gbase_bx40_d = 315

    	im attr media 10gbase bx40 d

    .. data:: im_attr_media_10gbase_bx40_u = 316

    	im attr media 10gbase bx40 u

    .. data:: im_attr_media_10gbase_bx80_d = 317

    	im attr media 10gbase bx80 d

    .. data:: im_attr_media_10gbase_bx80_u = 318

    	im attr media 10gbase bx80 u

    .. data:: im_attr_media_10gbase_bx120_d = 319

    	im attr media 10gbase bx120 d

    .. data:: im_attr_media_10gbase_bx120_u = 320

    	im attr media 10gbase bx120 u

    .. data:: im_attr_media_1000base_dr_lx = 321

    	im attr media 1000base dr lx

    .. data:: im_attr_media_100gbase_er4l = 322

    	im attr media 100gbase er4l

    .. data:: im_attr_media_100gbase_sr4 = 323

    	im attr media 100gbase sr4

    .. data:: im_attr_media_40gbase_sr_bd = 324

    	im attr media 40gbase sr bd

    .. data:: im_attr_media_25gbase_cr = 325

    	im attr media 25gbase cr

    .. data:: im_attr_media_25gbase_cr_s = 326

    	im attr media 25gbase cr s

    .. data:: im_attr_media_25gbase_kr = 327

    	im attr media 25gbase kr

    .. data:: im_attr_media_25gbase_kr_s = 328

    	im attr media 25gbase kr s

    .. data:: im_attr_media_25gbase_r = 329

    	im attr media 25gbase r

    .. data:: im_attr_media_25gbase_sr = 330

    	im attr media 25gbase sr

    .. data:: im_attr_media_25gbase_dwdm = 331

    	im attr media 25gbase dwdm

    .. data:: im_attr_media_25gbase_dwdm_tunable = 332

    	im attr media 25gbase dwdm tunable

    .. data:: im_attr_media_25gbase_cwdm = 333

    	im attr media 25gbase cwdm

    .. data:: im_attr_media_25gbase_cwdm_tunable = 334

    	im attr media 25gbase cwdm tunable

    .. data:: im_attr_media_100gbase_psm4 = 335

    	im attr media 100gbase psm4

    .. data:: im_attr_media_100gbase_er10 = 336

    	im attr media 100gbase er10

    .. data:: im_attr_media_100gbase_er10l = 337

    	im attr media 100gbase er10l

    .. data:: im_attr_media_100gbase_acc = 338

    	im attr media 100gbase acc

    .. data:: im_attr_media_100gbase_aoc = 339

    	im attr media 100gbase aoc

    .. data:: im_attr_media_100gbase_cwdm4 = 340

    	im attr media 100gbase cwdm4

    .. data:: im_attr_media_40gbase_psm4 = 341

    	im attr media 40gbase psm4

    .. data:: im_attr_media_100gbase_cr4 = 342

    	im attr media 100gbase cr4

    .. data:: im_attr_media_100gbase_act_loop = 343

    	im attr media 100gbase act loop

    .. data:: im_attr_media_100gbase_pas_loop = 344

    	im attr media 100gbase pas loop

    """

    im_attr_media_other = 0

    im_attr_media_unknown = 1

    im_attr_media_aui = 2

    im_attr_media_10base5 = 3

    im_attr_media_foirl = 4

    im_attr_media_10base2 = 5

    im_attr_media_10broad36 = 6

    im_attr_media_10base = 7

    im_attr_media_10base_thd = 8

    im_attr_media_10base_tfd = 9

    im_attr_media_10base_fp = 10

    im_attr_media_10base_fb = 11

    im_attr_media_10base_fl = 12

    im_attr_media_10base_flhd = 13

    im_attr_media_10base_flfd = 14

    im_attr_media_100base_t4 = 15

    im_attr_media_100base_tx = 16

    im_attr_media_100base_txhd = 17

    im_attr_media_100base_txfd = 18

    im_attr_media_100base_fx = 19

    im_attr_media_100base_fxhd = 20

    im_attr_media_100base_fxfd = 21

    im_attr_media_100base_ex = 22

    im_attr_media_100base_exhd = 23

    im_attr_media_100base_exfd = 24

    im_attr_media_100base_t2 = 25

    im_attr_media_100base_t2hd = 26

    im_attr_media_100base_t2fd = 27

    im_attr_media_1000base_x = 28

    im_attr_media_1000base_xhdx = 29

    im_attr_media_1000base_xfd = 30

    im_attr_media_1000base_lx = 31

    im_attr_media_1000base_lxhd = 32

    im_attr_media_1000base_lxfdx = 33

    im_attr_media_1000base_sx = 34

    im_attr_media_1000base_sxhd = 35

    im_attr_media_1000base_sxfd = 36

    im_attr_media_1000base_cx = 37

    im_attr_media_1000base_cxhdx = 38

    im_attr_media_1000base_cxfd = 39

    im_attr_media_1000base = 40

    im_attr_media_1000base_thd = 41

    im_attr_media_1000base_tfd = 42

    im_attr_media_10gbase_x = 43

    im_attr_media_10gbase_lx4 = 44

    im_attr_media_10gbase_r = 45

    im_attr_media_10gbase_er = 46

    im_attr_media_10gbase_lr = 47

    im_attr_media_10gbase_sr = 48

    im_attr_media_10gbase_w = 49

    im_attr_media_10gbase_ew = 50

    im_attr_media_10gbase_lw = 51

    im_attr_media_10gbase_sw = 52

    im_attr_media_10gbase_zr = 53

    im_attr_media_802_9a = 54

    im_attr_media_rj45 = 55

    im_attr_media_1000base_zx = 56

    im_attr_media_1000base_cwdm = 57

    im_attr_media_1000base_cwdm_1470 = 58

    im_attr_media_1000base_cwdm_1490 = 59

    im_attr_media_1000base_cwdm_1510 = 60

    im_attr_media_1000base_cwdm_1530 = 61

    im_attr_media_1000base_cwdm_1550 = 62

    im_attr_media_1000base_cwdm_1570 = 63

    im_attr_media_1000base_cwdm_1590 = 64

    im_attr_media_1000base_cwdm_1610 = 65

    im_attr_media_10gbase_dwdm = 66

    im_attr_media_100gbase_lr4 = 67

    im_attr_media_1000base_dwdm = 68

    im_attr_media_1000base_dwdm_1533 = 69

    im_attr_media_1000base_dwdm_1537 = 70

    im_attr_media_1000base_dwdm_1541 = 71

    im_attr_media_1000base_dwdm_1545 = 72

    im_attr_media_1000base_dwdm_1549 = 73

    im_attr_media_1000base_dwdm_1553 = 74

    im_attr_media_1000base_dwdm_1557 = 75

    im_attr_media_1000base_dwdm_1561 = 76

    im_attr_media_40gbase_lr4 = 77

    im_attr_media_40gbase_er4 = 78

    im_attr_media_100gbase_er4 = 79

    im_attr_media_1000base_ex = 80

    im_attr_media_1000base_bx10_d = 81

    im_attr_media_1000base_bx10_u = 82

    im_attr_media_1000base_dwdm_1561_42 = 83

    im_attr_media_1000base_dwdm_1560_61 = 84

    im_attr_media_1000base_dwdm_1559_79 = 85

    im_attr_media_1000base_dwdm_1558_98 = 86

    im_attr_media_1000base_dwdm_1558_17 = 87

    im_attr_media_1000base_dwdm_1557_36 = 88

    im_attr_media_1000base_dwdm_1556_55 = 89

    im_attr_media_1000base_dwdm_1555_75 = 90

    im_attr_media_1000base_dwdm_1554_94 = 91

    im_attr_media_1000base_dwdm_1554_13 = 92

    im_attr_media_1000base_dwdm_1553_33 = 93

    im_attr_media_1000base_dwdm_1552_52 = 94

    im_attr_media_1000base_dwdm_1551_72 = 95

    im_attr_media_1000base_dwdm_1550_92 = 96

    im_attr_media_1000base_dwdm_1550_12 = 97

    im_attr_media_1000base_dwdm_1549_32 = 98

    im_attr_media_1000base_dwdm_1548_51 = 99

    im_attr_media_1000base_dwdm_1547_72 = 100

    im_attr_media_1000base_dwdm_1546_92 = 101

    im_attr_media_1000base_dwdm_1546_12 = 102

    im_attr_media_1000base_dwdm_1545_32 = 103

    im_attr_media_1000base_dwdm_1544_53 = 104

    im_attr_media_1000base_dwdm_1543_73 = 105

    im_attr_media_1000base_dwdm_1542_94 = 106

    im_attr_media_1000base_dwdm_1542_14 = 107

    im_attr_media_1000base_dwdm_1541_35 = 108

    im_attr_media_1000base_dwdm_1540_56 = 109

    im_attr_media_1000base_dwdm_1539_77 = 110

    im_attr_media_1000base_dwdm_1538_98 = 111

    im_attr_media_1000base_dwdm_1538_19 = 112

    im_attr_media_1000base_dwdm_1537_40 = 113

    im_attr_media_1000base_dwdm_1536_61 = 114

    im_attr_media_1000base_dwdm_1535_82 = 115

    im_attr_media_1000base_dwdm_1535_04 = 116

    im_attr_media_1000base_dwdm_1534_25 = 117

    im_attr_media_1000base_dwdm_1533_47 = 118

    im_attr_media_1000base_dwdm_1532_68 = 119

    im_attr_media_1000base_dwdm_1531_90 = 120

    im_attr_media_1000base_dwdm_1531_12 = 121

    im_attr_media_1000base_dwdm_1530_33 = 122

    im_attr_media_1000base_dwdm_tunable = 123

    im_attr_media_10gbase_dwdm_1561_42 = 124

    im_attr_media_10gbase_dwdm_1560_61 = 125

    im_attr_media_10gbase_dwdm_1559_79 = 126

    im_attr_media_10gbase_dwdm_1558_98 = 127

    im_attr_media_10gbase_dwdm_1558_17 = 128

    im_attr_media_10gbase_dwdm_1557_36 = 129

    im_attr_media_10gbase_dwdm_1556_55 = 130

    im_attr_media_10gbase_dwdm_1555_75 = 131

    im_attr_media_10gbase_dwdm_1554_94 = 132

    im_attr_media_10gbase_dwdm_1554_13 = 133

    im_attr_media_10gbase_dwdm_1553_33 = 134

    im_attr_media_10gbase_dwdm_1552_52 = 135

    im_attr_media_10gbase_dwdm_1551_72 = 136

    im_attr_media_10gbase_dwdm_1550_92 = 137

    im_attr_media_10gbase_dwdm_1550_12 = 138

    im_attr_media_10gbase_dwdm_1549_32 = 139

    im_attr_media_10gbase_dwdm_1548_51 = 140

    im_attr_media_10gbase_dwdm_1547_72 = 141

    im_attr_media_10gbase_dwdm_1546_92 = 142

    im_attr_media_10gbase_dwdm_1546_12 = 143

    im_attr_media_10gbase_dwdm_1545_32 = 144

    im_attr_media_10gbase_dwdm_1544_53 = 145

    im_attr_media_10gbase_dwdm_1543_73 = 146

    im_attr_media_10gbase_dwdm_1542_94 = 147

    im_attr_media_10gbase_dwdm_1542_14 = 148

    im_attr_media_10gbase_dwdm_1541_35 = 149

    im_attr_media_10gbase_dwdm_1540_56 = 150

    im_attr_media_10gbase_dwdm_1539_77 = 151

    im_attr_media_10gbase_dwdm_1538_98 = 152

    im_attr_media_10gbase_dwdm_1538_19 = 153

    im_attr_media_10gbase_dwdm_1537_40 = 154

    im_attr_media_10gbase_dwdm_1536_61 = 155

    im_attr_media_10gbase_dwdm_1535_82 = 156

    im_attr_media_10gbase_dwdm_1535_04 = 157

    im_attr_media_10gbase_dwdm_1534_25 = 158

    im_attr_media_10gbase_dwdm_1533_47 = 159

    im_attr_media_10gbase_dwdm_1532_68 = 160

    im_attr_media_10gbase_dwdm_1531_90 = 161

    im_attr_media_10gbase_dwdm_1531_12 = 162

    im_attr_media_10gbase_dwdm_1530_33 = 163

    im_attr_media_10gbase_dwdm_tunable = 164

    im_attr_media_40gbase_dwdm_1561_42 = 165

    im_attr_media_40gbase_dwdm_1560_61 = 166

    im_attr_media_40gbase_dwdm_1559_79 = 167

    im_attr_media_40gbase_dwdm_1558_98 = 168

    im_attr_media_40gbase_dwdm_1558_17 = 169

    im_attr_media_40gbase_dwdm_1557_36 = 170

    im_attr_media_40gbase_dwdm_1556_55 = 171

    im_attr_media_40gbase_dwdm_1555_75 = 172

    im_attr_media_40gbase_dwdm_1554_94 = 173

    im_attr_media_40gbase_dwdm_1554_13 = 174

    im_attr_media_40gbase_dwdm_1553_33 = 175

    im_attr_media_40gbase_dwdm_1552_52 = 176

    im_attr_media_40gbase_dwdm_1551_72 = 177

    im_attr_media_40gbase_dwdm_1550_92 = 178

    im_attr_media_40gbase_dwdm_1550_12 = 179

    im_attr_media_40gbase_dwdm_1549_32 = 180

    im_attr_media_40gbase_dwdm_1548_51 = 181

    im_attr_media_40gbase_dwdm_1547_72 = 182

    im_attr_media_40gbase_dwdm_1546_92 = 183

    im_attr_media_40gbase_dwdm_1546_12 = 184

    im_attr_media_40gbase_dwdm_1545_32 = 185

    im_attr_media_40gbase_dwdm_1544_53 = 186

    im_attr_media_40gbase_dwdm_1543_73 = 187

    im_attr_media_40gbase_dwdm_1542_94 = 188

    im_attr_media_40gbase_dwdm_1542_14 = 189

    im_attr_media_40gbase_dwdm_1541_35 = 190

    im_attr_media_40gbase_dwdm_1540_56 = 191

    im_attr_media_40gbase_dwdm_1539_77 = 192

    im_attr_media_40gbase_dwdm_1538_98 = 193

    im_attr_media_40gbase_dwdm_1538_19 = 194

    im_attr_media_40gbase_dwdm_1537_40 = 195

    im_attr_media_40gbase_dwdm_1536_61 = 196

    im_attr_media_40gbase_dwdm_1535_82 = 197

    im_attr_media_40gbase_dwdm_1535_04 = 198

    im_attr_media_40gbase_dwdm_1534_25 = 199

    im_attr_media_40gbase_dwdm_1533_47 = 200

    im_attr_media_40gbase_dwdm_1532_68 = 201

    im_attr_media_40gbase_dwdm_1531_90 = 202

    im_attr_media_40gbase_dwdm_1531_12 = 203

    im_attr_media_40gbase_dwdm_1530_33 = 204

    im_attr_media_40gbase_dwdm_tunable = 205

    im_attr_media_100gbase_dwdm_1561_42 = 206

    im_attr_media_100gbase_dwdm_1560_61 = 207

    im_attr_media_100gbase_dwdm_1559_79 = 208

    im_attr_media_100gbase_dwdm_1558_98 = 209

    im_attr_media_100gbase_dwdm_1558_17 = 210

    im_attr_media_100gbase_dwdm_1557_36 = 211

    im_attr_media_100gbase_dwdm_1556_55 = 212

    im_attr_media_100gbase_dwdm_1555_75 = 213

    im_attr_media_100gbase_dwdm_1554_94 = 214

    im_attr_media_100gbase_dwdm_1554_13 = 215

    im_attr_media_100gbase_dwdm_1553_33 = 216

    im_attr_media_100gbase_dwdm_1552_52 = 217

    im_attr_media_100gbase_dwdm_1551_72 = 218

    im_attr_media_100gbase_dwdm_1550_92 = 219

    im_attr_media_100gbase_dwdm_1550_12 = 220

    im_attr_media_100gbase_dwdm_1549_32 = 221

    im_attr_media_100gbase_dwdm_1548_51 = 222

    im_attr_media_100gbase_dwdm_1547_72 = 223

    im_attr_media_100gbase_dwdm_1546_92 = 224

    im_attr_media_100gbase_dwdm_1546_12 = 225

    im_attr_media_100gbase_dwdm_1545_32 = 226

    im_attr_media_100gbase_dwdm_1544_53 = 227

    im_attr_media_100gbase_dwdm_1543_73 = 228

    im_attr_media_100gbase_dwdm_1542_94 = 229

    im_attr_media_100gbase_dwdm_1542_14 = 230

    im_attr_media_100gbase_dwdm_1541_35 = 231

    im_attr_media_100gbase_dwdm_1540_56 = 232

    im_attr_media_100gbase_dwdm_1539_77 = 233

    im_attr_media_100gbase_dwdm_1538_98 = 234

    im_attr_media_100gbase_dwdm_1538_19 = 235

    im_attr_media_100gbase_dwdm_1537_40 = 236

    im_attr_media_100gbase_dwdm_1536_61 = 237

    im_attr_media_100gbase_dwdm_1535_82 = 238

    im_attr_media_100gbase_dwdm_1535_04 = 239

    im_attr_media_100gbase_dwdm_1534_25 = 240

    im_attr_media_100gbase_dwdm_1533_47 = 241

    im_attr_media_100gbase_dwdm_1532_68 = 242

    im_attr_media_100gbase_dwdm_1531_90 = 243

    im_attr_media_100gbase_dwdm_1531_12 = 244

    im_attr_media_100gbase_dwdm_1530_33 = 245

    im_attr_media_100gbase_dwdm_tunable = 246

    im_attr_media_40gbase_kr4 = 247

    im_attr_media_40gbase_cr4 = 248

    im_attr_media_40gbase_sr4 = 249

    im_attr_media_40gbase_fr = 250

    im_attr_media_100gbase_cr10 = 251

    im_attr_media_100gbase_sr10 = 252

    im_attr_media_40gbase_csr4 = 253

    im_attr_media_10gbase_cwdm = 254

    im_attr_media_10gbase_cwdm_tunable = 255

    im_attr_media_10gbase_cwdm_1470 = 256

    im_attr_media_10gbase_cwdm_1490 = 257

    im_attr_media_10gbase_cwdm_1510 = 258

    im_attr_media_10gbase_cwdm_1530 = 259

    im_attr_media_10gbase_cwdm_1550 = 260

    im_attr_media_10gbase_cwdm_1570 = 261

    im_attr_media_10gbase_cwdm_1590 = 262

    im_attr_media_10gbase_cwdm_1610 = 263

    im_attr_media_40gbase_cwdm = 264

    im_attr_media_40gbase_cwdm_tunable = 265

    im_attr_media_40gbase_cwdm_1470 = 266

    im_attr_media_40gbase_cwdm_1490 = 267

    im_attr_media_40gbase_cwdm_1510 = 268

    im_attr_media_40gbase_cwdm_1530 = 269

    im_attr_media_40gbase_cwdm_1550 = 270

    im_attr_media_40gbase_cwdm_1570 = 271

    im_attr_media_40gbase_cwdm_1590 = 272

    im_attr_media_40gbase_cwdm_1610 = 273

    im_attr_media_100gbase_cwdm = 274

    im_attr_media_100gbase_cwdm_tunable = 275

    im_attr_media_100gbase_cwdm_1470 = 276

    im_attr_media_100gbase_cwdm_1490 = 277

    im_attr_media_100gbase_cwdm_1510 = 278

    im_attr_media_100gbase_cwdm_1530 = 279

    im_attr_media_100gbase_cwdm_1550 = 280

    im_attr_media_100gbase_cwdm_1570 = 281

    im_attr_media_100gbase_cwdm_1590 = 282

    im_attr_media_100gbase_cwdm_1610 = 283

    im_attr_media_40gbase_elpb = 284

    im_attr_media_100gbase_elpb = 285

    im_attr_media_100gbase_lr10 = 286

    im_attr_media_40gbase = 287

    im_attr_media_100gbase_kp4 = 288

    im_attr_media_100gbase_kr4 = 289

    im_attr_media_10gbase_lrm = 290

    im_attr_media_10gbase_cx4 = 291

    im_attr_media_10gbase = 292

    im_attr_media_10gbase_kx4 = 293

    im_attr_media_10gbase_kr = 294

    im_attr_media_10gbase_pr = 295

    im_attr_media_100base_lx = 296

    im_attr_media_100base_zx = 297

    im_attr_media_1000base_bx_d = 298

    im_attr_media_1000base_bx_u = 299

    im_attr_media_1000base_bx20_d = 300

    im_attr_media_1000base_bx20_u = 301

    im_attr_media_1000base_bx40_d = 302

    im_attr_media_1000base_bx40_da = 303

    im_attr_media_1000base_bx40_u = 304

    im_attr_media_1000base_bx80_d = 305

    im_attr_media_1000base_bx80_u = 306

    im_attr_media_1000base_bx120_d = 307

    im_attr_media_1000base_bx120_u = 308

    im_attr_media_10gbase_bx_d = 309

    im_attr_media_10gbase_bx_u = 310

    im_attr_media_10gbase_bx10_d = 311

    im_attr_media_10gbase_bx10_u = 312

    im_attr_media_10gbase_bx20_d = 313

    im_attr_media_10gbase_bx20_u = 314

    im_attr_media_10gbase_bx40_d = 315

    im_attr_media_10gbase_bx40_u = 316

    im_attr_media_10gbase_bx80_d = 317

    im_attr_media_10gbase_bx80_u = 318

    im_attr_media_10gbase_bx120_d = 319

    im_attr_media_10gbase_bx120_u = 320

    im_attr_media_1000base_dr_lx = 321

    im_attr_media_100gbase_er4l = 322

    im_attr_media_100gbase_sr4 = 323

    im_attr_media_40gbase_sr_bd = 324

    im_attr_media_25gbase_cr = 325

    im_attr_media_25gbase_cr_s = 326

    im_attr_media_25gbase_kr = 327

    im_attr_media_25gbase_kr_s = 328

    im_attr_media_25gbase_r = 329

    im_attr_media_25gbase_sr = 330

    im_attr_media_25gbase_dwdm = 331

    im_attr_media_25gbase_dwdm_tunable = 332

    im_attr_media_25gbase_cwdm = 333

    im_attr_media_25gbase_cwdm_tunable = 334

    im_attr_media_100gbase_psm4 = 335

    im_attr_media_100gbase_er10 = 336

    im_attr_media_100gbase_er10l = 337

    im_attr_media_100gbase_acc = 338

    im_attr_media_100gbase_aoc = 339

    im_attr_media_100gbase_cwdm4 = 340

    im_attr_media_40gbase_psm4 = 341

    im_attr_media_100gbase_cr4 = 342

    im_attr_media_100gbase_act_loop = 343

    im_attr_media_100gbase_pas_loop = 344


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrMediaEnum']


class ImAttrTransportModeEnum(Enum):
    """
    ImAttrTransportModeEnum

    Im attr transport mode

    .. data:: im_attr_transport_mode_unknown = 0

    	im attr transport mode unknown

    .. data:: im_attr_transport_mode_lan = 1

    	im attr transport mode lan

    .. data:: im_attr_transport_mode_wan = 2

    	im attr transport mode wan

    .. data:: im_attr_transport_mode_otn_bt_opu1e = 3

    	im attr transport mode otn bt opu1e

    .. data:: im_attr_transport_mode_otn_bt_opu2e = 4

    	im attr transport mode otn bt opu2e

    .. data:: im_attr_transport_mode_otn_opu3 = 5

    	im attr transport mode otn opu3

    .. data:: im_attr_transport_mode_otn_opu4 = 6

    	im attr transport mode otn opu4

    """

    im_attr_transport_mode_unknown = 0

    im_attr_transport_mode_lan = 1

    im_attr_transport_mode_wan = 2

    im_attr_transport_mode_otn_bt_opu1e = 3

    im_attr_transport_mode_otn_bt_opu2e = 4

    im_attr_transport_mode_otn_opu3 = 5

    im_attr_transport_mode_otn_opu4 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrTransportModeEnum']


class ImCmdEncapsEnumEnum(Enum):
    """
    ImCmdEncapsEnumEnum

    Im cmd encaps enum

    .. data:: frame_relay = 0

    	frame relay

    .. data:: vlan = 1

    	vlan

    .. data:: ppp = 2

    	ppp

    """

    frame_relay = 0

    vlan = 1

    ppp = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdEncapsEnumEnum']


class ImCmdFrTypeEnumEnum(Enum):
    """
    ImCmdFrTypeEnumEnum

    Im cmd fr type enum

    .. data:: frame_relay_cisco = 0

    	frame relay cisco

    .. data:: frame_relay_ietf = 1

    	frame relay ietf

    """

    frame_relay_cisco = 0

    frame_relay_ietf = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdFrTypeEnumEnum']


class ImCmdIntfTypeEnumEnum(Enum):
    """
    ImCmdIntfTypeEnumEnum

    Im cmd intf type enum

    .. data:: srp = 0

    	srp

    .. data:: tunnel = 1

    	tunnel

    .. data:: bundle = 2

    	bundle

    .. data:: serial = 3

    	serial

    .. data:: sonet_pos = 4

    	sonet pos

    .. data:: tunnel_gre = 5

    	tunnel gre

    .. data:: pseudowire_head_end = 6

    	pseudowire head end

    .. data:: cem = 7

    	cem

    .. data:: gcc = 8

    	gcc

    """

    srp = 0

    tunnel = 1

    bundle = 2

    serial = 3

    sonet_pos = 4

    tunnel_gre = 5

    pseudowire_head_end = 6

    cem = 7

    gcc = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdIntfTypeEnumEnum']


class ImCmdLmiTypeEnumEnum(Enum):
    """
    ImCmdLmiTypeEnumEnum

    Im cmd lmi type enum

    .. data:: lmi_type_auto = 0

    	lmi type auto

    .. data:: lmi_type_ansi = 1

    	lmi type ansi

    .. data:: lmi_type_ccitt = 2

    	lmi type ccitt

    .. data:: lmi_type_cisco = 3

    	lmi type cisco

    """

    lmi_type_auto = 0

    lmi_type_ansi = 1

    lmi_type_ccitt = 2

    lmi_type_cisco = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdLmiTypeEnumEnum']


class ImCmdLoopbackEnumEnum(Enum):
    """
    ImCmdLoopbackEnumEnum

    Im cmd loopback enum

    .. data:: no_loopback = 0

    	no loopback

    .. data:: internal_loopback = 1

    	internal loopback

    .. data:: external_loopback = 2

    	external loopback

    .. data:: line_loopback = 3

    	line loopback

    """

    no_loopback = 0

    internal_loopback = 1

    external_loopback = 2

    line_loopback = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdLoopbackEnumEnum']


class ImCmdStatsEnumEnum(Enum):
    """
    ImCmdStatsEnumEnum

    List of different interface stats structures

    .. data:: full = 1

    	full

    .. data:: basic = 2

    	basic

    """

    full = 1

    basic = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdStatsEnumEnum']


class ImStateEnumEnum(Enum):
    """
    ImStateEnumEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = 0

    im_state_admin_down = 1

    im_state_down = 2

    im_state_up = 3

    im_state_shutdown = 4

    im_state_err_disable = 5

    im_state_down_immediate = 6

    im_state_down_immediate_admin = 7

    im_state_down_graceful = 8

    im_state_begin_shutdown = 9

    im_state_end_shutdown = 10

    im_state_begin_error_disable = 11

    im_state_end_error_disable = 12

    im_state_begin_down_graceful = 13

    im_state_reset = 14

    im_state_operational = 15

    im_state_not_operational = 16

    im_state_unknown = 17

    im_state_last = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImStateEnumEnum']


class InterfaceTypeSetEnum(Enum):
    """
    InterfaceTypeSetEnum

    Interface type set

    .. data:: hardware_interfaces = 0

    	Restrict the output to hardware interfaces only

    """

    hardware_interfaces = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['InterfaceTypeSetEnum']


class NcpIdentEnum(Enum):
    """
    NcpIdentEnum

    Ncp ident

    .. data:: cdpcp = 1

    	CDP control protocol

    .. data:: ipcp = 2

    	IPv4 control protocol

    .. data:: ipcpiw = 3

    	IPv4 Interworking control protocol

    .. data:: ipv6cp = 4

    	IPv6 control protocol

    .. data:: mplscp = 5

    	MPLS control protocol

    .. data:: osicp = 6

    	OSI (CLNS) control protocol

    """

    cdpcp = 1

    ipcp = 2

    ipcpiw = 3

    ipv6cp = 4

    mplscp = 5

    osicp = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['NcpIdentEnum']


class PppFsmStateEnum(Enum):
    """
    PppFsmStateEnum

    Ppp fsm state

    .. data:: ppp_fsm_state_initial_0 = 0

    	Connection Idle

    .. data:: ppp_fsm_state_starting_1 = 1

    	This layer required, but lower layer down

    .. data:: ppp_fsm_state_closed_2 = 2

    	Lower layer up, but this layer not required

    .. data:: ppp_fsm_state_stopped_3 = 3

    	Listening for a Config Request

    .. data:: ppp_fsm_state_closing_4 = 4

    	Shutting down due to local change

    .. data:: ppp_fsm_state_stopping_5 = 5

    	Shutting down due to peer's actions

    .. data:: ppp_fsm_state_req_sent_6 = 6

    	Config Request Sent

    .. data:: ppp_fsm_state_ack_rcvd_7 = 7

    	Config Ack Received

    .. data:: ppp_fsm_state_ack_sent_8 = 8

    	Config Ack Sent

    .. data:: ppp_fsm_state_opened_9 = 9

    	Connection Open

    """

    ppp_fsm_state_initial_0 = 0

    ppp_fsm_state_starting_1 = 1

    ppp_fsm_state_closed_2 = 2

    ppp_fsm_state_stopped_3 = 3

    ppp_fsm_state_closing_4 = 4

    ppp_fsm_state_stopping_5 = 5

    ppp_fsm_state_req_sent_6 = 6

    ppp_fsm_state_ack_rcvd_7 = 7

    ppp_fsm_state_ack_sent_8 = 8

    ppp_fsm_state_opened_9 = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['PppFsmStateEnum']


class SonetApsEtEnum(Enum):
    """
    SonetApsEtEnum

    APS states

    .. data:: not_configured = 0

    	APS not configured on port

    .. data:: working_active = 1

    	Working port is up 

    .. data:: protect_active = 2

    	Protect port is up  

    .. data:: working_inactive = 3

    	Working port is down 

    .. data:: protect_inactive = 4

    	Protect port is down  

    """

    not_configured = 0

    working_active = 1

    protect_active = 2

    working_inactive = 3

    protect_inactive = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SonetApsEtEnum']


class SrpMgmtFailureEtEnum(Enum):
    """
    SrpMgmtFailureEtEnum

    SRP failure type

    .. data:: hardware_missing_failure = 0

    	Hardware missing

    .. data:: layer1_admin_state_failure = 1

    	L1 admin state

    .. data:: layer1_error_failure = 2

    	Layer 1 error

    .. data:: keepalive_missed_failure = 3

    	Keepalive missed

    .. data:: link_quality_degraded_failure = 4

    	Link quality degraded

    .. data:: mate_problem_failure = 5

    	Mate problem

    .. data:: side_mismatch_failure = 6

    	Side mismatch

    .. data:: unknown_failure = 7

    	Unknown

    """

    hardware_missing_failure = 0

    layer1_admin_state_failure = 1

    layer1_error_failure = 2

    keepalive_missed_failure = 3

    link_quality_degraded_failure = 4

    mate_problem_failure = 5

    side_mismatch_failure = 6

    unknown_failure = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtFailureEtEnum']


class SrpMgmtFailureStateEtEnum(Enum):
    """
    SrpMgmtFailureStateEtEnum

    SRP failure state type

    .. data:: idle_failure_state = 0

    	Idle

    .. data:: wait_to_restore_failure_state = 1

    	Wait To Restore

    .. data:: manual_switch_failure_state = 2

    	Manual Switch

    .. data:: signal_degrade_failure_state = 3

    	Signal Degrade

    .. data:: signal_fail_failure_state = 4

    	Signal Fail

    .. data:: forced_switch_failure_state = 5

    	Forced Switch

    .. data:: shutdown_failure_state = 6

    	Shutdown

    .. data:: invalid_failure_state = 7

    	Invalid

    .. data:: unknown_failure_state = 8

    	Unknown

    """

    idle_failure_state = 0

    wait_to_restore_failure_state = 1

    manual_switch_failure_state = 2

    signal_degrade_failure_state = 3

    signal_fail_failure_state = 4

    forced_switch_failure_state = 5

    shutdown_failure_state = 6

    invalid_failure_state = 7

    unknown_failure_state = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtFailureStateEtEnum']


class SrpMgmtIpsPathIndEnum(Enum):
    """
    SrpMgmtIpsPathIndEnum

    SRP IPS path indication

    .. data:: short_path = 0

    	SHORT

    .. data:: long_path = 1

    	LONG

    .. data:: unknown_path = 2

    	UNKNOWN

    """

    short_path = 0

    long_path = 1

    unknown_path = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtIpsPathIndEnum']


class SrpMgmtIpsReqEnum(Enum):
    """
    SrpMgmtIpsReqEnum

    SRP IPS request type

    .. data:: idle_ips_request = 0

    	Idle

    .. data:: wait_to_restore_ips_request = 1

    	Wait To Restore

    .. data:: manual_switch_ips_request = 2

    	Manual Switch

    .. data:: signal_degrade_ips_request = 3

    	Signal Degrade

    .. data:: signal_fail_ips_request = 4

    	Signal Fail

    .. data:: forced_switch_ips_request = 5

    	Forced Switch

    .. data:: unknown_ips_request = 6

    	UNKNOWN

    """

    idle_ips_request = 0

    wait_to_restore_ips_request = 1

    manual_switch_ips_request = 2

    signal_degrade_ips_request = 3

    signal_fail_ips_request = 4

    forced_switch_ips_request = 5

    unknown_ips_request = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtIpsReqEnum']


class SrpMgmtIpsWrapStateEnum(Enum):
    """
    SrpMgmtIpsWrapStateEnum

    SRP IPS side wrap state

    .. data:: idle_wrap_state = 0

    	Idle

    .. data:: wrapped_state = 1

    	Wrapped

    .. data:: locked_out_wrap_state = 2

    	Locked out

    .. data:: unknown_wrap_state = 3

    	UNKNOWN

    """

    idle_wrap_state = 0

    wrapped_state = 1

    locked_out_wrap_state = 2

    unknown_wrap_state = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtIpsWrapStateEnum']


class SrpMgmtSrrFailureEnum(Enum):
    """
    SrpMgmtSrrFailureEnum

    SRP SRR failure type

    .. data:: idle_srr_failure = 0

    	Idle

    .. data:: wait_to_restore_srr_failure = 1

    	Wait To Restore

    .. data:: signal_fail_srr_failure = 2

    	Signal Fail

    .. data:: forced_switch_srr_failure = 3

    	Forced Switch

    .. data:: unknown_srr_failure = 4

    	UNKNOWN

    """

    idle_srr_failure = 0

    wait_to_restore_srr_failure = 1

    signal_fail_srr_failure = 2

    forced_switch_srr_failure = 3

    unknown_srr_failure = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtSrrFailureEnum']


class SrpMgmtSrrNodeStateEnum(Enum):
    """
    SrpMgmtSrrNodeStateEnum

    SRP SRR node state

    .. data:: idle_srr_state = 0

    	Idle

    .. data:: discovery_srr_state = 1

    	Discovery

    .. data:: unknown_srr_state = 2

    	UNKNOWN

    """

    idle_srr_state = 0

    discovery_srr_state = 1

    unknown_srr_state = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtSrrNodeStateEnum']


class StatsCounterEnum(Enum):
    """
    StatsCounterEnum

    Stats counter

    .. data:: stats_counter_rate = 0

    	stats counter rate

    .. data:: stats_counter_uint32 = 1

    	stats counter uint32

    .. data:: stats_counter_uint64 = 2

    	stats counter uint64

    .. data:: stats_counter_generic = 3

    	stats counter generic

    .. data:: stats_counter_proto = 4

    	stats counter proto

    .. data:: stats_counter_srp = 5

    	stats counter srp

    .. data:: stats_counter_ipv4_prec = 6

    	stats counter ipv4 prec

    .. data:: stats_counter_ipv4_dscp = 7

    	stats counter ipv4 dscp

    .. data:: stats_counter_mpls_exp = 8

    	stats counter mpls exp

    .. data:: stats_counter_ipv4_bgppa = 9

    	stats counter ipv4 bgppa

    .. data:: stats_counter_src_bgppa = 10

    	stats counter src bgppa

    .. data:: stats_counter_basic = 11

    	stats counter basic

    .. data:: stats_counter_comp_generic = 12

    	stats counter comp generic

    .. data:: stats_counter_comp_proto = 13

    	stats counter comp proto

    .. data:: stats_counter_comp_basic = 14

    	stats counter comp basic

    .. data:: stats_counter_accounting = 15

    	stats counter accounting

    .. data:: stats_counter_comp_accounting = 16

    	stats counter comp accounting

    .. data:: stats_counter_flow = 17

    	stats counter flow

    .. data:: stats_counter_comp_flow = 18

    	stats counter comp flow

    """

    stats_counter_rate = 0

    stats_counter_uint32 = 1

    stats_counter_uint64 = 2

    stats_counter_generic = 3

    stats_counter_proto = 4

    stats_counter_srp = 5

    stats_counter_ipv4_prec = 6

    stats_counter_ipv4_dscp = 7

    stats_counter_mpls_exp = 8

    stats_counter_ipv4_bgppa = 9

    stats_counter_src_bgppa = 10

    stats_counter_basic = 11

    stats_counter_comp_generic = 12

    stats_counter_comp_proto = 13

    stats_counter_comp_basic = 14

    stats_counter_accounting = 15

    stats_counter_comp_accounting = 16

    stats_counter_flow = 17

    stats_counter_comp_flow = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['StatsCounterEnum']


class StatsIdEnum(Enum):
    """
    StatsIdEnum

    Stats id

    .. data:: stats_id_type_unknown = 0

    	stats id type unknown

    .. data:: stats_id_type_min = 1

    	stats id type min

    .. data:: stats_id_type_spare = 2

    	stats id type spare

    .. data:: stats_id_type_node = 3

    	stats id type node

    .. data:: stats_id_type_other = 4

    	stats id type other

    .. data:: stats_id_type_feature = 5

    	stats id type feature

    .. data:: stats_id_type_max = 6

    	stats id type max

    """

    stats_id_type_unknown = 0

    stats_id_type_min = 1

    stats_id_type_spare = 2

    stats_id_type_node = 3

    stats_id_type_other = 4

    stats_id_type_feature = 5

    stats_id_type_max = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['StatsIdEnum']


class StatsTypeContentsEnum(Enum):
    """
    StatsTypeContentsEnum

    Stats type contents

    .. data:: stats_type_single = 100

    	stats type single

    .. data:: stats_type_variable = 101

    	stats type variable

    """

    stats_type_single = 100

    stats_type_variable = 101


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['StatsTypeContentsEnum']


class TunlPfiAfIdEnum(Enum):
    """
    TunlPfiAfIdEnum

    Tunl pfi af id

    .. data:: tunl_pfi_af_id_none = 0

    	Unspecified AFI

    .. data:: tunl_pfi_af_id_ipv4 = 2

    	IPv4 AFI

    .. data:: tunl_pfi_af_id_ipv6 = 10

    	IPv6 AFI

    """

    tunl_pfi_af_id_none = 0

    tunl_pfi_af_id_ipv4 = 2

    tunl_pfi_af_id_ipv6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunlPfiAfIdEnum']


class TunnelGreModeEnum(Enum):
    """
    TunnelGreModeEnum

    Tunnel gre mode

    .. data:: unknown = 0

    	Tunnel GRE mode is Unknown

    .. data:: gr_eo_ipv4 = 1

    	Tunnel GRE Mode is IPv4

    .. data:: gr_eo_ipv6 = 2

    	Tunnel GRE Mode is IPv6

    .. data:: mgr_eo_ipv4 = 3

    	Tunnel MGRE Mode is IPv4

    .. data:: mgr_eo_ipv6 = 4

    	Tunnel MGRE Mode is IPv6

    .. data:: ipv4 = 5

    	Tunnel Mode is IPv4

    .. data:: ipv6 = 6

    	Tunnel Mode is IPv6

    """

    unknown = 0

    gr_eo_ipv4 = 1

    gr_eo_ipv6 = 2

    mgr_eo_ipv4 = 3

    mgr_eo_ipv6 = 4

    ipv4 = 5

    ipv6 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunnelGreModeEnum']


class TunnelKaDfStateEnum(Enum):
    """
    TunnelKaDfStateEnum

    Tunnel ka df state

    .. data:: disable = 0

    	Tunnel GRE KA State is Disabled

    .. data:: enable = 1

    	Tunnel GRE KA State is Enabled

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunnelKaDfStateEnum']


class TunnelKeyStateEnum(Enum):
    """
    TunnelKeyStateEnum

    Tunnel key state

    .. data:: absent = 0

    	Tunnel GRE Key is not present

    .. data:: present = 1

    	Tunnel GRE Key is present

    """

    absent = 0

    present = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunnelKeyStateEnum']


class VlanEncapsEnum(Enum):
    """
    VlanEncapsEnum

    VLAN encapsulation

    .. data:: no_encapsulation = 0

    	No encapsulation

    .. data:: dot1q = 1

    	IEEE 802.1Q encapsulation

    .. data:: qinq = 2

    	Double 802.1Q encapsulation

    .. data:: qin_any = 3

    	Double 802.1Q wildcarded encapsulation

    .. data:: dot1q_native = 4

    	IEEE 802.1Q native VLAN encapsulation

    .. data:: dot1ad = 5

    	IEEE 802.1ad encapsulation

    .. data:: dot1ad_native = 6

    	IEEE 802.1ad native VLAN encapsulation

    .. data:: service_instance = 7

    	Ethernet Service Instance

    .. data:: dot1ad_dot1q = 8

    	IEEE 802.1ad 802.1Q encapsulation

    .. data:: dot1ad_any = 9

    	IEEE 802.1ad wildcard 802.1Q encapsulation

    """

    no_encapsulation = 0

    dot1q = 1

    qinq = 2

    qin_any = 3

    dot1q_native = 4

    dot1ad = 5

    dot1ad_native = 6

    service_instance = 7

    dot1ad_dot1q = 8

    dot1ad_any = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['VlanEncapsEnum']



class Interfaces(object):
    """
    Interface operational data
    
    .. attribute:: interface_briefs
    
    	Brief operational data for interfaces
    	**type**\:   :py:class:`InterfaceBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceBriefs>`
    
    .. attribute:: interface_summary
    
    	Interface summary information
    	**type**\:   :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary>`
    
    .. attribute:: interface_xr
    
    	Detailed operational data for interfaces and configured features
    	**type**\:   :py:class:`InterfaceXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr>`
    
    .. attribute:: interfaces
    
    	Descriptions for interfaces
    	**type**\:   :py:class:`Interfaces_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.Interfaces_>`
    
    .. attribute:: inventory_summary
    
    	Inventory summary information
    	**type**\:   :py:class:`InventorySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary>`
    
    .. attribute:: node_type_sets
    
    	Node and/or interface type specific view of interface summary data
    	**type**\:   :py:class:`NodeTypeSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets>`
    
    

    """

    _prefix = 'pfi-im-cmd-oper'
    _revision = '2016-12-18'

    def __init__(self):
        self.interface_briefs = Interfaces.InterfaceBriefs()
        self.interface_briefs.parent = self
        self.interface_summary = Interfaces.InterfaceSummary()
        self.interface_summary.parent = self
        self.interface_xr = Interfaces.InterfaceXr()
        self.interface_xr.parent = self
        self.interfaces = Interfaces.Interfaces_()
        self.interfaces.parent = self
        self.inventory_summary = Interfaces.InventorySummary()
        self.inventory_summary.parent = self
        self.node_type_sets = Interfaces.NodeTypeSets()
        self.node_type_sets.parent = self


    class InterfaceXr(object):
        """
        Detailed operational data for interfaces and
        configured features
        
        .. attribute:: interface
        
        	Detailed operational data for a particular interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2016-12-18'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Detailed operational data for a particular
            interface
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: arp_information
            
            	Interface ARP type and timeout
            	**type**\:   :py:class:`ArpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.ArpInformation>`
            
            .. attribute:: bandwidth
            
            	Interface bandwidth (Kb/s)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: burned_in_address
            
            	Interface burned in address
            	**type**\:   :py:class:`BurnedInAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.BurnedInAddress>`
            
            .. attribute:: carrier_delay
            
            	Carrier Delay
            	**type**\:   :py:class:`CarrierDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.CarrierDelay>`
            
            .. attribute:: crc_length
            
            	Cyclic Redundancy Check length
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dampening_information
            
            	State dampening information
            	**type**\:   :py:class:`DampeningInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.DampeningInformation>`
            
            .. attribute:: data_rates
            
            	Packet and byte rates
            	**type**\:   :py:class:`DataRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.DataRates>`
            
            .. attribute:: description
            
            	Interface description string
            	**type**\:  str
            
            .. attribute:: duplexity
            
            	Interface duplexity
            	**type**\:   :py:class:`ImAttrDuplexEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrDuplexEnum>`
            
            .. attribute:: encapsulation
            
            	Interface encapsulation
            	**type**\:  str
            
            .. attribute:: encapsulation_information
            
            	Information specific to the encapsulation
            	**type**\:   :py:class:`EncapsulationInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation>`
            
            .. attribute:: encapsulation_type_string
            
            	Interface encapsulation description string
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: hardware_type_string
            
            	Hardware type description string
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: if_index
            
            	This is not supposed to be used. It is a dummy attribute to support ifindex for OC model
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_flow_control
            
            	Input flow control configuration
            	**type**\:   :py:class:`ImAttrFlowControlEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrFlowControlEnum>`
            
            .. attribute:: interface_handle
            
            	Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_statistics
            
            	Packet, byte and error counters
            	**type**\:   :py:class:`InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics>`
            
            .. attribute:: interface_type
            
            	Interface type
            	**type**\:  str
            
            .. attribute:: interface_type_information
            
            	Information specific to the interface type
            	**type**\:   :py:class:`InterfaceTypeInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation>`
            
            .. attribute:: ip_information
            
            	Interface IP address info
            	**type**\:   :py:class:`IpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.IpInformation>`
            
            .. attribute:: is_dampening_enabled
            
            	Dampening enabled flag
            	**type**\:  bool
            
            .. attribute:: is_data_inverted
            
            	Data invert flag
            	**type**\:  bool
            
            .. attribute:: is_l2_looped
            
            	Loopback detected by layer 2
            	**type**\:  bool
            
            .. attribute:: is_l2_transport_enabled
            
            	L2 transport flag
            	**type**\:  bool
            
            .. attribute:: is_maintenance_enabled
            
            	Maintenance embargo flag
            	**type**\:  bool
            
            .. attribute:: is_scramble_enabled
            
            	Interface scramble config
            	**type**\:  bool
            
            .. attribute:: keepalive
            
            	Interface keepalive time (s)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2_interface_statistics
            
            	L2 Protocol Statistics
            	**type**\:   :py:class:`L2InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics>`
            
            .. attribute:: last_state_transition_time
            
            	The time elasped after the last state transition
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: line_state
            
            	Line protocol state
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: link_type
            
            	Interface link type
            	**type**\:   :py:class:`ImAttrLinkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrLinkEnum>`
            
            .. attribute:: loopback_configuration
            
            	Interface loopback configuration
            	**type**\:   :py:class:`ImCmdLoopbackEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdLoopbackEnumEnum>`
            
            .. attribute:: mac_address
            
            	Interface MAC address
            	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.MacAddress>`
            
            .. attribute:: max_bandwidth
            
            	Maximum Interface bandwidth (Kb/s)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: media_type
            
            	Interface media type
            	**type**\:   :py:class:`ImAttrMediaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrMediaEnum>`
            
            .. attribute:: mtu
            
            	MTU in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: nv_optical
            
            	nV Optical Controller Information
            	**type**\:   :py:class:`NvOptical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.NvOptical>`
            
            .. attribute:: out_flow_control
            
            	Output flow control configuration
            	**type**\:   :py:class:`ImAttrFlowControlEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrFlowControlEnum>`
            
            .. attribute:: parent_interface_name
            
            	Parent interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: speed
            
            	Interface speed (Kb/s)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: state
            
            	Interface state
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: state_transition_count
            
            	The number of times the state has changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: transport_mode
            
            	Interface transport mode
            	**type**\:   :py:class:`ImAttrTransportModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrTransportModeEnum>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.arp_information = Interfaces.InterfaceXr.Interface.ArpInformation()
                self.arp_information.parent = self
                self.bandwidth = None
                self.burned_in_address = Interfaces.InterfaceXr.Interface.BurnedInAddress()
                self.burned_in_address.parent = self
                self.carrier_delay = Interfaces.InterfaceXr.Interface.CarrierDelay()
                self.carrier_delay.parent = self
                self.crc_length = None
                self.dampening_information = Interfaces.InterfaceXr.Interface.DampeningInformation()
                self.dampening_information.parent = self
                self.data_rates = Interfaces.InterfaceXr.Interface.DataRates()
                self.data_rates.parent = self
                self.description = None
                self.duplexity = None
                self.encapsulation = None
                self.encapsulation_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation()
                self.encapsulation_information.parent = self
                self.encapsulation_type_string = None
                self.hardware_type_string = None
                self.if_index = None
                self.in_flow_control = None
                self.interface_handle = None
                self.interface_statistics = Interfaces.InterfaceXr.Interface.InterfaceStatistics()
                self.interface_statistics.parent = self
                self.interface_type = None
                self.interface_type_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation()
                self.interface_type_information.parent = self
                self.ip_information = Interfaces.InterfaceXr.Interface.IpInformation()
                self.ip_information.parent = self
                self.is_dampening_enabled = None
                self.is_data_inverted = None
                self.is_l2_looped = None
                self.is_l2_transport_enabled = None
                self.is_maintenance_enabled = None
                self.is_scramble_enabled = None
                self.keepalive = None
                self.l2_interface_statistics = Interfaces.InterfaceXr.Interface.L2InterfaceStatistics()
                self.l2_interface_statistics.parent = self
                self.last_state_transition_time = None
                self.line_state = None
                self.link_type = None
                self.loopback_configuration = None
                self.mac_address = Interfaces.InterfaceXr.Interface.MacAddress()
                self.mac_address.parent = self
                self.max_bandwidth = None
                self.media_type = None
                self.mtu = None
                self.nv_optical = Interfaces.InterfaceXr.Interface.NvOptical()
                self.nv_optical.parent = self
                self.out_flow_control = None
                self.parent_interface_name = None
                self.speed = None
                self.state = None
                self.state_transition_count = None
                self.transport_mode = None


            class DampeningInformation(object):
                """
                State dampening information
                
                .. attribute:: half_life
                
                	Configured decay half life in mins
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: is_suppressed_enabled
                
                	Flag showing if state is suppressed
                	**type**\:  bool
                
                .. attribute:: maximum_suppress_time
                
                	Maximum suppress time in mins
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: penalty
                
                	Dampening penalty of the interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: restart_penalty
                
                	Configured restart penalty
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: reuse_threshold
                
                	Configured reuse threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_remaining
                
                	Remaining period of suppression in secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: suppress_threshold
                
                	Value of suppress threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.half_life = None
                    self.is_suppressed_enabled = None
                    self.maximum_suppress_time = None
                    self.penalty = None
                    self.restart_penalty = None
                    self.reuse_threshold = None
                    self.seconds_remaining = None
                    self.suppress_threshold = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:dampening-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.half_life is not None:
                        return True

                    if self.is_suppressed_enabled is not None:
                        return True

                    if self.maximum_suppress_time is not None:
                        return True

                    if self.penalty is not None:
                        return True

                    if self.restart_penalty is not None:
                        return True

                    if self.reuse_threshold is not None:
                        return True

                    if self.seconds_remaining is not None:
                        return True

                    if self.suppress_threshold is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.DampeningInformation']['meta_info']


            class MacAddress(object):
                """
                Interface MAC address
                
                .. attribute:: address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:mac-address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.MacAddress']['meta_info']


            class BurnedInAddress(object):
                """
                Interface burned in address
                
                .. attribute:: address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:burned-in-address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.BurnedInAddress']['meta_info']


            class CarrierDelay(object):
                """
                Carrier Delay
                
                .. attribute:: carrier_delay_down
                
                	Carrier delay on state down (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: carrier_delay_up
                
                	Carrier delay on state up (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.carrier_delay_down = None
                    self.carrier_delay_up = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:carrier-delay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.carrier_delay_down is not None:
                        return True

                    if self.carrier_delay_up is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.CarrierDelay']['meta_info']


            class ArpInformation(object):
                """
                Interface ARP type and timeout
                
                .. attribute:: arp_is_learning_disabled
                
                	Whether the interface has dynamic learning disabled
                	**type**\:  bool
                
                .. attribute:: arp_timeout
                
                	ARP timeout in seconds. Only valid if 'ARPIsLearningDisabled' is 'false'
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: arp_type_name
                
                	ARP type name
                	**type**\:  str
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.arp_is_learning_disabled = None
                    self.arp_timeout = None
                    self.arp_type_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:arp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.arp_is_learning_disabled is not None:
                        return True

                    if self.arp_timeout is not None:
                        return True

                    if self.arp_type_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.ArpInformation']['meta_info']


            class IpInformation(object):
                """
                Interface IP address info
                
                .. attribute:: ip_address
                
                	Interface IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: subnet_mask_length
                
                	Interface subnet mask length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.ip_address = None
                    self.subnet_mask_length = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ip-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ip_address is not None:
                        return True

                    if self.subnet_mask_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.IpInformation']['meta_info']


            class EncapsulationInformation(object):
                """
                Information specific to the encapsulation
                
                .. attribute:: dot1q_information
                
                	VLAN 802.1q information
                	**type**\:   :py:class:`Dot1QInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation>`
                
                .. attribute:: encapsulation_type
                
                	EncapsulationType
                	**type**\:   :py:class:`ImCmdEncapsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdEncapsEnumEnum>`
                
                .. attribute:: frame_relay_information
                
                	Frame Relay information
                	**type**\:   :py:class:`FrameRelayInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation>`
                
                .. attribute:: ppp_information
                
                	PPP information
                	**type**\:   :py:class:`PppInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.dot1q_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation()
                    self.dot1q_information.parent = self
                    self.encapsulation_type = None
                    self.frame_relay_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation()
                    self.frame_relay_information.parent = self
                    self.ppp_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation()
                    self.ppp_information.parent = self


                class FrameRelayInformation(object):
                    """
                    Frame Relay information
                    
                    .. attribute:: enquiries_received
                    
                    	Number of enquiry messages received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: enquiries_sent
                    
                    	Number of enquiry messages sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fr_encapsulation_type
                    
                    	Frame Relay encapsulation type
                    	**type**\:   :py:class:`ImCmdFrTypeEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdFrTypeEnumEnum>`
                    
                    .. attribute:: is_dte
                    
                    	The DTE/DCE LMI interface type
                    	**type**\:  bool
                    
                    .. attribute:: is_lmi_enabled
                    
                    	The status of FR LMI for an interface
                    	**type**\:  bool
                    
                    .. attribute:: is_lmi_nni_dce_up
                    
                    	Flag indicating whether the LMI  NNI\-DCE state is UP
                    	**type**\:  bool
                    
                    .. attribute:: is_lmi_up
                    
                    	Flag indicating whether the LMI  DTE/DCE/NNI\-DTE state is UP
                    	**type**\:  bool
                    
                    .. attribute:: is_nni
                    
                    	The NNI LMI interface type
                    	**type**\:  bool
                    
                    .. attribute:: lmi_type
                    
                    	The LMI type\: Autosense, ANSI, CCITT or CISCO
                    	**type**\:   :py:class:`ImCmdLmiTypeEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdLmiTypeEnumEnum>`
                    
                    .. attribute:: lmidlci
                    
                    	LMI DLCI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_received
                    
                    	Number of status messages received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_sent
                    
                    	Number of status messages sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_status_received
                    
                    	Number of update status messages received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_status_sent
                    
                    	Number of update status messages sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.enquiries_received = None
                        self.enquiries_sent = None
                        self.fr_encapsulation_type = None
                        self.is_dte = None
                        self.is_lmi_enabled = None
                        self.is_lmi_nni_dce_up = None
                        self.is_lmi_up = None
                        self.is_nni = None
                        self.lmi_type = None
                        self.lmidlci = None
                        self.status_received = None
                        self.status_sent = None
                        self.update_status_received = None
                        self.update_status_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:frame-relay-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.enquiries_received is not None:
                            return True

                        if self.enquiries_sent is not None:
                            return True

                        if self.fr_encapsulation_type is not None:
                            return True

                        if self.is_dte is not None:
                            return True

                        if self.is_lmi_enabled is not None:
                            return True

                        if self.is_lmi_nni_dce_up is not None:
                            return True

                        if self.is_lmi_up is not None:
                            return True

                        if self.is_nni is not None:
                            return True

                        if self.lmi_type is not None:
                            return True

                        if self.lmidlci is not None:
                            return True

                        if self.status_received is not None:
                            return True

                        if self.status_sent is not None:
                            return True

                        if self.update_status_received is not None:
                            return True

                        if self.update_status_sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation']['meta_info']


                class Dot1QInformation(object):
                    """
                    VLAN 802.1q information
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.encapsulation_details = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails()
                        self.encapsulation_details.parent = self


                    class EncapsulationDetails(object):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncapsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.VlanEncapsEnum>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.dot1ad_dot1q_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None
                            self.dot1ad_tag = None
                            self.native_tag = None
                            self.outer_tag = None
                            self.service_instance_details = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self.stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self.tag = None
                            self.vlan_encapsulation = None


                        class Stack(object):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.Stack']['meta_info']


                        class ServiceInstanceDetails(object):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpPayloadEtypeEnum>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.destination_mac_match = None
                                self.is_exact_match = None
                                self.is_native_preserving = None
                                self.is_native_vlan = None
                                self.local_traffic_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self.payload_ethertype = None
                                self.pushe = YList()
                                self.pushe.parent = self
                                self.pushe.name = 'pushe'
                                self.source_mac_match = None
                                self.tags_popped = None
                                self.tags_to_match = YList()
                                self.tags_to_match.parent = self
                                self.tags_to_match.name = 'tags_to_match'


                            class LocalTrafficStack(object):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.local_traffic_tag = YList()
                                    self.local_traffic_tag.parent = self
                                    self.local_traffic_tag.name = 'local_traffic_tag'


                                class LocalTrafficTag(object):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtypeEnum>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.ethertype = None
                                        self.vlan_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-traffic-tag'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.ethertype is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-traffic-stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.local_traffic_tag is not None:
                                        for child_ref in self.local_traffic_tag:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info']


                            class TagsToMatch(object):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtypeEnum>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagPriorityEnum>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.priority = None
                                    self.vlan_range = YList()
                                    self.vlan_range.parent = self
                                    self.vlan_range.name = 'vlan_range'


                                class VlanRange(object):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.vlan_id_high = None
                                        self.vlan_id_low = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:vlan-range'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.vlan_id_high is not None:
                                            return True

                                        if self.vlan_id_low is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:tags-to-match'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ethertype is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.vlan_range is not None:
                                        for child_ref in self.vlan_range:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info']


                            class Pushe(object):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtypeEnum>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.vlan_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:pushe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ethertype is not None:
                                        return True

                                    if self.vlan_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:service-instance-details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.destination_mac_match is not None:
                                    return True

                                if self.is_exact_match is not None:
                                    return True

                                if self.is_native_preserving is not None:
                                    return True

                                if self.is_native_vlan is not None:
                                    return True

                                if self.local_traffic_stack is not None and self.local_traffic_stack._has_data():
                                    return True

                                if self.payload_ethertype is not None:
                                    return True

                                if self.pushe is not None:
                                    for child_ref in self.pushe:
                                        if child_ref._has_data():
                                            return True

                                if self.source_mac_match is not None:
                                    return True

                                if self.tags_popped is not None:
                                    return True

                                if self.tags_to_match is not None:
                                    for child_ref in self.tags_to_match:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.ServiceInstanceDetails']['meta_info']


                        class Dot1AdDot1QStack(object):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:dot1ad-dot1q-stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails.Dot1AdDot1QStack']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:encapsulation-details'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack._has_data():
                                return True

                            if self.dot1ad_native_tag is not None:
                                return True

                            if self.dot1ad_outer_tag is not None:
                                return True

                            if self.dot1ad_tag is not None:
                                return True

                            if self.native_tag is not None:
                                return True

                            if self.outer_tag is not None:
                                return True

                            if self.service_instance_details is not None and self.service_instance_details._has_data():
                                return True

                            if self.stack is not None and self.stack._has_data():
                                return True

                            if self.tag is not None:
                                return True

                            if self.vlan_encapsulation is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation.EncapsulationDetails']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:dot1q-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.encapsulation_details is not None and self.encapsulation_details._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1QInformation']['meta_info']


                class PppInformation(object):
                    """
                    PPP information
                    
                    .. attribute:: is_loopback_detected
                    
                    	Loopback detected
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_mp_bundle_member
                    
                    	MP Bundle Member
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_multilink_open
                    
                    	Is Multilink Open
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lcp_state
                    
                    	LCP State
                    	**type**\:   :py:class:`PppFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.PppFsmStateEnum>`
                    
                    .. attribute:: ncp_info_array
                    
                    	Array of per\-NCP data
                    	**type**\: list of    :py:class:`NcpInfoArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.is_loopback_detected = None
                        self.is_mp_bundle_member = None
                        self.is_multilink_open = None
                        self.keepalive_period = None
                        self.lcp_state = None
                        self.ncp_info_array = YList()
                        self.ncp_info_array.parent = self
                        self.ncp_info_array.name = 'ncp_info_array'


                    class NcpInfoArray(object):
                        """
                        Array of per\-NCP data
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP state identifier
                        	**type**\:   :py:class:`NcpIdentEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.NcpIdentEnum>`
                        
                        .. attribute:: ncp_state
                        
                        	NCP state value
                        	**type**\:   :py:class:`PppFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.PppFsmStateEnum>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.ncp_identifier = None
                            self.ncp_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ncp-info-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ncp_identifier is not None:
                                return True

                            if self.ncp_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ppp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.is_loopback_detected is not None:
                            return True

                        if self.is_mp_bundle_member is not None:
                            return True

                        if self.is_multilink_open is not None:
                            return True

                        if self.keepalive_period is not None:
                            return True

                        if self.lcp_state is not None:
                            return True

                        if self.ncp_info_array is not None:
                            for child_ref in self.ncp_info_array:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:encapsulation-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.dot1q_information is not None and self.dot1q_information._has_data():
                        return True

                    if self.encapsulation_type is not None:
                        return True

                    if self.frame_relay_information is not None and self.frame_relay_information._has_data():
                        return True

                    if self.ppp_information is not None and self.ppp_information._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation']['meta_info']


            class InterfaceTypeInformation(object):
                """
                Information specific to the interface type
                
                .. attribute:: bundle_information
                
                	Bundle interface information
                	**type**\:   :py:class:`BundleInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation>`
                
                .. attribute:: cem_information
                
                	Cem interface information
                	**type**\:   :py:class:`CemInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation>`
                
                .. attribute:: gcc_information
                
                	GCC interface information
                	**type**\:   :py:class:`GccInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation>`
                
                .. attribute:: interface_type_info
                
                	InterfaceTypeInfo
                	**type**\:   :py:class:`ImCmdIntfTypeEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdIntfTypeEnumEnum>`
                
                .. attribute:: pseudowire_head_end_information
                
                	PseudowireHeadEnd interface information
                	**type**\:   :py:class:`PseudowireHeadEndInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation>`
                
                .. attribute:: serial_information
                
                	Serial interface information
                	**type**\:   :py:class:`SerialInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation>`
                
                .. attribute:: sonet_pos_information
                
                	SONET POS interface information
                	**type**\:   :py:class:`SonetPosInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation>`
                
                .. attribute:: srp_information
                
                	SRP interface information
                	**type**\:   :py:class:`SrpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation>`
                
                .. attribute:: tunnel_gre_information
                
                	Tunnel GRE interface information
                	**type**\:   :py:class:`TunnelGreInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation>`
                
                .. attribute:: tunnel_information
                
                	Tunnel interface information
                	**type**\:   :py:class:`TunnelInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.bundle_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation()
                    self.bundle_information.parent = self
                    self.cem_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation()
                    self.cem_information.parent = self
                    self.gcc_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation()
                    self.gcc_information.parent = self
                    self.interface_type_info = None
                    self.pseudowire_head_end_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation()
                    self.pseudowire_head_end_information.parent = self
                    self.serial_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation()
                    self.serial_information.parent = self
                    self.sonet_pos_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation()
                    self.sonet_pos_information.parent = self
                    self.srp_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation()
                    self.srp_information.parent = self
                    self.tunnel_gre_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation()
                    self.tunnel_gre_information.parent = self
                    self.tunnel_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation()
                    self.tunnel_information.parent = self


                class SrpInformation(object):
                    """
                    SRP interface information
                    
                    .. attribute:: srp_information
                    
                    	SRP\-specific data
                    	**type**\:   :py:class:`SrpInformation_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_>`
                    
                    .. attribute:: srp_statistics
                    
                    	SRP\-specific packet and byte counters
                    	**type**\:   :py:class:`SrpStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.srp_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_()
                        self.srp_information.parent = self
                        self.srp_statistics = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics()
                        self.srp_statistics.parent = self


                    class SrpInformation_(object):
                        """
                        SRP\-specific data
                        
                        .. attribute:: ips_info
                        
                        	SRP IPS information
                        	**type**\:   :py:class:`IpsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo>`
                        
                        .. attribute:: rate_limit_info
                        
                        	SRP rate limit information
                        	**type**\:   :py:class:`RateLimitInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo>`
                        
                        .. attribute:: srr_info
                        
                        	SRP SRR information
                        	**type**\:   :py:class:`SrrInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo>`
                        
                        .. attribute:: topology_info
                        
                        	SRP topology information
                        	**type**\:   :py:class:`TopologyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.ips_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo()
                            self.ips_info.parent = self
                            self.rate_limit_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo()
                            self.rate_limit_info.parent = self
                            self.srr_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo()
                            self.srr_info.parent = self
                            self.topology_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo()
                            self.topology_info.parent = self


                        class IpsInfo(object):
                            """
                            SRP IPS information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_information
                            
                            	IPS information
                            	**type**\: list of    :py:class:`LocalInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.local_information = YList()
                                self.local_information.parent = self
                                self.local_information.name = 'local_information'


                            class LocalInformation(object):
                                """
                                IPS information
                                
                                .. attribute:: is_inter_card_bus_enabled
                                
                                	Inter card bus enabled
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: mac_address
                                
                                	MAC address for node
                                	**type**\:  str
                                
                                .. attribute:: side_a
                                
                                	Side A IPS details
                                	**type**\:   :py:class:`SideA <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA>`
                                
                                .. attribute:: side_b
                                
                                	Side B IPS details
                                	**type**\:   :py:class:`SideB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB>`
                                
                                .. attribute:: wtr_timer_period
                                
                                	IPS Wait To Restore period in seconds
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.is_inter_card_bus_enabled = None
                                    self.mac_address = None
                                    self.side_a = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA()
                                    self.side_a.parent = self
                                    self.side_b = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB()
                                    self.side_b.parent = self
                                    self.wtr_timer_period = None


                                class SideA(object):
                                    """
                                    Side A IPS details
                                    
                                    .. attribute:: asserted_failure
                                    
                                    	Failures presently asserted
                                    	**type**\: list of    :py:class:`AssertedFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA.AssertedFailure>`
                                    
                                    .. attribute:: delay_keep_alive_trigger
                                    
                                    	Number of milliseconds to wait after an L1 failure is detected before triggering an L2 wrap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\:  str
                                    
                                    .. attribute:: packet_sent_timer
                                    
                                    	SRP IPS packet send interval in seconds
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: remote_request
                                    
                                    	Remote Requests
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: rx_message_type
                                    
                                    	Type of message received
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: rx_neighbor_mac_address
                                    
                                    	Neighbour mac address for received message
                                    	**type**\:  str
                                    
                                    .. attribute:: rx_packet_test
                                    
                                    	Test for existence of an RX packet
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: rx_path_type
                                    
                                    	Short/long path for received message
                                    	**type**\:   :py:class:`SrpMgmtIpsPathIndEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathIndEnum>`
                                    
                                    .. attribute:: rx_ttl
                                    
                                    	Time to live for received message
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: self_detected_request
                                    
                                    	Self Detected Requests
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: send_timer_time_remaining
                                    
                                    	Time in seconds remaining until next send of an IPS request
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: tx_message_type
                                    
                                    	Type of message transmitted
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: tx_neighbor_mac_address
                                    
                                    	Mac address of node receiving TXed messages
                                    	**type**\:  str
                                    
                                    .. attribute:: tx_packet_test
                                    
                                    	Test for existence of a TX packet
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: tx_path_type
                                    
                                    	Short/long path of transmitted message
                                    	**type**\:   :py:class:`SrpMgmtIpsPathIndEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathIndEnum>`
                                    
                                    .. attribute:: tx_ttl
                                    
                                    	Time to live for transmitted message
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: wrap_state
                                    
                                    	Wrap state
                                    	**type**\:   :py:class:`SrpMgmtIpsWrapStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsWrapStateEnum>`
                                    
                                    .. attribute:: wtr_timer_remaining
                                    
                                    	Time in seconds until wrap removal
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.asserted_failure = YList()
                                        self.asserted_failure.parent = self
                                        self.asserted_failure.name = 'asserted_failure'
                                        self.delay_keep_alive_trigger = None
                                        self.mac_address = None
                                        self.packet_sent_timer = None
                                        self.remote_request = None
                                        self.rx_message_type = None
                                        self.rx_neighbor_mac_address = None
                                        self.rx_packet_test = None
                                        self.rx_path_type = None
                                        self.rx_ttl = None
                                        self.self_detected_request = None
                                        self.send_timer_time_remaining = None
                                        self.tx_message_type = None
                                        self.tx_neighbor_mac_address = None
                                        self.tx_packet_test = None
                                        self.tx_path_type = None
                                        self.tx_ttl = None
                                        self.wrap_state = None
                                        self.wtr_timer_remaining = None


                                    class AssertedFailure(object):
                                        """
                                        Failures presently asserted
                                        
                                        .. attribute:: current_state
                                        
                                        	Current state
                                        	**type**\:   :py:class:`SrpMgmtFailureStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEtEnum>`
                                        
                                        .. attribute:: debounced_delay
                                        
                                        	Debounce delay
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: debounced_state
                                        
                                        	Debounced state
                                        	**type**\:   :py:class:`SrpMgmtFailureStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEtEnum>`
                                        
                                        .. attribute:: reported_state
                                        
                                        	Reported state
                                        	**type**\:   :py:class:`SrpMgmtFailureStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEtEnum>`
                                        
                                        .. attribute:: stable_time
                                        
                                        	Stable time
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: type
                                        
                                        	Failure type
                                        	**type**\:   :py:class:`SrpMgmtFailureEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureEtEnum>`
                                        
                                        

                                        """

                                        _prefix = 'pfi-im-cmd-oper'
                                        _revision = '2016-12-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.current_state = None
                                            self.debounced_delay = None
                                            self.debounced_state = None
                                            self.reported_state = None
                                            self.stable_time = None
                                            self.type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:asserted-failure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.current_state is not None:
                                                return True

                                            if self.debounced_delay is not None:
                                                return True

                                            if self.debounced_state is not None:
                                                return True

                                            if self.reported_state is not None:
                                                return True

                                            if self.stable_time is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA.AssertedFailure']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-a'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.asserted_failure is not None:
                                            for child_ref in self.asserted_failure:
                                                if child_ref._has_data():
                                                    return True

                                        if self.delay_keep_alive_trigger is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.packet_sent_timer is not None:
                                            return True

                                        if self.remote_request is not None:
                                            return True

                                        if self.rx_message_type is not None:
                                            return True

                                        if self.rx_neighbor_mac_address is not None:
                                            return True

                                        if self.rx_packet_test is not None:
                                            return True

                                        if self.rx_path_type is not None:
                                            return True

                                        if self.rx_ttl is not None:
                                            return True

                                        if self.self_detected_request is not None:
                                            return True

                                        if self.send_timer_time_remaining is not None:
                                            return True

                                        if self.tx_message_type is not None:
                                            return True

                                        if self.tx_neighbor_mac_address is not None:
                                            return True

                                        if self.tx_packet_test is not None:
                                            return True

                                        if self.tx_path_type is not None:
                                            return True

                                        if self.tx_ttl is not None:
                                            return True

                                        if self.wrap_state is not None:
                                            return True

                                        if self.wtr_timer_remaining is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA']['meta_info']


                                class SideB(object):
                                    """
                                    Side B IPS details
                                    
                                    .. attribute:: asserted_failure
                                    
                                    	Failures presently asserted
                                    	**type**\: list of    :py:class:`AssertedFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB.AssertedFailure>`
                                    
                                    .. attribute:: delay_keep_alive_trigger
                                    
                                    	Number of milliseconds to wait after an L1 failure is detected before triggering an L2 wrap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\:  str
                                    
                                    .. attribute:: packet_sent_timer
                                    
                                    	SRP IPS packet send interval in seconds
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: remote_request
                                    
                                    	Remote Requests
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: rx_message_type
                                    
                                    	Type of message received
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: rx_neighbor_mac_address
                                    
                                    	Neighbour mac address for received message
                                    	**type**\:  str
                                    
                                    .. attribute:: rx_packet_test
                                    
                                    	Test for existence of an RX packet
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: rx_path_type
                                    
                                    	Short/long path for received message
                                    	**type**\:   :py:class:`SrpMgmtIpsPathIndEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathIndEnum>`
                                    
                                    .. attribute:: rx_ttl
                                    
                                    	Time to live for received message
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: self_detected_request
                                    
                                    	Self Detected Requests
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: send_timer_time_remaining
                                    
                                    	Time in seconds remaining until next send of an IPS request
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: tx_message_type
                                    
                                    	Type of message transmitted
                                    	**type**\:   :py:class:`SrpMgmtIpsReqEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReqEnum>`
                                    
                                    .. attribute:: tx_neighbor_mac_address
                                    
                                    	Mac address of node receiving TXed messages
                                    	**type**\:  str
                                    
                                    .. attribute:: tx_packet_test
                                    
                                    	Test for existence of a TX packet
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: tx_path_type
                                    
                                    	Short/long path of transmitted message
                                    	**type**\:   :py:class:`SrpMgmtIpsPathIndEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathIndEnum>`
                                    
                                    .. attribute:: tx_ttl
                                    
                                    	Time to live for transmitted message
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: wrap_state
                                    
                                    	Wrap state
                                    	**type**\:   :py:class:`SrpMgmtIpsWrapStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsWrapStateEnum>`
                                    
                                    .. attribute:: wtr_timer_remaining
                                    
                                    	Time in seconds until wrap removal
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.asserted_failure = YList()
                                        self.asserted_failure.parent = self
                                        self.asserted_failure.name = 'asserted_failure'
                                        self.delay_keep_alive_trigger = None
                                        self.mac_address = None
                                        self.packet_sent_timer = None
                                        self.remote_request = None
                                        self.rx_message_type = None
                                        self.rx_neighbor_mac_address = None
                                        self.rx_packet_test = None
                                        self.rx_path_type = None
                                        self.rx_ttl = None
                                        self.self_detected_request = None
                                        self.send_timer_time_remaining = None
                                        self.tx_message_type = None
                                        self.tx_neighbor_mac_address = None
                                        self.tx_packet_test = None
                                        self.tx_path_type = None
                                        self.tx_ttl = None
                                        self.wrap_state = None
                                        self.wtr_timer_remaining = None


                                    class AssertedFailure(object):
                                        """
                                        Failures presently asserted
                                        
                                        .. attribute:: current_state
                                        
                                        	Current state
                                        	**type**\:   :py:class:`SrpMgmtFailureStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEtEnum>`
                                        
                                        .. attribute:: debounced_delay
                                        
                                        	Debounce delay
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: debounced_state
                                        
                                        	Debounced state
                                        	**type**\:   :py:class:`SrpMgmtFailureStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEtEnum>`
                                        
                                        .. attribute:: reported_state
                                        
                                        	Reported state
                                        	**type**\:   :py:class:`SrpMgmtFailureStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEtEnum>`
                                        
                                        .. attribute:: stable_time
                                        
                                        	Stable time
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: type
                                        
                                        	Failure type
                                        	**type**\:   :py:class:`SrpMgmtFailureEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureEtEnum>`
                                        
                                        

                                        """

                                        _prefix = 'pfi-im-cmd-oper'
                                        _revision = '2016-12-18'

                                        def __init__(self):
                                            self.parent = None
                                            self.current_state = None
                                            self.debounced_delay = None
                                            self.debounced_state = None
                                            self.reported_state = None
                                            self.stable_time = None
                                            self.type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:asserted-failure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.current_state is not None:
                                                return True

                                            if self.debounced_delay is not None:
                                                return True

                                            if self.debounced_state is not None:
                                                return True

                                            if self.reported_state is not None:
                                                return True

                                            if self.stable_time is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB.AssertedFailure']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-b'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.asserted_failure is not None:
                                            for child_ref in self.asserted_failure:
                                                if child_ref._has_data():
                                                    return True

                                        if self.delay_keep_alive_trigger is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.packet_sent_timer is not None:
                                            return True

                                        if self.remote_request is not None:
                                            return True

                                        if self.rx_message_type is not None:
                                            return True

                                        if self.rx_neighbor_mac_address is not None:
                                            return True

                                        if self.rx_packet_test is not None:
                                            return True

                                        if self.rx_path_type is not None:
                                            return True

                                        if self.rx_ttl is not None:
                                            return True

                                        if self.self_detected_request is not None:
                                            return True

                                        if self.send_timer_time_remaining is not None:
                                            return True

                                        if self.tx_message_type is not None:
                                            return True

                                        if self.tx_neighbor_mac_address is not None:
                                            return True

                                        if self.tx_packet_test is not None:
                                            return True

                                        if self.tx_path_type is not None:
                                            return True

                                        if self.tx_ttl is not None:
                                            return True

                                        if self.wrap_state is not None:
                                            return True

                                        if self.wtr_timer_remaining is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_inter_card_bus_enabled is not None:
                                        return True

                                    if self.mac_address is not None:
                                        return True

                                    if self.side_a is not None and self.side_a._has_data():
                                        return True

                                    if self.side_b is not None and self.side_b._has_data():
                                        return True

                                    if self.wtr_timer_period is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ips-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_admin_down is not None:
                                    return True

                                if self.local_information is not None:
                                    for child_ref in self.local_information:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo']['meta_info']


                        class TopologyInfo(object):
                            """
                            SRP topology information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_information
                            
                            	Detailed SRP topology information
                            	**type**\: list of    :py:class:`LocalInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.local_information = YList()
                                self.local_information.parent = self
                                self.local_information.name = 'local_information'


                            class LocalInformation(object):
                                """
                                Detailed SRP topology information
                                
                                .. attribute:: next_topology_packet_delay
                                
                                	Time remaining until next topo pkt sent
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: number_of_nodes_on_ring
                                
                                	Number of nodes on ring
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: ring_node
                                
                                	List of nodes on the ring info
                                	**type**\: list of    :py:class:`RingNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation.RingNode>`
                                
                                .. attribute:: time_since_last_topology_change
                                
                                	Time since last topology change
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_since_last_topology_packet_received
                                
                                	Time since last topo pkt was received
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: topology_timer
                                
                                	How often a topology pkt is sent
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.next_topology_packet_delay = None
                                    self.number_of_nodes_on_ring = None
                                    self.ring_node = YList()
                                    self.ring_node.parent = self
                                    self.ring_node.name = 'ring_node'
                                    self.time_since_last_topology_change = None
                                    self.time_since_last_topology_packet_received = None
                                    self.topology_timer = None


                                class RingNode(object):
                                    """
                                    List of nodes on the ring info
                                    
                                    .. attribute:: hop_count
                                    
                                    	Outer\-ring hops to reach this node
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: is_srr_supported
                                    
                                    	SRR protocol supported
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: is_wrapped
                                    
                                    	Wrap state
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\:  str
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.hop_count = None
                                        self.ipv4_address = None
                                        self.is_srr_supported = None
                                        self.is_wrapped = None
                                        self.mac_address = None
                                        self.node_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ring-node'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.hop_count is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.is_srr_supported is not None:
                                            return True

                                        if self.is_wrapped is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.node_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation.RingNode']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.next_topology_packet_delay is not None:
                                        return True

                                    if self.number_of_nodes_on_ring is not None:
                                        return True

                                    if self.ring_node is not None:
                                        for child_ref in self.ring_node:
                                            if child_ref._has_data():
                                                return True

                                    if self.time_since_last_topology_change is not None:
                                        return True

                                    if self.time_since_last_topology_packet_received is not None:
                                        return True

                                    if self.topology_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:topology-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_admin_down is not None:
                                    return True

                                if self.local_information is not None:
                                    for child_ref in self.local_information:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo']['meta_info']


                        class SrrInfo(object):
                            """
                            SRP SRR information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_srr_enabled
                            
                            	SRR enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: srr_detailed_info
                            
                            	SRP information
                            	**type**\: list of    :py:class:`SrrDetailedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.is_srr_enabled = None
                                self.srr_detailed_info = YList()
                                self.srr_detailed_info.parent = self
                                self.srr_detailed_info.name = 'srr_detailed_info'


                            class SrrDetailedInfo(object):
                                """
                                SRP information
                                
                                .. attribute:: inner_fail_type
                                
                                	Inner fail type
                                	**type**\:   :py:class:`SrpMgmtSrrFailureEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailureEnum>`
                                
                                .. attribute:: is_announce
                                
                                	Is announcing enabled
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_inner_ring_in_use
                                
                                	 Is the inner ring in use
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_outer_ring_in_use
                                
                                	Is the outer ring in use
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_wrong_version_received
                                
                                	Wrong version recieved
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: last_wrong_version_receive_time
                                
                                	Time that last wrong version message recieved
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mac_address
                                
                                	SRR node mac address
                                	**type**\:  str
                                
                                .. attribute:: next_srr_packet_send_time
                                
                                	Time remaining in seconds to next SRR packet send
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: node_state
                                
                                	SRR node state
                                	**type**\:   :py:class:`SrpMgmtSrrNodeStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrNodeStateEnum>`
                                
                                .. attribute:: nodes_not_on_ring
                                
                                	nodes not in topology map
                                	**type**\: list of    :py:class:`NodesNotOnRing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesNotOnRing>`
                                
                                .. attribute:: nodes_on_ring
                                
                                	List of nodes on the ring info
                                	**type**\: list of    :py:class:`NodesOnRing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesOnRing>`
                                
                                .. attribute:: outer_fail_type
                                
                                	Outer fail type
                                	**type**\:   :py:class:`SrpMgmtSrrFailureEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailureEnum>`
                                
                                .. attribute:: packet_send_timer
                                
                                	SRR packet send timer interval in seconds
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: single_ring_bw
                                
                                	Single ring bandwidth Mbps
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: Mbit/s
                                
                                .. attribute:: version_number
                                
                                	Version number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wtr_time
                                
                                	SRR Wait To Restore interval delay in seconds
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: wtr_timer_remaining_inner_ring
                                
                                	Time remaining in seconds until next inner ring wrap removal
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: wtr_timer_remaining_outer_ring
                                
                                	Time remaining in seconds until next outer ring wrap removal
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.inner_fail_type = None
                                    self.is_announce = None
                                    self.is_inner_ring_in_use = None
                                    self.is_outer_ring_in_use = None
                                    self.is_wrong_version_received = None
                                    self.last_wrong_version_receive_time = None
                                    self.mac_address = None
                                    self.next_srr_packet_send_time = None
                                    self.node_state = None
                                    self.nodes_not_on_ring = YList()
                                    self.nodes_not_on_ring.parent = self
                                    self.nodes_not_on_ring.name = 'nodes_not_on_ring'
                                    self.nodes_on_ring = YList()
                                    self.nodes_on_ring.parent = self
                                    self.nodes_on_ring.name = 'nodes_on_ring'
                                    self.outer_fail_type = None
                                    self.packet_send_timer = None
                                    self.single_ring_bw = None
                                    self.version_number = None
                                    self.wtr_time = None
                                    self.wtr_timer_remaining_inner_ring = None
                                    self.wtr_timer_remaining_outer_ring = None


                                class NodesOnRing(object):
                                    """
                                    List of nodes on the ring info
                                    
                                    .. attribute:: inner_failure
                                    
                                    	Inner failure
                                    	**type**\:   :py:class:`SrpMgmtSrrFailureEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailureEnum>`
                                    
                                    .. attribute:: is_last_announce_received
                                    
                                    	Announce last received ?
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: last_announce_received_time
                                    
                                    	Announce last received
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mac_address
                                    
                                    	node mac address
                                    	**type**\:  str
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\:  str
                                    
                                    .. attribute:: outer_failure
                                    
                                    	Outer failure
                                    	**type**\:   :py:class:`SrpMgmtSrrFailureEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailureEnum>`
                                    
                                    .. attribute:: srr_entry_exits
                                    
                                    	Does the SRR information exist for this node
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.inner_failure = None
                                        self.is_last_announce_received = None
                                        self.last_announce_received_time = None
                                        self.mac_address = None
                                        self.node_name = None
                                        self.outer_failure = None
                                        self.srr_entry_exits = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:nodes-on-ring'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.inner_failure is not None:
                                            return True

                                        if self.is_last_announce_received is not None:
                                            return True

                                        if self.last_announce_received_time is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.node_name is not None:
                                            return True

                                        if self.outer_failure is not None:
                                            return True

                                        if self.srr_entry_exits is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesOnRing']['meta_info']


                                class NodesNotOnRing(object):
                                    """
                                    nodes not in topology map
                                    
                                    .. attribute:: inner_failure
                                    
                                    	Inner failure
                                    	**type**\:   :py:class:`SrpMgmtSrrFailureEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailureEnum>`
                                    
                                    .. attribute:: is_last_announce_received
                                    
                                    	Announce last received ?
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: last_announce_received_time
                                    
                                    	Announce last received
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mac_address
                                    
                                    	node mac address
                                    	**type**\:  str
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\:  str
                                    
                                    .. attribute:: outer_failure
                                    
                                    	Outer failure
                                    	**type**\:   :py:class:`SrpMgmtSrrFailureEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailureEnum>`
                                    
                                    .. attribute:: srr_entry_exits
                                    
                                    	Does the SRR information exist for this node
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2016-12-18'

                                    def __init__(self):
                                        self.parent = None
                                        self.inner_failure = None
                                        self.is_last_announce_received = None
                                        self.last_announce_received_time = None
                                        self.mac_address = None
                                        self.node_name = None
                                        self.outer_failure = None
                                        self.srr_entry_exits = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:nodes-not-on-ring'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.inner_failure is not None:
                                            return True

                                        if self.is_last_announce_received is not None:
                                            return True

                                        if self.last_announce_received_time is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.node_name is not None:
                                            return True

                                        if self.outer_failure is not None:
                                            return True

                                        if self.srr_entry_exits is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesNotOnRing']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srr-detailed-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.inner_fail_type is not None:
                                        return True

                                    if self.is_announce is not None:
                                        return True

                                    if self.is_inner_ring_in_use is not None:
                                        return True

                                    if self.is_outer_ring_in_use is not None:
                                        return True

                                    if self.is_wrong_version_received is not None:
                                        return True

                                    if self.last_wrong_version_receive_time is not None:
                                        return True

                                    if self.mac_address is not None:
                                        return True

                                    if self.next_srr_packet_send_time is not None:
                                        return True

                                    if self.node_state is not None:
                                        return True

                                    if self.nodes_not_on_ring is not None:
                                        for child_ref in self.nodes_not_on_ring:
                                            if child_ref._has_data():
                                                return True

                                    if self.nodes_on_ring is not None:
                                        for child_ref in self.nodes_on_ring:
                                            if child_ref._has_data():
                                                return True

                                    if self.outer_fail_type is not None:
                                        return True

                                    if self.packet_send_timer is not None:
                                        return True

                                    if self.single_ring_bw is not None:
                                        return True

                                    if self.version_number is not None:
                                        return True

                                    if self.wtr_time is not None:
                                        return True

                                    if self.wtr_timer_remaining_inner_ring is not None:
                                        return True

                                    if self.wtr_timer_remaining_outer_ring is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srr-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_admin_down is not None:
                                    return True

                                if self.is_srr_enabled is not None:
                                    return True

                                if self.srr_detailed_info is not None:
                                    for child_ref in self.srr_detailed_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo']['meta_info']


                        class RateLimitInfo(object):
                            """
                            SRP rate limit information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate_limit_detailed_info
                            
                            	SRP rate limit information
                            	**type**\: list of    :py:class:`RateLimitDetailedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo.RateLimitDetailedInfo>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.rate_limit_detailed_info = YList()
                                self.rate_limit_detailed_info.parent = self
                                self.rate_limit_detailed_info.name = 'rate_limit_detailed_info'


                            class RateLimitDetailedInfo(object):
                                """
                                SRP rate limit information
                                
                                .. attribute:: min_priority_value
                                
                                	Minimum SRP priority for high\-priority transmit queue
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.min_priority_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:rate-limit-detailed-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.min_priority_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo.RateLimitDetailedInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:rate-limit-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_admin_down is not None:
                                    return True

                                if self.rate_limit_detailed_info is not None:
                                    for child_ref in self.rate_limit_detailed_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srp-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ips_info is not None and self.ips_info._has_data():
                                return True

                            if self.rate_limit_info is not None and self.rate_limit_info._has_data():
                                return True

                            if self.srr_info is not None and self.srr_info._has_data():
                                return True

                            if self.topology_info is not None and self.topology_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_']['meta_info']


                    class SrpStatistics(object):
                        """
                        SRP\-specific packet and byte counters
                        
                        .. attribute:: data_rate_interval
                        
                        	Data rate interval (5 mins or 30 seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: side_a_data_rate
                        
                        	Data rates for side A interface
                        	**type**\:   :py:class:`SideADataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate>`
                        
                        .. attribute:: side_a_errors
                        
                        	Errors for side A interface
                        	**type**\:   :py:class:`SideAErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors>`
                        
                        .. attribute:: side_b_data_rate
                        
                        	Data rates for side B interface
                        	**type**\:   :py:class:`SideBDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate>`
                        
                        .. attribute:: side_b_errors
                        
                        	Errors for side B interface
                        	**type**\:   :py:class:`SideBErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.data_rate_interval = None
                            self.side_a_data_rate = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate()
                            self.side_a_data_rate.parent = self
                            self.side_a_errors = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors()
                            self.side_a_errors.parent = self
                            self.side_b_data_rate = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate()
                            self.side_b_data_rate.parent = self
                            self.side_b_errors = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors()
                            self.side_b_errors.parent = self


                        class SideADataRate(object):
                            """
                            Data rates for side A interface
                            
                            .. attribute:: bit_rate_received
                            
                            	Received bit rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bit_rate_sent
                            
                            	Sent bit rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_received
                            
                            	Received packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_sent
                            
                            	Sent packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.bit_rate_received = None
                                self.bit_rate_sent = None
                                self.packet_rate_received = None
                                self.packet_rate_sent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-a-data-rate'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bit_rate_received is not None:
                                    return True

                                if self.bit_rate_sent is not None:
                                    return True

                                if self.packet_rate_received is not None:
                                    return True

                                if self.packet_rate_sent is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate']['meta_info']


                        class SideBDataRate(object):
                            """
                            Data rates for side B interface
                            
                            .. attribute:: bit_rate_received
                            
                            	Received bit rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bit_rate_sent
                            
                            	Sent bit rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_received
                            
                            	Received packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_sent
                            
                            	Sent packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.bit_rate_received = None
                                self.bit_rate_sent = None
                                self.packet_rate_received = None
                                self.packet_rate_sent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-b-data-rate'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bit_rate_received is not None:
                                    return True

                                if self.bit_rate_sent is not None:
                                    return True

                                if self.packet_rate_received is not None:
                                    return True

                                if self.packet_rate_sent is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate']['meta_info']


                        class SideAErrors(object):
                            """
                            Errors for side A interface
                            
                            .. attribute:: crc_errors
                            
                            	Input CRC errors
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error_packets_received
                            
                            	Error packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_aborts_received
                            
                            	Aborts received at framer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_giant_packets_received
                            
                            	Too large packets received at framer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_runt_packets_received
                            
                            	Too small packets received at framer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_insufficient_resource_events
                            
                            	Input insufficient resources events
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_aborts_received
                            
                            	Aborts received at MAC/RAC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_giant_packets_received
                            
                            	Too large packets received at MAC/RAC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_runt_packets_received
                            
                            	Too small packets received at MAC/RAC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.crc_errors = None
                                self.error_packets_received = None
                                self.framer_aborts_received = None
                                self.framer_giant_packets_received = None
                                self.framer_runt_packets_received = None
                                self.input_insufficient_resource_events = None
                                self.mac_aborts_received = None
                                self.mac_giant_packets_received = None
                                self.mac_runt_packets_received = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-a-errors'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.crc_errors is not None:
                                    return True

                                if self.error_packets_received is not None:
                                    return True

                                if self.framer_aborts_received is not None:
                                    return True

                                if self.framer_giant_packets_received is not None:
                                    return True

                                if self.framer_runt_packets_received is not None:
                                    return True

                                if self.input_insufficient_resource_events is not None:
                                    return True

                                if self.mac_aborts_received is not None:
                                    return True

                                if self.mac_giant_packets_received is not None:
                                    return True

                                if self.mac_runt_packets_received is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors']['meta_info']


                        class SideBErrors(object):
                            """
                            Errors for side B interface
                            
                            .. attribute:: crc_errors
                            
                            	Input CRC errors
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error_packets_received
                            
                            	Error packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_aborts_received
                            
                            	Aborts received at framer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_giant_packets_received
                            
                            	Too large packets received at framer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_runt_packets_received
                            
                            	Too small packets received at framer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_insufficient_resource_events
                            
                            	Input insufficient resources events
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_aborts_received
                            
                            	Aborts received at MAC/RAC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_giant_packets_received
                            
                            	Too large packets received at MAC/RAC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_runt_packets_received
                            
                            	Too small packets received at MAC/RAC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.crc_errors = None
                                self.error_packets_received = None
                                self.framer_aborts_received = None
                                self.framer_giant_packets_received = None
                                self.framer_runt_packets_received = None
                                self.input_insufficient_resource_events = None
                                self.mac_aborts_received = None
                                self.mac_giant_packets_received = None
                                self.mac_runt_packets_received = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-b-errors'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.crc_errors is not None:
                                    return True

                                if self.error_packets_received is not None:
                                    return True

                                if self.framer_aborts_received is not None:
                                    return True

                                if self.framer_giant_packets_received is not None:
                                    return True

                                if self.framer_runt_packets_received is not None:
                                    return True

                                if self.input_insufficient_resource_events is not None:
                                    return True

                                if self.mac_aborts_received is not None:
                                    return True

                                if self.mac_giant_packets_received is not None:
                                    return True

                                if self.mac_runt_packets_received is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srp-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.data_rate_interval is not None:
                                return True

                            if self.side_a_data_rate is not None and self.side_a_data_rate._has_data():
                                return True

                            if self.side_a_errors is not None and self.side_a_errors._has_data():
                                return True

                            if self.side_b_data_rate is not None and self.side_b_data_rate._has_data():
                                return True

                            if self.side_b_errors is not None and self.side_b_errors._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.srp_information is not None and self.srp_information._has_data():
                            return True

                        if self.srp_statistics is not None and self.srp_statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation']['meta_info']


                class TunnelInformation(object):
                    """
                    Tunnel interface information
                    
                    .. attribute:: destination_ipv4_address
                    
                    	Tunnel destination IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: key
                    
                    	GRE tunnel key
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_ipv4_address
                    
                    	Tunnel source IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: source_name
                    
                    	Tunnel source name
                    	**type**\:  str
                    
                    .. attribute:: ttl
                    
                    	GRE tunnel TTL
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tunnel_type
                    
                    	Tunnel protocol/transport
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.destination_ipv4_address = None
                        self.key = None
                        self.source_ipv4_address = None
                        self.source_name = None
                        self.ttl = None
                        self.tunnel_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:tunnel-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_ipv4_address is not None:
                            return True

                        if self.key is not None:
                            return True

                        if self.source_ipv4_address is not None:
                            return True

                        if self.source_name is not None:
                            return True

                        if self.ttl is not None:
                            return True

                        if self.tunnel_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation']['meta_info']


                class BundleInformation(object):
                    """
                    Bundle interface information
                    
                    .. attribute:: member
                    
                    	List of bundle members and their properties
                    	**type**\: list of    :py:class:`Member <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'


                    class Member(object):
                        """
                        List of bundle members and their properties
                        
                        .. attribute:: bandwidth
                        
                        	Bandwidth of this member (kbps)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: counters
                        
                        	Counters data about member link
                        	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters>`
                        
                        .. attribute:: iccp_node
                        
                        	Location of member
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name
                        
                        	Member's interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: link_data
                        
                        	Lacp data about member link
                        	**type**\:   :py:class:`LinkData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData>`
                        
                        .. attribute:: link_order_number
                        
                        	Member's link order number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac_address
                        
                        	MAC address of this member (deprecated)
                        	**type**\:   :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress>`
                        
                        .. attribute:: member_mux_data
                        
                        	Mux state machine data
                        	**type**\:   :py:class:`MemberMuxData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData>`
                        
                        .. attribute:: member_name
                        
                        	Member's (short form) name
                        	**type**\:  str
                        
                        .. attribute:: member_type
                        
                        	Member's type (local/foreign)
                        	**type**\:   :py:class:`BmdMemberTypeEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmdMemberTypeEnumEnum>`
                        
                        .. attribute:: port_number
                        
                        	Member's link number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: port_priority
                        
                        	The priority of this member
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: underlying_link_id
                        
                        	Member's underlying link ID
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.bandwidth = None
                            self.counters = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters()
                            self.counters.parent = self
                            self.iccp_node = None
                            self.interface_name = None
                            self.link_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData()
                            self.link_data.parent = self
                            self.link_order_number = None
                            self.mac_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress()
                            self.mac_address.parent = self
                            self.member_mux_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData()
                            self.member_mux_data.parent = self
                            self.member_name = None
                            self.member_type = None
                            self.port_number = None
                            self.port_priority = None
                            self.underlying_link_id = None


                        class Counters(object):
                            """
                            Counters data about member link
                            
                            .. attribute:: defaulted
                            
                            	State flag set to Defaulted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excess_lacpd_us_received
                            
                            	LACPDUs received that exceed the rate limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excess_marker_packets_received
                            
                            	Marker packets received that exceed the rate limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: expired
                            
                            	State flag set to Expired
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: illegal_packets_received
                            
                            	Illegal and unknown packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lacpd_us_received
                            
                            	LACPDUs received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lacpd_us_transmitted
                            
                            	LACPDUs transmitted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: last_cleared_nsec
                            
                            	Last time counters cleared (nsec) (deprecated)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: last_cleared_sec
                            
                            	Last time counters cleared (s) (deprecated)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: marker_packets_received
                            
                            	Marker packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: marker_responses_transmitted
                            
                            	Marker response packets transmitted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.defaulted = None
                                self.excess_lacpd_us_received = None
                                self.excess_marker_packets_received = None
                                self.expired = None
                                self.illegal_packets_received = None
                                self.lacpd_us_received = None
                                self.lacpd_us_transmitted = None
                                self.last_cleared_nsec = None
                                self.last_cleared_sec = None
                                self.marker_packets_received = None
                                self.marker_responses_transmitted = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:counters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.defaulted is not None:
                                    return True

                                if self.excess_lacpd_us_received is not None:
                                    return True

                                if self.excess_marker_packets_received is not None:
                                    return True

                                if self.expired is not None:
                                    return True

                                if self.illegal_packets_received is not None:
                                    return True

                                if self.lacpd_us_received is not None:
                                    return True

                                if self.lacpd_us_transmitted is not None:
                                    return True

                                if self.last_cleared_nsec is not None:
                                    return True

                                if self.last_cleared_sec is not None:
                                    return True

                                if self.marker_packets_received is not None:
                                    return True

                                if self.marker_responses_transmitted is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters']['meta_info']


                        class LinkData(object):
                            """
                            Lacp data about member link
                            
                            .. attribute:: actor_operational_key
                            
                            	Operational key for this port
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: actor_port_id
                            
                            	Port number of this port
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: actor_port_priority
                            
                            	Priority of this port
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: actor_port_state
                            
                            	LACP state of this port
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: actor_system_mac_address
                            
                            	MAC Address of the actor system
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: actor_system_priority
                            
                            	System priority of actor system
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: attached_aggregator_id
                            
                            	MIB ifindex of attached bundle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_handle
                            
                            	Member's interface handle
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: partner_operational_key
                            
                            	Operational key for partner port
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_port_id
                            
                            	Port number of the partner's port
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_port_priority
                            
                            	Priority of the partner's port
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_port_state
                            
                            	LACP state of the partner's port
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: partner_system_mac_address
                            
                            	MAC Address used to identify the partner system
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: partner_system_priority
                            
                            	System priority of partner system
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: selected_aggregator_id
                            
                            	MIB ifindex of selected bundle
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.actor_operational_key = None
                                self.actor_port_id = None
                                self.actor_port_priority = None
                                self.actor_port_state = None
                                self.actor_system_mac_address = None
                                self.actor_system_priority = None
                                self.attached_aggregator_id = None
                                self.interface_handle = None
                                self.partner_operational_key = None
                                self.partner_port_id = None
                                self.partner_port_priority = None
                                self.partner_port_state = None
                                self.partner_system_mac_address = None
                                self.partner_system_priority = None
                                self.selected_aggregator_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:link-data'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.actor_operational_key is not None:
                                    return True

                                if self.actor_port_id is not None:
                                    return True

                                if self.actor_port_priority is not None:
                                    return True

                                if self.actor_port_state is not None:
                                    return True

                                if self.actor_system_mac_address is not None:
                                    return True

                                if self.actor_system_priority is not None:
                                    return True

                                if self.attached_aggregator_id is not None:
                                    return True

                                if self.interface_handle is not None:
                                    return True

                                if self.partner_operational_key is not None:
                                    return True

                                if self.partner_port_id is not None:
                                    return True

                                if self.partner_port_priority is not None:
                                    return True

                                if self.partner_port_state is not None:
                                    return True

                                if self.partner_system_mac_address is not None:
                                    return True

                                if self.partner_system_priority is not None:
                                    return True

                                if self.selected_aggregator_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData']['meta_info']


                        class MemberMuxData(object):
                            """
                            Mux state machine data
                            
                            .. attribute:: error
                            
                            	Internal value indicating if an error occurred trying to put a link into the desired state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: member_mux_state_reason
                            
                            	Reason for last Mux state change
                            	**type**\:   :py:class:`BmMbrStateReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmMbrStateReasonEnum>`
                            
                            .. attribute:: member_mux_state_reason_data
                            
                            	Data regarding the reason for last Mux state change
                            	**type**\:   :py:class:`MemberMuxStateReasonData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData>`
                            
                            .. attribute:: member_state
                            
                            	Current internal state of this bundle member
                            	**type**\:   :py:class:`BmdMemberStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmdMemberStateEnum>`
                            
                            .. attribute:: mux_state
                            
                            	Current state of this bundle member
                            	**type**\:   :py:class:`BmMuxstateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmMuxstateEnum>`
                            
                            .. attribute:: mux_state_reason
                            
                            	Reason for last Mux state change (Deprecated)
                            	**type**\:   :py:class:`BmMuxreasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmMuxreasonEnum>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.error = None
                                self.member_mux_state_reason = None
                                self.member_mux_state_reason_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData()
                                self.member_mux_state_reason_data.parent = self
                                self.member_state = None
                                self.mux_state = None
                                self.mux_state_reason = None


                            class MemberMuxStateReasonData(object):
                                """
                                Data regarding the reason for last Mux state
                                change
                                
                                .. attribute:: reason_type
                                
                                	The item the reason applies to
                                	**type**\:   :py:class:`BmStateReasonTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmStateReasonTargetEnum>`
                                
                                .. attribute:: severity
                                
                                	The severity of the reason
                                	**type**\:   :py:class:`BmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmSeverityEnum>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2016-12-18'

                                def __init__(self):
                                    self.parent = None
                                    self.reason_type = None
                                    self.severity = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:member-mux-state-reason-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.reason_type is not None:
                                        return True

                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:member-mux-data'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.error is not None:
                                    return True

                                if self.member_mux_state_reason is not None:
                                    return True

                                if self.member_mux_state_reason_data is not None and self.member_mux_state_reason_data._has_data():
                                    return True

                                if self.member_state is not None:
                                    return True

                                if self.mux_state is not None:
                                    return True

                                if self.mux_state_reason is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData']['meta_info']


                        class MacAddress(object):
                            """
                            MAC address of this member (deprecated)
                            
                            .. attribute:: address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2016-12-18'

                            def __init__(self):
                                self.parent = None
                                self.address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:mac-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:member'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bandwidth is not None:
                                return True

                            if self.counters is not None and self.counters._has_data():
                                return True

                            if self.iccp_node is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.link_data is not None and self.link_data._has_data():
                                return True

                            if self.link_order_number is not None:
                                return True

                            if self.mac_address is not None and self.mac_address._has_data():
                                return True

                            if self.member_mux_data is not None and self.member_mux_data._has_data():
                                return True

                            if self.member_name is not None:
                                return True

                            if self.member_type is not None:
                                return True

                            if self.port_number is not None:
                                return True

                            if self.port_priority is not None:
                                return True

                            if self.underlying_link_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:bundle-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation']['meta_info']


                class SerialInformation(object):
                    """
                    Serial interface information
                    
                    .. attribute:: timeslots
                    
                    	Timeslots separated by \: or \- from 1 to 31. \: indicates individual timeslot and \- represents a range. E.g. 1\-3\:5 represents timeslots 1, 2, 3, and 5
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.timeslots = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:serial-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.timeslots is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation']['meta_info']


                class SonetPosInformation(object):
                    """
                    SONET POS interface information
                    
                    .. attribute:: aps_state
                    
                    	APS state
                    	**type**\:   :py:class:`SonetApsEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SonetApsEtEnum>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.aps_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:sonet-pos-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.aps_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation']['meta_info']


                class TunnelGreInformation(object):
                    """
                    Tunnel GRE interface information
                    
                    .. attribute:: destination_ip_address
                    
                    	Tunnel destination IP address
                    	**type**\:   :py:class:`DestinationIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress>`
                    
                    .. attribute:: destination_ip_address_length
                    
                    	Tunnel destination IP address length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: df_bit_state
                    
                    	DF Bit State
                    	**type**\:   :py:class:`TunnelKaDfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKaDfStateEnum>`
                    
                    .. attribute:: keepalive_maximum_retry
                    
                    	Keepalive retry
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive period in seconds
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: second
                    
                    .. attribute:: keepalive_state
                    
                    	Keepalive State
                    	**type**\:   :py:class:`TunnelKaDfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKaDfStateEnum>`
                    
                    .. attribute:: key
                    
                    	Key value for GRE Packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: key_bit_state
                    
                    	Key Config State
                    	**type**\:   :py:class:`TunnelKeyStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKeyStateEnum>`
                    
                    .. attribute:: source_ip_address
                    
                    	Tunnel source IP address
                    	**type**\:   :py:class:`SourceIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress>`
                    
                    .. attribute:: source_name
                    
                    	Tunnel source name
                    	**type**\:  str
                    
                    .. attribute:: tunnel_mode
                    
                    	Tunnel GRE Mode
                    	**type**\:   :py:class:`TunnelGreModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelGreModeEnum>`
                    
                    .. attribute:: tunnel_mode_decap
                    
                    	Tunnel Mode Decap
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tunnel_tos
                    
                    	GRE tunnel TOS
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tunnel_ttl
                    
                    	GRE tunnel TTL
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.destination_ip_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress()
                        self.destination_ip_address.parent = self
                        self.destination_ip_address_length = None
                        self.df_bit_state = None
                        self.keepalive_maximum_retry = None
                        self.keepalive_period = None
                        self.keepalive_state = None
                        self.key = None
                        self.key_bit_state = None
                        self.source_ip_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress()
                        self.source_ip_address.parent = self
                        self.source_name = None
                        self.tunnel_mode = None
                        self.tunnel_mode_decap = None
                        self.tunnel_tos = None
                        self.tunnel_ttl = None


                    class SourceIpAddress(object):
                        """
                        Tunnel source IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:   :py:class:`TunlPfiAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunlPfiAfIdEnum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.afi = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:source-ip-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.afi is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress']['meta_info']


                    class DestinationIpAddress(object):
                        """
                        Tunnel destination IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:   :py:class:`TunlPfiAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunlPfiAfIdEnum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.afi = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:destination-ip-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.afi is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:tunnel-gre-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_ip_address is not None and self.destination_ip_address._has_data():
                            return True

                        if self.destination_ip_address_length is not None:
                            return True

                        if self.df_bit_state is not None:
                            return True

                        if self.keepalive_maximum_retry is not None:
                            return True

                        if self.keepalive_period is not None:
                            return True

                        if self.keepalive_state is not None:
                            return True

                        if self.key is not None:
                            return True

                        if self.key_bit_state is not None:
                            return True

                        if self.source_ip_address is not None and self.source_ip_address._has_data():
                            return True

                        if self.source_name is not None:
                            return True

                        if self.tunnel_mode is not None:
                            return True

                        if self.tunnel_mode_decap is not None:
                            return True

                        if self.tunnel_tos is not None:
                            return True

                        if self.tunnel_ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation']['meta_info']


                class PseudowireHeadEndInformation(object):
                    """
                    PseudowireHeadEnd interface information
                    
                    .. attribute:: interface_list_name
                    
                    	Interface list Name
                    	**type**\:  str
                    
                    .. attribute:: internal_label
                    
                    	Internal Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2_overhead
                    
                    	L2 Overhead
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.interface_list_name = None
                        self.internal_label = None
                        self.l2_overhead = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:pseudowire-head-end-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_list_name is not None:
                            return True

                        if self.internal_label is not None:
                            return True

                        if self.l2_overhead is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation']['meta_info']


                class CemInformation(object):
                    """
                    Cem interface information
                    
                    .. attribute:: dejitter_buffer
                    
                    	Dejitter buffer length configuredin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: millisecond
                    
                    .. attribute:: framing
                    
                    	 If framing is TRUE then the CEM  interface is structure aware ; otherwise it is structure agnostic
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: payload
                    
                    	Payload size in bytes configured on CEM interface
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: timeslots
                    
                    	Timeslots separated by \: or \- from 1 to 32. \: indicates individual timeslot and \- represents a range. E.g. 1\-3\:5 represents timeslots 1, 2, 3, and 5
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.dejitter_buffer = None
                        self.framing = None
                        self.payload = None
                        self.timeslots = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:cem-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dejitter_buffer is not None:
                            return True

                        if self.framing is not None:
                            return True

                        if self.payload is not None:
                            return True

                        if self.timeslots is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation']['meta_info']


                class GccInformation(object):
                    """
                    GCC interface information
                    
                    .. attribute:: derived_mode
                    
                    	Derived State
                    	**type**\:   :py:class:`GccDerStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.GccDerStateEnum>`
                    
                    .. attribute:: sec_state
                    
                    	Sec State 
                    	**type**\:   :py:class:`GccSecStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.GccSecStateEnum>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.derived_mode = None
                        self.sec_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:gcc-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.derived_mode is not None:
                            return True

                        if self.sec_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bundle_information is not None and self.bundle_information._has_data():
                        return True

                    if self.cem_information is not None and self.cem_information._has_data():
                        return True

                    if self.gcc_information is not None and self.gcc_information._has_data():
                        return True

                    if self.interface_type_info is not None:
                        return True

                    if self.pseudowire_head_end_information is not None and self.pseudowire_head_end_information._has_data():
                        return True

                    if self.serial_information is not None and self.serial_information._has_data():
                        return True

                    if self.sonet_pos_information is not None and self.sonet_pos_information._has_data():
                        return True

                    if self.srp_information is not None and self.srp_information._has_data():
                        return True

                    if self.tunnel_gre_information is not None and self.tunnel_gre_information._has_data():
                        return True

                    if self.tunnel_information is not None and self.tunnel_information._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation']['meta_info']


            class DataRates(object):
                """
                Packet and byte rates
                
                .. attribute:: bandwidth
                
                	Bandwidth (in kbps)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: kbit/s
                
                .. attribute:: input_data_rate
                
                	Input data rate in 1000's of bps
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: input_load
                
                	Input load as fraction of 255
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: input_packet_rate
                
                	Input packets per second
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: load_interval
                
                	Number of 30\-sec intervals less one
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_data_rate
                
                	Output data rate in 1000's of bps
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: output_load
                
                	Output load as fraction of 255
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: output_packet_rate
                
                	Output packets per second
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: peak_input_data_rate
                
                	Peak input data rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_packet_rate
                
                	Peak input packet rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_data_rate
                
                	Peak output data rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_packet_rate
                
                	Peak output packet rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reliability
                
                	Reliability coefficient
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.bandwidth = None
                    self.input_data_rate = None
                    self.input_load = None
                    self.input_packet_rate = None
                    self.load_interval = None
                    self.output_data_rate = None
                    self.output_load = None
                    self.output_packet_rate = None
                    self.peak_input_data_rate = None
                    self.peak_input_packet_rate = None
                    self.peak_output_data_rate = None
                    self.peak_output_packet_rate = None
                    self.reliability = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:data-rates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bandwidth is not None:
                        return True

                    if self.input_data_rate is not None:
                        return True

                    if self.input_load is not None:
                        return True

                    if self.input_packet_rate is not None:
                        return True

                    if self.load_interval is not None:
                        return True

                    if self.output_data_rate is not None:
                        return True

                    if self.output_load is not None:
                        return True

                    if self.output_packet_rate is not None:
                        return True

                    if self.peak_input_data_rate is not None:
                        return True

                    if self.peak_input_packet_rate is not None:
                        return True

                    if self.peak_output_data_rate is not None:
                        return True

                    if self.peak_output_packet_rate is not None:
                        return True

                    if self.reliability is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.DataRates']['meta_info']


            class InterfaceStatistics(object):
                """
                Packet, byte and error counters
                
                .. attribute:: basic_interface_stats
                
                	Packet, byte and selected error counters
                	**type**\:   :py:class:`BasicInterfaceStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats>`
                
                .. attribute:: full_interface_stats
                
                	Packet, byte and all error counters
                	**type**\:   :py:class:`FullInterfaceStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats>`
                
                .. attribute:: stats_type
                
                	StatsType
                	**type**\:   :py:class:`ImCmdStatsEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdStatsEnumEnum>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.basic_interface_stats = Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats()
                    self.basic_interface_stats.parent = self
                    self.full_interface_stats = Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats()
                    self.full_interface_stats.parent = self
                    self.stats_type = None


                class FullInterfaceStats(object):
                    """
                    Packet, byte and all error counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:full-interface-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats']['meta_info']


                class BasicInterfaceStats(object):
                    """
                    Packet, byte and selected error counters
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:basic-interface-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.basic_interface_stats is not None and self.basic_interface_stats._has_data():
                        return True

                    if self.full_interface_stats is not None and self.full_interface_stats._has_data():
                        return True

                    if self.stats_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceStatistics']['meta_info']


            class L2InterfaceStatistics(object):
                """
                L2 Protocol Statistics
                
                .. attribute:: block_array
                
                	Block Array
                	**type**\: list of    :py:class:`BlockArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray>`
                
                .. attribute:: contents
                
                	Bag contents
                	**type**\:   :py:class:`StatsTypeContentsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsTypeContentsEnum>`
                
                .. attribute:: element_array
                
                	Element Array
                	**type**\: list of    :py:class:`ElementArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray>`
                
                .. attribute:: stats_id
                
                	Identifier
                	**type**\:   :py:class:`StatsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId>`
                
                .. attribute:: stats_type
                
                	Stats type value
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.block_array = YList()
                    self.block_array.parent = self
                    self.block_array.name = 'block_array'
                    self.contents = None
                    self.element_array = YList()
                    self.element_array.parent = self
                    self.element_array.name = 'element_array'
                    self.stats_id = Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId()
                    self.stats_id.parent = self
                    self.stats_type = None


                class StatsId(object):
                    """
                    Identifier
                    
                    .. attribute:: feature_id
                    
                    	Feature ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: id
                    
                    	ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: id_type
                    
                    	id type
                    	**type**\:   :py:class:`StatsIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsIdEnum>`
                    
                    .. attribute:: interface_handle
                    
                    	Interface Handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: node_id
                    
                    	Node ID
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: unused
                    
                    	Unused
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.feature_id = None
                        self.id = None
                        self.id_type = None
                        self.interface_handle = None
                        self.node_id = None
                        self.unused = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:stats-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.feature_id is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.id_type is not None:
                            return True

                        if self.interface_handle is not None:
                            return True

                        if self.node_id is not None:
                            return True

                        if self.unused is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId']['meta_info']


                class BlockArray(object):
                    """
                    Block Array
                    
                    .. attribute:: count
                    
                    	count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: type
                    
                    	type
                    	**type**\:   :py:class:`StatsCounterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsCounterEnum>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.count = None
                        self.data = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:block-array'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            return True

                        if self.data is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray']['meta_info']


                class ElementArray(object):
                    """
                    Element Array
                    
                    .. attribute:: block_array
                    
                    	block array
                    	**type**\: list of    :py:class:`BlockArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray>`
                    
                    .. attribute:: key
                    
                    	key
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.block_array = YList()
                        self.block_array.parent = self
                        self.block_array.name = 'block_array'
                        self.key = None


                    class BlockArray(object):
                        """
                        block array
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: data
                        
                        	data
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\:   :py:class:`StatsCounterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsCounterEnum>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.count = None
                            self.data = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:block-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.count is not None:
                                return True

                            if self.data is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:element-array'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.block_array is not None:
                            for child_ref in self.block_array:
                                if child_ref._has_data():
                                    return True

                        if self.key is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:l2-interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.block_array is not None:
                        for child_ref in self.block_array:
                            if child_ref._has_data():
                                return True

                    if self.contents is not None:
                        return True

                    if self.element_array is not None:
                        for child_ref in self.element_array:
                            if child_ref._has_data():
                                return True

                    if self.stats_id is not None and self.stats_id._has_data():
                        return True

                    if self.stats_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics']['meta_info']


            class NvOptical(object):
                """
                nV Optical Controller Information
                
                .. attribute:: controller
                
                	Controller that nV controller maps to
                	**type**\:  str
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.controller = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:nv-optical'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.controller is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.NvOptical']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-xr/Cisco-IOS-XR-pfi-im-cmd-oper:interface[Cisco-IOS-XR-pfi-im-cmd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.arp_information is not None and self.arp_information._has_data():
                    return True

                if self.bandwidth is not None:
                    return True

                if self.burned_in_address is not None and self.burned_in_address._has_data():
                    return True

                if self.carrier_delay is not None and self.carrier_delay._has_data():
                    return True

                if self.crc_length is not None:
                    return True

                if self.dampening_information is not None and self.dampening_information._has_data():
                    return True

                if self.data_rates is not None and self.data_rates._has_data():
                    return True

                if self.description is not None:
                    return True

                if self.duplexity is not None:
                    return True

                if self.encapsulation is not None:
                    return True

                if self.encapsulation_information is not None and self.encapsulation_information._has_data():
                    return True

                if self.encapsulation_type_string is not None:
                    return True

                if self.hardware_type_string is not None:
                    return True

                if self.if_index is not None:
                    return True

                if self.in_flow_control is not None:
                    return True

                if self.interface_handle is not None:
                    return True

                if self.interface_statistics is not None and self.interface_statistics._has_data():
                    return True

                if self.interface_type is not None:
                    return True

                if self.interface_type_information is not None and self.interface_type_information._has_data():
                    return True

                if self.ip_information is not None and self.ip_information._has_data():
                    return True

                if self.is_dampening_enabled is not None:
                    return True

                if self.is_data_inverted is not None:
                    return True

                if self.is_l2_looped is not None:
                    return True

                if self.is_l2_transport_enabled is not None:
                    return True

                if self.is_maintenance_enabled is not None:
                    return True

                if self.is_scramble_enabled is not None:
                    return True

                if self.keepalive is not None:
                    return True

                if self.l2_interface_statistics is not None and self.l2_interface_statistics._has_data():
                    return True

                if self.last_state_transition_time is not None:
                    return True

                if self.line_state is not None:
                    return True

                if self.link_type is not None:
                    return True

                if self.loopback_configuration is not None:
                    return True

                if self.mac_address is not None and self.mac_address._has_data():
                    return True

                if self.max_bandwidth is not None:
                    return True

                if self.media_type is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.nv_optical is not None and self.nv_optical._has_data():
                    return True

                if self.out_flow_control is not None:
                    return True

                if self.parent_interface_name is not None:
                    return True

                if self.speed is not None:
                    return True

                if self.state is not None:
                    return True

                if self.state_transition_count is not None:
                    return True

                if self.transport_mode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceXr.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-xr'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InterfaceXr']['meta_info']


    class NodeTypeSets(object):
        """
        Node and/or interface type specific view of
        interface summary data
        
        .. attribute:: node_type_set
        
        	Summary data for all interfaces on a particular node
        	**type**\: list of    :py:class:`NodeTypeSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2016-12-18'

        def __init__(self):
            self.parent = None
            self.node_type_set = YList()
            self.node_type_set.parent = self
            self.node_type_set.name = 'node_type_set'


        class NodeTypeSet(object):
            """
            Summary data for all interfaces on a particular
            node
            
            .. attribute:: interface_summary
            
            	Interface summary information
            	**type**\:   :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary>`
            
            .. attribute:: node_name
            
            	The location to filter on
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: type_set_name
            
            	The interface type to filter on
            	**type**\:   :py:class:`InterfaceTypeSetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.InterfaceTypeSetEnum>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.interface_summary = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary()
                self.interface_summary.parent = self
                self.node_name = None
                self.type_set_name = None


            class InterfaceSummary(object):
                """
                Interface summary information
                
                .. attribute:: interface_counts
                
                	Counts for all interfaces
                	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts>`
                
                .. attribute:: interface_type
                
                	List of per interface type summary information
                	**type**\: list of    :py:class:`InterfaceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.interface_counts = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts()
                    self.interface_counts.parent = self
                    self.interface_type = YList()
                    self.interface_type.parent = self
                    self.interface_type.name = 'interface_type'


                class InterfaceCounts(object):
                    """
                    Counts for all interfaces
                    
                    .. attribute:: admin_down_interface_count
                    
                    	Number of interfaces in an ADMINDOWN state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: down_interface_count
                    
                    	Number of interfaces in DOWN state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_count
                    
                    	Number of interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up_interface_count
                    
                    	Number of interfaces in UP state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.admin_down_interface_count = None
                        self.down_interface_count = None
                        self.interface_count = None
                        self.up_interface_count = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_down_interface_count is not None:
                            return True

                        if self.down_interface_count is not None:
                            return True

                        if self.interface_count is not None:
                            return True

                        if self.up_interface_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts']['meta_info']


                class InterfaceType(object):
                    """
                    List of per interface type summary information
                    
                    .. attribute:: interface_counts
                    
                    	Counts for interfaces of this type
                    	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts>`
                    
                    .. attribute:: interface_type_description
                    
                    	Description of the interface type
                    	**type**\:  str
                    
                    .. attribute:: interface_type_name
                    
                    	Name of the interface type
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2016-12-18'

                    def __init__(self):
                        self.parent = None
                        self.interface_counts = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts()
                        self.interface_counts.parent = self
                        self.interface_type_description = None
                        self.interface_type_name = None


                    class InterfaceCounts(object):
                        """
                        Counts for interfaces of this type
                        
                        .. attribute:: admin_down_interface_count
                        
                        	Number of interfaces in an ADMINDOWN state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: down_interface_count
                        
                        	Number of interfaces in DOWN state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_count
                        
                        	Number of interfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: up_interface_count
                        
                        	Number of interfaces in UP state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2016-12-18'

                        def __init__(self):
                            self.parent = None
                            self.admin_down_interface_count = None
                            self.down_interface_count = None
                            self.interface_count = None
                            self.up_interface_count = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.admin_down_interface_count is not None:
                                return True

                            if self.down_interface_count is not None:
                                return True

                            if self.interface_count is not None:
                                return True

                            if self.up_interface_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_counts is not None and self.interface_counts._has_data():
                            return True

                        if self.interface_type_description is not None:
                            return True

                        if self.interface_type_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_counts is not None and self.interface_counts._has_data():
                        return True

                    if self.interface_type is not None:
                        for child_ref in self.interface_type:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_summary is not None and self.interface_summary._has_data():
                    return True

                if self.node_name is not None:
                    return True

                if self.type_set_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node_type_set is not None:
                for child_ref in self.node_type_set:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.NodeTypeSets']['meta_info']


    class InterfaceBriefs(object):
        """
        Brief operational data for interfaces
        
        .. attribute:: interface_brief
        
        	Brief operational attributes for a particular interface
        	**type**\: list of    :py:class:`InterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceBriefs.InterfaceBrief>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2016-12-18'

        def __init__(self):
            self.parent = None
            self.interface_brief = YList()
            self.interface_brief.parent = self
            self.interface_brief.name = 'interface_brief'


        class InterfaceBrief(object):
            """
            Brief operational attributes for a particular
            interface
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: actual_line_state
            
            	Line protocol state with no translation of error disable or shutdown
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: actual_state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: bandwidth
            
            	Interface bandwidth (Kb/s)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: encapsulation
            
            	Interface encapsulation
            	**type**\:  str
            
            .. attribute:: encapsulation_type_string
            
            	Interface encapsulation description string
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: interface
            
            	Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: l2_transport
            
            	L2 transport
            	**type**\:  bool
            
            .. attribute:: line_state
            
            	Line protocol state
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: mtu
            
            	MTU in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: parent_interface
            
            	Parent Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: state
            
            	Operational state
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: sub_interface_mtu_overhead
            
            	Subif MTU overhead
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: type
            
            	Interface type
            	**type**\:  str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.actual_line_state = None
                self.actual_state = None
                self.bandwidth = None
                self.encapsulation = None
                self.encapsulation_type_string = None
                self.interface = None
                self.l2_transport = None
                self.line_state = None
                self.mtu = None
                self.parent_interface = None
                self.state = None
                self.sub_interface_mtu_overhead = None
                self.type = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-briefs/Cisco-IOS-XR-pfi-im-cmd-oper:interface-brief[Cisco-IOS-XR-pfi-im-cmd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.actual_line_state is not None:
                    return True

                if self.actual_state is not None:
                    return True

                if self.bandwidth is not None:
                    return True

                if self.encapsulation is not None:
                    return True

                if self.encapsulation_type_string is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.l2_transport is not None:
                    return True

                if self.line_state is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.parent_interface is not None:
                    return True

                if self.state is not None:
                    return True

                if self.sub_interface_mtu_overhead is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceBriefs.InterfaceBrief']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-briefs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_brief is not None:
                for child_ref in self.interface_brief:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InterfaceBriefs']['meta_info']


    class InventorySummary(object):
        """
        Inventory summary information
        
        .. attribute:: interface_counts
        
        	Counts for all interfaces
        	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceCounts>`
        
        .. attribute:: interface_type
        
        	List of per interface type summary information
        	**type**\: list of    :py:class:`InterfaceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceType>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2016-12-18'

        def __init__(self):
            self.parent = None
            self.interface_counts = Interfaces.InventorySummary.InterfaceCounts()
            self.interface_counts.parent = self
            self.interface_type = YList()
            self.interface_type.parent = self
            self.interface_type.name = 'interface_type'


        class InterfaceCounts(object):
            """
            Counts for all interfaces
            
            .. attribute:: admin_down_interface_count
            
            	Number of interfaces in an ADMINDOWN state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: down_interface_count
            
            	Number of interfaces in DOWN state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Number of interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_interface_count
            
            	Number of interfaces in UP state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.admin_down_interface_count = None
                self.down_interface_count = None
                self.interface_count = None
                self.up_interface_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.admin_down_interface_count is not None:
                    return True

                if self.down_interface_count is not None:
                    return True

                if self.interface_count is not None:
                    return True

                if self.up_interface_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InventorySummary.InterfaceCounts']['meta_info']


        class InterfaceType(object):
            """
            List of per interface type summary information
            
            .. attribute:: interface_counts
            
            	Counts for interfaces of this type
            	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceType.InterfaceCounts>`
            
            .. attribute:: interface_type_description
            
            	Description of the interface type
            	**type**\:  str
            
            .. attribute:: interface_type_name
            
            	Name of the interface type
            	**type**\:  str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.interface_counts = Interfaces.InventorySummary.InterfaceType.InterfaceCounts()
                self.interface_counts.parent = self
                self.interface_type_description = None
                self.interface_type_name = None


            class InterfaceCounts(object):
                """
                Counts for interfaces of this type
                
                .. attribute:: admin_down_interface_count
                
                	Number of interfaces in an ADMINDOWN state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_interface_count
                
                	Number of interfaces in DOWN state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_count
                
                	Number of interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_interface_count
                
                	Number of interfaces in UP state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.admin_down_interface_count = None
                    self.down_interface_count = None
                    self.interface_count = None
                    self.up_interface_count = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_down_interface_count is not None:
                        return True

                    if self.down_interface_count is not None:
                        return True

                    if self.interface_count is not None:
                        return True

                    if self.up_interface_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InventorySummary.InterfaceType.InterfaceCounts']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_counts is not None and self.interface_counts._has_data():
                    return True

                if self.interface_type_description is not None:
                    return True

                if self.interface_type_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InventorySummary.InterfaceType']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_counts is not None and self.interface_counts._has_data():
                return True

            if self.interface_type is not None:
                for child_ref in self.interface_type:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InventorySummary']['meta_info']


    class Interfaces_(object):
        """
        Descriptions for interfaces
        
        .. attribute:: interface
        
        	Description for a particular interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.Interfaces_.Interface>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2016-12-18'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Description for a particular interface
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: description
            
            	Interface description string
            	**type**\:  str
            
            .. attribute:: interface
            
            	Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: line_state
            
            	Line protocol state with no translation of error disable or shutdown
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            .. attribute:: state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnumEnum>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.description = None
                self.interface = None
                self.line_state = None
                self.state = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface[Cisco-IOS-XR-pfi-im-cmd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.description is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.line_state is not None:
                    return True

                if self.state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.Interfaces_.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.Interfaces_']['meta_info']


    class InterfaceSummary(object):
        """
        Interface summary information
        
        .. attribute:: interface_counts
        
        	Counts for all interfaces
        	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceCounts>`
        
        .. attribute:: interface_type
        
        	List of per interface type summary information
        	**type**\: list of    :py:class:`InterfaceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceType>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2016-12-18'

        def __init__(self):
            self.parent = None
            self.interface_counts = Interfaces.InterfaceSummary.InterfaceCounts()
            self.interface_counts.parent = self
            self.interface_type = YList()
            self.interface_type.parent = self
            self.interface_type.name = 'interface_type'


        class InterfaceCounts(object):
            """
            Counts for all interfaces
            
            .. attribute:: admin_down_interface_count
            
            	Number of interfaces in an ADMINDOWN state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: down_interface_count
            
            	Number of interfaces in DOWN state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Number of interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_interface_count
            
            	Number of interfaces in UP state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.admin_down_interface_count = None
                self.down_interface_count = None
                self.interface_count = None
                self.up_interface_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.admin_down_interface_count is not None:
                    return True

                if self.down_interface_count is not None:
                    return True

                if self.interface_count is not None:
                    return True

                if self.up_interface_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceSummary.InterfaceCounts']['meta_info']


        class InterfaceType(object):
            """
            List of per interface type summary information
            
            .. attribute:: interface_counts
            
            	Counts for interfaces of this type
            	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts>`
            
            .. attribute:: interface_type_description
            
            	Description of the interface type
            	**type**\:  str
            
            .. attribute:: interface_type_name
            
            	Name of the interface type
            	**type**\:  str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2016-12-18'

            def __init__(self):
                self.parent = None
                self.interface_counts = Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts()
                self.interface_counts.parent = self
                self.interface_type_description = None
                self.interface_type_name = None


            class InterfaceCounts(object):
                """
                Counts for interfaces of this type
                
                .. attribute:: admin_down_interface_count
                
                	Number of interfaces in an ADMINDOWN state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_interface_count
                
                	Number of interfaces in DOWN state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_count
                
                	Number of interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_interface_count
                
                	Number of interfaces in UP state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2016-12-18'

                def __init__(self):
                    self.parent = None
                    self.admin_down_interface_count = None
                    self.down_interface_count = None
                    self.interface_count = None
                    self.up_interface_count = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.admin_down_interface_count is not None:
                        return True

                    if self.down_interface_count is not None:
                        return True

                    if self.interface_count is not None:
                        return True

                    if self.up_interface_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_counts is not None and self.interface_counts._has_data():
                    return True

                if self.interface_type_description is not None:
                    return True

                if self.interface_type_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceSummary.InterfaceType']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_counts is not None and self.interface_counts._has_data():
                return True

            if self.interface_type is not None:
                for child_ref in self.interface_type:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InterfaceSummary']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interface_briefs is not None and self.interface_briefs._has_data():
            return True

        if self.interface_summary is not None and self.interface_summary._has_data():
            return True

        if self.interface_xr is not None and self.interface_xr._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.inventory_summary is not None and self.inventory_summary._has_data():
            return True

        if self.node_type_sets is not None and self.node_type_sets._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['Interfaces']['meta_info']


