""" Cisco_IOS_XR_pfi_im_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pfi\-im\-cmd package operational data.

This module contains definitions
for the following management objects\:
  interfaces\: Interface operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BmMbrStateReason(Enum):
    """
    BmMbrStateReason (Enum Class)

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

    bm_mbr_state_reason_unknown = Enum.YLeaf(0, "bm-mbr-state-reason-unknown")

    bm_mbr_state_reason_unselectable_unknown = Enum.YLeaf(1, "bm-mbr-state-reason-unselectable-unknown")

    bm_mbr_state_reason_link_down = Enum.YLeaf(2, "bm-mbr-state-reason-link-down")

    bm_mbr_state_reason_link_deleting = Enum.YLeaf(3, "bm-mbr-state-reason-link-deleting")

    bm_mbr_state_reason_creating = Enum.YLeaf(4, "bm-mbr-state-reason-creating")

    bm_mbr_state_reason_bundle_creating = Enum.YLeaf(5, "bm-mbr-state-reason-bundle-creating")

    bm_mbr_state_reason_bundle_deleting = Enum.YLeaf(6, "bm-mbr-state-reason-bundle-deleting")

    bm_mbr_state_reason_bundle_admin_down = Enum.YLeaf(7, "bm-mbr-state-reason-bundle-admin-down")

    bm_mbr_state_reason_replicating = Enum.YLeaf(8, "bm-mbr-state-reason-replicating")

    bm_mbr_state_reason_bandwidth = Enum.YLeaf(9, "bm-mbr-state-reason-bandwidth")

    bm_mbr_state_reason_loop_back = Enum.YLeaf(10, "bm-mbr-state-reason-loop-back")

    bm_mbr_state_reason_activity_type = Enum.YLeaf(11, "bm-mbr-state-reason-activity-type")

    bm_mbr_state_reason_bundle_shutdown = Enum.YLeaf(12, "bm-mbr-state-reason-bundle-shutdown")

    bm_mbr_state_reason_min_selected = Enum.YLeaf(13, "bm-mbr-state-reason-min-selected")

    bm_mbr_state_reason_max_selected = Enum.YLeaf(14, "bm-mbr-state-reason-max-selected")

    bm_mbr_state_reason_link_limit = Enum.YLeaf(15, "bm-mbr-state-reason-link-limit")

    bm_mbr_state_reason_active_limit = Enum.YLeaf(16, "bm-mbr-state-reason-active-limit")

    bm_mbr_state_reason_standby_unknown = Enum.YLeaf(17, "bm-mbr-state-reason-standby-unknown")

    bm_mbr_state_reason_expired = Enum.YLeaf(18, "bm-mbr-state-reason-expired")

    bm_mbr_state_reason_defaulted = Enum.YLeaf(19, "bm-mbr-state-reason-defaulted")

    bm_mbr_state_reason_act_or_not_agg = Enum.YLeaf(20, "bm-mbr-state-reason-act-or-not-agg")

    bm_mbr_state_reason_partner_not_agg = Enum.YLeaf(21, "bm-mbr-state-reason-partner-not-agg")

    bm_mbr_state_reason_lagid = Enum.YLeaf(22, "bm-mbr-state-reason-lagid")

    bm_mbr_state_reason_bundle_not_cfgd = Enum.YLeaf(23, "bm-mbr-state-reason-bundle-not-cfgd")

    bm_mbr_state_reason_bundle_not_ready = Enum.YLeaf(24, "bm-mbr-state-reason-bundle-not-ready")

    bm_mbr_state_reason_partner_ood = Enum.YLeaf(25, "bm-mbr-state-reason-partner-ood")

    bm_mbr_state_reason_partner_not_in_sync = Enum.YLeaf(26, "bm-mbr-state-reason-partner-not-in-sync")

    bm_mbr_state_reason_foreign_partner_oos = Enum.YLeaf(27, "bm-mbr-state-reason-foreign-partner-oos")

    bm_mbr_state_reason_attach_unknown = Enum.YLeaf(28, "bm-mbr-state-reason-attach-unknown")

    bm_mbr_state_reason_partner_not_collecting = Enum.YLeaf(29, "bm-mbr-state-reason-partner-not-collecting")

    bm_mbr_state_reason_collect_unknown = Enum.YLeaf(30, "bm-mbr-state-reason-collect-unknown")

    bm_mbr_state_reason_standby_foreign = Enum.YLeaf(31, "bm-mbr-state-reason-standby-foreign")

    bm_mbr_state_reason_bfd_starting = Enum.YLeaf(32, "bm-mbr-state-reason-bfd-starting")

    bm_mbr_state_reason_bfd_down = Enum.YLeaf(33, "bm-mbr-state-reason-bfd-down")

    bm_mbr_state_reason_bfd_nbr_unconfig = Enum.YLeaf(34, "bm-mbr-state-reason-bfd-nbr-unconfig")

    bm_mbr_state_reason_mlacp = Enum.YLeaf(35, "bm-mbr-state-reason-mlacp")

    bm_mbr_state_reason_pe_isolated = Enum.YLeaf(36, "bm-mbr-state-reason-pe-isolated")

    bm_mbr_state_reason_forced_switchover = Enum.YLeaf(37, "bm-mbr-state-reason-forced-switchover")

    bm_mbr_state_reason_errdis_unknown = Enum.YLeaf(38, "bm-mbr-state-reason-errdis-unknown")

    bm_mbr_state_reason_mlacp_no_mbr_state_info = Enum.YLeaf(39, "bm-mbr-state-reason-mlacp-no-mbr-state-info")

    bm_mbr_state_reason_active = Enum.YLeaf(40, "bm-mbr-state-reason-active")

    bm_mbr_state_reason_mlacp_no_bdl_state_info = Enum.YLeaf(41, "bm-mbr-state-reason-mlacp-no-bdl-state-info")

    bm_mbr_state_reason_mlacp_no_bdl_config_info = Enum.YLeaf(42, "bm-mbr-state-reason-mlacp-no-bdl-config-info")

    bm_mbr_state_reason_mlacp_no_bdl_sync = Enum.YLeaf(43, "bm-mbr-state-reason-mlacp-no-bdl-sync")

    bm_mbr_state_reason_mlacp_bdl_has_no_peer = Enum.YLeaf(44, "bm-mbr-state-reason-mlacp-bdl-has-no-peer")

    bm_mbr_state_reason_mlacp_nak = Enum.YLeaf(45, "bm-mbr-state-reason-mlacp-nak")

    bm_mbr_state_reason_mlacp_transport_unavailable = Enum.YLeaf(46, "bm-mbr-state-reason-mlacp-transport-unavailable")

    bm_mbr_state_reason_mlacp_not_configured = Enum.YLeaf(47, "bm-mbr-state-reason-mlacp-not-configured")

    bm_mbr_state_reason_recovery_timer = Enum.YLeaf(48, "bm-mbr-state-reason-recovery-timer")

    bm_mbr_state_reason_mlacp_standby = Enum.YLeaf(49, "bm-mbr-state-reason-mlacp-standby")

    bm_mbr_state_reason_maximized_out = Enum.YLeaf(50, "bm-mbr-state-reason-maximized-out")

    bm_mbr_state_reason_mlacp_peer_selected = Enum.YLeaf(51, "bm-mbr-state-reason-mlacp-peer-selected")

    bm_mbr_state_reason_mlacp_connect_timer_running = Enum.YLeaf(52, "bm-mbr-state-reason-mlacp-connect-timer-running")

    bm_mbr_state_reason_bundle_not_mlacp = Enum.YLeaf(53, "bm-mbr-state-reason-bundle-not-mlacp")

    bm_mbr_state_reason_no_lon = Enum.YLeaf(54, "bm-mbr-state-reason-no-lon")

    bm_mbr_state_reason_cumul_rel_bw_limit = Enum.YLeaf(55, "bm-mbr-state-reason-cumul-rel-bw-limit")

    bm_mbr_state_reason_no_mac = Enum.YLeaf(56, "bm-mbr-state-reason-no-mac")

    bm_mbr_state_reason_no_system_id = Enum.YLeaf(57, "bm-mbr-state-reason-no-system-id")

    bm_mbr_state_reason_link_shutdown = Enum.YLeaf(58, "bm-mbr-state-reason-link-shutdown")

    bm_mbr_state_reason_activity_mlacp = Enum.YLeaf(59, "bm-mbr-state-reason-activity-mlacp")

    bm_mbr_state_reason_activity_iccp = Enum.YLeaf(60, "bm-mbr-state-reason-activity-iccp")

    bm_mbr_state_reason_bundle_icpe_mlacp = Enum.YLeaf(61, "bm-mbr-state-reason-bundle-icpe-mlacp")

    bm_mbr_state_reason_no_link_num = Enum.YLeaf(62, "bm-mbr-state-reason-no-link-num")

    bm_mbr_state_reason_standby_peer_higher_prio = Enum.YLeaf(63, "bm-mbr-state-reason-standby-peer-higher-prio")

    bm_mbr_state_reason_red_state_standby = Enum.YLeaf(64, "bm-mbr-state-reason-red-state-standby")

    bm_mbr_state_reason_other_red_state_standby = Enum.YLeaf(65, "bm-mbr-state-reason-other-red-state-standby")

    bm_mbr_state_reason_hold_ing = Enum.YLeaf(66, "bm-mbr-state-reason-hold-ing")

    bm_mbr_state_reason_bundle_error_disabled = Enum.YLeaf(67, "bm-mbr-state-reason-bundle-error-disabled")

    bm_mbr_state_reason_bundle_efd_disabled = Enum.YLeaf(68, "bm-mbr-state-reason-bundle-efd-disabled")

    bm_mbr_state_reason_singleton_pe_isolated = Enum.YLeaf(69, "bm-mbr-state-reason-singleton-pe-isolated")

    bm_mbr_state_reason_bfd_ipv6_starting = Enum.YLeaf(70, "bm-mbr-state-reason-bfd-ipv6-starting")

    bm_mbr_state_reason_bfd_ipv6_down = Enum.YLeaf(71, "bm-mbr-state-reason-bfd-ipv6-down")

    bm_mbr_state_reason_bfd_ipv6_nbr_unconfig = Enum.YLeaf(72, "bm-mbr-state-reason-bfd-ipv6-nbr-unconfig")

    bm_mbr_state_reason_timer_running = Enum.YLeaf(73, "bm-mbr-state-reason-timer-running")

    bm_mbr_state_reason_client_bundle_ctrl = Enum.YLeaf(74, "bm-mbr-state-reason-client-bundle-ctrl")

    bm_mbr_state_reason_count = Enum.YLeaf(75, "bm-mbr-state-reason-count")


class BmMuxreason(Enum):
    """
    BmMuxreason (Enum Class)

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

    bm_mux_reason_no_reason = Enum.YLeaf(0, "bm-mux-reason-no-reason")

    bm_mux_reason_link_down = Enum.YLeaf(1, "bm-mux-reason-link-down")

    bm_mux_reason_link_deleted = Enum.YLeaf(2, "bm-mux-reason-link-deleted")

    bm_mux_reason_duplex = Enum.YLeaf(3, "bm-mux-reason-duplex")

    bm_mux_reason_bandwidth = Enum.YLeaf(4, "bm-mux-reason-bandwidth")

    bm_mux_reason_loop_back = Enum.YLeaf(5, "bm-mux-reason-loop-back")

    bm_mux_reason_activity_type = Enum.YLeaf(6, "bm-mux-reason-activity-type")

    bm_mux_reason_link_limit = Enum.YLeaf(7, "bm-mux-reason-link-limit")

    bm_mux_reason_shared = Enum.YLeaf(8, "bm-mux-reason-shared")

    bm_mux_reason_lagid = Enum.YLeaf(9, "bm-mux-reason-lagid")

    bm_mux_reason_no_bundle = Enum.YLeaf(10, "bm-mux-reason-no-bundle")

    bm_mux_reason_no_primary = Enum.YLeaf(11, "bm-mux-reason-no-primary")

    bm_mux_reason_bundle_down = Enum.YLeaf(12, "bm-mux-reason-bundle-down")

    bm_mux_reason_individual = Enum.YLeaf(13, "bm-mux-reason-individual")

    bm_mux_reason_defaulted = Enum.YLeaf(14, "bm-mux-reason-defaulted")

    bm_mux_reason_in_sync = Enum.YLeaf(15, "bm-mux-reason-in-sync")

    bm_mux_reason_collecting = Enum.YLeaf(16, "bm-mux-reason-collecting")

    bm_mux_reason_active_link_limit = Enum.YLeaf(17, "bm-mux-reason-active-link-limit")

    bm_mux_reason_distributing = Enum.YLeaf(18, "bm-mux-reason-distributing")

    bm_mux_reason_count = Enum.YLeaf(19, "bm-mux-reason-count")


class BmMuxstate(Enum):
    """
    BmMuxstate (Enum Class)

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

    detached = Enum.YLeaf(1, "detached")

    waiting = Enum.YLeaf(2, "waiting")

    attached = Enum.YLeaf(3, "attached")

    collecting = Enum.YLeaf(4, "collecting")

    distributing = Enum.YLeaf(5, "distributing")

    collecting_distributing = Enum.YLeaf(6, "collecting-distributing")


class BmSeverity(Enum):
    """
    BmSeverity (Enum Class)

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

    ok = Enum.YLeaf(0, "ok")

    information = Enum.YLeaf(1, "information")

    misconfiguration = Enum.YLeaf(2, "misconfiguration")

    warning = Enum.YLeaf(3, "warning")

    error = Enum.YLeaf(5, "error")


class BmStateReasonTarget(Enum):
    """
    BmStateReasonTarget (Enum Class)

    Scope of the state reason

    .. data:: member_reason = 0

    	Member applicable reason

    .. data:: bundle_reason = 1

    	Bundle applicable reason

    """

    member_reason = Enum.YLeaf(0, "member-reason")

    bundle_reason = Enum.YLeaf(1, "bundle-reason")


class BmdMemberState(Enum):
    """
    BmdMemberState (Enum Class)

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

    bmd_mbr_state_configured = Enum.YLeaf(1, "bmd-mbr-state-configured")

    bmd_mbr_state_standby = Enum.YLeaf(2, "bmd-mbr-state-standby")

    bmd_mbr_state_hot_standby = Enum.YLeaf(3, "bmd-mbr-state-hot-standby")

    bmd_mbr_state_negotiating = Enum.YLeaf(4, "bmd-mbr-state-negotiating")

    bmd_mbr_state_bfd_running = Enum.YLeaf(5, "bmd-mbr-state-bfd-running")

    bmd_mbr_state_active = Enum.YLeaf(6, "bmd-mbr-state-active")


class BmdMemberTypeEnum(Enum):
    """
    BmdMemberTypeEnum (Enum Class)

    Bmd member type enum

    .. data:: bmd_mbr_local = 0

    	Member has been configured on the local device

    .. data:: bmd_mbr_foreign = 1

    	Member has been configured on an mLACP peer

    	device

    .. data:: bmd_mbr_unknown = 2

    	Member's type is unknown

    """

    bmd_mbr_local = Enum.YLeaf(0, "bmd-mbr-local")

    bmd_mbr_foreign = Enum.YLeaf(1, "bmd-mbr-foreign")

    bmd_mbr_unknown = Enum.YLeaf(2, "bmd-mbr-unknown")


class EfpPayloadEtype(Enum):
    """
    EfpPayloadEtype (Enum Class)

    Payload ethertype match

    .. data:: payload_ethertype_any = 0

    	Any

    .. data:: payload_ethertype_ip = 1

    	IP

    .. data:: payload_ethertype_pppoe = 2

    	PPPoE

    """

    payload_ethertype_any = Enum.YLeaf(0, "payload-ethertype-any")

    payload_ethertype_ip = Enum.YLeaf(1, "payload-ethertype-ip")

    payload_ethertype_pppoe = Enum.YLeaf(2, "payload-ethertype-pppoe")


class EfpTagEtype(Enum):
    """
    EfpTagEtype (Enum Class)

    Tag ethertype

    .. data:: untagged = 0

    	Untagged

    .. data:: dot1q = 33024

    	Dot1Q

    .. data:: dot1ad = 34984

    	Dot1ad

    """

    untagged = Enum.YLeaf(0, "untagged")

    dot1q = Enum.YLeaf(33024, "dot1q")

    dot1ad = Enum.YLeaf(34984, "dot1ad")


class EfpTagPriority(Enum):
    """
    EfpTagPriority (Enum Class)

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

    priority0 = Enum.YLeaf(0, "priority0")

    priority1 = Enum.YLeaf(1, "priority1")

    priority2 = Enum.YLeaf(2, "priority2")

    priority3 = Enum.YLeaf(3, "priority3")

    priority4 = Enum.YLeaf(4, "priority4")

    priority5 = Enum.YLeaf(5, "priority5")

    priority6 = Enum.YLeaf(6, "priority6")

    priority7 = Enum.YLeaf(7, "priority7")

    priority_any = Enum.YLeaf(8, "priority-any")


class GccDerState(Enum):
    """
    GccDerState (Enum Class)

    Gcc der state

    .. data:: in_service = 0

    	In Service

    .. data:: out_of_service = 1

    	Out Of Service

    .. data:: maintenance = 2

    	Maintenance

    .. data:: ais = 3

    	Automatic In Service

    """

    in_service = Enum.YLeaf(0, "in-service")

    out_of_service = Enum.YLeaf(1, "out-of-service")

    maintenance = Enum.YLeaf(2, "maintenance")

    ais = Enum.YLeaf(3, "ais")


class GccSecState(Enum):
    """
    GccSecState (Enum Class)

    Gcc sec state

    .. data:: normal = 0

    	Normal

    .. data:: maintenance = 1

    	Maintenance

    .. data:: ais = 2

    	Automatic In Service

    """

    normal = Enum.YLeaf(0, "normal")

    maintenance = Enum.YLeaf(1, "maintenance")

    ais = Enum.YLeaf(2, "ais")


class ImAttrDuplex(Enum):
    """
    ImAttrDuplex (Enum Class)

    Im attr duplex

    .. data:: im_attr_duplex_unknown = 0

    	im attr duplex unknown

    .. data:: im_attr_duplex_half = 1

    	im attr duplex half

    .. data:: im_attr_duplex_full = 2

    	im attr duplex full

    """

    im_attr_duplex_unknown = Enum.YLeaf(0, "im-attr-duplex-unknown")

    im_attr_duplex_half = Enum.YLeaf(1, "im-attr-duplex-half")

    im_attr_duplex_full = Enum.YLeaf(2, "im-attr-duplex-full")


class ImAttrFlowControl(Enum):
    """
    ImAttrFlowControl (Enum Class)

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

    im_attr_flow_control_off = Enum.YLeaf(0, "im-attr-flow-control-off")

    im_attr_flow_control_on = Enum.YLeaf(1, "im-attr-flow-control-on")

    im_attr_flow_control_not_sup = Enum.YLeaf(2, "im-attr-flow-control-not-sup")

    im_attr_flow_control_priority = Enum.YLeaf(3, "im-attr-flow-control-priority")


class ImAttrLink(Enum):
    """
    ImAttrLink (Enum Class)

    Im attr link

    .. data:: im_attr_link_type_auto = 0

    	im attr link type auto

    .. data:: im_attr_link_type_force = 1

    	im attr link type force

    """

    im_attr_link_type_auto = Enum.YLeaf(0, "im-attr-link-type-auto")

    im_attr_link_type_force = Enum.YLeaf(1, "im-attr-link-type-force")


class ImAttrMedia(Enum):
    """
    ImAttrMedia (Enum Class)

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

    .. data:: im_attr_media_50gbase_cr2 = 345

    	im attr media 50gbase cr2

    .. data:: im_attr_media_50gbase_sr2 = 346

    	im attr media 50gbase sr2

    .. data:: im_attr_media_50gbase_psm2 = 347

    	im attr media 50gbase psm2

    .. data:: im_attr_media_200gbase_cr4 = 348

    	im attr media 200gbase cr4

    .. data:: im_attr_media_400gbase_fr4 = 349

    	im attr media 400gbase fr4

    .. data:: im_attr_media_400gbase_dr4 = 350

    	im attr media 400gbase dr4

    .. data:: im_attr_media_400gbase_cr4 = 351

    	im attr media 400gbase cr4

    .. data:: im_attr_media_10gbase_cr = 352

    	im attr media 10gbase cr

    .. data:: im_attr_media_10gbase_aoc = 353

    	im attr media 10gbase aoc

    .. data:: im_attr_media_40gbase_aoc = 354

    	im attr media 40gbase aoc

    .. data:: im_attr_media_40gbase_acu = 355

    	im attr media 40gbase acu

    .. data:: im_attr_media_100gbase_acu = 356

    	im attr media 100gbase acu

    .. data:: im_attr_media_10gbase_cu1m = 357

    	im attr media 10gbase cu1m

    .. data:: im_attr_media_10gbase_cu3m = 358

    	im attr media 10gbase cu3m

    .. data:: im_attr_media_10gbase_cu5m = 359

    	im attr media 10gbase cu5m

    .. data:: im_attr_media_10gbase_acu7m = 360

    	im attr media 10gbase acu7m

    .. data:: im_attr_media_10gbase_acu10m = 361

    	im attr media 10gbase acu10m

    .. data:: im_attr_media_4x10g_base_lr = 362

    	im attr media 4x10g base lr

    .. data:: im_attr_media_10gbase_cu1_5m = 363

    	im attr media 10gbase cu1 5m

    .. data:: im_attr_media_10gbase_cu2m = 364

    	im attr media 10gbase cu2m

    .. data:: im_attr_media_10gbase_cu2_5m = 365

    	im attr media 10gbase cu2 5m

    .. data:: im_attr_media_10gbase_aoc1m = 366

    	im attr media 10gbase aoc1m

    .. data:: im_attr_media_10gbase_aoc2m = 367

    	im attr media 10gbase aoc2m

    .. data:: im_attr_media_10gbase_aoc3m = 368

    	im attr media 10gbase aoc3m

    .. data:: im_attr_media_10gbase_aoc5m = 369

    	im attr media 10gbase aoc5m

    .. data:: im_attr_media_10gbase_aoc7m = 370

    	im attr media 10gbase aoc7m

    .. data:: im_attr_media_10gbase_aoc10m = 371

    	im attr media 10gbase aoc10m

    .. data:: im_attr_media_40gbase_acu1m = 372

    	im attr media 40gbase acu1m

    .. data:: im_attr_media_40gbase_acu3m = 373

    	im attr media 40gbase acu3m

    .. data:: im_attr_media_40gbase_acu5m = 374

    	im attr media 40gbase acu5m

    .. data:: im_attr_media_40gbase_acu7m = 375

    	im attr media 40gbase acu7m

    .. data:: im_attr_media_40gbase_acu10m = 376

    	im attr media 40gbase acu10m

    .. data:: im_attr_media_25gbase_cu1m = 377

    	im attr media 25gbase cu1m

    .. data:: im_attr_media_25gbase_cu2m = 378

    	im attr media 25gbase cu2m

    .. data:: im_attr_media_25gbase_cu3m = 379

    	im attr media 25gbase cu3m

    .. data:: im_attr_media_25gbase_cu5m = 380

    	im attr media 25gbase cu5m

    .. data:: im_attr_media_100gbase_sm_sr = 381

    	im attr media 100gbase sm sr

    """

    im_attr_media_other = Enum.YLeaf(0, "im-attr-media-other")

    im_attr_media_unknown = Enum.YLeaf(1, "im-attr-media-unknown")

    im_attr_media_aui = Enum.YLeaf(2, "im-attr-media-aui")

    im_attr_media_10base5 = Enum.YLeaf(3, "im-attr-media-10base5")

    im_attr_media_foirl = Enum.YLeaf(4, "im-attr-media-foirl")

    im_attr_media_10base2 = Enum.YLeaf(5, "im-attr-media-10base2")

    im_attr_media_10broad36 = Enum.YLeaf(6, "im-attr-media-10broad36")

    im_attr_media_10base = Enum.YLeaf(7, "im-attr-media-10base")

    im_attr_media_10base_thd = Enum.YLeaf(8, "im-attr-media-10base-thd")

    im_attr_media_10base_tfd = Enum.YLeaf(9, "im-attr-media-10base-tfd")

    im_attr_media_10base_fp = Enum.YLeaf(10, "im-attr-media-10base-fp")

    im_attr_media_10base_fb = Enum.YLeaf(11, "im-attr-media-10base-fb")

    im_attr_media_10base_fl = Enum.YLeaf(12, "im-attr-media-10base-fl")

    im_attr_media_10base_flhd = Enum.YLeaf(13, "im-attr-media-10base-flhd")

    im_attr_media_10base_flfd = Enum.YLeaf(14, "im-attr-media-10base-flfd")

    im_attr_media_100base_t4 = Enum.YLeaf(15, "im-attr-media-100base-t4")

    im_attr_media_100base_tx = Enum.YLeaf(16, "im-attr-media-100base-tx")

    im_attr_media_100base_txhd = Enum.YLeaf(17, "im-attr-media-100base-txhd")

    im_attr_media_100base_txfd = Enum.YLeaf(18, "im-attr-media-100base-txfd")

    im_attr_media_100base_fx = Enum.YLeaf(19, "im-attr-media-100base-fx")

    im_attr_media_100base_fxhd = Enum.YLeaf(20, "im-attr-media-100base-fxhd")

    im_attr_media_100base_fxfd = Enum.YLeaf(21, "im-attr-media-100base-fxfd")

    im_attr_media_100base_ex = Enum.YLeaf(22, "im-attr-media-100base-ex")

    im_attr_media_100base_exhd = Enum.YLeaf(23, "im-attr-media-100base-exhd")

    im_attr_media_100base_exfd = Enum.YLeaf(24, "im-attr-media-100base-exfd")

    im_attr_media_100base_t2 = Enum.YLeaf(25, "im-attr-media-100base-t2")

    im_attr_media_100base_t2hd = Enum.YLeaf(26, "im-attr-media-100base-t2hd")

    im_attr_media_100base_t2fd = Enum.YLeaf(27, "im-attr-media-100base-t2fd")

    im_attr_media_1000base_x = Enum.YLeaf(28, "im-attr-media-1000base-x")

    im_attr_media_1000base_xhdx = Enum.YLeaf(29, "im-attr-media-1000base-xhdx")

    im_attr_media_1000base_xfd = Enum.YLeaf(30, "im-attr-media-1000base-xfd")

    im_attr_media_1000base_lx = Enum.YLeaf(31, "im-attr-media-1000base-lx")

    im_attr_media_1000base_lxhd = Enum.YLeaf(32, "im-attr-media-1000base-lxhd")

    im_attr_media_1000base_lxfdx = Enum.YLeaf(33, "im-attr-media-1000base-lxfdx")

    im_attr_media_1000base_sx = Enum.YLeaf(34, "im-attr-media-1000base-sx")

    im_attr_media_1000base_sxhd = Enum.YLeaf(35, "im-attr-media-1000base-sxhd")

    im_attr_media_1000base_sxfd = Enum.YLeaf(36, "im-attr-media-1000base-sxfd")

    im_attr_media_1000base_cx = Enum.YLeaf(37, "im-attr-media-1000base-cx")

    im_attr_media_1000base_cxhdx = Enum.YLeaf(38, "im-attr-media-1000base-cxhdx")

    im_attr_media_1000base_cxfd = Enum.YLeaf(39, "im-attr-media-1000base-cxfd")

    im_attr_media_1000base = Enum.YLeaf(40, "im-attr-media-1000base")

    im_attr_media_1000base_thd = Enum.YLeaf(41, "im-attr-media-1000base-thd")

    im_attr_media_1000base_tfd = Enum.YLeaf(42, "im-attr-media-1000base-tfd")

    im_attr_media_10gbase_x = Enum.YLeaf(43, "im-attr-media-10gbase-x")

    im_attr_media_10gbase_lx4 = Enum.YLeaf(44, "im-attr-media-10gbase-lx4")

    im_attr_media_10gbase_r = Enum.YLeaf(45, "im-attr-media-10gbase-r")

    im_attr_media_10gbase_er = Enum.YLeaf(46, "im-attr-media-10gbase-er")

    im_attr_media_10gbase_lr = Enum.YLeaf(47, "im-attr-media-10gbase-lr")

    im_attr_media_10gbase_sr = Enum.YLeaf(48, "im-attr-media-10gbase-sr")

    im_attr_media_10gbase_w = Enum.YLeaf(49, "im-attr-media-10gbase-w")

    im_attr_media_10gbase_ew = Enum.YLeaf(50, "im-attr-media-10gbase-ew")

    im_attr_media_10gbase_lw = Enum.YLeaf(51, "im-attr-media-10gbase-lw")

    im_attr_media_10gbase_sw = Enum.YLeaf(52, "im-attr-media-10gbase-sw")

    im_attr_media_10gbase_zr = Enum.YLeaf(53, "im-attr-media-10gbase-zr")

    im_attr_media_802_9a = Enum.YLeaf(54, "im-attr-media-802-9a")

    im_attr_media_rj45 = Enum.YLeaf(55, "im-attr-media-rj45")

    im_attr_media_1000base_zx = Enum.YLeaf(56, "im-attr-media-1000base-zx")

    im_attr_media_1000base_cwdm = Enum.YLeaf(57, "im-attr-media-1000base-cwdm")

    im_attr_media_1000base_cwdm_1470 = Enum.YLeaf(58, "im-attr-media-1000base-cwdm-1470")

    im_attr_media_1000base_cwdm_1490 = Enum.YLeaf(59, "im-attr-media-1000base-cwdm-1490")

    im_attr_media_1000base_cwdm_1510 = Enum.YLeaf(60, "im-attr-media-1000base-cwdm-1510")

    im_attr_media_1000base_cwdm_1530 = Enum.YLeaf(61, "im-attr-media-1000base-cwdm-1530")

    im_attr_media_1000base_cwdm_1550 = Enum.YLeaf(62, "im-attr-media-1000base-cwdm-1550")

    im_attr_media_1000base_cwdm_1570 = Enum.YLeaf(63, "im-attr-media-1000base-cwdm-1570")

    im_attr_media_1000base_cwdm_1590 = Enum.YLeaf(64, "im-attr-media-1000base-cwdm-1590")

    im_attr_media_1000base_cwdm_1610 = Enum.YLeaf(65, "im-attr-media-1000base-cwdm-1610")

    im_attr_media_10gbase_dwdm = Enum.YLeaf(66, "im-attr-media-10gbase-dwdm")

    im_attr_media_100gbase_lr4 = Enum.YLeaf(67, "im-attr-media-100gbase-lr4")

    im_attr_media_1000base_dwdm = Enum.YLeaf(68, "im-attr-media-1000base-dwdm")

    im_attr_media_1000base_dwdm_1533 = Enum.YLeaf(69, "im-attr-media-1000base-dwdm-1533")

    im_attr_media_1000base_dwdm_1537 = Enum.YLeaf(70, "im-attr-media-1000base-dwdm-1537")

    im_attr_media_1000base_dwdm_1541 = Enum.YLeaf(71, "im-attr-media-1000base-dwdm-1541")

    im_attr_media_1000base_dwdm_1545 = Enum.YLeaf(72, "im-attr-media-1000base-dwdm-1545")

    im_attr_media_1000base_dwdm_1549 = Enum.YLeaf(73, "im-attr-media-1000base-dwdm-1549")

    im_attr_media_1000base_dwdm_1553 = Enum.YLeaf(74, "im-attr-media-1000base-dwdm-1553")

    im_attr_media_1000base_dwdm_1557 = Enum.YLeaf(75, "im-attr-media-1000base-dwdm-1557")

    im_attr_media_1000base_dwdm_1561 = Enum.YLeaf(76, "im-attr-media-1000base-dwdm-1561")

    im_attr_media_40gbase_lr4 = Enum.YLeaf(77, "im-attr-media-40gbase-lr4")

    im_attr_media_40gbase_er4 = Enum.YLeaf(78, "im-attr-media-40gbase-er4")

    im_attr_media_100gbase_er4 = Enum.YLeaf(79, "im-attr-media-100gbase-er4")

    im_attr_media_1000base_ex = Enum.YLeaf(80, "im-attr-media-1000base-ex")

    im_attr_media_1000base_bx10_d = Enum.YLeaf(81, "im-attr-media-1000base-bx10-d")

    im_attr_media_1000base_bx10_u = Enum.YLeaf(82, "im-attr-media-1000base-bx10-u")

    im_attr_media_1000base_dwdm_1561_42 = Enum.YLeaf(83, "im-attr-media-1000base-dwdm-1561-42")

    im_attr_media_1000base_dwdm_1560_61 = Enum.YLeaf(84, "im-attr-media-1000base-dwdm-1560-61")

    im_attr_media_1000base_dwdm_1559_79 = Enum.YLeaf(85, "im-attr-media-1000base-dwdm-1559-79")

    im_attr_media_1000base_dwdm_1558_98 = Enum.YLeaf(86, "im-attr-media-1000base-dwdm-1558-98")

    im_attr_media_1000base_dwdm_1558_17 = Enum.YLeaf(87, "im-attr-media-1000base-dwdm-1558-17")

    im_attr_media_1000base_dwdm_1557_36 = Enum.YLeaf(88, "im-attr-media-1000base-dwdm-1557-36")

    im_attr_media_1000base_dwdm_1556_55 = Enum.YLeaf(89, "im-attr-media-1000base-dwdm-1556-55")

    im_attr_media_1000base_dwdm_1555_75 = Enum.YLeaf(90, "im-attr-media-1000base-dwdm-1555-75")

    im_attr_media_1000base_dwdm_1554_94 = Enum.YLeaf(91, "im-attr-media-1000base-dwdm-1554-94")

    im_attr_media_1000base_dwdm_1554_13 = Enum.YLeaf(92, "im-attr-media-1000base-dwdm-1554-13")

    im_attr_media_1000base_dwdm_1553_33 = Enum.YLeaf(93, "im-attr-media-1000base-dwdm-1553-33")

    im_attr_media_1000base_dwdm_1552_52 = Enum.YLeaf(94, "im-attr-media-1000base-dwdm-1552-52")

    im_attr_media_1000base_dwdm_1551_72 = Enum.YLeaf(95, "im-attr-media-1000base-dwdm-1551-72")

    im_attr_media_1000base_dwdm_1550_92 = Enum.YLeaf(96, "im-attr-media-1000base-dwdm-1550-92")

    im_attr_media_1000base_dwdm_1550_12 = Enum.YLeaf(97, "im-attr-media-1000base-dwdm-1550-12")

    im_attr_media_1000base_dwdm_1549_32 = Enum.YLeaf(98, "im-attr-media-1000base-dwdm-1549-32")

    im_attr_media_1000base_dwdm_1548_51 = Enum.YLeaf(99, "im-attr-media-1000base-dwdm-1548-51")

    im_attr_media_1000base_dwdm_1547_72 = Enum.YLeaf(100, "im-attr-media-1000base-dwdm-1547-72")

    im_attr_media_1000base_dwdm_1546_92 = Enum.YLeaf(101, "im-attr-media-1000base-dwdm-1546-92")

    im_attr_media_1000base_dwdm_1546_12 = Enum.YLeaf(102, "im-attr-media-1000base-dwdm-1546-12")

    im_attr_media_1000base_dwdm_1545_32 = Enum.YLeaf(103, "im-attr-media-1000base-dwdm-1545-32")

    im_attr_media_1000base_dwdm_1544_53 = Enum.YLeaf(104, "im-attr-media-1000base-dwdm-1544-53")

    im_attr_media_1000base_dwdm_1543_73 = Enum.YLeaf(105, "im-attr-media-1000base-dwdm-1543-73")

    im_attr_media_1000base_dwdm_1542_94 = Enum.YLeaf(106, "im-attr-media-1000base-dwdm-1542-94")

    im_attr_media_1000base_dwdm_1542_14 = Enum.YLeaf(107, "im-attr-media-1000base-dwdm-1542-14")

    im_attr_media_1000base_dwdm_1541_35 = Enum.YLeaf(108, "im-attr-media-1000base-dwdm-1541-35")

    im_attr_media_1000base_dwdm_1540_56 = Enum.YLeaf(109, "im-attr-media-1000base-dwdm-1540-56")

    im_attr_media_1000base_dwdm_1539_77 = Enum.YLeaf(110, "im-attr-media-1000base-dwdm-1539-77")

    im_attr_media_1000base_dwdm_1538_98 = Enum.YLeaf(111, "im-attr-media-1000base-dwdm-1538-98")

    im_attr_media_1000base_dwdm_1538_19 = Enum.YLeaf(112, "im-attr-media-1000base-dwdm-1538-19")

    im_attr_media_1000base_dwdm_1537_40 = Enum.YLeaf(113, "im-attr-media-1000base-dwdm-1537-40")

    im_attr_media_1000base_dwdm_1536_61 = Enum.YLeaf(114, "im-attr-media-1000base-dwdm-1536-61")

    im_attr_media_1000base_dwdm_1535_82 = Enum.YLeaf(115, "im-attr-media-1000base-dwdm-1535-82")

    im_attr_media_1000base_dwdm_1535_04 = Enum.YLeaf(116, "im-attr-media-1000base-dwdm-1535-04")

    im_attr_media_1000base_dwdm_1534_25 = Enum.YLeaf(117, "im-attr-media-1000base-dwdm-1534-25")

    im_attr_media_1000base_dwdm_1533_47 = Enum.YLeaf(118, "im-attr-media-1000base-dwdm-1533-47")

    im_attr_media_1000base_dwdm_1532_68 = Enum.YLeaf(119, "im-attr-media-1000base-dwdm-1532-68")

    im_attr_media_1000base_dwdm_1531_90 = Enum.YLeaf(120, "im-attr-media-1000base-dwdm-1531-90")

    im_attr_media_1000base_dwdm_1531_12 = Enum.YLeaf(121, "im-attr-media-1000base-dwdm-1531-12")

    im_attr_media_1000base_dwdm_1530_33 = Enum.YLeaf(122, "im-attr-media-1000base-dwdm-1530-33")

    im_attr_media_1000base_dwdm_tunable = Enum.YLeaf(123, "im-attr-media-1000base-dwdm-tunable")

    im_attr_media_10gbase_dwdm_1561_42 = Enum.YLeaf(124, "im-attr-media-10gbase-dwdm-1561-42")

    im_attr_media_10gbase_dwdm_1560_61 = Enum.YLeaf(125, "im-attr-media-10gbase-dwdm-1560-61")

    im_attr_media_10gbase_dwdm_1559_79 = Enum.YLeaf(126, "im-attr-media-10gbase-dwdm-1559-79")

    im_attr_media_10gbase_dwdm_1558_98 = Enum.YLeaf(127, "im-attr-media-10gbase-dwdm-1558-98")

    im_attr_media_10gbase_dwdm_1558_17 = Enum.YLeaf(128, "im-attr-media-10gbase-dwdm-1558-17")

    im_attr_media_10gbase_dwdm_1557_36 = Enum.YLeaf(129, "im-attr-media-10gbase-dwdm-1557-36")

    im_attr_media_10gbase_dwdm_1556_55 = Enum.YLeaf(130, "im-attr-media-10gbase-dwdm-1556-55")

    im_attr_media_10gbase_dwdm_1555_75 = Enum.YLeaf(131, "im-attr-media-10gbase-dwdm-1555-75")

    im_attr_media_10gbase_dwdm_1554_94 = Enum.YLeaf(132, "im-attr-media-10gbase-dwdm-1554-94")

    im_attr_media_10gbase_dwdm_1554_13 = Enum.YLeaf(133, "im-attr-media-10gbase-dwdm-1554-13")

    im_attr_media_10gbase_dwdm_1553_33 = Enum.YLeaf(134, "im-attr-media-10gbase-dwdm-1553-33")

    im_attr_media_10gbase_dwdm_1552_52 = Enum.YLeaf(135, "im-attr-media-10gbase-dwdm-1552-52")

    im_attr_media_10gbase_dwdm_1551_72 = Enum.YLeaf(136, "im-attr-media-10gbase-dwdm-1551-72")

    im_attr_media_10gbase_dwdm_1550_92 = Enum.YLeaf(137, "im-attr-media-10gbase-dwdm-1550-92")

    im_attr_media_10gbase_dwdm_1550_12 = Enum.YLeaf(138, "im-attr-media-10gbase-dwdm-1550-12")

    im_attr_media_10gbase_dwdm_1549_32 = Enum.YLeaf(139, "im-attr-media-10gbase-dwdm-1549-32")

    im_attr_media_10gbase_dwdm_1548_51 = Enum.YLeaf(140, "im-attr-media-10gbase-dwdm-1548-51")

    im_attr_media_10gbase_dwdm_1547_72 = Enum.YLeaf(141, "im-attr-media-10gbase-dwdm-1547-72")

    im_attr_media_10gbase_dwdm_1546_92 = Enum.YLeaf(142, "im-attr-media-10gbase-dwdm-1546-92")

    im_attr_media_10gbase_dwdm_1546_12 = Enum.YLeaf(143, "im-attr-media-10gbase-dwdm-1546-12")

    im_attr_media_10gbase_dwdm_1545_32 = Enum.YLeaf(144, "im-attr-media-10gbase-dwdm-1545-32")

    im_attr_media_10gbase_dwdm_1544_53 = Enum.YLeaf(145, "im-attr-media-10gbase-dwdm-1544-53")

    im_attr_media_10gbase_dwdm_1543_73 = Enum.YLeaf(146, "im-attr-media-10gbase-dwdm-1543-73")

    im_attr_media_10gbase_dwdm_1542_94 = Enum.YLeaf(147, "im-attr-media-10gbase-dwdm-1542-94")

    im_attr_media_10gbase_dwdm_1542_14 = Enum.YLeaf(148, "im-attr-media-10gbase-dwdm-1542-14")

    im_attr_media_10gbase_dwdm_1541_35 = Enum.YLeaf(149, "im-attr-media-10gbase-dwdm-1541-35")

    im_attr_media_10gbase_dwdm_1540_56 = Enum.YLeaf(150, "im-attr-media-10gbase-dwdm-1540-56")

    im_attr_media_10gbase_dwdm_1539_77 = Enum.YLeaf(151, "im-attr-media-10gbase-dwdm-1539-77")

    im_attr_media_10gbase_dwdm_1538_98 = Enum.YLeaf(152, "im-attr-media-10gbase-dwdm-1538-98")

    im_attr_media_10gbase_dwdm_1538_19 = Enum.YLeaf(153, "im-attr-media-10gbase-dwdm-1538-19")

    im_attr_media_10gbase_dwdm_1537_40 = Enum.YLeaf(154, "im-attr-media-10gbase-dwdm-1537-40")

    im_attr_media_10gbase_dwdm_1536_61 = Enum.YLeaf(155, "im-attr-media-10gbase-dwdm-1536-61")

    im_attr_media_10gbase_dwdm_1535_82 = Enum.YLeaf(156, "im-attr-media-10gbase-dwdm-1535-82")

    im_attr_media_10gbase_dwdm_1535_04 = Enum.YLeaf(157, "im-attr-media-10gbase-dwdm-1535-04")

    im_attr_media_10gbase_dwdm_1534_25 = Enum.YLeaf(158, "im-attr-media-10gbase-dwdm-1534-25")

    im_attr_media_10gbase_dwdm_1533_47 = Enum.YLeaf(159, "im-attr-media-10gbase-dwdm-1533-47")

    im_attr_media_10gbase_dwdm_1532_68 = Enum.YLeaf(160, "im-attr-media-10gbase-dwdm-1532-68")

    im_attr_media_10gbase_dwdm_1531_90 = Enum.YLeaf(161, "im-attr-media-10gbase-dwdm-1531-90")

    im_attr_media_10gbase_dwdm_1531_12 = Enum.YLeaf(162, "im-attr-media-10gbase-dwdm-1531-12")

    im_attr_media_10gbase_dwdm_1530_33 = Enum.YLeaf(163, "im-attr-media-10gbase-dwdm-1530-33")

    im_attr_media_10gbase_dwdm_tunable = Enum.YLeaf(164, "im-attr-media-10gbase-dwdm-tunable")

    im_attr_media_40gbase_dwdm_1561_42 = Enum.YLeaf(165, "im-attr-media-40gbase-dwdm-1561-42")

    im_attr_media_40gbase_dwdm_1560_61 = Enum.YLeaf(166, "im-attr-media-40gbase-dwdm-1560-61")

    im_attr_media_40gbase_dwdm_1559_79 = Enum.YLeaf(167, "im-attr-media-40gbase-dwdm-1559-79")

    im_attr_media_40gbase_dwdm_1558_98 = Enum.YLeaf(168, "im-attr-media-40gbase-dwdm-1558-98")

    im_attr_media_40gbase_dwdm_1558_17 = Enum.YLeaf(169, "im-attr-media-40gbase-dwdm-1558-17")

    im_attr_media_40gbase_dwdm_1557_36 = Enum.YLeaf(170, "im-attr-media-40gbase-dwdm-1557-36")

    im_attr_media_40gbase_dwdm_1556_55 = Enum.YLeaf(171, "im-attr-media-40gbase-dwdm-1556-55")

    im_attr_media_40gbase_dwdm_1555_75 = Enum.YLeaf(172, "im-attr-media-40gbase-dwdm-1555-75")

    im_attr_media_40gbase_dwdm_1554_94 = Enum.YLeaf(173, "im-attr-media-40gbase-dwdm-1554-94")

    im_attr_media_40gbase_dwdm_1554_13 = Enum.YLeaf(174, "im-attr-media-40gbase-dwdm-1554-13")

    im_attr_media_40gbase_dwdm_1553_33 = Enum.YLeaf(175, "im-attr-media-40gbase-dwdm-1553-33")

    im_attr_media_40gbase_dwdm_1552_52 = Enum.YLeaf(176, "im-attr-media-40gbase-dwdm-1552-52")

    im_attr_media_40gbase_dwdm_1551_72 = Enum.YLeaf(177, "im-attr-media-40gbase-dwdm-1551-72")

    im_attr_media_40gbase_dwdm_1550_92 = Enum.YLeaf(178, "im-attr-media-40gbase-dwdm-1550-92")

    im_attr_media_40gbase_dwdm_1550_12 = Enum.YLeaf(179, "im-attr-media-40gbase-dwdm-1550-12")

    im_attr_media_40gbase_dwdm_1549_32 = Enum.YLeaf(180, "im-attr-media-40gbase-dwdm-1549-32")

    im_attr_media_40gbase_dwdm_1548_51 = Enum.YLeaf(181, "im-attr-media-40gbase-dwdm-1548-51")

    im_attr_media_40gbase_dwdm_1547_72 = Enum.YLeaf(182, "im-attr-media-40gbase-dwdm-1547-72")

    im_attr_media_40gbase_dwdm_1546_92 = Enum.YLeaf(183, "im-attr-media-40gbase-dwdm-1546-92")

    im_attr_media_40gbase_dwdm_1546_12 = Enum.YLeaf(184, "im-attr-media-40gbase-dwdm-1546-12")

    im_attr_media_40gbase_dwdm_1545_32 = Enum.YLeaf(185, "im-attr-media-40gbase-dwdm-1545-32")

    im_attr_media_40gbase_dwdm_1544_53 = Enum.YLeaf(186, "im-attr-media-40gbase-dwdm-1544-53")

    im_attr_media_40gbase_dwdm_1543_73 = Enum.YLeaf(187, "im-attr-media-40gbase-dwdm-1543-73")

    im_attr_media_40gbase_dwdm_1542_94 = Enum.YLeaf(188, "im-attr-media-40gbase-dwdm-1542-94")

    im_attr_media_40gbase_dwdm_1542_14 = Enum.YLeaf(189, "im-attr-media-40gbase-dwdm-1542-14")

    im_attr_media_40gbase_dwdm_1541_35 = Enum.YLeaf(190, "im-attr-media-40gbase-dwdm-1541-35")

    im_attr_media_40gbase_dwdm_1540_56 = Enum.YLeaf(191, "im-attr-media-40gbase-dwdm-1540-56")

    im_attr_media_40gbase_dwdm_1539_77 = Enum.YLeaf(192, "im-attr-media-40gbase-dwdm-1539-77")

    im_attr_media_40gbase_dwdm_1538_98 = Enum.YLeaf(193, "im-attr-media-40gbase-dwdm-1538-98")

    im_attr_media_40gbase_dwdm_1538_19 = Enum.YLeaf(194, "im-attr-media-40gbase-dwdm-1538-19")

    im_attr_media_40gbase_dwdm_1537_40 = Enum.YLeaf(195, "im-attr-media-40gbase-dwdm-1537-40")

    im_attr_media_40gbase_dwdm_1536_61 = Enum.YLeaf(196, "im-attr-media-40gbase-dwdm-1536-61")

    im_attr_media_40gbase_dwdm_1535_82 = Enum.YLeaf(197, "im-attr-media-40gbase-dwdm-1535-82")

    im_attr_media_40gbase_dwdm_1535_04 = Enum.YLeaf(198, "im-attr-media-40gbase-dwdm-1535-04")

    im_attr_media_40gbase_dwdm_1534_25 = Enum.YLeaf(199, "im-attr-media-40gbase-dwdm-1534-25")

    im_attr_media_40gbase_dwdm_1533_47 = Enum.YLeaf(200, "im-attr-media-40gbase-dwdm-1533-47")

    im_attr_media_40gbase_dwdm_1532_68 = Enum.YLeaf(201, "im-attr-media-40gbase-dwdm-1532-68")

    im_attr_media_40gbase_dwdm_1531_90 = Enum.YLeaf(202, "im-attr-media-40gbase-dwdm-1531-90")

    im_attr_media_40gbase_dwdm_1531_12 = Enum.YLeaf(203, "im-attr-media-40gbase-dwdm-1531-12")

    im_attr_media_40gbase_dwdm_1530_33 = Enum.YLeaf(204, "im-attr-media-40gbase-dwdm-1530-33")

    im_attr_media_40gbase_dwdm_tunable = Enum.YLeaf(205, "im-attr-media-40gbase-dwdm-tunable")

    im_attr_media_100gbase_dwdm_1561_42 = Enum.YLeaf(206, "im-attr-media-100gbase-dwdm-1561-42")

    im_attr_media_100gbase_dwdm_1560_61 = Enum.YLeaf(207, "im-attr-media-100gbase-dwdm-1560-61")

    im_attr_media_100gbase_dwdm_1559_79 = Enum.YLeaf(208, "im-attr-media-100gbase-dwdm-1559-79")

    im_attr_media_100gbase_dwdm_1558_98 = Enum.YLeaf(209, "im-attr-media-100gbase-dwdm-1558-98")

    im_attr_media_100gbase_dwdm_1558_17 = Enum.YLeaf(210, "im-attr-media-100gbase-dwdm-1558-17")

    im_attr_media_100gbase_dwdm_1557_36 = Enum.YLeaf(211, "im-attr-media-100gbase-dwdm-1557-36")

    im_attr_media_100gbase_dwdm_1556_55 = Enum.YLeaf(212, "im-attr-media-100gbase-dwdm-1556-55")

    im_attr_media_100gbase_dwdm_1555_75 = Enum.YLeaf(213, "im-attr-media-100gbase-dwdm-1555-75")

    im_attr_media_100gbase_dwdm_1554_94 = Enum.YLeaf(214, "im-attr-media-100gbase-dwdm-1554-94")

    im_attr_media_100gbase_dwdm_1554_13 = Enum.YLeaf(215, "im-attr-media-100gbase-dwdm-1554-13")

    im_attr_media_100gbase_dwdm_1553_33 = Enum.YLeaf(216, "im-attr-media-100gbase-dwdm-1553-33")

    im_attr_media_100gbase_dwdm_1552_52 = Enum.YLeaf(217, "im-attr-media-100gbase-dwdm-1552-52")

    im_attr_media_100gbase_dwdm_1551_72 = Enum.YLeaf(218, "im-attr-media-100gbase-dwdm-1551-72")

    im_attr_media_100gbase_dwdm_1550_92 = Enum.YLeaf(219, "im-attr-media-100gbase-dwdm-1550-92")

    im_attr_media_100gbase_dwdm_1550_12 = Enum.YLeaf(220, "im-attr-media-100gbase-dwdm-1550-12")

    im_attr_media_100gbase_dwdm_1549_32 = Enum.YLeaf(221, "im-attr-media-100gbase-dwdm-1549-32")

    im_attr_media_100gbase_dwdm_1548_51 = Enum.YLeaf(222, "im-attr-media-100gbase-dwdm-1548-51")

    im_attr_media_100gbase_dwdm_1547_72 = Enum.YLeaf(223, "im-attr-media-100gbase-dwdm-1547-72")

    im_attr_media_100gbase_dwdm_1546_92 = Enum.YLeaf(224, "im-attr-media-100gbase-dwdm-1546-92")

    im_attr_media_100gbase_dwdm_1546_12 = Enum.YLeaf(225, "im-attr-media-100gbase-dwdm-1546-12")

    im_attr_media_100gbase_dwdm_1545_32 = Enum.YLeaf(226, "im-attr-media-100gbase-dwdm-1545-32")

    im_attr_media_100gbase_dwdm_1544_53 = Enum.YLeaf(227, "im-attr-media-100gbase-dwdm-1544-53")

    im_attr_media_100gbase_dwdm_1543_73 = Enum.YLeaf(228, "im-attr-media-100gbase-dwdm-1543-73")

    im_attr_media_100gbase_dwdm_1542_94 = Enum.YLeaf(229, "im-attr-media-100gbase-dwdm-1542-94")

    im_attr_media_100gbase_dwdm_1542_14 = Enum.YLeaf(230, "im-attr-media-100gbase-dwdm-1542-14")

    im_attr_media_100gbase_dwdm_1541_35 = Enum.YLeaf(231, "im-attr-media-100gbase-dwdm-1541-35")

    im_attr_media_100gbase_dwdm_1540_56 = Enum.YLeaf(232, "im-attr-media-100gbase-dwdm-1540-56")

    im_attr_media_100gbase_dwdm_1539_77 = Enum.YLeaf(233, "im-attr-media-100gbase-dwdm-1539-77")

    im_attr_media_100gbase_dwdm_1538_98 = Enum.YLeaf(234, "im-attr-media-100gbase-dwdm-1538-98")

    im_attr_media_100gbase_dwdm_1538_19 = Enum.YLeaf(235, "im-attr-media-100gbase-dwdm-1538-19")

    im_attr_media_100gbase_dwdm_1537_40 = Enum.YLeaf(236, "im-attr-media-100gbase-dwdm-1537-40")

    im_attr_media_100gbase_dwdm_1536_61 = Enum.YLeaf(237, "im-attr-media-100gbase-dwdm-1536-61")

    im_attr_media_100gbase_dwdm_1535_82 = Enum.YLeaf(238, "im-attr-media-100gbase-dwdm-1535-82")

    im_attr_media_100gbase_dwdm_1535_04 = Enum.YLeaf(239, "im-attr-media-100gbase-dwdm-1535-04")

    im_attr_media_100gbase_dwdm_1534_25 = Enum.YLeaf(240, "im-attr-media-100gbase-dwdm-1534-25")

    im_attr_media_100gbase_dwdm_1533_47 = Enum.YLeaf(241, "im-attr-media-100gbase-dwdm-1533-47")

    im_attr_media_100gbase_dwdm_1532_68 = Enum.YLeaf(242, "im-attr-media-100gbase-dwdm-1532-68")

    im_attr_media_100gbase_dwdm_1531_90 = Enum.YLeaf(243, "im-attr-media-100gbase-dwdm-1531-90")

    im_attr_media_100gbase_dwdm_1531_12 = Enum.YLeaf(244, "im-attr-media-100gbase-dwdm-1531-12")

    im_attr_media_100gbase_dwdm_1530_33 = Enum.YLeaf(245, "im-attr-media-100gbase-dwdm-1530-33")

    im_attr_media_100gbase_dwdm_tunable = Enum.YLeaf(246, "im-attr-media-100gbase-dwdm-tunable")

    im_attr_media_40gbase_kr4 = Enum.YLeaf(247, "im-attr-media-40gbase-kr4")

    im_attr_media_40gbase_cr4 = Enum.YLeaf(248, "im-attr-media-40gbase-cr4")

    im_attr_media_40gbase_sr4 = Enum.YLeaf(249, "im-attr-media-40gbase-sr4")

    im_attr_media_40gbase_fr = Enum.YLeaf(250, "im-attr-media-40gbase-fr")

    im_attr_media_100gbase_cr10 = Enum.YLeaf(251, "im-attr-media-100gbase-cr10")

    im_attr_media_100gbase_sr10 = Enum.YLeaf(252, "im-attr-media-100gbase-sr10")

    im_attr_media_40gbase_csr4 = Enum.YLeaf(253, "im-attr-media-40gbase-csr4")

    im_attr_media_10gbase_cwdm = Enum.YLeaf(254, "im-attr-media-10gbase-cwdm")

    im_attr_media_10gbase_cwdm_tunable = Enum.YLeaf(255, "im-attr-media-10gbase-cwdm-tunable")

    im_attr_media_10gbase_cwdm_1470 = Enum.YLeaf(256, "im-attr-media-10gbase-cwdm-1470")

    im_attr_media_10gbase_cwdm_1490 = Enum.YLeaf(257, "im-attr-media-10gbase-cwdm-1490")

    im_attr_media_10gbase_cwdm_1510 = Enum.YLeaf(258, "im-attr-media-10gbase-cwdm-1510")

    im_attr_media_10gbase_cwdm_1530 = Enum.YLeaf(259, "im-attr-media-10gbase-cwdm-1530")

    im_attr_media_10gbase_cwdm_1550 = Enum.YLeaf(260, "im-attr-media-10gbase-cwdm-1550")

    im_attr_media_10gbase_cwdm_1570 = Enum.YLeaf(261, "im-attr-media-10gbase-cwdm-1570")

    im_attr_media_10gbase_cwdm_1590 = Enum.YLeaf(262, "im-attr-media-10gbase-cwdm-1590")

    im_attr_media_10gbase_cwdm_1610 = Enum.YLeaf(263, "im-attr-media-10gbase-cwdm-1610")

    im_attr_media_40gbase_cwdm = Enum.YLeaf(264, "im-attr-media-40gbase-cwdm")

    im_attr_media_40gbase_cwdm_tunable = Enum.YLeaf(265, "im-attr-media-40gbase-cwdm-tunable")

    im_attr_media_40gbase_cwdm_1470 = Enum.YLeaf(266, "im-attr-media-40gbase-cwdm-1470")

    im_attr_media_40gbase_cwdm_1490 = Enum.YLeaf(267, "im-attr-media-40gbase-cwdm-1490")

    im_attr_media_40gbase_cwdm_1510 = Enum.YLeaf(268, "im-attr-media-40gbase-cwdm-1510")

    im_attr_media_40gbase_cwdm_1530 = Enum.YLeaf(269, "im-attr-media-40gbase-cwdm-1530")

    im_attr_media_40gbase_cwdm_1550 = Enum.YLeaf(270, "im-attr-media-40gbase-cwdm-1550")

    im_attr_media_40gbase_cwdm_1570 = Enum.YLeaf(271, "im-attr-media-40gbase-cwdm-1570")

    im_attr_media_40gbase_cwdm_1590 = Enum.YLeaf(272, "im-attr-media-40gbase-cwdm-1590")

    im_attr_media_40gbase_cwdm_1610 = Enum.YLeaf(273, "im-attr-media-40gbase-cwdm-1610")

    im_attr_media_100gbase_cwdm = Enum.YLeaf(274, "im-attr-media-100gbase-cwdm")

    im_attr_media_100gbase_cwdm_tunable = Enum.YLeaf(275, "im-attr-media-100gbase-cwdm-tunable")

    im_attr_media_100gbase_cwdm_1470 = Enum.YLeaf(276, "im-attr-media-100gbase-cwdm-1470")

    im_attr_media_100gbase_cwdm_1490 = Enum.YLeaf(277, "im-attr-media-100gbase-cwdm-1490")

    im_attr_media_100gbase_cwdm_1510 = Enum.YLeaf(278, "im-attr-media-100gbase-cwdm-1510")

    im_attr_media_100gbase_cwdm_1530 = Enum.YLeaf(279, "im-attr-media-100gbase-cwdm-1530")

    im_attr_media_100gbase_cwdm_1550 = Enum.YLeaf(280, "im-attr-media-100gbase-cwdm-1550")

    im_attr_media_100gbase_cwdm_1570 = Enum.YLeaf(281, "im-attr-media-100gbase-cwdm-1570")

    im_attr_media_100gbase_cwdm_1590 = Enum.YLeaf(282, "im-attr-media-100gbase-cwdm-1590")

    im_attr_media_100gbase_cwdm_1610 = Enum.YLeaf(283, "im-attr-media-100gbase-cwdm-1610")

    im_attr_media_40gbase_elpb = Enum.YLeaf(284, "im-attr-media-40gbase-elpb")

    im_attr_media_100gbase_elpb = Enum.YLeaf(285, "im-attr-media-100gbase-elpb")

    im_attr_media_100gbase_lr10 = Enum.YLeaf(286, "im-attr-media-100gbase-lr10")

    im_attr_media_40gbase = Enum.YLeaf(287, "im-attr-media-40gbase")

    im_attr_media_100gbase_kp4 = Enum.YLeaf(288, "im-attr-media-100gbase-kp4")

    im_attr_media_100gbase_kr4 = Enum.YLeaf(289, "im-attr-media-100gbase-kr4")

    im_attr_media_10gbase_lrm = Enum.YLeaf(290, "im-attr-media-10gbase-lrm")

    im_attr_media_10gbase_cx4 = Enum.YLeaf(291, "im-attr-media-10gbase-cx4")

    im_attr_media_10gbase = Enum.YLeaf(292, "im-attr-media-10gbase")

    im_attr_media_10gbase_kx4 = Enum.YLeaf(293, "im-attr-media-10gbase-kx4")

    im_attr_media_10gbase_kr = Enum.YLeaf(294, "im-attr-media-10gbase-kr")

    im_attr_media_10gbase_pr = Enum.YLeaf(295, "im-attr-media-10gbase-pr")

    im_attr_media_100base_lx = Enum.YLeaf(296, "im-attr-media-100base-lx")

    im_attr_media_100base_zx = Enum.YLeaf(297, "im-attr-media-100base-zx")

    im_attr_media_1000base_bx_d = Enum.YLeaf(298, "im-attr-media-1000base-bx-d")

    im_attr_media_1000base_bx_u = Enum.YLeaf(299, "im-attr-media-1000base-bx-u")

    im_attr_media_1000base_bx20_d = Enum.YLeaf(300, "im-attr-media-1000base-bx20-d")

    im_attr_media_1000base_bx20_u = Enum.YLeaf(301, "im-attr-media-1000base-bx20-u")

    im_attr_media_1000base_bx40_d = Enum.YLeaf(302, "im-attr-media-1000base-bx40-d")

    im_attr_media_1000base_bx40_da = Enum.YLeaf(303, "im-attr-media-1000base-bx40-da")

    im_attr_media_1000base_bx40_u = Enum.YLeaf(304, "im-attr-media-1000base-bx40-u")

    im_attr_media_1000base_bx80_d = Enum.YLeaf(305, "im-attr-media-1000base-bx80-d")

    im_attr_media_1000base_bx80_u = Enum.YLeaf(306, "im-attr-media-1000base-bx80-u")

    im_attr_media_1000base_bx120_d = Enum.YLeaf(307, "im-attr-media-1000base-bx120-d")

    im_attr_media_1000base_bx120_u = Enum.YLeaf(308, "im-attr-media-1000base-bx120-u")

    im_attr_media_10gbase_bx_d = Enum.YLeaf(309, "im-attr-media-10gbase-bx-d")

    im_attr_media_10gbase_bx_u = Enum.YLeaf(310, "im-attr-media-10gbase-bx-u")

    im_attr_media_10gbase_bx10_d = Enum.YLeaf(311, "im-attr-media-10gbase-bx10-d")

    im_attr_media_10gbase_bx10_u = Enum.YLeaf(312, "im-attr-media-10gbase-bx10-u")

    im_attr_media_10gbase_bx20_d = Enum.YLeaf(313, "im-attr-media-10gbase-bx20-d")

    im_attr_media_10gbase_bx20_u = Enum.YLeaf(314, "im-attr-media-10gbase-bx20-u")

    im_attr_media_10gbase_bx40_d = Enum.YLeaf(315, "im-attr-media-10gbase-bx40-d")

    im_attr_media_10gbase_bx40_u = Enum.YLeaf(316, "im-attr-media-10gbase-bx40-u")

    im_attr_media_10gbase_bx80_d = Enum.YLeaf(317, "im-attr-media-10gbase-bx80-d")

    im_attr_media_10gbase_bx80_u = Enum.YLeaf(318, "im-attr-media-10gbase-bx80-u")

    im_attr_media_10gbase_bx120_d = Enum.YLeaf(319, "im-attr-media-10gbase-bx120-d")

    im_attr_media_10gbase_bx120_u = Enum.YLeaf(320, "im-attr-media-10gbase-bx120-u")

    im_attr_media_1000base_dr_lx = Enum.YLeaf(321, "im-attr-media-1000base-dr-lx")

    im_attr_media_100gbase_er4l = Enum.YLeaf(322, "im-attr-media-100gbase-er4l")

    im_attr_media_100gbase_sr4 = Enum.YLeaf(323, "im-attr-media-100gbase-sr4")

    im_attr_media_40gbase_sr_bd = Enum.YLeaf(324, "im-attr-media-40gbase-sr-bd")

    im_attr_media_25gbase_cr = Enum.YLeaf(325, "im-attr-media-25gbase-cr")

    im_attr_media_25gbase_cr_s = Enum.YLeaf(326, "im-attr-media-25gbase-cr-s")

    im_attr_media_25gbase_kr = Enum.YLeaf(327, "im-attr-media-25gbase-kr")

    im_attr_media_25gbase_kr_s = Enum.YLeaf(328, "im-attr-media-25gbase-kr-s")

    im_attr_media_25gbase_r = Enum.YLeaf(329, "im-attr-media-25gbase-r")

    im_attr_media_25gbase_sr = Enum.YLeaf(330, "im-attr-media-25gbase-sr")

    im_attr_media_25gbase_dwdm = Enum.YLeaf(331, "im-attr-media-25gbase-dwdm")

    im_attr_media_25gbase_dwdm_tunable = Enum.YLeaf(332, "im-attr-media-25gbase-dwdm-tunable")

    im_attr_media_25gbase_cwdm = Enum.YLeaf(333, "im-attr-media-25gbase-cwdm")

    im_attr_media_25gbase_cwdm_tunable = Enum.YLeaf(334, "im-attr-media-25gbase-cwdm-tunable")

    im_attr_media_100gbase_psm4 = Enum.YLeaf(335, "im-attr-media-100gbase-psm4")

    im_attr_media_100gbase_er10 = Enum.YLeaf(336, "im-attr-media-100gbase-er10")

    im_attr_media_100gbase_er10l = Enum.YLeaf(337, "im-attr-media-100gbase-er10l")

    im_attr_media_100gbase_acc = Enum.YLeaf(338, "im-attr-media-100gbase-acc")

    im_attr_media_100gbase_aoc = Enum.YLeaf(339, "im-attr-media-100gbase-aoc")

    im_attr_media_100gbase_cwdm4 = Enum.YLeaf(340, "im-attr-media-100gbase-cwdm4")

    im_attr_media_40gbase_psm4 = Enum.YLeaf(341, "im-attr-media-40gbase-psm4")

    im_attr_media_100gbase_cr4 = Enum.YLeaf(342, "im-attr-media-100gbase-cr4")

    im_attr_media_100gbase_act_loop = Enum.YLeaf(343, "im-attr-media-100gbase-act-loop")

    im_attr_media_100gbase_pas_loop = Enum.YLeaf(344, "im-attr-media-100gbase-pas-loop")

    im_attr_media_50gbase_cr2 = Enum.YLeaf(345, "im-attr-media-50gbase-cr2")

    im_attr_media_50gbase_sr2 = Enum.YLeaf(346, "im-attr-media-50gbase-sr2")

    im_attr_media_50gbase_psm2 = Enum.YLeaf(347, "im-attr-media-50gbase-psm2")

    im_attr_media_200gbase_cr4 = Enum.YLeaf(348, "im-attr-media-200gbase-cr4")

    im_attr_media_400gbase_fr4 = Enum.YLeaf(349, "im-attr-media-400gbase-fr4")

    im_attr_media_400gbase_dr4 = Enum.YLeaf(350, "im-attr-media-400gbase-dr4")

    im_attr_media_400gbase_cr4 = Enum.YLeaf(351, "im-attr-media-400gbase-cr4")

    im_attr_media_10gbase_cr = Enum.YLeaf(352, "im-attr-media-10gbase-cr")

    im_attr_media_10gbase_aoc = Enum.YLeaf(353, "im-attr-media-10gbase-aoc")

    im_attr_media_40gbase_aoc = Enum.YLeaf(354, "im-attr-media-40gbase-aoc")

    im_attr_media_40gbase_acu = Enum.YLeaf(355, "im-attr-media-40gbase-acu")

    im_attr_media_100gbase_acu = Enum.YLeaf(356, "im-attr-media-100gbase-acu")

    im_attr_media_10gbase_cu1m = Enum.YLeaf(357, "im-attr-media-10gbase-cu1m")

    im_attr_media_10gbase_cu3m = Enum.YLeaf(358, "im-attr-media-10gbase-cu3m")

    im_attr_media_10gbase_cu5m = Enum.YLeaf(359, "im-attr-media-10gbase-cu5m")

    im_attr_media_10gbase_acu7m = Enum.YLeaf(360, "im-attr-media-10gbase-acu7m")

    im_attr_media_10gbase_acu10m = Enum.YLeaf(361, "im-attr-media-10gbase-acu10m")

    im_attr_media_4x10g_base_lr = Enum.YLeaf(362, "im-attr-media-4x10g-base-lr")

    im_attr_media_10gbase_cu1_5m = Enum.YLeaf(363, "im-attr-media-10gbase-cu1-5m")

    im_attr_media_10gbase_cu2m = Enum.YLeaf(364, "im-attr-media-10gbase-cu2m")

    im_attr_media_10gbase_cu2_5m = Enum.YLeaf(365, "im-attr-media-10gbase-cu2-5m")

    im_attr_media_10gbase_aoc1m = Enum.YLeaf(366, "im-attr-media-10gbase-aoc1m")

    im_attr_media_10gbase_aoc2m = Enum.YLeaf(367, "im-attr-media-10gbase-aoc2m")

    im_attr_media_10gbase_aoc3m = Enum.YLeaf(368, "im-attr-media-10gbase-aoc3m")

    im_attr_media_10gbase_aoc5m = Enum.YLeaf(369, "im-attr-media-10gbase-aoc5m")

    im_attr_media_10gbase_aoc7m = Enum.YLeaf(370, "im-attr-media-10gbase-aoc7m")

    im_attr_media_10gbase_aoc10m = Enum.YLeaf(371, "im-attr-media-10gbase-aoc10m")

    im_attr_media_40gbase_acu1m = Enum.YLeaf(372, "im-attr-media-40gbase-acu1m")

    im_attr_media_40gbase_acu3m = Enum.YLeaf(373, "im-attr-media-40gbase-acu3m")

    im_attr_media_40gbase_acu5m = Enum.YLeaf(374, "im-attr-media-40gbase-acu5m")

    im_attr_media_40gbase_acu7m = Enum.YLeaf(375, "im-attr-media-40gbase-acu7m")

    im_attr_media_40gbase_acu10m = Enum.YLeaf(376, "im-attr-media-40gbase-acu10m")

    im_attr_media_25gbase_cu1m = Enum.YLeaf(377, "im-attr-media-25gbase-cu1m")

    im_attr_media_25gbase_cu2m = Enum.YLeaf(378, "im-attr-media-25gbase-cu2m")

    im_attr_media_25gbase_cu3m = Enum.YLeaf(379, "im-attr-media-25gbase-cu3m")

    im_attr_media_25gbase_cu5m = Enum.YLeaf(380, "im-attr-media-25gbase-cu5m")

    im_attr_media_100gbase_sm_sr = Enum.YLeaf(381, "im-attr-media-100gbase-sm-sr")


class ImAttrTransportMode(Enum):
    """
    ImAttrTransportMode (Enum Class)

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

    im_attr_transport_mode_unknown = Enum.YLeaf(0, "im-attr-transport-mode-unknown")

    im_attr_transport_mode_lan = Enum.YLeaf(1, "im-attr-transport-mode-lan")

    im_attr_transport_mode_wan = Enum.YLeaf(2, "im-attr-transport-mode-wan")

    im_attr_transport_mode_otn_bt_opu1e = Enum.YLeaf(3, "im-attr-transport-mode-otn-bt-opu1e")

    im_attr_transport_mode_otn_bt_opu2e = Enum.YLeaf(4, "im-attr-transport-mode-otn-bt-opu2e")

    im_attr_transport_mode_otn_opu3 = Enum.YLeaf(5, "im-attr-transport-mode-otn-opu3")

    im_attr_transport_mode_otn_opu4 = Enum.YLeaf(6, "im-attr-transport-mode-otn-opu4")


class ImCmdEncapsEnum(Enum):
    """
    ImCmdEncapsEnum (Enum Class)

    Im cmd encaps enum

    .. data:: frame_relay = 0

    	frame relay

    .. data:: vlan = 1

    	vlan

    .. data:: ppp = 2

    	ppp

    """

    frame_relay = Enum.YLeaf(0, "frame-relay")

    vlan = Enum.YLeaf(1, "vlan")

    ppp = Enum.YLeaf(2, "ppp")


class ImCmdFrTypeEnum(Enum):
    """
    ImCmdFrTypeEnum (Enum Class)

    Im cmd fr type enum

    .. data:: frame_relay_cisco = 0

    	frame relay cisco

    .. data:: frame_relay_ietf = 1

    	frame relay ietf

    """

    frame_relay_cisco = Enum.YLeaf(0, "frame-relay-cisco")

    frame_relay_ietf = Enum.YLeaf(1, "frame-relay-ietf")


class ImCmdIntfTypeEnum(Enum):
    """
    ImCmdIntfTypeEnum (Enum Class)

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

    srp = Enum.YLeaf(0, "srp")

    tunnel = Enum.YLeaf(1, "tunnel")

    bundle = Enum.YLeaf(2, "bundle")

    serial = Enum.YLeaf(3, "serial")

    sonet_pos = Enum.YLeaf(4, "sonet-pos")

    tunnel_gre = Enum.YLeaf(5, "tunnel-gre")

    pseudowire_head_end = Enum.YLeaf(6, "pseudowire-head-end")

    cem = Enum.YLeaf(7, "cem")

    gcc = Enum.YLeaf(8, "gcc")


class ImCmdLmiTypeEnum(Enum):
    """
    ImCmdLmiTypeEnum (Enum Class)

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

    lmi_type_auto = Enum.YLeaf(0, "lmi-type-auto")

    lmi_type_ansi = Enum.YLeaf(1, "lmi-type-ansi")

    lmi_type_ccitt = Enum.YLeaf(2, "lmi-type-ccitt")

    lmi_type_cisco = Enum.YLeaf(3, "lmi-type-cisco")


class ImCmdLoopbackEnum(Enum):
    """
    ImCmdLoopbackEnum (Enum Class)

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

    no_loopback = Enum.YLeaf(0, "no-loopback")

    internal_loopback = Enum.YLeaf(1, "internal-loopback")

    external_loopback = Enum.YLeaf(2, "external-loopback")

    line_loopback = Enum.YLeaf(3, "line-loopback")


class ImCmdStatsEnum(Enum):
    """
    ImCmdStatsEnum (Enum Class)

    List of different interface stats structures

    .. data:: full = 1

    	full

    .. data:: basic = 2

    	basic

    """

    full = Enum.YLeaf(1, "full")

    basic = Enum.YLeaf(2, "basic")


class ImStateEnum(Enum):
    """
    ImStateEnum (Enum Class)

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

    im_state_not_ready = Enum.YLeaf(0, "im-state-not-ready")

    im_state_admin_down = Enum.YLeaf(1, "im-state-admin-down")

    im_state_down = Enum.YLeaf(2, "im-state-down")

    im_state_up = Enum.YLeaf(3, "im-state-up")

    im_state_shutdown = Enum.YLeaf(4, "im-state-shutdown")

    im_state_err_disable = Enum.YLeaf(5, "im-state-err-disable")

    im_state_down_immediate = Enum.YLeaf(6, "im-state-down-immediate")

    im_state_down_immediate_admin = Enum.YLeaf(7, "im-state-down-immediate-admin")

    im_state_down_graceful = Enum.YLeaf(8, "im-state-down-graceful")

    im_state_begin_shutdown = Enum.YLeaf(9, "im-state-begin-shutdown")

    im_state_end_shutdown = Enum.YLeaf(10, "im-state-end-shutdown")

    im_state_begin_error_disable = Enum.YLeaf(11, "im-state-begin-error-disable")

    im_state_end_error_disable = Enum.YLeaf(12, "im-state-end-error-disable")

    im_state_begin_down_graceful = Enum.YLeaf(13, "im-state-begin-down-graceful")

    im_state_reset = Enum.YLeaf(14, "im-state-reset")

    im_state_operational = Enum.YLeaf(15, "im-state-operational")

    im_state_not_operational = Enum.YLeaf(16, "im-state-not-operational")

    im_state_unknown = Enum.YLeaf(17, "im-state-unknown")

    im_state_last = Enum.YLeaf(18, "im-state-last")


class InterfaceTypeSet(Enum):
    """
    InterfaceTypeSet (Enum Class)

    Interface type set

    .. data:: hardware_interfaces = 0

    	Restrict the output to hardware interfaces only

    """

    hardware_interfaces = Enum.YLeaf(0, "hardware-interfaces")


class NcpIdent(Enum):
    """
    NcpIdent (Enum Class)

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

    cdpcp = Enum.YLeaf(1, "cdpcp")

    ipcp = Enum.YLeaf(2, "ipcp")

    ipcpiw = Enum.YLeaf(3, "ipcpiw")

    ipv6cp = Enum.YLeaf(4, "ipv6cp")

    mplscp = Enum.YLeaf(5, "mplscp")

    osicp = Enum.YLeaf(6, "osicp")


class PppFsmState(Enum):
    """
    PppFsmState (Enum Class)

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

    ppp_fsm_state_initial_0 = Enum.YLeaf(0, "ppp-fsm-state-initial-0")

    ppp_fsm_state_starting_1 = Enum.YLeaf(1, "ppp-fsm-state-starting-1")

    ppp_fsm_state_closed_2 = Enum.YLeaf(2, "ppp-fsm-state-closed-2")

    ppp_fsm_state_stopped_3 = Enum.YLeaf(3, "ppp-fsm-state-stopped-3")

    ppp_fsm_state_closing_4 = Enum.YLeaf(4, "ppp-fsm-state-closing-4")

    ppp_fsm_state_stopping_5 = Enum.YLeaf(5, "ppp-fsm-state-stopping-5")

    ppp_fsm_state_req_sent_6 = Enum.YLeaf(6, "ppp-fsm-state-req-sent-6")

    ppp_fsm_state_ack_rcvd_7 = Enum.YLeaf(7, "ppp-fsm-state-ack-rcvd-7")

    ppp_fsm_state_ack_sent_8 = Enum.YLeaf(8, "ppp-fsm-state-ack-sent-8")

    ppp_fsm_state_opened_9 = Enum.YLeaf(9, "ppp-fsm-state-opened-9")


class SonetApsEt(Enum):
    """
    SonetApsEt (Enum Class)

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

    not_configured = Enum.YLeaf(0, "not-configured")

    working_active = Enum.YLeaf(1, "working-active")

    protect_active = Enum.YLeaf(2, "protect-active")

    working_inactive = Enum.YLeaf(3, "working-inactive")

    protect_inactive = Enum.YLeaf(4, "protect-inactive")


class SrpMgmtFailureEt(Enum):
    """
    SrpMgmtFailureEt (Enum Class)

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

    hardware_missing_failure = Enum.YLeaf(0, "hardware-missing-failure")

    layer1_admin_state_failure = Enum.YLeaf(1, "layer1-admin-state-failure")

    layer1_error_failure = Enum.YLeaf(2, "layer1-error-failure")

    keepalive_missed_failure = Enum.YLeaf(3, "keepalive-missed-failure")

    link_quality_degraded_failure = Enum.YLeaf(4, "link-quality-degraded-failure")

    mate_problem_failure = Enum.YLeaf(5, "mate-problem-failure")

    side_mismatch_failure = Enum.YLeaf(6, "side-mismatch-failure")

    unknown_failure = Enum.YLeaf(7, "unknown-failure")


class SrpMgmtFailureStateEt(Enum):
    """
    SrpMgmtFailureStateEt (Enum Class)

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

    idle_failure_state = Enum.YLeaf(0, "idle-failure-state")

    wait_to_restore_failure_state = Enum.YLeaf(1, "wait-to-restore-failure-state")

    manual_switch_failure_state = Enum.YLeaf(2, "manual-switch-failure-state")

    signal_degrade_failure_state = Enum.YLeaf(3, "signal-degrade-failure-state")

    signal_fail_failure_state = Enum.YLeaf(4, "signal-fail-failure-state")

    forced_switch_failure_state = Enum.YLeaf(5, "forced-switch-failure-state")

    shutdown_failure_state = Enum.YLeaf(6, "shutdown-failure-state")

    invalid_failure_state = Enum.YLeaf(7, "invalid-failure-state")

    unknown_failure_state = Enum.YLeaf(8, "unknown-failure-state")


class SrpMgmtIpsPathInd(Enum):
    """
    SrpMgmtIpsPathInd (Enum Class)

    SRP IPS path indication

    .. data:: short_path = 0

    	SHORT

    .. data:: long_path = 1

    	LONG

    .. data:: unknown_path = 2

    	UNKNOWN

    """

    short_path = Enum.YLeaf(0, "short-path")

    long_path = Enum.YLeaf(1, "long-path")

    unknown_path = Enum.YLeaf(2, "unknown-path")


class SrpMgmtIpsReq(Enum):
    """
    SrpMgmtIpsReq (Enum Class)

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

    idle_ips_request = Enum.YLeaf(0, "idle-ips-request")

    wait_to_restore_ips_request = Enum.YLeaf(1, "wait-to-restore-ips-request")

    manual_switch_ips_request = Enum.YLeaf(2, "manual-switch-ips-request")

    signal_degrade_ips_request = Enum.YLeaf(3, "signal-degrade-ips-request")

    signal_fail_ips_request = Enum.YLeaf(4, "signal-fail-ips-request")

    forced_switch_ips_request = Enum.YLeaf(5, "forced-switch-ips-request")

    unknown_ips_request = Enum.YLeaf(6, "unknown-ips-request")


class SrpMgmtIpsWrapState(Enum):
    """
    SrpMgmtIpsWrapState (Enum Class)

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

    idle_wrap_state = Enum.YLeaf(0, "idle-wrap-state")

    wrapped_state = Enum.YLeaf(1, "wrapped-state")

    locked_out_wrap_state = Enum.YLeaf(2, "locked-out-wrap-state")

    unknown_wrap_state = Enum.YLeaf(3, "unknown-wrap-state")


class SrpMgmtSrrFailure(Enum):
    """
    SrpMgmtSrrFailure (Enum Class)

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

    idle_srr_failure = Enum.YLeaf(0, "idle-srr-failure")

    wait_to_restore_srr_failure = Enum.YLeaf(1, "wait-to-restore-srr-failure")

    signal_fail_srr_failure = Enum.YLeaf(2, "signal-fail-srr-failure")

    forced_switch_srr_failure = Enum.YLeaf(3, "forced-switch-srr-failure")

    unknown_srr_failure = Enum.YLeaf(4, "unknown-srr-failure")


class SrpMgmtSrrNodeState(Enum):
    """
    SrpMgmtSrrNodeState (Enum Class)

    SRP SRR node state

    .. data:: idle_srr_state = 0

    	Idle

    .. data:: discovery_srr_state = 1

    	Discovery

    .. data:: unknown_srr_state = 2

    	UNKNOWN

    """

    idle_srr_state = Enum.YLeaf(0, "idle-srr-state")

    discovery_srr_state = Enum.YLeaf(1, "discovery-srr-state")

    unknown_srr_state = Enum.YLeaf(2, "unknown-srr-state")


class StatsCounter(Enum):
    """
    StatsCounter (Enum Class)

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

    .. data:: stats_counter_ipv4_bgp_pa = 9

    	stats counter ipv4 bgp pa

    .. data:: stats_counter_src_bgp_pa = 10

    	stats counter src bgp pa

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

    stats_counter_rate = Enum.YLeaf(0, "stats-counter-rate")

    stats_counter_uint32 = Enum.YLeaf(1, "stats-counter-uint32")

    stats_counter_uint64 = Enum.YLeaf(2, "stats-counter-uint64")

    stats_counter_generic = Enum.YLeaf(3, "stats-counter-generic")

    stats_counter_proto = Enum.YLeaf(4, "stats-counter-proto")

    stats_counter_srp = Enum.YLeaf(5, "stats-counter-srp")

    stats_counter_ipv4_prec = Enum.YLeaf(6, "stats-counter-ipv4-prec")

    stats_counter_ipv4_dscp = Enum.YLeaf(7, "stats-counter-ipv4-dscp")

    stats_counter_mpls_exp = Enum.YLeaf(8, "stats-counter-mpls-exp")

    stats_counter_ipv4_bgp_pa = Enum.YLeaf(9, "stats-counter-ipv4-bgp-pa")

    stats_counter_src_bgp_pa = Enum.YLeaf(10, "stats-counter-src-bgp-pa")

    stats_counter_basic = Enum.YLeaf(11, "stats-counter-basic")

    stats_counter_comp_generic = Enum.YLeaf(12, "stats-counter-comp-generic")

    stats_counter_comp_proto = Enum.YLeaf(13, "stats-counter-comp-proto")

    stats_counter_comp_basic = Enum.YLeaf(14, "stats-counter-comp-basic")

    stats_counter_accounting = Enum.YLeaf(15, "stats-counter-accounting")

    stats_counter_comp_accounting = Enum.YLeaf(16, "stats-counter-comp-accounting")

    stats_counter_flow = Enum.YLeaf(17, "stats-counter-flow")

    stats_counter_comp_flow = Enum.YLeaf(18, "stats-counter-comp-flow")


class StatsId(Enum):
    """
    StatsId (Enum Class)

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

    stats_id_type_unknown = Enum.YLeaf(0, "stats-id-type-unknown")

    stats_id_type_min = Enum.YLeaf(1, "stats-id-type-min")

    stats_id_type_spare = Enum.YLeaf(2, "stats-id-type-spare")

    stats_id_type_node = Enum.YLeaf(3, "stats-id-type-node")

    stats_id_type_other = Enum.YLeaf(4, "stats-id-type-other")

    stats_id_type_feature = Enum.YLeaf(5, "stats-id-type-feature")

    stats_id_type_max = Enum.YLeaf(6, "stats-id-type-max")


class StatsTypeContents(Enum):
    """
    StatsTypeContents (Enum Class)

    Stats type contents

    .. data:: stats_type_single = 100

    	stats type single

    .. data:: stats_type_variable = 101

    	stats type variable

    """

    stats_type_single = Enum.YLeaf(100, "stats-type-single")

    stats_type_variable = Enum.YLeaf(101, "stats-type-variable")


class TunlIpModeDir(Enum):
    """
    TunlIpModeDir (Enum Class)

    Tunl ip mode dir

    .. data:: tunl_ip_mode_dir_none = 0

    	tunl ip mode dir none

    .. data:: tunl_ip_mode_dir_decap = 1

    	tunl ip mode dir decap

    .. data:: tunl_ip_mode_dir_encap = 2

    	tunl ip mode dir encap

    .. data:: tunl_ip_mode_dir_max = 3

    	tunl ip mode dir max

    """

    tunl_ip_mode_dir_none = Enum.YLeaf(0, "tunl-ip-mode-dir-none")

    tunl_ip_mode_dir_decap = Enum.YLeaf(1, "tunl-ip-mode-dir-decap")

    tunl_ip_mode_dir_encap = Enum.YLeaf(2, "tunl-ip-mode-dir-encap")

    tunl_ip_mode_dir_max = Enum.YLeaf(3, "tunl-ip-mode-dir-max")


class TunlPfiAfId(Enum):
    """
    TunlPfiAfId (Enum Class)

    Tunl pfi af id

    .. data:: tunl_pfi_af_id_none = 0

    	Unspecified AFI

    .. data:: tunl_pfi_af_id_ipv4 = 2

    	IPv4 AFI

    .. data:: tunl_pfi_af_id_ipv6 = 10

    	IPv6 AFI

    """

    tunl_pfi_af_id_none = Enum.YLeaf(0, "tunl-pfi-af-id-none")

    tunl_pfi_af_id_ipv4 = Enum.YLeaf(2, "tunl-pfi-af-id-ipv4")

    tunl_pfi_af_id_ipv6 = Enum.YLeaf(10, "tunl-pfi-af-id-ipv6")


class TunnelGreMode(Enum):
    """
    TunnelGreMode (Enum Class)

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

    unknown = Enum.YLeaf(0, "unknown")

    gr_eo_ipv4 = Enum.YLeaf(1, "gr-eo-ipv4")

    gr_eo_ipv6 = Enum.YLeaf(2, "gr-eo-ipv6")

    mgr_eo_ipv4 = Enum.YLeaf(3, "mgr-eo-ipv4")

    mgr_eo_ipv6 = Enum.YLeaf(4, "mgr-eo-ipv6")

    ipv4 = Enum.YLeaf(5, "ipv4")

    ipv6 = Enum.YLeaf(6, "ipv6")


class TunnelKaDfState(Enum):
    """
    TunnelKaDfState (Enum Class)

    Tunnel ka df state

    .. data:: disable = 0

    	Tunnel GRE KA State is Disabled

    .. data:: enable = 1

    	Tunnel GRE KA State is Enabled

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class TunnelKeyState(Enum):
    """
    TunnelKeyState (Enum Class)

    Tunnel key state

    .. data:: absent = 0

    	Tunnel GRE Key is not present

    .. data:: present = 1

    	Tunnel GRE Key is present

    """

    absent = Enum.YLeaf(0, "absent")

    present = Enum.YLeaf(1, "present")


class VlanEncaps(Enum):
    """
    VlanEncaps (Enum Class)

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

    no_encapsulation = Enum.YLeaf(0, "no-encapsulation")

    dot1q = Enum.YLeaf(1, "dot1q")

    qinq = Enum.YLeaf(2, "qinq")

    qin_any = Enum.YLeaf(3, "qin-any")

    dot1q_native = Enum.YLeaf(4, "dot1q-native")

    dot1ad = Enum.YLeaf(5, "dot1ad")

    dot1ad_native = Enum.YLeaf(6, "dot1ad-native")

    service_instance = Enum.YLeaf(7, "service-instance")

    dot1ad_dot1q = Enum.YLeaf(8, "dot1ad-dot1q")

    dot1ad_any = Enum.YLeaf(9, "dot1ad-any")


class VlanSwitchedMode(Enum):
    """
    VlanSwitchedMode (Enum Class)

    VLAN\-Switched mode

    .. data:: none = 0

    	Disabled

    .. data:: trunk_port = 1

    	Trunk port

    .. data:: access_port = 2

    	Access port

    """

    none = Enum.YLeaf(0, "none")

    trunk_port = Enum.YLeaf(1, "trunk-port")

    access_port = Enum.YLeaf(2, "access-port")



class Interfaces(Entity):
    """
    Interface operational data
    
    .. attribute:: interface_xr
    
    	Detailed operational data for interfaces and configured features
    	**type**\:  :py:class:`InterfaceXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr>`
    
    .. attribute:: node_type_sets
    
    	Node and/or interface type specific view of interface summary data
    	**type**\:  :py:class:`NodeTypeSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets>`
    
    .. attribute:: interface_briefs
    
    	Brief operational data for interfaces
    	**type**\:  :py:class:`InterfaceBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceBriefs>`
    
    .. attribute:: inventory_summary
    
    	Inventory summary information
    	**type**\:  :py:class:`InventorySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary>`
    
    .. attribute:: interfaces
    
    	Descriptions for interfaces
    	**type**\:  :py:class:`Interfaces_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.Interfaces_>`
    
    .. attribute:: interface_summary
    
    	Interface summary information
    	**type**\:  :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary>`
    
    

    """

    _prefix = 'pfi-im-cmd-oper'
    _revision = '2017-06-26'

    def __init__(self):
        super(Interfaces, self).__init__()
        self._top_entity = None

        self.yang_name = "interfaces"
        self.yang_parent_name = "Cisco-IOS-XR-pfi-im-cmd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interface-xr", ("interface_xr", Interfaces.InterfaceXr)), ("node-type-sets", ("node_type_sets", Interfaces.NodeTypeSets)), ("interface-briefs", ("interface_briefs", Interfaces.InterfaceBriefs)), ("inventory-summary", ("inventory_summary", Interfaces.InventorySummary)), ("interfaces", ("interfaces", Interfaces.Interfaces_)), ("interface-summary", ("interface_summary", Interfaces.InterfaceSummary))])
        self._leafs = OrderedDict()

        self.interface_xr = Interfaces.InterfaceXr()
        self.interface_xr.parent = self
        self._children_name_map["interface_xr"] = "interface-xr"

        self.node_type_sets = Interfaces.NodeTypeSets()
        self.node_type_sets.parent = self
        self._children_name_map["node_type_sets"] = "node-type-sets"

        self.interface_briefs = Interfaces.InterfaceBriefs()
        self.interface_briefs.parent = self
        self._children_name_map["interface_briefs"] = "interface-briefs"

        self.inventory_summary = Interfaces.InventorySummary()
        self.inventory_summary.parent = self
        self._children_name_map["inventory_summary"] = "inventory-summary"

        self.interfaces = Interfaces.Interfaces_()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.interface_summary = Interfaces.InterfaceSummary()
        self.interface_summary.parent = self
        self._children_name_map["interface_summary"] = "interface-summary"
        self._segment_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Interfaces, [], name, value)


    class InterfaceXr(Entity):
        """
        Detailed operational data for interfaces and
        configured features
        
        .. attribute:: interface
        
        	Detailed operational data for a particular interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Interfaces.InterfaceXr, self).__init__()

            self.yang_name = "interface-xr"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Interfaces.InterfaceXr.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interface-xr"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.InterfaceXr, [], name, value)


        class Interface(Entity):
            """
            Detailed operational data for a particular
            interface
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: dampening_information
            
            	State dampening information
            	**type**\:  :py:class:`DampeningInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.DampeningInformation>`
            
            .. attribute:: mac_address
            
            	Interface MAC address
            	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.MacAddress>`
            
            .. attribute:: burned_in_address
            
            	Interface burned in address
            	**type**\:  :py:class:`BurnedInAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.BurnedInAddress>`
            
            .. attribute:: carrier_delay
            
            	Carrier Delay
            	**type**\:  :py:class:`CarrierDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.CarrierDelay>`
            
            .. attribute:: arp_information
            
            	Interface ARP type and timeout
            	**type**\:  :py:class:`ArpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.ArpInformation>`
            
            .. attribute:: ip_information
            
            	Interface IP address info
            	**type**\:  :py:class:`IpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.IpInformation>`
            
            .. attribute:: encapsulation_information
            
            	Information specific to the encapsulation
            	**type**\:  :py:class:`EncapsulationInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation>`
            
            .. attribute:: interface_type_information
            
            	Information specific to the interface type
            	**type**\:  :py:class:`InterfaceTypeInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation>`
            
            .. attribute:: data_rates
            
            	Packet and byte rates
            	**type**\:  :py:class:`DataRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.DataRates>`
            
            .. attribute:: interface_statistics
            
            	Packet, byte and error counters
            	**type**\:  :py:class:`InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics>`
            
            .. attribute:: l2_interface_statistics
            
            	L2 Protocol Statistics
            	**type**\:  :py:class:`L2InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics>`
            
            .. attribute:: interface_handle
            
            	Interface name
            	**type**\: str
            
            .. attribute:: interface_type
            
            	Interface type
            	**type**\: str
            
            .. attribute:: hardware_type_string
            
            	Hardware type description string
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: state
            
            	Interface state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: line_state
            
            	Line protocol state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: encapsulation
            
            	Interface encapsulation
            	**type**\: str
            
            .. attribute:: encapsulation_type_string
            
            	Interface encapsulation description string
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtu
            
            	MTU in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: is_l2_transport_enabled
            
            	L2 transport flag
            	**type**\: bool
            
            .. attribute:: state_transition_count
            
            	The number of times the state has changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_state_transition_time
            
            	The time elasped after the last state transition
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_dampening_enabled
            
            	Dampening enabled flag
            	**type**\: bool
            
            .. attribute:: speed
            
            	Interface speed (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: crc_length
            
            	Cyclic Redundancy Check length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_scramble_enabled
            
            	Interface scramble config
            	**type**\: bool
            
            .. attribute:: duplexity
            
            	Interface duplexity
            	**type**\:  :py:class:`ImAttrDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrDuplex>`
            
            .. attribute:: media_type
            
            	Interface media type
            	**type**\:  :py:class:`ImAttrMedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrMedia>`
            
            .. attribute:: link_type
            
            	Interface link type
            	**type**\:  :py:class:`ImAttrLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrLink>`
            
            .. attribute:: in_flow_control
            
            	Input flow control configuration
            	**type**\:  :py:class:`ImAttrFlowControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrFlowControl>`
            
            .. attribute:: out_flow_control
            
            	Output flow control configuration
            	**type**\:  :py:class:`ImAttrFlowControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrFlowControl>`
            
            .. attribute:: bandwidth
            
            	Interface bandwidth (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_bandwidth
            
            	Maximum Interface bandwidth (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: keepalive
            
            	Interface keepalive time (s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_l2_looped
            
            	Loopback detected by layer 2
            	**type**\: bool
            
            .. attribute:: parent_interface_name
            
            	Parent interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: loopback_configuration
            
            	Interface loopback configuration
            	**type**\:  :py:class:`ImCmdLoopbackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdLoopbackEnum>`
            
            .. attribute:: description
            
            	Interface description string
            	**type**\: str
            
            .. attribute:: is_maintenance_enabled
            
            	Maintenance embargo flag
            	**type**\: bool
            
            .. attribute:: is_data_inverted
            
            	Data invert flag
            	**type**\: bool
            
            .. attribute:: transport_mode
            
            	Interface transport mode
            	**type**\:  :py:class:`ImAttrTransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrTransportMode>`
            
            .. attribute:: fast_shutdown
            
            	Fast Shutdown flag
            	**type**\: bool
            
            .. attribute:: if_index
            
            	This is not supposed to be used. It is a dummy attribute to support ifindex for OC model
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.InterfaceXr.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interface-xr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("dampening-information", ("dampening_information", Interfaces.InterfaceXr.Interface.DampeningInformation)), ("mac-address", ("mac_address", Interfaces.InterfaceXr.Interface.MacAddress)), ("burned-in-address", ("burned_in_address", Interfaces.InterfaceXr.Interface.BurnedInAddress)), ("carrier-delay", ("carrier_delay", Interfaces.InterfaceXr.Interface.CarrierDelay)), ("arp-information", ("arp_information", Interfaces.InterfaceXr.Interface.ArpInformation)), ("ip-information", ("ip_information", Interfaces.InterfaceXr.Interface.IpInformation)), ("encapsulation-information", ("encapsulation_information", Interfaces.InterfaceXr.Interface.EncapsulationInformation)), ("interface-type-information", ("interface_type_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation)), ("data-rates", ("data_rates", Interfaces.InterfaceXr.Interface.DataRates)), ("interface-statistics", ("interface_statistics", Interfaces.InterfaceXr.Interface.InterfaceStatistics)), ("l2-interface-statistics", ("l2_interface_statistics", Interfaces.InterfaceXr.Interface.L2InterfaceStatistics))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                    ('interface_type', (YLeaf(YType.str, 'interface-type'), ['str'])),
                    ('hardware_type_string', (YLeaf(YType.str, 'hardware-type-string'), ['str'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('encapsulation', (YLeaf(YType.str, 'encapsulation'), ['str'])),
                    ('encapsulation_type_string', (YLeaf(YType.str, 'encapsulation-type-string'), ['str'])),
                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                    ('is_l2_transport_enabled', (YLeaf(YType.boolean, 'is-l2-transport-enabled'), ['bool'])),
                    ('state_transition_count', (YLeaf(YType.uint32, 'state-transition-count'), ['int'])),
                    ('last_state_transition_time', (YLeaf(YType.uint32, 'last-state-transition-time'), ['int'])),
                    ('is_dampening_enabled', (YLeaf(YType.boolean, 'is-dampening-enabled'), ['bool'])),
                    ('speed', (YLeaf(YType.uint32, 'speed'), ['int'])),
                    ('crc_length', (YLeaf(YType.uint32, 'crc-length'), ['int'])),
                    ('is_scramble_enabled', (YLeaf(YType.boolean, 'is-scramble-enabled'), ['bool'])),
                    ('duplexity', (YLeaf(YType.enumeration, 'duplexity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImAttrDuplex', '')])),
                    ('media_type', (YLeaf(YType.enumeration, 'media-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImAttrMedia', '')])),
                    ('link_type', (YLeaf(YType.enumeration, 'link-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImAttrLink', '')])),
                    ('in_flow_control', (YLeaf(YType.enumeration, 'in-flow-control'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImAttrFlowControl', '')])),
                    ('out_flow_control', (YLeaf(YType.enumeration, 'out-flow-control'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImAttrFlowControl', '')])),
                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                    ('max_bandwidth', (YLeaf(YType.uint32, 'max-bandwidth'), ['int'])),
                    ('keepalive', (YLeaf(YType.uint32, 'keepalive'), ['int'])),
                    ('is_l2_looped', (YLeaf(YType.boolean, 'is-l2-looped'), ['bool'])),
                    ('parent_interface_name', (YLeaf(YType.str, 'parent-interface-name'), ['str'])),
                    ('loopback_configuration', (YLeaf(YType.enumeration, 'loopback-configuration'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImCmdLoopbackEnum', '')])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('is_maintenance_enabled', (YLeaf(YType.boolean, 'is-maintenance-enabled'), ['bool'])),
                    ('is_data_inverted', (YLeaf(YType.boolean, 'is-data-inverted'), ['bool'])),
                    ('transport_mode', (YLeaf(YType.enumeration, 'transport-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImAttrTransportMode', '')])),
                    ('fast_shutdown', (YLeaf(YType.boolean, 'fast-shutdown'), ['bool'])),
                    ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                ])
                self.interface_name = None
                self.interface_handle = None
                self.interface_type = None
                self.hardware_type_string = None
                self.state = None
                self.line_state = None
                self.encapsulation = None
                self.encapsulation_type_string = None
                self.mtu = None
                self.is_l2_transport_enabled = None
                self.state_transition_count = None
                self.last_state_transition_time = None
                self.is_dampening_enabled = None
                self.speed = None
                self.crc_length = None
                self.is_scramble_enabled = None
                self.duplexity = None
                self.media_type = None
                self.link_type = None
                self.in_flow_control = None
                self.out_flow_control = None
                self.bandwidth = None
                self.max_bandwidth = None
                self.keepalive = None
                self.is_l2_looped = None
                self.parent_interface_name = None
                self.loopback_configuration = None
                self.description = None
                self.is_maintenance_enabled = None
                self.is_data_inverted = None
                self.transport_mode = None
                self.fast_shutdown = None
                self.if_index = None

                self.dampening_information = Interfaces.InterfaceXr.Interface.DampeningInformation()
                self.dampening_information.parent = self
                self._children_name_map["dampening_information"] = "dampening-information"

                self.mac_address = Interfaces.InterfaceXr.Interface.MacAddress()
                self.mac_address.parent = self
                self._children_name_map["mac_address"] = "mac-address"

                self.burned_in_address = Interfaces.InterfaceXr.Interface.BurnedInAddress()
                self.burned_in_address.parent = self
                self._children_name_map["burned_in_address"] = "burned-in-address"

                self.carrier_delay = Interfaces.InterfaceXr.Interface.CarrierDelay()
                self.carrier_delay.parent = self
                self._children_name_map["carrier_delay"] = "carrier-delay"

                self.arp_information = Interfaces.InterfaceXr.Interface.ArpInformation()
                self.arp_information.parent = self
                self._children_name_map["arp_information"] = "arp-information"

                self.ip_information = Interfaces.InterfaceXr.Interface.IpInformation()
                self.ip_information.parent = self
                self._children_name_map["ip_information"] = "ip-information"

                self.encapsulation_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation()
                self.encapsulation_information.parent = self
                self._children_name_map["encapsulation_information"] = "encapsulation-information"

                self.interface_type_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation()
                self.interface_type_information.parent = self
                self._children_name_map["interface_type_information"] = "interface-type-information"

                self.data_rates = Interfaces.InterfaceXr.Interface.DataRates()
                self.data_rates.parent = self
                self._children_name_map["data_rates"] = "data-rates"

                self.interface_statistics = Interfaces.InterfaceXr.Interface.InterfaceStatistics()
                self.interface_statistics.parent = self
                self._children_name_map["interface_statistics"] = "interface-statistics"

                self.l2_interface_statistics = Interfaces.InterfaceXr.Interface.L2InterfaceStatistics()
                self.l2_interface_statistics.parent = self
                self._children_name_map["l2_interface_statistics"] = "l2-interface-statistics"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interface-xr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.InterfaceXr.Interface, ['interface_name', 'interface_handle', 'interface_type', 'hardware_type_string', 'state', 'line_state', 'encapsulation', 'encapsulation_type_string', 'mtu', 'is_l2_transport_enabled', 'state_transition_count', 'last_state_transition_time', 'is_dampening_enabled', 'speed', 'crc_length', 'is_scramble_enabled', 'duplexity', 'media_type', 'link_type', 'in_flow_control', 'out_flow_control', 'bandwidth', 'max_bandwidth', 'keepalive', 'is_l2_looped', 'parent_interface_name', 'loopback_configuration', 'description', 'is_maintenance_enabled', 'is_data_inverted', 'transport_mode', 'fast_shutdown', 'if_index'], name, value)


            class DampeningInformation(Entity):
                """
                State dampening information
                
                .. attribute:: penalty
                
                	Dampening penalty of the interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_suppressed_enabled
                
                	Flag showing if state is suppressed
                	**type**\: bool
                
                .. attribute:: seconds_remaining
                
                	Remaining period of suppression in secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: half_life
                
                	Configured decay half life in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: reuse_threshold
                
                	Configured reuse threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: suppress_threshold
                
                	Value of suppress threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_suppress_time
                
                	Maximum suppress time in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: restart_penalty
                
                	Configured restart penalty
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.DampeningInformation, self).__init__()

                    self.yang_name = "dampening-information"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                        ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                        ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                        ('half_life', (YLeaf(YType.uint32, 'half-life'), ['int'])),
                        ('reuse_threshold', (YLeaf(YType.uint32, 'reuse-threshold'), ['int'])),
                        ('suppress_threshold', (YLeaf(YType.uint32, 'suppress-threshold'), ['int'])),
                        ('maximum_suppress_time', (YLeaf(YType.uint32, 'maximum-suppress-time'), ['int'])),
                        ('restart_penalty', (YLeaf(YType.uint32, 'restart-penalty'), ['int'])),
                    ])
                    self.penalty = None
                    self.is_suppressed_enabled = None
                    self.seconds_remaining = None
                    self.half_life = None
                    self.reuse_threshold = None
                    self.suppress_threshold = None
                    self.maximum_suppress_time = None
                    self.restart_penalty = None
                    self._segment_path = lambda: "dampening-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.DampeningInformation, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'half_life', 'reuse_threshold', 'suppress_threshold', 'maximum_suppress_time', 'restart_penalty'], name, value)


            class MacAddress(Entity):
                """
                Interface MAC address
                
                .. attribute:: address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.MacAddress, self).__init__()

                    self.yang_name = "mac-address"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ])
                    self.address = None
                    self._segment_path = lambda: "mac-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.MacAddress, ['address'], name, value)


            class BurnedInAddress(Entity):
                """
                Interface burned in address
                
                .. attribute:: address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.BurnedInAddress, self).__init__()

                    self.yang_name = "burned-in-address"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ])
                    self.address = None
                    self._segment_path = lambda: "burned-in-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.BurnedInAddress, ['address'], name, value)


            class CarrierDelay(Entity):
                """
                Carrier Delay
                
                .. attribute:: carrier_delay_up
                
                	Carrier delay on state up (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: carrier_delay_down
                
                	Carrier delay on state down (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.CarrierDelay, self).__init__()

                    self.yang_name = "carrier-delay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('carrier_delay_up', (YLeaf(YType.uint32, 'carrier-delay-up'), ['int'])),
                        ('carrier_delay_down', (YLeaf(YType.uint32, 'carrier-delay-down'), ['int'])),
                    ])
                    self.carrier_delay_up = None
                    self.carrier_delay_down = None
                    self._segment_path = lambda: "carrier-delay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.CarrierDelay, ['carrier_delay_up', 'carrier_delay_down'], name, value)


            class ArpInformation(Entity):
                """
                Interface ARP type and timeout
                
                .. attribute:: arp_timeout
                
                	ARP timeout in seconds. Only valid if 'ARPIsLearningDisabled' is 'false'
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: arp_type_name
                
                	ARP type name
                	**type**\: str
                
                .. attribute:: arp_is_learning_disabled
                
                	Whether the interface has dynamic learning disabled
                	**type**\: bool
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.ArpInformation, self).__init__()

                    self.yang_name = "arp-information"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('arp_timeout', (YLeaf(YType.uint32, 'arp-timeout'), ['int'])),
                        ('arp_type_name', (YLeaf(YType.str, 'arp-type-name'), ['str'])),
                        ('arp_is_learning_disabled', (YLeaf(YType.boolean, 'arp-is-learning-disabled'), ['bool'])),
                    ])
                    self.arp_timeout = None
                    self.arp_type_name = None
                    self.arp_is_learning_disabled = None
                    self._segment_path = lambda: "arp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.ArpInformation, ['arp_timeout', 'arp_type_name', 'arp_is_learning_disabled'], name, value)


            class IpInformation(Entity):
                """
                Interface IP address info
                
                .. attribute:: ip_address
                
                	Interface IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: subnet_mask_length
                
                	Interface subnet mask length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.IpInformation, self).__init__()

                    self.yang_name = "ip-information"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                        ('subnet_mask_length', (YLeaf(YType.uint32, 'subnet-mask-length'), ['int'])),
                    ])
                    self.ip_address = None
                    self.subnet_mask_length = None
                    self._segment_path = lambda: "ip-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.IpInformation, ['ip_address', 'subnet_mask_length'], name, value)


            class EncapsulationInformation(Entity):
                """
                Information specific to the encapsulation
                
                .. attribute:: frame_relay_information
                
                	Frame Relay information
                	**type**\:  :py:class:`FrameRelayInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation>`
                
                .. attribute:: dot1q_information
                
                	VLAN 802.1q information
                	**type**\:  :py:class:`Dot1qInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation>`
                
                .. attribute:: ppp_information
                
                	PPP information
                	**type**\:  :py:class:`PppInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation>`
                
                .. attribute:: encapsulation_type
                
                	EncapsulationType
                	**type**\:  :py:class:`ImCmdEncapsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdEncapsEnum>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation, self).__init__()

                    self.yang_name = "encapsulation-information"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("frame-relay-information", ("frame_relay_information", Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation)), ("dot1q-information", ("dot1q_information", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation)), ("ppp-information", ("ppp_information", Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation))])
                    self._leafs = OrderedDict([
                        ('encapsulation_type', (YLeaf(YType.enumeration, 'encapsulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImCmdEncapsEnum', '')])),
                    ])
                    self.encapsulation_type = None

                    self.frame_relay_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation()
                    self.frame_relay_information.parent = self
                    self._children_name_map["frame_relay_information"] = "frame-relay-information"

                    self.dot1q_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation()
                    self.dot1q_information.parent = self
                    self._children_name_map["dot1q_information"] = "dot1q-information"

                    self.ppp_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation()
                    self.ppp_information.parent = self
                    self._children_name_map["ppp_information"] = "ppp-information"
                    self._segment_path = lambda: "encapsulation-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation, ['encapsulation_type'], name, value)


                class FrameRelayInformation(Entity):
                    """
                    Frame Relay information
                    
                    .. attribute:: fr_encapsulation_type
                    
                    	Frame Relay encapsulation type
                    	**type**\:  :py:class:`ImCmdFrTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdFrTypeEnum>`
                    
                    .. attribute:: lmi_type
                    
                    	The LMI type\: Autosense, ANSI, CCITT or CISCO
                    	**type**\:  :py:class:`ImCmdLmiTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdLmiTypeEnum>`
                    
                    .. attribute:: lmidlci
                    
                    	LMI DLCI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_nni
                    
                    	The NNI LMI interface type
                    	**type**\: bool
                    
                    .. attribute:: is_dte
                    
                    	The DTE/DCE LMI interface type
                    	**type**\: bool
                    
                    .. attribute:: is_lmi_up
                    
                    	Flag indicating whether the LMI  DTE/DCE/NNI\-DTE state is UP
                    	**type**\: bool
                    
                    .. attribute:: is_lmi_nni_dce_up
                    
                    	Flag indicating whether the LMI  NNI\-DCE state is UP
                    	**type**\: bool
                    
                    .. attribute:: is_lmi_enabled
                    
                    	The status of FR LMI for an interface
                    	**type**\: bool
                    
                    .. attribute:: enquiries_received
                    
                    	Number of enquiry messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: enquiries_sent
                    
                    	Number of enquiry messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_received
                    
                    	Number of status messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_sent
                    
                    	Number of status messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_status_received
                    
                    	Number of update status messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_status_sent
                    
                    	Number of update status messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation, self).__init__()

                        self.yang_name = "frame-relay-information"
                        self.yang_parent_name = "encapsulation-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fr_encapsulation_type', (YLeaf(YType.enumeration, 'fr-encapsulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImCmdFrTypeEnum', '')])),
                            ('lmi_type', (YLeaf(YType.enumeration, 'lmi-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImCmdLmiTypeEnum', '')])),
                            ('lmidlci', (YLeaf(YType.uint32, 'lmidlci'), ['int'])),
                            ('is_nni', (YLeaf(YType.boolean, 'is-nni'), ['bool'])),
                            ('is_dte', (YLeaf(YType.boolean, 'is-dte'), ['bool'])),
                            ('is_lmi_up', (YLeaf(YType.boolean, 'is-lmi-up'), ['bool'])),
                            ('is_lmi_nni_dce_up', (YLeaf(YType.boolean, 'is-lmi-nni-dce-up'), ['bool'])),
                            ('is_lmi_enabled', (YLeaf(YType.boolean, 'is-lmi-enabled'), ['bool'])),
                            ('enquiries_received', (YLeaf(YType.uint32, 'enquiries-received'), ['int'])),
                            ('enquiries_sent', (YLeaf(YType.uint32, 'enquiries-sent'), ['int'])),
                            ('status_received', (YLeaf(YType.uint32, 'status-received'), ['int'])),
                            ('status_sent', (YLeaf(YType.uint32, 'status-sent'), ['int'])),
                            ('update_status_received', (YLeaf(YType.uint32, 'update-status-received'), ['int'])),
                            ('update_status_sent', (YLeaf(YType.uint32, 'update-status-sent'), ['int'])),
                        ])
                        self.fr_encapsulation_type = None
                        self.lmi_type = None
                        self.lmidlci = None
                        self.is_nni = None
                        self.is_dte = None
                        self.is_lmi_up = None
                        self.is_lmi_nni_dce_up = None
                        self.is_lmi_enabled = None
                        self.enquiries_received = None
                        self.enquiries_sent = None
                        self.status_received = None
                        self.status_sent = None
                        self.update_status_received = None
                        self.update_status_sent = None
                        self._segment_path = lambda: "frame-relay-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation, ['fr_encapsulation_type', 'lmi_type', 'lmidlci', 'is_nni', 'is_dte', 'is_lmi_up', 'is_lmi_nni_dce_up', 'is_lmi_enabled', 'enquiries_received', 'enquiries_sent', 'status_received', 'status_sent', 'update_status_received', 'update_status_sent'], name, value)


                class Dot1qInformation(Entity):
                    """
                    VLAN 802.1q information
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:  :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails>`
                    
                    .. attribute:: vlan_switched
                    
                    	VLAN\-Switched information
                    	**type**\:  :py:class:`VlanSwitched <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation, self).__init__()

                        self.yang_name = "dot1q-information"
                        self.yang_parent_name = "encapsulation-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("encapsulation-details", ("encapsulation_details", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails)), ("vlan-switched", ("vlan_switched", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched))])
                        self._leafs = OrderedDict()

                        self.encapsulation_details = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"

                        self.vlan_switched = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched()
                        self.vlan_switched.parent = self
                        self._children_name_map["vlan_switched"] = "vlan-switched"
                        self._segment_path = lambda: "dot1q-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation, [], name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:  :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:  :py:class:`Dot1adDot1qStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack>`
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:  :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.VlanEncaps>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "dot1q-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stack", ("stack", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack)), ("service-instance-details", ("service_instance_details", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails)), ("dot1ad-dot1q-stack", ("dot1ad_dot1q_stack", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack))])
                            self._leafs = OrderedDict([
                                ('vlan_encapsulation', (YLeaf(YType.enumeration, 'vlan-encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'VlanEncaps', '')])),
                                ('tag', (YLeaf(YType.uint16, 'tag'), ['int'])),
                                ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                ('native_tag', (YLeaf(YType.uint16, 'native-tag'), ['int'])),
                                ('dot1ad_tag', (YLeaf(YType.uint16, 'dot1ad-tag'), ['int'])),
                                ('dot1ad_native_tag', (YLeaf(YType.uint16, 'dot1ad-native-tag'), ['int'])),
                                ('dot1ad_outer_tag', (YLeaf(YType.uint16, 'dot1ad-outer-tag'), ['int'])),
                            ])
                            self.vlan_encapsulation = None
                            self.tag = None
                            self.outer_tag = None
                            self.native_tag = None
                            self.dot1ad_tag = None
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None

                            self.stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"

                            self.service_instance_details = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"

                            self.dot1ad_dot1q_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._segment_path = lambda: "encapsulation-details"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails, ['vlan_encapsulation', 'tag', 'outer_tag', 'native_tag', 'dot1ad_tag', 'dot1ad_native_tag', 'dot1ad_outer_tag'], name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack, self).__init__()

                                self.yang_name = "stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                    ('second_tag', (YLeaf(YType.uint16, 'second-tag'), ['int'])),
                                ])
                                self.outer_tag = None
                                self.second_tag = None
                                self._segment_path = lambda: "stack"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack, ['outer_tag', 'second_tag'], name, value)


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:  :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:  :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpPayloadEtype>`
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of  		 :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of  		 :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-traffic-stack", ("local_traffic_stack", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack)), ("tags-to-match", ("tags_to_match", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch)), ("pushe", ("pushe", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe))])
                                self._leafs = OrderedDict([
                                    ('payload_ethertype', (YLeaf(YType.enumeration, 'payload-ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpPayloadEtype', '')])),
                                    ('tags_popped', (YLeaf(YType.uint16, 'tags-popped'), ['int'])),
                                    ('is_exact_match', (YLeaf(YType.int32, 'is-exact-match'), ['int'])),
                                    ('is_native_vlan', (YLeaf(YType.int32, 'is-native-vlan'), ['int'])),
                                    ('is_native_preserving', (YLeaf(YType.int32, 'is-native-preserving'), ['int'])),
                                    ('source_mac_match', (YLeaf(YType.str, 'source-mac-match'), ['str'])),
                                    ('destination_mac_match', (YLeaf(YType.str, 'destination-mac-match'), ['str'])),
                                ])
                                self.payload_ethertype = None
                                self.tags_popped = None
                                self.is_exact_match = None
                                self.is_native_vlan = None
                                self.is_native_preserving = None
                                self.source_mac_match = None
                                self.destination_mac_match = None

                                self.local_traffic_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"

                                self.tags_to_match = YList(self)
                                self.pushe = YList(self)
                                self._segment_path = lambda: "service-instance-details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails, ['payload_ethertype', 'tags_popped', 'is_exact_match', 'is_native_vlan', 'is_native_preserving', 'source_mac_match', 'destination_mac_match'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of  		 :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("local-traffic-tag", ("local_traffic_tag", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag))])
                                    self._leafs = OrderedDict()

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagEtype', '')])),
                                            ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                        ])
                                        self.ethertype = None
                                        self.vlan_id = None
                                        self._segment_path = lambda: "local-traffic-tag"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:  :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of  		 :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("vlan-range", ("vlan_range", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange))])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagEtype', '')])),
                                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagPriority', '')])),
                                    ])
                                    self.ethertype = None
                                    self.priority = None

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('vlan_id_low', (YLeaf(YType.uint16, 'vlan-id-low'), ['int'])),
                                            ('vlan_id_high', (YLeaf(YType.uint16, 'vlan-id-high'), ['int'])),
                                        ])
                                        self.vlan_id_low = None
                                        self.vlan_id_high = None
                                        self._segment_path = lambda: "vlan-range"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, ['vlan_id_low', 'vlan_id_high'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagEtype', '')])),
                                        ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                    ])
                                    self.ethertype = None
                                    self.vlan_id = None
                                    self._segment_path = lambda: "pushe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe, ['ethertype', 'vlan_id'], name, value)


                        class Dot1adDot1qStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                    ('second_tag', (YLeaf(YType.uint16, 'second-tag'), ['int'])),
                                ])
                                self.outer_tag = None
                                self.second_tag = None
                                self._segment_path = lambda: "dot1ad-dot1q-stack"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack, ['outer_tag', 'second_tag'], name, value)


                    class VlanSwitched(Entity):
                        """
                        VLAN\-Switched information
                        
                        .. attribute:: trunk_vlan_ranges
                        
                        	VLAN\-Switched Trunk VLAN ranges
                        	**type**\:  :py:class:`TrunkVlanRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges>`
                        
                        .. attribute:: mode
                        
                        	VLAN\-Switched mode
                        	**type**\:  :py:class:`VlanSwitchedMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.VlanSwitchedMode>`
                        
                        .. attribute:: access_vlan
                        
                        	VLAN\-Switched Access VLAN
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched, self).__init__()

                            self.yang_name = "vlan-switched"
                            self.yang_parent_name = "dot1q-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("trunk-vlan-ranges", ("trunk_vlan_ranges", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges))])
                            self._leafs = OrderedDict([
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'VlanSwitchedMode', '')])),
                                ('access_vlan', (YLeaf(YType.uint16, 'access-vlan'), ['int'])),
                            ])
                            self.mode = None
                            self.access_vlan = None

                            self.trunk_vlan_ranges = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges()
                            self.trunk_vlan_ranges.parent = self
                            self._children_name_map["trunk_vlan_ranges"] = "trunk-vlan-ranges"
                            self._segment_path = lambda: "vlan-switched"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched, ['mode', 'access_vlan'], name, value)


                        class TrunkVlanRanges(Entity):
                            """
                            VLAN\-Switched Trunk VLAN ranges
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:  :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:  :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpPayloadEtype>`
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of  		 :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of  		 :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.Pushe>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges, self).__init__()

                                self.yang_name = "trunk-vlan-ranges"
                                self.yang_parent_name = "vlan-switched"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-traffic-stack", ("local_traffic_stack", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack)), ("tags-to-match", ("tags_to_match", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch)), ("pushe", ("pushe", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.Pushe))])
                                self._leafs = OrderedDict([
                                    ('payload_ethertype', (YLeaf(YType.enumeration, 'payload-ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpPayloadEtype', '')])),
                                    ('tags_popped', (YLeaf(YType.uint16, 'tags-popped'), ['int'])),
                                    ('is_exact_match', (YLeaf(YType.int32, 'is-exact-match'), ['int'])),
                                    ('is_native_vlan', (YLeaf(YType.int32, 'is-native-vlan'), ['int'])),
                                    ('is_native_preserving', (YLeaf(YType.int32, 'is-native-preserving'), ['int'])),
                                    ('source_mac_match', (YLeaf(YType.str, 'source-mac-match'), ['str'])),
                                    ('destination_mac_match', (YLeaf(YType.str, 'destination-mac-match'), ['str'])),
                                ])
                                self.payload_ethertype = None
                                self.tags_popped = None
                                self.is_exact_match = None
                                self.is_native_vlan = None
                                self.is_native_preserving = None
                                self.source_mac_match = None
                                self.destination_mac_match = None

                                self.local_traffic_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"

                                self.tags_to_match = YList(self)
                                self.pushe = YList(self)
                                self._segment_path = lambda: "trunk-vlan-ranges"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges, ['payload_ethertype', 'tags_popped', 'is_exact_match', 'is_native_vlan', 'is_native_preserving', 'source_mac_match', 'destination_mac_match'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of  		 :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "trunk-vlan-ranges"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("local-traffic-tag", ("local_traffic_tag", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag))])
                                    self._leafs = OrderedDict()

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagEtype', '')])),
                                            ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                        ])
                                        self.ethertype = None
                                        self.vlan_id = None
                                        self._segment_path = lambda: "local-traffic-tag"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:  :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of  		 :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "trunk-vlan-ranges"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("vlan-range", ("vlan_range", Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange))])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagEtype', '')])),
                                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagPriority', '')])),
                                    ])
                                    self.ethertype = None
                                    self.priority = None

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('vlan_id_low', (YLeaf(YType.uint16, 'vlan-id-low'), ['int'])),
                                            ('vlan_id_high', (YLeaf(YType.uint16, 'vlan-id-high'), ['int'])),
                                        ])
                                        self.vlan_id_low = None
                                        self.vlan_id_high = None
                                        self._segment_path = lambda: "vlan-range"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange, ['vlan_id_low', 'vlan_id_high'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "trunk-vlan-ranges"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'EfpTagEtype', '')])),
                                        ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                    ])
                                    self.ethertype = None
                                    self.vlan_id = None
                                    self._segment_path = lambda: "pushe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.VlanSwitched.TrunkVlanRanges.Pushe, ['ethertype', 'vlan_id'], name, value)


                class PppInformation(Entity):
                    """
                    PPP information
                    
                    .. attribute:: lcp_state
                    
                    	LCP State
                    	**type**\:  :py:class:`PppFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.PppFsmState>`
                    
                    .. attribute:: is_loopback_detected
                    
                    	Loopback detected
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_mp_bundle_member
                    
                    	MP Bundle Member
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_multilink_open
                    
                    	Is Multilink Open
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ncp_info_array
                    
                    	Array of per\-NCP data
                    	**type**\: list of  		 :py:class:`NcpInfoArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation, self).__init__()

                        self.yang_name = "ppp-information"
                        self.yang_parent_name = "encapsulation-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ncp-info-array", ("ncp_info_array", Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray))])
                        self._leafs = OrderedDict([
                            ('lcp_state', (YLeaf(YType.enumeration, 'lcp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'PppFsmState', '')])),
                            ('is_loopback_detected', (YLeaf(YType.int32, 'is-loopback-detected'), ['int'])),
                            ('keepalive_period', (YLeaf(YType.uint32, 'keepalive-period'), ['int'])),
                            ('is_mp_bundle_member', (YLeaf(YType.int32, 'is-mp-bundle-member'), ['int'])),
                            ('is_multilink_open', (YLeaf(YType.int32, 'is-multilink-open'), ['int'])),
                        ])
                        self.lcp_state = None
                        self.is_loopback_detected = None
                        self.keepalive_period = None
                        self.is_mp_bundle_member = None
                        self.is_multilink_open = None

                        self.ncp_info_array = YList(self)
                        self._segment_path = lambda: "ppp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation, ['lcp_state', 'is_loopback_detected', 'keepalive_period', 'is_mp_bundle_member', 'is_multilink_open'], name, value)


                    class NcpInfoArray(Entity):
                        """
                        Array of per\-NCP data
                        
                        .. attribute:: ncp_state
                        
                        	NCP state value
                        	**type**\:  :py:class:`PppFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.PppFsmState>`
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP state identifier
                        	**type**\:  :py:class:`NcpIdent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.NcpIdent>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray, self).__init__()

                            self.yang_name = "ncp-info-array"
                            self.yang_parent_name = "ppp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ncp_state', (YLeaf(YType.enumeration, 'ncp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'PppFsmState', '')])),
                                ('ncp_identifier', (YLeaf(YType.enumeration, 'ncp-identifier'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'NcpIdent', '')])),
                            ])
                            self.ncp_state = None
                            self.ncp_identifier = None
                            self._segment_path = lambda: "ncp-info-array"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray, ['ncp_state', 'ncp_identifier'], name, value)


            class InterfaceTypeInformation(Entity):
                """
                Information specific to the interface type
                
                .. attribute:: srp_information
                
                	SRP interface information
                	**type**\:  :py:class:`SrpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation>`
                
                .. attribute:: tunnel_information
                
                	Tunnel interface information
                	**type**\:  :py:class:`TunnelInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation>`
                
                .. attribute:: bundle_information
                
                	Bundle interface information
                	**type**\:  :py:class:`BundleInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation>`
                
                .. attribute:: serial_information
                
                	Serial interface information
                	**type**\:  :py:class:`SerialInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation>`
                
                .. attribute:: sonet_pos_information
                
                	SONET POS interface information
                	**type**\:  :py:class:`SonetPosInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation>`
                
                .. attribute:: tunnel_gre_information
                
                	Tunnel GRE interface information
                	**type**\:  :py:class:`TunnelGreInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation>`
                
                .. attribute:: pseudowire_head_end_information
                
                	PseudowireHeadEnd interface information
                	**type**\:  :py:class:`PseudowireHeadEndInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation>`
                
                .. attribute:: cem_information
                
                	Cem interface information
                	**type**\:  :py:class:`CemInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation>`
                
                .. attribute:: gcc_information
                
                	GCC interface information
                	**type**\:  :py:class:`GccInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation>`
                
                .. attribute:: interface_type_info
                
                	InterfaceTypeInfo
                	**type**\:  :py:class:`ImCmdIntfTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdIntfTypeEnum>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation, self).__init__()

                    self.yang_name = "interface-type-information"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("srp-information", ("srp_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation)), ("tunnel-information", ("tunnel_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation)), ("bundle-information", ("bundle_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation)), ("serial-information", ("serial_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation)), ("sonet-pos-information", ("sonet_pos_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation)), ("tunnel-gre-information", ("tunnel_gre_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation)), ("pseudowire-head-end-information", ("pseudowire_head_end_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation)), ("cem-information", ("cem_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation)), ("gcc-information", ("gcc_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation))])
                    self._leafs = OrderedDict([
                        ('interface_type_info', (YLeaf(YType.enumeration, 'interface-type-info'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImCmdIntfTypeEnum', '')])),
                    ])
                    self.interface_type_info = None

                    self.srp_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation()
                    self.srp_information.parent = self
                    self._children_name_map["srp_information"] = "srp-information"

                    self.tunnel_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation()
                    self.tunnel_information.parent = self
                    self._children_name_map["tunnel_information"] = "tunnel-information"

                    self.bundle_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation()
                    self.bundle_information.parent = self
                    self._children_name_map["bundle_information"] = "bundle-information"

                    self.serial_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation()
                    self.serial_information.parent = self
                    self._children_name_map["serial_information"] = "serial-information"

                    self.sonet_pos_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation()
                    self.sonet_pos_information.parent = self
                    self._children_name_map["sonet_pos_information"] = "sonet-pos-information"

                    self.tunnel_gre_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation()
                    self.tunnel_gre_information.parent = self
                    self._children_name_map["tunnel_gre_information"] = "tunnel-gre-information"

                    self.pseudowire_head_end_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation()
                    self.pseudowire_head_end_information.parent = self
                    self._children_name_map["pseudowire_head_end_information"] = "pseudowire-head-end-information"

                    self.cem_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation()
                    self.cem_information.parent = self
                    self._children_name_map["cem_information"] = "cem-information"

                    self.gcc_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation()
                    self.gcc_information.parent = self
                    self._children_name_map["gcc_information"] = "gcc-information"
                    self._segment_path = lambda: "interface-type-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation, ['interface_type_info'], name, value)


                class SrpInformation(Entity):
                    """
                    SRP interface information
                    
                    .. attribute:: srp_information
                    
                    	SRP\-specific data
                    	**type**\:  :py:class:`SrpInformation_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_>`
                    
                    .. attribute:: srp_statistics
                    
                    	SRP\-specific packet and byte counters
                    	**type**\:  :py:class:`SrpStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation, self).__init__()

                        self.yang_name = "srp-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("srp-information", ("srp_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_)), ("srp-statistics", ("srp_statistics", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics))])
                        self._leafs = OrderedDict()

                        self.srp_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_()
                        self.srp_information.parent = self
                        self._children_name_map["srp_information"] = "srp-information"

                        self.srp_statistics = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics()
                        self.srp_statistics.parent = self
                        self._children_name_map["srp_statistics"] = "srp-statistics"
                        self._segment_path = lambda: "srp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation, [], name, value)


                    class SrpInformation_(Entity):
                        """
                        SRP\-specific data
                        
                        .. attribute:: ips_info
                        
                        	SRP IPS information
                        	**type**\:  :py:class:`IpsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo>`
                        
                        .. attribute:: topology_info
                        
                        	SRP topology information
                        	**type**\:  :py:class:`TopologyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo>`
                        
                        .. attribute:: srr_info
                        
                        	SRP SRR information
                        	**type**\:  :py:class:`SrrInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo>`
                        
                        .. attribute:: rate_limit_info
                        
                        	SRP rate limit information
                        	**type**\:  :py:class:`RateLimitInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_, self).__init__()

                            self.yang_name = "srp-information"
                            self.yang_parent_name = "srp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ips-info", ("ips_info", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo)), ("topology-info", ("topology_info", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo)), ("srr-info", ("srr_info", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo)), ("rate-limit-info", ("rate_limit_info", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo))])
                            self._leafs = OrderedDict()

                            self.ips_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo()
                            self.ips_info.parent = self
                            self._children_name_map["ips_info"] = "ips-info"

                            self.topology_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo()
                            self.topology_info.parent = self
                            self._children_name_map["topology_info"] = "topology-info"

                            self.srr_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo()
                            self.srr_info.parent = self
                            self._children_name_map["srr_info"] = "srr-info"

                            self.rate_limit_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo()
                            self.rate_limit_info.parent = self
                            self._children_name_map["rate_limit_info"] = "rate-limit-info"
                            self._segment_path = lambda: "srp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_, [], name, value)


                        class IpsInfo(Entity):
                            """
                            SRP IPS information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_information
                            
                            	IPS information
                            	**type**\: list of  		 :py:class:`LocalInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo, self).__init__()

                                self.yang_name = "ips-info"
                                self.yang_parent_name = "srp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-information", ("local_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation))])
                                self._leafs = OrderedDict([
                                    ('is_admin_down', (YLeaf(YType.int32, 'is-admin-down'), ['int'])),
                                ])
                                self.is_admin_down = None

                                self.local_information = YList(self)
                                self._segment_path = lambda: "ips-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo, ['is_admin_down'], name, value)


                            class LocalInformation(Entity):
                                """
                                IPS information
                                
                                .. attribute:: side_a
                                
                                	Side A IPS details
                                	**type**\:  :py:class:`SideA <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA>`
                                
                                .. attribute:: side_b
                                
                                	Side B IPS details
                                	**type**\:  :py:class:`SideB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB>`
                                
                                .. attribute:: mac_address
                                
                                	MAC address for node
                                	**type**\: str
                                
                                .. attribute:: is_inter_card_bus_enabled
                                
                                	Inter card bus enabled
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: wtr_timer_period
                                
                                	IPS Wait To Restore period in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation, self).__init__()

                                    self.yang_name = "local-information"
                                    self.yang_parent_name = "ips-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("side-a", ("side_a", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA)), ("side-b", ("side_b", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB))])
                                    self._leafs = OrderedDict([
                                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                        ('is_inter_card_bus_enabled', (YLeaf(YType.int32, 'is-inter-card-bus-enabled'), ['int'])),
                                        ('wtr_timer_period', (YLeaf(YType.uint32, 'wtr-timer-period'), ['int'])),
                                    ])
                                    self.mac_address = None
                                    self.is_inter_card_bus_enabled = None
                                    self.wtr_timer_period = None

                                    self.side_a = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA()
                                    self.side_a.parent = self
                                    self._children_name_map["side_a"] = "side-a"

                                    self.side_b = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB()
                                    self.side_b.parent = self
                                    self._children_name_map["side_b"] = "side-b"
                                    self._segment_path = lambda: "local-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation, ['mac_address', 'is_inter_card_bus_enabled', 'wtr_timer_period'], name, value)


                                class SideA(Entity):
                                    """
                                    Side A IPS details
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    .. attribute:: wrap_state
                                    
                                    	Wrap state
                                    	**type**\:  :py:class:`SrpMgmtIpsWrapState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsWrapState>`
                                    
                                    .. attribute:: packet_sent_timer
                                    
                                    	SRP IPS packet send interval in seconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: send_timer_time_remaining
                                    
                                    	Time in seconds remaining until next send of an IPS request
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: wtr_timer_remaining
                                    
                                    	Time in seconds until wrap removal
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: self_detected_request
                                    
                                    	Self Detected Requests
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: remote_request
                                    
                                    	Remote Requests
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: rx_neighbor_mac_address
                                    
                                    	Neighbour mac address for received message
                                    	**type**\: str
                                    
                                    .. attribute:: rx_message_type
                                    
                                    	Type of message received
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: rx_path_type
                                    
                                    	Short/long path for received message
                                    	**type**\:  :py:class:`SrpMgmtIpsPathInd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd>`
                                    
                                    .. attribute:: rx_ttl
                                    
                                    	Time to live for received message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: rx_packet_test
                                    
                                    	Test for existence of an RX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: tx_neighbor_mac_address
                                    
                                    	Mac address of node receiving TXed messages
                                    	**type**\: str
                                    
                                    .. attribute:: tx_message_type
                                    
                                    	Type of message transmitted
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: tx_path_type
                                    
                                    	Short/long path of transmitted message
                                    	**type**\:  :py:class:`SrpMgmtIpsPathInd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd>`
                                    
                                    .. attribute:: tx_ttl
                                    
                                    	Time to live for transmitted message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tx_packet_test
                                    
                                    	Test for existence of a TX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: delay_keep_alive_trigger
                                    
                                    	Number of milliseconds to wait after an L1 failure is detected before triggering an L2 wrap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: asserted_failure
                                    
                                    	Failures presently asserted
                                    	**type**\: list of  		 :py:class:`AssertedFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA.AssertedFailure>`
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA, self).__init__()

                                        self.yang_name = "side-a"
                                        self.yang_parent_name = "local-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("asserted-failure", ("asserted_failure", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA.AssertedFailure))])
                                        self._leafs = OrderedDict([
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ('wrap_state', (YLeaf(YType.enumeration, 'wrap-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsWrapState', '')])),
                                            ('packet_sent_timer', (YLeaf(YType.uint32, 'packet-sent-timer'), ['int'])),
                                            ('send_timer_time_remaining', (YLeaf(YType.uint32, 'send-timer-time-remaining'), ['int'])),
                                            ('wtr_timer_remaining', (YLeaf(YType.uint32, 'wtr-timer-remaining'), ['int'])),
                                            ('self_detected_request', (YLeaf(YType.enumeration, 'self-detected-request'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('remote_request', (YLeaf(YType.enumeration, 'remote-request'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('rx_neighbor_mac_address', (YLeaf(YType.str, 'rx-neighbor-mac-address'), ['str'])),
                                            ('rx_message_type', (YLeaf(YType.enumeration, 'rx-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('rx_path_type', (YLeaf(YType.enumeration, 'rx-path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsPathInd', '')])),
                                            ('rx_ttl', (YLeaf(YType.uint32, 'rx-ttl'), ['int'])),
                                            ('rx_packet_test', (YLeaf(YType.int32, 'rx-packet-test'), ['int'])),
                                            ('tx_neighbor_mac_address', (YLeaf(YType.str, 'tx-neighbor-mac-address'), ['str'])),
                                            ('tx_message_type', (YLeaf(YType.enumeration, 'tx-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('tx_path_type', (YLeaf(YType.enumeration, 'tx-path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsPathInd', '')])),
                                            ('tx_ttl', (YLeaf(YType.uint32, 'tx-ttl'), ['int'])),
                                            ('tx_packet_test', (YLeaf(YType.int32, 'tx-packet-test'), ['int'])),
                                            ('delay_keep_alive_trigger', (YLeaf(YType.uint32, 'delay-keep-alive-trigger'), ['int'])),
                                        ])
                                        self.mac_address = None
                                        self.wrap_state = None
                                        self.packet_sent_timer = None
                                        self.send_timer_time_remaining = None
                                        self.wtr_timer_remaining = None
                                        self.self_detected_request = None
                                        self.remote_request = None
                                        self.rx_neighbor_mac_address = None
                                        self.rx_message_type = None
                                        self.rx_path_type = None
                                        self.rx_ttl = None
                                        self.rx_packet_test = None
                                        self.tx_neighbor_mac_address = None
                                        self.tx_message_type = None
                                        self.tx_path_type = None
                                        self.tx_ttl = None
                                        self.tx_packet_test = None
                                        self.delay_keep_alive_trigger = None

                                        self.asserted_failure = YList(self)
                                        self._segment_path = lambda: "side-a"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA, ['mac_address', 'wrap_state', 'packet_sent_timer', 'send_timer_time_remaining', 'wtr_timer_remaining', 'self_detected_request', 'remote_request', 'rx_neighbor_mac_address', 'rx_message_type', 'rx_path_type', 'rx_ttl', 'rx_packet_test', 'tx_neighbor_mac_address', 'tx_message_type', 'tx_path_type', 'tx_ttl', 'tx_packet_test', 'delay_keep_alive_trigger'], name, value)


                                    class AssertedFailure(Entity):
                                        """
                                        Failures presently asserted
                                        
                                        .. attribute:: type
                                        
                                        	Failure type
                                        	**type**\:  :py:class:`SrpMgmtFailureEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureEt>`
                                        
                                        .. attribute:: reported_state
                                        
                                        	Reported state
                                        	**type**\:  :py:class:`SrpMgmtFailureStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt>`
                                        
                                        .. attribute:: debounced_state
                                        
                                        	Debounced state
                                        	**type**\:  :py:class:`SrpMgmtFailureStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt>`
                                        
                                        .. attribute:: current_state
                                        
                                        	Current state
                                        	**type**\:  :py:class:`SrpMgmtFailureStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt>`
                                        
                                        .. attribute:: stable_time
                                        
                                        	Stable time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: debounced_delay
                                        
                                        	Debounce delay
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'pfi-im-cmd-oper'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA.AssertedFailure, self).__init__()

                                            self.yang_name = "asserted-failure"
                                            self.yang_parent_name = "side-a"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureEt', '')])),
                                                ('reported_state', (YLeaf(YType.enumeration, 'reported-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureStateEt', '')])),
                                                ('debounced_state', (YLeaf(YType.enumeration, 'debounced-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureStateEt', '')])),
                                                ('current_state', (YLeaf(YType.enumeration, 'current-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureStateEt', '')])),
                                                ('stable_time', (YLeaf(YType.uint64, 'stable-time'), ['int'])),
                                                ('debounced_delay', (YLeaf(YType.uint32, 'debounced-delay'), ['int'])),
                                            ])
                                            self.type = None
                                            self.reported_state = None
                                            self.debounced_state = None
                                            self.current_state = None
                                            self.stable_time = None
                                            self.debounced_delay = None
                                            self._segment_path = lambda: "asserted-failure"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideA.AssertedFailure, ['type', 'reported_state', 'debounced_state', 'current_state', 'stable_time', 'debounced_delay'], name, value)


                                class SideB(Entity):
                                    """
                                    Side B IPS details
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    .. attribute:: wrap_state
                                    
                                    	Wrap state
                                    	**type**\:  :py:class:`SrpMgmtIpsWrapState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsWrapState>`
                                    
                                    .. attribute:: packet_sent_timer
                                    
                                    	SRP IPS packet send interval in seconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: send_timer_time_remaining
                                    
                                    	Time in seconds remaining until next send of an IPS request
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: wtr_timer_remaining
                                    
                                    	Time in seconds until wrap removal
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: self_detected_request
                                    
                                    	Self Detected Requests
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: remote_request
                                    
                                    	Remote Requests
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: rx_neighbor_mac_address
                                    
                                    	Neighbour mac address for received message
                                    	**type**\: str
                                    
                                    .. attribute:: rx_message_type
                                    
                                    	Type of message received
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: rx_path_type
                                    
                                    	Short/long path for received message
                                    	**type**\:  :py:class:`SrpMgmtIpsPathInd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd>`
                                    
                                    .. attribute:: rx_ttl
                                    
                                    	Time to live for received message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: rx_packet_test
                                    
                                    	Test for existence of an RX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: tx_neighbor_mac_address
                                    
                                    	Mac address of node receiving TXed messages
                                    	**type**\: str
                                    
                                    .. attribute:: tx_message_type
                                    
                                    	Type of message transmitted
                                    	**type**\:  :py:class:`SrpMgmtIpsReq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq>`
                                    
                                    .. attribute:: tx_path_type
                                    
                                    	Short/long path of transmitted message
                                    	**type**\:  :py:class:`SrpMgmtIpsPathInd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd>`
                                    
                                    .. attribute:: tx_ttl
                                    
                                    	Time to live for transmitted message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tx_packet_test
                                    
                                    	Test for existence of a TX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: delay_keep_alive_trigger
                                    
                                    	Number of milliseconds to wait after an L1 failure is detected before triggering an L2 wrap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: millisecond
                                    
                                    .. attribute:: asserted_failure
                                    
                                    	Failures presently asserted
                                    	**type**\: list of  		 :py:class:`AssertedFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB.AssertedFailure>`
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB, self).__init__()

                                        self.yang_name = "side-b"
                                        self.yang_parent_name = "local-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("asserted-failure", ("asserted_failure", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB.AssertedFailure))])
                                        self._leafs = OrderedDict([
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ('wrap_state', (YLeaf(YType.enumeration, 'wrap-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsWrapState', '')])),
                                            ('packet_sent_timer', (YLeaf(YType.uint32, 'packet-sent-timer'), ['int'])),
                                            ('send_timer_time_remaining', (YLeaf(YType.uint32, 'send-timer-time-remaining'), ['int'])),
                                            ('wtr_timer_remaining', (YLeaf(YType.uint32, 'wtr-timer-remaining'), ['int'])),
                                            ('self_detected_request', (YLeaf(YType.enumeration, 'self-detected-request'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('remote_request', (YLeaf(YType.enumeration, 'remote-request'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('rx_neighbor_mac_address', (YLeaf(YType.str, 'rx-neighbor-mac-address'), ['str'])),
                                            ('rx_message_type', (YLeaf(YType.enumeration, 'rx-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('rx_path_type', (YLeaf(YType.enumeration, 'rx-path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsPathInd', '')])),
                                            ('rx_ttl', (YLeaf(YType.uint32, 'rx-ttl'), ['int'])),
                                            ('rx_packet_test', (YLeaf(YType.int32, 'rx-packet-test'), ['int'])),
                                            ('tx_neighbor_mac_address', (YLeaf(YType.str, 'tx-neighbor-mac-address'), ['str'])),
                                            ('tx_message_type', (YLeaf(YType.enumeration, 'tx-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsReq', '')])),
                                            ('tx_path_type', (YLeaf(YType.enumeration, 'tx-path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtIpsPathInd', '')])),
                                            ('tx_ttl', (YLeaf(YType.uint32, 'tx-ttl'), ['int'])),
                                            ('tx_packet_test', (YLeaf(YType.int32, 'tx-packet-test'), ['int'])),
                                            ('delay_keep_alive_trigger', (YLeaf(YType.uint32, 'delay-keep-alive-trigger'), ['int'])),
                                        ])
                                        self.mac_address = None
                                        self.wrap_state = None
                                        self.packet_sent_timer = None
                                        self.send_timer_time_remaining = None
                                        self.wtr_timer_remaining = None
                                        self.self_detected_request = None
                                        self.remote_request = None
                                        self.rx_neighbor_mac_address = None
                                        self.rx_message_type = None
                                        self.rx_path_type = None
                                        self.rx_ttl = None
                                        self.rx_packet_test = None
                                        self.tx_neighbor_mac_address = None
                                        self.tx_message_type = None
                                        self.tx_path_type = None
                                        self.tx_ttl = None
                                        self.tx_packet_test = None
                                        self.delay_keep_alive_trigger = None

                                        self.asserted_failure = YList(self)
                                        self._segment_path = lambda: "side-b"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB, ['mac_address', 'wrap_state', 'packet_sent_timer', 'send_timer_time_remaining', 'wtr_timer_remaining', 'self_detected_request', 'remote_request', 'rx_neighbor_mac_address', 'rx_message_type', 'rx_path_type', 'rx_ttl', 'rx_packet_test', 'tx_neighbor_mac_address', 'tx_message_type', 'tx_path_type', 'tx_ttl', 'tx_packet_test', 'delay_keep_alive_trigger'], name, value)


                                    class AssertedFailure(Entity):
                                        """
                                        Failures presently asserted
                                        
                                        .. attribute:: type
                                        
                                        	Failure type
                                        	**type**\:  :py:class:`SrpMgmtFailureEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureEt>`
                                        
                                        .. attribute:: reported_state
                                        
                                        	Reported state
                                        	**type**\:  :py:class:`SrpMgmtFailureStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt>`
                                        
                                        .. attribute:: debounced_state
                                        
                                        	Debounced state
                                        	**type**\:  :py:class:`SrpMgmtFailureStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt>`
                                        
                                        .. attribute:: current_state
                                        
                                        	Current state
                                        	**type**\:  :py:class:`SrpMgmtFailureStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt>`
                                        
                                        .. attribute:: stable_time
                                        
                                        	Stable time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: debounced_delay
                                        
                                        	Debounce delay
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'pfi-im-cmd-oper'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB.AssertedFailure, self).__init__()

                                            self.yang_name = "asserted-failure"
                                            self.yang_parent_name = "side-b"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureEt', '')])),
                                                ('reported_state', (YLeaf(YType.enumeration, 'reported-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureStateEt', '')])),
                                                ('debounced_state', (YLeaf(YType.enumeration, 'debounced-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureStateEt', '')])),
                                                ('current_state', (YLeaf(YType.enumeration, 'current-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtFailureStateEt', '')])),
                                                ('stable_time', (YLeaf(YType.uint64, 'stable-time'), ['int'])),
                                                ('debounced_delay', (YLeaf(YType.uint32, 'debounced-delay'), ['int'])),
                                            ])
                                            self.type = None
                                            self.reported_state = None
                                            self.debounced_state = None
                                            self.current_state = None
                                            self.stable_time = None
                                            self.debounced_delay = None
                                            self._segment_path = lambda: "asserted-failure"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.IpsInfo.LocalInformation.SideB.AssertedFailure, ['type', 'reported_state', 'debounced_state', 'current_state', 'stable_time', 'debounced_delay'], name, value)


                        class TopologyInfo(Entity):
                            """
                            SRP topology information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_information
                            
                            	Detailed SRP topology information
                            	**type**\: list of  		 :py:class:`LocalInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo, self).__init__()

                                self.yang_name = "topology-info"
                                self.yang_parent_name = "srp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-information", ("local_information", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation))])
                                self._leafs = OrderedDict([
                                    ('is_admin_down', (YLeaf(YType.int32, 'is-admin-down'), ['int'])),
                                ])
                                self.is_admin_down = None

                                self.local_information = YList(self)
                                self._segment_path = lambda: "topology-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo, ['is_admin_down'], name, value)


                            class LocalInformation(Entity):
                                """
                                Detailed SRP topology information
                                
                                .. attribute:: topology_timer
                                
                                	How often a topology pkt is sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_topology_packet_delay
                                
                                	Time remaining until next topo pkt sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_since_last_topology_packet_received
                                
                                	Time since last topo pkt was received
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_since_last_topology_change
                                
                                	Time since last topology change
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: number_of_nodes_on_ring
                                
                                	Number of nodes on ring
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: ring_node
                                
                                	List of nodes on the ring info
                                	**type**\: list of  		 :py:class:`RingNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation.RingNode>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation, self).__init__()

                                    self.yang_name = "local-information"
                                    self.yang_parent_name = "topology-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("ring-node", ("ring_node", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation.RingNode))])
                                    self._leafs = OrderedDict([
                                        ('topology_timer', (YLeaf(YType.uint32, 'topology-timer'), ['int'])),
                                        ('next_topology_packet_delay', (YLeaf(YType.uint32, 'next-topology-packet-delay'), ['int'])),
                                        ('time_since_last_topology_packet_received', (YLeaf(YType.uint32, 'time-since-last-topology-packet-received'), ['int'])),
                                        ('time_since_last_topology_change', (YLeaf(YType.uint32, 'time-since-last-topology-change'), ['int'])),
                                        ('number_of_nodes_on_ring', (YLeaf(YType.uint16, 'number-of-nodes-on-ring'), ['int'])),
                                    ])
                                    self.topology_timer = None
                                    self.next_topology_packet_delay = None
                                    self.time_since_last_topology_packet_received = None
                                    self.time_since_last_topology_change = None
                                    self.number_of_nodes_on_ring = None

                                    self.ring_node = YList(self)
                                    self._segment_path = lambda: "local-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation, ['topology_timer', 'next_topology_packet_delay', 'time_since_last_topology_packet_received', 'time_since_last_topology_change', 'number_of_nodes_on_ring'], name, value)


                                class RingNode(Entity):
                                    """
                                    List of nodes on the ring info
                                    
                                    .. attribute:: hop_count
                                    
                                    	Outer\-ring hops to reach this node
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: is_wrapped
                                    
                                    	Wrap state
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: is_srr_supported
                                    
                                    	SRR protocol supported
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation.RingNode, self).__init__()

                                        self.yang_name = "ring-node"
                                        self.yang_parent_name = "local-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('hop_count', (YLeaf(YType.uint16, 'hop-count'), ['int'])),
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('is_wrapped', (YLeaf(YType.int32, 'is-wrapped'), ['int'])),
                                            ('is_srr_supported', (YLeaf(YType.int32, 'is-srr-supported'), ['int'])),
                                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                        ])
                                        self.hop_count = None
                                        self.mac_address = None
                                        self.ipv4_address = None
                                        self.is_wrapped = None
                                        self.is_srr_supported = None
                                        self.node_name = None
                                        self._segment_path = lambda: "ring-node"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.TopologyInfo.LocalInformation.RingNode, ['hop_count', 'mac_address', 'ipv4_address', 'is_wrapped', 'is_srr_supported', 'node_name'], name, value)


                        class SrrInfo(Entity):
                            """
                            SRP SRR information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_srr_enabled
                            
                            	SRR enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: srr_detailed_info
                            
                            	SRP information
                            	**type**\: list of  		 :py:class:`SrrDetailedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo, self).__init__()

                                self.yang_name = "srr-info"
                                self.yang_parent_name = "srp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("srr-detailed-info", ("srr_detailed_info", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo))])
                                self._leafs = OrderedDict([
                                    ('is_admin_down', (YLeaf(YType.int32, 'is-admin-down'), ['int'])),
                                    ('is_srr_enabled', (YLeaf(YType.int32, 'is-srr-enabled'), ['int'])),
                                ])
                                self.is_admin_down = None
                                self.is_srr_enabled = None

                                self.srr_detailed_info = YList(self)
                                self._segment_path = lambda: "srr-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo, ['is_admin_down', 'is_srr_enabled'], name, value)


                            class SrrDetailedInfo(Entity):
                                """
                                SRP information
                                
                                .. attribute:: version_number
                                
                                	Version number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_wrong_version_received
                                
                                	Wrong version recieved
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: last_wrong_version_receive_time
                                
                                	Time that last wrong version message recieved
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mac_address
                                
                                	SRR node mac address
                                	**type**\: str
                                
                                .. attribute:: node_state
                                
                                	SRR node state
                                	**type**\:  :py:class:`SrpMgmtSrrNodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrNodeState>`
                                
                                .. attribute:: is_outer_ring_in_use
                                
                                	Is the outer ring in use
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_inner_ring_in_use
                                
                                	 Is the inner ring in use
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_announce
                                
                                	Is announcing enabled
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: outer_fail_type
                                
                                	Outer fail type
                                	**type**\:  :py:class:`SrpMgmtSrrFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure>`
                                
                                .. attribute:: inner_fail_type
                                
                                	Inner fail type
                                	**type**\:  :py:class:`SrpMgmtSrrFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure>`
                                
                                .. attribute:: packet_send_timer
                                
                                	SRR packet send timer interval in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: next_srr_packet_send_time
                                
                                	Time remaining in seconds to next SRR packet send
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: single_ring_bw
                                
                                	Single ring bandwidth Mbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: Mbit/s
                                
                                .. attribute:: wtr_time
                                
                                	SRR Wait To Restore interval delay in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: wtr_timer_remaining_outer_ring
                                
                                	Time remaining in seconds until next outer ring wrap removal
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: wtr_timer_remaining_inner_ring
                                
                                	Time remaining in seconds until next inner ring wrap removal
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: nodes_on_ring
                                
                                	List of nodes on the ring info
                                	**type**\: list of  		 :py:class:`NodesOnRing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesOnRing>`
                                
                                .. attribute:: nodes_not_on_ring
                                
                                	nodes not in topology map
                                	**type**\: list of  		 :py:class:`NodesNotOnRing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesNotOnRing>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo, self).__init__()

                                    self.yang_name = "srr-detailed-info"
                                    self.yang_parent_name = "srr-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("nodes-on-ring", ("nodes_on_ring", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesOnRing)), ("nodes-not-on-ring", ("nodes_not_on_ring", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesNotOnRing))])
                                    self._leafs = OrderedDict([
                                        ('version_number', (YLeaf(YType.uint32, 'version-number'), ['int'])),
                                        ('is_wrong_version_received', (YLeaf(YType.int32, 'is-wrong-version-received'), ['int'])),
                                        ('last_wrong_version_receive_time', (YLeaf(YType.uint32, 'last-wrong-version-receive-time'), ['int'])),
                                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                        ('node_state', (YLeaf(YType.enumeration, 'node-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrNodeState', '')])),
                                        ('is_outer_ring_in_use', (YLeaf(YType.int32, 'is-outer-ring-in-use'), ['int'])),
                                        ('is_inner_ring_in_use', (YLeaf(YType.int32, 'is-inner-ring-in-use'), ['int'])),
                                        ('is_announce', (YLeaf(YType.int32, 'is-announce'), ['int'])),
                                        ('outer_fail_type', (YLeaf(YType.enumeration, 'outer-fail-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrFailure', '')])),
                                        ('inner_fail_type', (YLeaf(YType.enumeration, 'inner-fail-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrFailure', '')])),
                                        ('packet_send_timer', (YLeaf(YType.uint32, 'packet-send-timer'), ['int'])),
                                        ('next_srr_packet_send_time', (YLeaf(YType.uint32, 'next-srr-packet-send-time'), ['int'])),
                                        ('single_ring_bw', (YLeaf(YType.uint32, 'single-ring-bw'), ['int'])),
                                        ('wtr_time', (YLeaf(YType.uint32, 'wtr-time'), ['int'])),
                                        ('wtr_timer_remaining_outer_ring', (YLeaf(YType.uint32, 'wtr-timer-remaining-outer-ring'), ['int'])),
                                        ('wtr_timer_remaining_inner_ring', (YLeaf(YType.uint32, 'wtr-timer-remaining-inner-ring'), ['int'])),
                                    ])
                                    self.version_number = None
                                    self.is_wrong_version_received = None
                                    self.last_wrong_version_receive_time = None
                                    self.mac_address = None
                                    self.node_state = None
                                    self.is_outer_ring_in_use = None
                                    self.is_inner_ring_in_use = None
                                    self.is_announce = None
                                    self.outer_fail_type = None
                                    self.inner_fail_type = None
                                    self.packet_send_timer = None
                                    self.next_srr_packet_send_time = None
                                    self.single_ring_bw = None
                                    self.wtr_time = None
                                    self.wtr_timer_remaining_outer_ring = None
                                    self.wtr_timer_remaining_inner_ring = None

                                    self.nodes_on_ring = YList(self)
                                    self.nodes_not_on_ring = YList(self)
                                    self._segment_path = lambda: "srr-detailed-info"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo, ['version_number', 'is_wrong_version_received', 'last_wrong_version_receive_time', 'mac_address', 'node_state', 'is_outer_ring_in_use', 'is_inner_ring_in_use', 'is_announce', 'outer_fail_type', 'inner_fail_type', 'packet_send_timer', 'next_srr_packet_send_time', 'single_ring_bw', 'wtr_time', 'wtr_timer_remaining_outer_ring', 'wtr_timer_remaining_inner_ring'], name, value)


                                class NodesOnRing(Entity):
                                    """
                                    List of nodes on the ring info
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\: str
                                    
                                    .. attribute:: srr_entry_exits
                                    
                                    	Does the SRR information exist for this node
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: mac_address
                                    
                                    	node mac address
                                    	**type**\: str
                                    
                                    .. attribute:: outer_failure
                                    
                                    	Outer failure
                                    	**type**\:  :py:class:`SrpMgmtSrrFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure>`
                                    
                                    .. attribute:: inner_failure
                                    
                                    	Inner failure
                                    	**type**\:  :py:class:`SrpMgmtSrrFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure>`
                                    
                                    .. attribute:: is_last_announce_received
                                    
                                    	Announce last received ?
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: last_announce_received_time
                                    
                                    	Announce last received
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesOnRing, self).__init__()

                                        self.yang_name = "nodes-on-ring"
                                        self.yang_parent_name = "srr-detailed-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                            ('srr_entry_exits', (YLeaf(YType.int32, 'srr-entry-exits'), ['int'])),
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ('outer_failure', (YLeaf(YType.enumeration, 'outer-failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrFailure', '')])),
                                            ('inner_failure', (YLeaf(YType.enumeration, 'inner-failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrFailure', '')])),
                                            ('is_last_announce_received', (YLeaf(YType.int32, 'is-last-announce-received'), ['int'])),
                                            ('last_announce_received_time', (YLeaf(YType.uint32, 'last-announce-received-time'), ['int'])),
                                        ])
                                        self.node_name = None
                                        self.srr_entry_exits = None
                                        self.mac_address = None
                                        self.outer_failure = None
                                        self.inner_failure = None
                                        self.is_last_announce_received = None
                                        self.last_announce_received_time = None
                                        self._segment_path = lambda: "nodes-on-ring"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesOnRing, ['node_name', 'srr_entry_exits', 'mac_address', 'outer_failure', 'inner_failure', 'is_last_announce_received', 'last_announce_received_time'], name, value)


                                class NodesNotOnRing(Entity):
                                    """
                                    nodes not in topology map
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\: str
                                    
                                    .. attribute:: srr_entry_exits
                                    
                                    	Does the SRR information exist for this node
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: mac_address
                                    
                                    	node mac address
                                    	**type**\: str
                                    
                                    .. attribute:: outer_failure
                                    
                                    	Outer failure
                                    	**type**\:  :py:class:`SrpMgmtSrrFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure>`
                                    
                                    .. attribute:: inner_failure
                                    
                                    	Inner failure
                                    	**type**\:  :py:class:`SrpMgmtSrrFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure>`
                                    
                                    .. attribute:: is_last_announce_received
                                    
                                    	Announce last received ?
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: last_announce_received_time
                                    
                                    	Announce last received
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesNotOnRing, self).__init__()

                                        self.yang_name = "nodes-not-on-ring"
                                        self.yang_parent_name = "srr-detailed-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                            ('srr_entry_exits', (YLeaf(YType.int32, 'srr-entry-exits'), ['int'])),
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ('outer_failure', (YLeaf(YType.enumeration, 'outer-failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrFailure', '')])),
                                            ('inner_failure', (YLeaf(YType.enumeration, 'inner-failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SrpMgmtSrrFailure', '')])),
                                            ('is_last_announce_received', (YLeaf(YType.int32, 'is-last-announce-received'), ['int'])),
                                            ('last_announce_received_time', (YLeaf(YType.uint32, 'last-announce-received-time'), ['int'])),
                                        ])
                                        self.node_name = None
                                        self.srr_entry_exits = None
                                        self.mac_address = None
                                        self.outer_failure = None
                                        self.inner_failure = None
                                        self.is_last_announce_received = None
                                        self.last_announce_received_time = None
                                        self._segment_path = lambda: "nodes-not-on-ring"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.SrrInfo.SrrDetailedInfo.NodesNotOnRing, ['node_name', 'srr_entry_exits', 'mac_address', 'outer_failure', 'inner_failure', 'is_last_announce_received', 'last_announce_received_time'], name, value)


                        class RateLimitInfo(Entity):
                            """
                            SRP rate limit information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate_limit_detailed_info
                            
                            	SRP rate limit information
                            	**type**\: list of  		 :py:class:`RateLimitDetailedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo.RateLimitDetailedInfo>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo, self).__init__()

                                self.yang_name = "rate-limit-info"
                                self.yang_parent_name = "srp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("rate-limit-detailed-info", ("rate_limit_detailed_info", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo.RateLimitDetailedInfo))])
                                self._leafs = OrderedDict([
                                    ('is_admin_down', (YLeaf(YType.int32, 'is-admin-down'), ['int'])),
                                ])
                                self.is_admin_down = None

                                self.rate_limit_detailed_info = YList(self)
                                self._segment_path = lambda: "rate-limit-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo, ['is_admin_down'], name, value)


                            class RateLimitDetailedInfo(Entity):
                                """
                                SRP rate limit information
                                
                                .. attribute:: min_priority_value
                                
                                	Minimum SRP priority for high\-priority transmit queue
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo.RateLimitDetailedInfo, self).__init__()

                                    self.yang_name = "rate-limit-detailed-info"
                                    self.yang_parent_name = "rate-limit-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('min_priority_value', (YLeaf(YType.uint16, 'min-priority-value'), ['int'])),
                                    ])
                                    self.min_priority_value = None
                                    self._segment_path = lambda: "rate-limit-detailed-info"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation_.RateLimitInfo.RateLimitDetailedInfo, ['min_priority_value'], name, value)


                    class SrpStatistics(Entity):
                        """
                        SRP\-specific packet and byte counters
                        
                        .. attribute:: side_a_data_rate
                        
                        	Data rates for side A interface
                        	**type**\:  :py:class:`SideADataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate>`
                        
                        .. attribute:: side_b_data_rate
                        
                        	Data rates for side B interface
                        	**type**\:  :py:class:`SideBDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate>`
                        
                        .. attribute:: side_a_errors
                        
                        	Errors for side A interface
                        	**type**\:  :py:class:`SideAErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors>`
                        
                        .. attribute:: side_b_errors
                        
                        	Errors for side B interface
                        	**type**\:  :py:class:`SideBErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors>`
                        
                        .. attribute:: data_rate_interval
                        
                        	Data rate interval (5 mins or 30 seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics, self).__init__()

                            self.yang_name = "srp-statistics"
                            self.yang_parent_name = "srp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("side-a-data-rate", ("side_a_data_rate", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate)), ("side-b-data-rate", ("side_b_data_rate", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate)), ("side-a-errors", ("side_a_errors", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors)), ("side-b-errors", ("side_b_errors", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors))])
                            self._leafs = OrderedDict([
                                ('data_rate_interval', (YLeaf(YType.uint32, 'data-rate-interval'), ['int'])),
                            ])
                            self.data_rate_interval = None

                            self.side_a_data_rate = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate()
                            self.side_a_data_rate.parent = self
                            self._children_name_map["side_a_data_rate"] = "side-a-data-rate"

                            self.side_b_data_rate = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate()
                            self.side_b_data_rate.parent = self
                            self._children_name_map["side_b_data_rate"] = "side-b-data-rate"

                            self.side_a_errors = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors()
                            self.side_a_errors.parent = self
                            self._children_name_map["side_a_errors"] = "side-a-errors"

                            self.side_b_errors = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors()
                            self.side_b_errors.parent = self
                            self._children_name_map["side_b_errors"] = "side-b-errors"
                            self._segment_path = lambda: "srp-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics, ['data_rate_interval'], name, value)


                        class SideADataRate(Entity):
                            """
                            Data rates for side A interface
                            
                            .. attribute:: bit_rate_sent
                            
                            	Sent bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_sent
                            
                            	Sent packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bit_rate_received
                            
                            	Received bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_received
                            
                            	Received packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate, self).__init__()

                                self.yang_name = "side-a-data-rate"
                                self.yang_parent_name = "srp-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bit_rate_sent', (YLeaf(YType.uint32, 'bit-rate-sent'), ['int'])),
                                    ('packet_rate_sent', (YLeaf(YType.uint32, 'packet-rate-sent'), ['int'])),
                                    ('bit_rate_received', (YLeaf(YType.uint32, 'bit-rate-received'), ['int'])),
                                    ('packet_rate_received', (YLeaf(YType.uint32, 'packet-rate-received'), ['int'])),
                                ])
                                self.bit_rate_sent = None
                                self.packet_rate_sent = None
                                self.bit_rate_received = None
                                self.packet_rate_received = None
                                self._segment_path = lambda: "side-a-data-rate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate, ['bit_rate_sent', 'packet_rate_sent', 'bit_rate_received', 'packet_rate_received'], name, value)


                        class SideBDataRate(Entity):
                            """
                            Data rates for side B interface
                            
                            .. attribute:: bit_rate_sent
                            
                            	Sent bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_sent
                            
                            	Sent packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bit_rate_received
                            
                            	Received bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_received
                            
                            	Received packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate, self).__init__()

                                self.yang_name = "side-b-data-rate"
                                self.yang_parent_name = "srp-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bit_rate_sent', (YLeaf(YType.uint32, 'bit-rate-sent'), ['int'])),
                                    ('packet_rate_sent', (YLeaf(YType.uint32, 'packet-rate-sent'), ['int'])),
                                    ('bit_rate_received', (YLeaf(YType.uint32, 'bit-rate-received'), ['int'])),
                                    ('packet_rate_received', (YLeaf(YType.uint32, 'packet-rate-received'), ['int'])),
                                ])
                                self.bit_rate_sent = None
                                self.packet_rate_sent = None
                                self.bit_rate_received = None
                                self.packet_rate_received = None
                                self._segment_path = lambda: "side-b-data-rate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate, ['bit_rate_sent', 'packet_rate_sent', 'bit_rate_received', 'packet_rate_received'], name, value)


                        class SideAErrors(Entity):
                            """
                            Errors for side A interface
                            
                            .. attribute:: error_packets_received
                            
                            	Error packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: crc_errors
                            
                            	Input CRC errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_insufficient_resource_events
                            
                            	Input insufficient resources events
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_aborts_received
                            
                            	Aborts received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_runt_packets_received
                            
                            	Too small packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_giant_packets_received
                            
                            	Too large packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_runt_packets_received
                            
                            	Too small packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_giant_packets_received
                            
                            	Too large packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_aborts_received
                            
                            	Aborts received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors, self).__init__()

                                self.yang_name = "side-a-errors"
                                self.yang_parent_name = "srp-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('error_packets_received', (YLeaf(YType.uint32, 'error-packets-received'), ['int'])),
                                    ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                                    ('input_insufficient_resource_events', (YLeaf(YType.uint32, 'input-insufficient-resource-events'), ['int'])),
                                    ('mac_aborts_received', (YLeaf(YType.uint32, 'mac-aborts-received'), ['int'])),
                                    ('mac_runt_packets_received', (YLeaf(YType.uint32, 'mac-runt-packets-received'), ['int'])),
                                    ('mac_giant_packets_received', (YLeaf(YType.uint32, 'mac-giant-packets-received'), ['int'])),
                                    ('framer_runt_packets_received', (YLeaf(YType.uint32, 'framer-runt-packets-received'), ['int'])),
                                    ('framer_giant_packets_received', (YLeaf(YType.uint32, 'framer-giant-packets-received'), ['int'])),
                                    ('framer_aborts_received', (YLeaf(YType.uint32, 'framer-aborts-received'), ['int'])),
                                ])
                                self.error_packets_received = None
                                self.crc_errors = None
                                self.input_insufficient_resource_events = None
                                self.mac_aborts_received = None
                                self.mac_runt_packets_received = None
                                self.mac_giant_packets_received = None
                                self.framer_runt_packets_received = None
                                self.framer_giant_packets_received = None
                                self.framer_aborts_received = None
                                self._segment_path = lambda: "side-a-errors"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors, ['error_packets_received', 'crc_errors', 'input_insufficient_resource_events', 'mac_aborts_received', 'mac_runt_packets_received', 'mac_giant_packets_received', 'framer_runt_packets_received', 'framer_giant_packets_received', 'framer_aborts_received'], name, value)


                        class SideBErrors(Entity):
                            """
                            Errors for side B interface
                            
                            .. attribute:: error_packets_received
                            
                            	Error packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: crc_errors
                            
                            	Input CRC errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_insufficient_resource_events
                            
                            	Input insufficient resources events
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_aborts_received
                            
                            	Aborts received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_runt_packets_received
                            
                            	Too small packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_giant_packets_received
                            
                            	Too large packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_runt_packets_received
                            
                            	Too small packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_giant_packets_received
                            
                            	Too large packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_aborts_received
                            
                            	Aborts received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors, self).__init__()

                                self.yang_name = "side-b-errors"
                                self.yang_parent_name = "srp-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('error_packets_received', (YLeaf(YType.uint32, 'error-packets-received'), ['int'])),
                                    ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                                    ('input_insufficient_resource_events', (YLeaf(YType.uint32, 'input-insufficient-resource-events'), ['int'])),
                                    ('mac_aborts_received', (YLeaf(YType.uint32, 'mac-aborts-received'), ['int'])),
                                    ('mac_runt_packets_received', (YLeaf(YType.uint32, 'mac-runt-packets-received'), ['int'])),
                                    ('mac_giant_packets_received', (YLeaf(YType.uint32, 'mac-giant-packets-received'), ['int'])),
                                    ('framer_runt_packets_received', (YLeaf(YType.uint32, 'framer-runt-packets-received'), ['int'])),
                                    ('framer_giant_packets_received', (YLeaf(YType.uint32, 'framer-giant-packets-received'), ['int'])),
                                    ('framer_aborts_received', (YLeaf(YType.uint32, 'framer-aborts-received'), ['int'])),
                                ])
                                self.error_packets_received = None
                                self.crc_errors = None
                                self.input_insufficient_resource_events = None
                                self.mac_aborts_received = None
                                self.mac_runt_packets_received = None
                                self.mac_giant_packets_received = None
                                self.framer_runt_packets_received = None
                                self.framer_giant_packets_received = None
                                self.framer_aborts_received = None
                                self._segment_path = lambda: "side-b-errors"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors, ['error_packets_received', 'crc_errors', 'input_insufficient_resource_events', 'mac_aborts_received', 'mac_runt_packets_received', 'mac_giant_packets_received', 'framer_runt_packets_received', 'framer_giant_packets_received', 'framer_aborts_received'], name, value)


                class TunnelInformation(Entity):
                    """
                    Tunnel interface information
                    
                    .. attribute:: source_name
                    
                    	Tunnel source name
                    	**type**\: str
                    
                    .. attribute:: source_ipv4_address
                    
                    	Tunnel source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_ipv4_address
                    
                    	Tunnel destination IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel_type
                    
                    	Tunnel protocol/transport
                    	**type**\: str
                    
                    .. attribute:: key
                    
                    	GRE tunnel key
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ttl
                    
                    	GRE tunnel TTL
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation, self).__init__()

                        self.yang_name = "tunnel-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('source_name', (YLeaf(YType.str, 'source-name'), ['str'])),
                            ('source_ipv4_address', (YLeaf(YType.str, 'source-ipv4-address'), ['str'])),
                            ('destination_ipv4_address', (YLeaf(YType.str, 'destination-ipv4-address'), ['str'])),
                            ('tunnel_type', (YLeaf(YType.str, 'tunnel-type'), ['str'])),
                            ('key', (YLeaf(YType.uint32, 'key'), ['int'])),
                            ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                        ])
                        self.source_name = None
                        self.source_ipv4_address = None
                        self.destination_ipv4_address = None
                        self.tunnel_type = None
                        self.key = None
                        self.ttl = None
                        self._segment_path = lambda: "tunnel-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation, ['source_name', 'source_ipv4_address', 'destination_ipv4_address', 'tunnel_type', 'key', 'ttl'], name, value)


                class BundleInformation(Entity):
                    """
                    Bundle interface information
                    
                    .. attribute:: member
                    
                    	List of bundle members and their properties
                    	**type**\: list of  		 :py:class:`Member <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation, self).__init__()

                        self.yang_name = "bundle-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("member", ("member", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member))])
                        self._leafs = OrderedDict()

                        self.member = YList(self)
                        self._segment_path = lambda: "bundle-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation, [], name, value)


                    class Member(Entity):
                        """
                        List of bundle members and their properties
                        
                        .. attribute:: counters
                        
                        	Counters data about member link
                        	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters>`
                        
                        .. attribute:: link_data
                        
                        	Lacp data about member link
                        	**type**\:  :py:class:`LinkData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData>`
                        
                        .. attribute:: member_mux_data
                        
                        	Mux state machine data
                        	**type**\:  :py:class:`MemberMuxData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address of this member (deprecated)
                        	**type**\:  :py:class:`MacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress>`
                        
                        .. attribute:: interface_name
                        
                        	Member's interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: port_priority
                        
                        	The priority of this member
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: port_number
                        
                        	Member's link number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: underlying_link_id
                        
                        	Member's underlying link ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: link_order_number
                        
                        	Member's link order number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: iccp_node
                        
                        	Location of member
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bandwidth
                        
                        	Bandwidth of this member (kbps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: lacp_enabled
                        
                        	Boolean indicating LACP enabled or not
                        	**type**\: str
                        
                        .. attribute:: member_type
                        
                        	Member's type (local/foreign)
                        	**type**\:  :py:class:`BmdMemberTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmdMemberTypeEnum>`
                        
                        .. attribute:: member_name
                        
                        	Member's (short form) name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member, self).__init__()

                            self.yang_name = "member"
                            self.yang_parent_name = "bundle-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("counters", ("counters", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters)), ("link-data", ("link_data", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData)), ("member-mux-data", ("member_mux_data", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData)), ("mac-address", ("mac_address", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('port_priority', (YLeaf(YType.uint16, 'port-priority'), ['int'])),
                                ('port_number', (YLeaf(YType.uint16, 'port-number'), ['int'])),
                                ('underlying_link_id', (YLeaf(YType.uint16, 'underlying-link-id'), ['int'])),
                                ('link_order_number', (YLeaf(YType.uint16, 'link-order-number'), ['int'])),
                                ('iccp_node', (YLeaf(YType.uint32, 'iccp-node'), ['int'])),
                                ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                ('lacp_enabled', (YLeaf(YType.str, 'lacp-enabled'), ['str'])),
                                ('member_type', (YLeaf(YType.enumeration, 'member-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmdMemberTypeEnum', '')])),
                                ('member_name', (YLeaf(YType.str, 'member-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self.port_priority = None
                            self.port_number = None
                            self.underlying_link_id = None
                            self.link_order_number = None
                            self.iccp_node = None
                            self.bandwidth = None
                            self.lacp_enabled = None
                            self.member_type = None
                            self.member_name = None

                            self.counters = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters()
                            self.counters.parent = self
                            self._children_name_map["counters"] = "counters"

                            self.link_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData()
                            self.link_data.parent = self
                            self._children_name_map["link_data"] = "link-data"

                            self.member_mux_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData()
                            self.member_mux_data.parent = self
                            self._children_name_map["member_mux_data"] = "member-mux-data"

                            self.mac_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress()
                            self.mac_address.parent = self
                            self._children_name_map["mac_address"] = "mac-address"
                            self._segment_path = lambda: "member"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member, ['interface_name', 'port_priority', 'port_number', 'underlying_link_id', 'link_order_number', 'iccp_node', 'bandwidth', 'lacp_enabled', 'member_type', 'member_name'], name, value)


                        class Counters(Entity):
                            """
                            Counters data about member link
                            
                            .. attribute:: lacpd_us_received
                            
                            	LACPDUs received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lacpd_us_transmitted
                            
                            	LACPDUs transmitted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: marker_packets_received
                            
                            	Marker packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: marker_responses_transmitted
                            
                            	Marker response packets transmitted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: illegal_packets_received
                            
                            	Illegal and unknown packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excess_lacpd_us_received
                            
                            	LACPDUs received that exceed the rate limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excess_marker_packets_received
                            
                            	Marker packets received that exceed the rate limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: defaulted
                            
                            	State flag set to Defaulted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: expired
                            
                            	State flag set to Expired
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: last_cleared_sec
                            
                            	Last time counters cleared (s) (deprecated)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: last_cleared_nsec
                            
                            	Last time counters cleared (nsec) (deprecated)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters, self).__init__()

                                self.yang_name = "counters"
                                self.yang_parent_name = "member"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lacpd_us_received', (YLeaf(YType.uint32, 'lacpd-us-received'), ['int'])),
                                    ('lacpd_us_transmitted', (YLeaf(YType.uint32, 'lacpd-us-transmitted'), ['int'])),
                                    ('marker_packets_received', (YLeaf(YType.uint32, 'marker-packets-received'), ['int'])),
                                    ('marker_responses_transmitted', (YLeaf(YType.uint32, 'marker-responses-transmitted'), ['int'])),
                                    ('illegal_packets_received', (YLeaf(YType.uint32, 'illegal-packets-received'), ['int'])),
                                    ('excess_lacpd_us_received', (YLeaf(YType.uint32, 'excess-lacpd-us-received'), ['int'])),
                                    ('excess_marker_packets_received', (YLeaf(YType.uint32, 'excess-marker-packets-received'), ['int'])),
                                    ('defaulted', (YLeaf(YType.uint32, 'defaulted'), ['int'])),
                                    ('expired', (YLeaf(YType.uint32, 'expired'), ['int'])),
                                    ('last_cleared_sec', (YLeaf(YType.uint32, 'last-cleared-sec'), ['int'])),
                                    ('last_cleared_nsec', (YLeaf(YType.uint32, 'last-cleared-nsec'), ['int'])),
                                ])
                                self.lacpd_us_received = None
                                self.lacpd_us_transmitted = None
                                self.marker_packets_received = None
                                self.marker_responses_transmitted = None
                                self.illegal_packets_received = None
                                self.excess_lacpd_us_received = None
                                self.excess_marker_packets_received = None
                                self.defaulted = None
                                self.expired = None
                                self.last_cleared_sec = None
                                self.last_cleared_nsec = None
                                self._segment_path = lambda: "counters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.Counters, ['lacpd_us_received', 'lacpd_us_transmitted', 'marker_packets_received', 'marker_responses_transmitted', 'illegal_packets_received', 'excess_lacpd_us_received', 'excess_marker_packets_received', 'defaulted', 'expired', 'last_cleared_sec', 'last_cleared_nsec'], name, value)


                        class LinkData(Entity):
                            """
                            Lacp data about member link
                            
                            .. attribute:: interface_handle
                            
                            	Member's interface handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: actor_system_priority
                            
                            	System priority of actor system
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: actor_system_mac_address
                            
                            	MAC Address of the actor system
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: actor_operational_key
                            
                            	Operational key for this port
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_system_priority
                            
                            	System priority of partner system
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_system_mac_address
                            
                            	MAC Address used to identify the partner system
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: partner_operational_key
                            
                            	Operational key for partner port
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: selected_aggregator_id
                            
                            	MIB ifindex of selected bundle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: attached_aggregator_id
                            
                            	MIB ifindex of attached bundle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: actor_port_id
                            
                            	Port number of this port
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: actor_port_priority
                            
                            	Priority of this port
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_port_id
                            
                            	Port number of the partner's port
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_port_priority
                            
                            	Priority of the partner's port
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: actor_port_state
                            
                            	LACP state of this port
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: partner_port_state
                            
                            	LACP state of the partner's port
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData, self).__init__()

                                self.yang_name = "link-data"
                                self.yang_parent_name = "member"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                    ('actor_system_priority', (YLeaf(YType.uint16, 'actor-system-priority'), ['int'])),
                                    ('actor_system_mac_address', (YLeaf(YType.str, 'actor-system-mac-address'), ['str'])),
                                    ('actor_operational_key', (YLeaf(YType.uint16, 'actor-operational-key'), ['int'])),
                                    ('partner_system_priority', (YLeaf(YType.uint16, 'partner-system-priority'), ['int'])),
                                    ('partner_system_mac_address', (YLeaf(YType.str, 'partner-system-mac-address'), ['str'])),
                                    ('partner_operational_key', (YLeaf(YType.uint16, 'partner-operational-key'), ['int'])),
                                    ('selected_aggregator_id', (YLeaf(YType.uint32, 'selected-aggregator-id'), ['int'])),
                                    ('attached_aggregator_id', (YLeaf(YType.uint32, 'attached-aggregator-id'), ['int'])),
                                    ('actor_port_id', (YLeaf(YType.uint16, 'actor-port-id'), ['int'])),
                                    ('actor_port_priority', (YLeaf(YType.uint16, 'actor-port-priority'), ['int'])),
                                    ('partner_port_id', (YLeaf(YType.uint16, 'partner-port-id'), ['int'])),
                                    ('partner_port_priority', (YLeaf(YType.uint16, 'partner-port-priority'), ['int'])),
                                    ('actor_port_state', (YLeaf(YType.uint8, 'actor-port-state'), ['int'])),
                                    ('partner_port_state', (YLeaf(YType.uint8, 'partner-port-state'), ['int'])),
                                ])
                                self.interface_handle = None
                                self.actor_system_priority = None
                                self.actor_system_mac_address = None
                                self.actor_operational_key = None
                                self.partner_system_priority = None
                                self.partner_system_mac_address = None
                                self.partner_operational_key = None
                                self.selected_aggregator_id = None
                                self.attached_aggregator_id = None
                                self.actor_port_id = None
                                self.actor_port_priority = None
                                self.partner_port_id = None
                                self.partner_port_priority = None
                                self.actor_port_state = None
                                self.partner_port_state = None
                                self._segment_path = lambda: "link-data"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.LinkData, ['interface_handle', 'actor_system_priority', 'actor_system_mac_address', 'actor_operational_key', 'partner_system_priority', 'partner_system_mac_address', 'partner_operational_key', 'selected_aggregator_id', 'attached_aggregator_id', 'actor_port_id', 'actor_port_priority', 'partner_port_id', 'partner_port_priority', 'actor_port_state', 'partner_port_state'], name, value)


                        class MemberMuxData(Entity):
                            """
                            Mux state machine data
                            
                            .. attribute:: member_mux_state_reason_data
                            
                            	Data regarding the reason for last Mux state change
                            	**type**\:  :py:class:`MemberMuxStateReasonData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData>`
                            
                            .. attribute:: mux_state
                            
                            	Current state of this bundle member
                            	**type**\:  :py:class:`BmMuxstate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmMuxstate>`
                            
                            .. attribute:: error
                            
                            	Internal value indicating if an error occurred trying to put a link into the desired state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: member_mux_state_reason
                            
                            	Reason for last Mux state change
                            	**type**\:  :py:class:`BmMbrStateReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmMbrStateReason>`
                            
                            .. attribute:: member_state
                            
                            	Current internal state of this bundle member
                            	**type**\:  :py:class:`BmdMemberState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmdMemberState>`
                            
                            .. attribute:: mux_state_reason
                            
                            	Reason for last Mux state change (Deprecated)
                            	**type**\:  :py:class:`BmMuxreason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmMuxreason>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData, self).__init__()

                                self.yang_name = "member-mux-data"
                                self.yang_parent_name = "member"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("member-mux-state-reason-data", ("member_mux_state_reason_data", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData))])
                                self._leafs = OrderedDict([
                                    ('mux_state', (YLeaf(YType.enumeration, 'mux-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmMuxstate', '')])),
                                    ('error', (YLeaf(YType.uint32, 'error'), ['int'])),
                                    ('member_mux_state_reason', (YLeaf(YType.enumeration, 'member-mux-state-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmMbrStateReason', '')])),
                                    ('member_state', (YLeaf(YType.enumeration, 'member-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmdMemberState', '')])),
                                    ('mux_state_reason', (YLeaf(YType.enumeration, 'mux-state-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmMuxreason', '')])),
                                ])
                                self.mux_state = None
                                self.error = None
                                self.member_mux_state_reason = None
                                self.member_state = None
                                self.mux_state_reason = None

                                self.member_mux_state_reason_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData()
                                self.member_mux_state_reason_data.parent = self
                                self._children_name_map["member_mux_state_reason_data"] = "member-mux-state-reason-data"
                                self._segment_path = lambda: "member-mux-data"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData, ['mux_state', 'error', 'member_mux_state_reason', 'member_state', 'mux_state_reason'], name, value)


                            class MemberMuxStateReasonData(Entity):
                                """
                                Data regarding the reason for last Mux state
                                change
                                
                                .. attribute:: reason_type
                                
                                	The item the reason applies to
                                	**type**\:  :py:class:`BmStateReasonTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmStateReasonTarget>`
                                
                                .. attribute:: severity
                                
                                	The severity of the reason
                                	**type**\:  :py:class:`BmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.BmSeverity>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData, self).__init__()

                                    self.yang_name = "member-mux-state-reason-data"
                                    self.yang_parent_name = "member-mux-data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('reason_type', (YLeaf(YType.enumeration, 'reason-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmStateReasonTarget', '')])),
                                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'BmSeverity', '')])),
                                    ])
                                    self.reason_type = None
                                    self.severity = None
                                    self._segment_path = lambda: "member-mux-state-reason-data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData, ['reason_type', 'severity'], name, value)


                        class MacAddress(Entity):
                            """
                            MAC address of this member (deprecated)
                            
                            .. attribute:: address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress, self).__init__()

                                self.yang_name = "mac-address"
                                self.yang_parent_name = "member"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ])
                                self.address = None
                                self._segment_path = lambda: "mac-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress, ['address'], name, value)


                class SerialInformation(Entity):
                    """
                    Serial interface information
                    
                    .. attribute:: timeslots
                    
                    	Timeslots separated by \: or \- from 1 to 31. \: indicates individual timeslot and \- represents a range. E.g. 1\-3\:5 represents timeslots 1, 2, 3, and 5
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation, self).__init__()

                        self.yang_name = "serial-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('timeslots', (YLeaf(YType.str, 'timeslots'), ['str'])),
                        ])
                        self.timeslots = None
                        self._segment_path = lambda: "serial-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation, ['timeslots'], name, value)


                class SonetPosInformation(Entity):
                    """
                    SONET POS interface information
                    
                    .. attribute:: aps_state
                    
                    	APS state
                    	**type**\:  :py:class:`SonetApsEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.SonetApsEt>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation, self).__init__()

                        self.yang_name = "sonet-pos-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aps_state', (YLeaf(YType.enumeration, 'aps-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'SonetApsEt', '')])),
                        ])
                        self.aps_state = None
                        self._segment_path = lambda: "sonet-pos-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation, ['aps_state'], name, value)


                class TunnelGreInformation(Entity):
                    """
                    Tunnel GRE interface information
                    
                    .. attribute:: source_ip_address
                    
                    	Tunnel source IP address
                    	**type**\:  :py:class:`SourceIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress>`
                    
                    .. attribute:: destination_ip_address
                    
                    	Tunnel destination IP address
                    	**type**\:  :py:class:`DestinationIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress>`
                    
                    .. attribute:: source_name
                    
                    	Tunnel source name
                    	**type**\: str
                    
                    .. attribute:: destination_ip_address_length
                    
                    	Tunnel destination IP address length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tunnel_tos
                    
                    	GRE tunnel TOS
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tunnel_ttl
                    
                    	GRE tunnel TTL
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: key
                    
                    	Key value for GRE Packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive period in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**units**\: second
                    
                    .. attribute:: keepalive_maximum_retry
                    
                    	Keepalive retry
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tunnel_mode
                    
                    	Tunnel GRE Mode
                    	**type**\:  :py:class:`TunnelGreMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelGreMode>`
                    
                    .. attribute:: tunnel_mode_direction
                    
                    	Tunnel Mode Direction
                    	**type**\:  :py:class:`TunlIpModeDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunlIpModeDir>`
                    
                    .. attribute:: keepalive_state
                    
                    	Keepalive State
                    	**type**\:  :py:class:`TunnelKaDfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKaDfState>`
                    
                    .. attribute:: df_bit_state
                    
                    	DF Bit State
                    	**type**\:  :py:class:`TunnelKaDfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKaDfState>`
                    
                    .. attribute:: key_bit_state
                    
                    	Key Config State
                    	**type**\:  :py:class:`TunnelKeyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKeyState>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation, self).__init__()

                        self.yang_name = "tunnel-gre-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source-ip-address", ("source_ip_address", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress)), ("destination-ip-address", ("destination_ip_address", Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress))])
                        self._leafs = OrderedDict([
                            ('source_name', (YLeaf(YType.str, 'source-name'), ['str'])),
                            ('destination_ip_address_length', (YLeaf(YType.uint8, 'destination-ip-address-length'), ['int'])),
                            ('tunnel_tos', (YLeaf(YType.uint32, 'tunnel-tos'), ['int'])),
                            ('tunnel_ttl', (YLeaf(YType.uint32, 'tunnel-ttl'), ['int'])),
                            ('key', (YLeaf(YType.uint32, 'key'), ['int'])),
                            ('keepalive_period', (YLeaf(YType.uint16, 'keepalive-period'), ['int'])),
                            ('keepalive_maximum_retry', (YLeaf(YType.uint8, 'keepalive-maximum-retry'), ['int'])),
                            ('tunnel_mode', (YLeaf(YType.enumeration, 'tunnel-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunnelGreMode', '')])),
                            ('tunnel_mode_direction', (YLeaf(YType.enumeration, 'tunnel-mode-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunlIpModeDir', '')])),
                            ('keepalive_state', (YLeaf(YType.enumeration, 'keepalive-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunnelKaDfState', '')])),
                            ('df_bit_state', (YLeaf(YType.enumeration, 'df-bit-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunnelKaDfState', '')])),
                            ('key_bit_state', (YLeaf(YType.enumeration, 'key-bit-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunnelKeyState', '')])),
                        ])
                        self.source_name = None
                        self.destination_ip_address_length = None
                        self.tunnel_tos = None
                        self.tunnel_ttl = None
                        self.key = None
                        self.keepalive_period = None
                        self.keepalive_maximum_retry = None
                        self.tunnel_mode = None
                        self.tunnel_mode_direction = None
                        self.keepalive_state = None
                        self.df_bit_state = None
                        self.key_bit_state = None

                        self.source_ip_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress()
                        self.source_ip_address.parent = self
                        self._children_name_map["source_ip_address"] = "source-ip-address"

                        self.destination_ip_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress()
                        self.destination_ip_address.parent = self
                        self._children_name_map["destination_ip_address"] = "destination-ip-address"
                        self._segment_path = lambda: "tunnel-gre-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation, ['source_name', 'destination_ip_address_length', 'tunnel_tos', 'tunnel_ttl', 'key', 'keepalive_period', 'keepalive_maximum_retry', 'tunnel_mode', 'tunnel_mode_direction', 'keepalive_state', 'df_bit_state', 'key_bit_state'], name, value)


                    class SourceIpAddress(Entity):
                        """
                        Tunnel source IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:  :py:class:`TunlPfiAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunlPfiAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress, self).__init__()

                            self.yang_name = "source-ip-address"
                            self.yang_parent_name = "tunnel-gre-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunlPfiAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.afi = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "source-ip-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress, ['afi', 'ipv4', 'ipv6'], name, value)


                    class DestinationIpAddress(Entity):
                        """
                        Tunnel destination IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:  :py:class:`TunlPfiAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.TunlPfiAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress, self).__init__()

                            self.yang_name = "destination-ip-address"
                            self.yang_parent_name = "tunnel-gre-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'TunlPfiAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.afi = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "destination-ip-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress, ['afi', 'ipv4', 'ipv6'], name, value)


                class PseudowireHeadEndInformation(Entity):
                    """
                    PseudowireHeadEnd interface information
                    
                    .. attribute:: interface_list_name
                    
                    	Interface list Name
                    	**type**\: str
                    
                    .. attribute:: l2_overhead
                    
                    	L2 Overhead
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_label
                    
                    	Internal Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation, self).__init__()

                        self.yang_name = "pseudowire-head-end-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_list_name', (YLeaf(YType.str, 'interface-list-name'), ['str'])),
                            ('l2_overhead', (YLeaf(YType.uint32, 'l2-overhead'), ['int'])),
                            ('internal_label', (YLeaf(YType.uint32, 'internal-label'), ['int'])),
                        ])
                        self.interface_list_name = None
                        self.l2_overhead = None
                        self.internal_label = None
                        self._segment_path = lambda: "pseudowire-head-end-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation, ['interface_list_name', 'l2_overhead', 'internal_label'], name, value)


                class CemInformation(Entity):
                    """
                    Cem interface information
                    
                    .. attribute:: timeslots
                    
                    	Timeslots separated by \: or \- from 1 to 32. \: indicates individual timeslot and \- represents a range. E.g. 1\-3\:5 represents timeslots 1, 2, 3, and 5
                    	**type**\: str
                    
                    .. attribute:: payload
                    
                    	Payload size in bytes configured on CEM interface
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: dejitter_buffer
                    
                    	Dejitter buffer length configuredin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**units**\: millisecond
                    
                    .. attribute:: framing
                    
                    	 If framing is TRUE then the CEM  interface is structure aware ; otherwise it is structure agnostic
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation, self).__init__()

                        self.yang_name = "cem-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('timeslots', (YLeaf(YType.str, 'timeslots'), ['str'])),
                            ('payload', (YLeaf(YType.uint16, 'payload'), ['int'])),
                            ('dejitter_buffer', (YLeaf(YType.uint16, 'dejitter-buffer'), ['int'])),
                            ('framing', (YLeaf(YType.int32, 'framing'), ['int'])),
                        ])
                        self.timeslots = None
                        self.payload = None
                        self.dejitter_buffer = None
                        self.framing = None
                        self._segment_path = lambda: "cem-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation, ['timeslots', 'payload', 'dejitter_buffer', 'framing'], name, value)


                class GccInformation(Entity):
                    """
                    GCC interface information
                    
                    .. attribute:: derived_mode
                    
                    	Derived State
                    	**type**\:  :py:class:`GccDerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.GccDerState>`
                    
                    .. attribute:: sec_state
                    
                    	Sec State 
                    	**type**\:  :py:class:`GccSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.GccSecState>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation, self).__init__()

                        self.yang_name = "gcc-information"
                        self.yang_parent_name = "interface-type-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('derived_mode', (YLeaf(YType.enumeration, 'derived-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'GccDerState', '')])),
                            ('sec_state', (YLeaf(YType.enumeration, 'sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'GccSecState', '')])),
                        ])
                        self.derived_mode = None
                        self.sec_state = None
                        self._segment_path = lambda: "gcc-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation, ['derived_mode', 'sec_state'], name, value)


            class DataRates(Entity):
                """
                Packet and byte rates
                
                .. attribute:: input_data_rate
                
                	Input data rate in 1000's of bps
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: input_packet_rate
                
                	Input packets per second
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: output_data_rate
                
                	Output data rate in 1000's of bps
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: output_packet_rate
                
                	Output packets per second
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: peak_input_data_rate
                
                	Peak input data rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_packet_rate
                
                	Peak input packet rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_data_rate
                
                	Peak output data rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_packet_rate
                
                	Peak output packet rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bandwidth
                
                	Bandwidth (in kbps)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: kbit/s
                
                .. attribute:: load_interval
                
                	Number of 30\-sec intervals less one
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_load
                
                	Output load as fraction of 255
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: input_load
                
                	Input load as fraction of 255
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: reliability
                
                	Reliability coefficient
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.DataRates, self).__init__()

                    self.yang_name = "data-rates"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                        ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                        ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                        ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                        ('peak_input_data_rate', (YLeaf(YType.uint64, 'peak-input-data-rate'), ['int'])),
                        ('peak_input_packet_rate', (YLeaf(YType.uint64, 'peak-input-packet-rate'), ['int'])),
                        ('peak_output_data_rate', (YLeaf(YType.uint64, 'peak-output-data-rate'), ['int'])),
                        ('peak_output_packet_rate', (YLeaf(YType.uint64, 'peak-output-packet-rate'), ['int'])),
                        ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                        ('load_interval', (YLeaf(YType.uint32, 'load-interval'), ['int'])),
                        ('output_load', (YLeaf(YType.uint8, 'output-load'), ['int'])),
                        ('input_load', (YLeaf(YType.uint8, 'input-load'), ['int'])),
                        ('reliability', (YLeaf(YType.uint8, 'reliability'), ['int'])),
                    ])
                    self.input_data_rate = None
                    self.input_packet_rate = None
                    self.output_data_rate = None
                    self.output_packet_rate = None
                    self.peak_input_data_rate = None
                    self.peak_input_packet_rate = None
                    self.peak_output_data_rate = None
                    self.peak_output_packet_rate = None
                    self.bandwidth = None
                    self.load_interval = None
                    self.output_load = None
                    self.input_load = None
                    self.reliability = None
                    self._segment_path = lambda: "data-rates"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.DataRates, ['input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'bandwidth', 'load_interval', 'output_load', 'input_load', 'reliability'], name, value)


            class InterfaceStatistics(Entity):
                """
                Packet, byte and error counters
                
                .. attribute:: full_interface_stats
                
                	Packet, byte and all error counters
                	**type**\:  :py:class:`FullInterfaceStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats>`
                
                .. attribute:: basic_interface_stats
                
                	Packet, byte and selected error counters
                	**type**\:  :py:class:`BasicInterfaceStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats>`
                
                .. attribute:: stats_type
                
                	StatsType
                	**type**\:  :py:class:`ImCmdStatsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdStatsEnum>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.InterfaceStatistics, self).__init__()

                    self.yang_name = "interface-statistics"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("full-interface-stats", ("full_interface_stats", Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats)), ("basic-interface-stats", ("basic_interface_stats", Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats))])
                    self._leafs = OrderedDict([
                        ('stats_type', (YLeaf(YType.enumeration, 'stats-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImCmdStatsEnum', '')])),
                    ])
                    self.stats_type = None

                    self.full_interface_stats = Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats()
                    self.full_interface_stats.parent = self
                    self._children_name_map["full_interface_stats"] = "full-interface-stats"

                    self.basic_interface_stats = Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats()
                    self.basic_interface_stats.parent = self
                    self._children_name_map["basic_interface_stats"] = "basic-interface-stats"
                    self._segment_path = lambda: "interface-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceStatistics, ['stats_type'], name, value)


                class FullInterfaceStats(Entity):
                    """
                    Packet, byte and all error counters
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats, self).__init__()

                        self.yang_name = "full-interface-stats"
                        self.yang_parent_name = "interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "full-interface-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


                class BasicInterfaceStats(Entity):
                    """
                    Packet, byte and selected error counters
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats, self).__init__()

                        self.yang_name = "basic-interface-stats"
                        self.yang_parent_name = "interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.input_errors = None
                        self.unknown_protocol_packets_received = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.output_errors = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "basic-interface-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'input_drops', 'input_queue_drops', 'input_errors', 'unknown_protocol_packets_received', 'output_drops', 'output_queue_drops', 'output_errors', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


            class L2InterfaceStatistics(Entity):
                """
                L2 Protocol Statistics
                
                .. attribute:: stats_id
                
                	Identifier
                	**type**\:  :py:class:`StatsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId>`
                
                .. attribute:: stats_type
                
                	Stats type value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: contents
                
                	Bag contents
                	**type**\:  :py:class:`StatsTypeContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsTypeContents>`
                
                .. attribute:: block_array
                
                	Block Array
                	**type**\: list of  		 :py:class:`BlockArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray>`
                
                .. attribute:: element_array
                
                	Element Array
                	**type**\: list of  		 :py:class:`ElementArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics, self).__init__()

                    self.yang_name = "l2-interface-statistics"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stats-id", ("stats_id", Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId)), ("block-array", ("block_array", Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray)), ("element-array", ("element_array", Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray))])
                    self._leafs = OrderedDict([
                        ('stats_type', (YLeaf(YType.uint32, 'stats-type'), ['int'])),
                        ('contents', (YLeaf(YType.enumeration, 'contents'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'StatsTypeContents', '')])),
                    ])
                    self.stats_type = None
                    self.contents = None

                    self.stats_id = Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId()
                    self.stats_id.parent = self
                    self._children_name_map["stats_id"] = "stats-id"

                    self.block_array = YList(self)
                    self.element_array = YList(self)
                    self._segment_path = lambda: "l2-interface-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics, ['stats_type', 'contents'], name, value)


                class StatsId(Entity):
                    """
                    Identifier
                    
                    .. attribute:: id_type
                    
                    	id type
                    	**type**\:  :py:class:`StatsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsId>`
                    
                    .. attribute:: unused
                    
                    	Unused
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_handle
                    
                    	Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: node_id
                    
                    	Node ID
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: feature_id
                    
                    	Feature ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: id
                    
                    	ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId, self).__init__()

                        self.yang_name = "stats-id"
                        self.yang_parent_name = "l2-interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id_type', (YLeaf(YType.enumeration, 'id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'StatsId', '')])),
                            ('unused', (YLeaf(YType.uint32, 'unused'), ['int'])),
                            ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                            ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                            ('feature_id', (YLeaf(YType.uint32, 'feature-id'), ['int'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                        ])
                        self.id_type = None
                        self.unused = None
                        self.interface_handle = None
                        self.node_id = None
                        self.feature_id = None
                        self.id = None
                        self._segment_path = lambda: "stats-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId, ['id_type', 'unused', 'interface_handle', 'node_id', 'feature_id', 'id'], name, value)


                class BlockArray(Entity):
                    """
                    Block Array
                    
                    .. attribute:: type
                    
                    	type
                    	**type**\:  :py:class:`StatsCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsCounter>`
                    
                    .. attribute:: count
                    
                    	count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray, self).__init__()

                        self.yang_name = "block-array"
                        self.yang_parent_name = "l2-interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'StatsCounter', '')])),
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('data', (YLeaf(YType.str, 'data'), ['str'])),
                        ])
                        self.type = None
                        self.count = None
                        self.data = None
                        self._segment_path = lambda: "block-array"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray, ['type', 'count', 'data'], name, value)


                class ElementArray(Entity):
                    """
                    Element Array
                    
                    .. attribute:: key
                    
                    	key
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: block_array
                    
                    	block array
                    	**type**\: list of  		 :py:class:`BlockArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray, self).__init__()

                        self.yang_name = "element-array"
                        self.yang_parent_name = "l2-interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("block-array", ("block_array", Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray))])
                        self._leafs = OrderedDict([
                            ('key', (YLeaf(YType.str, 'key'), ['str'])),
                        ])
                        self.key = None

                        self.block_array = YList(self)
                        self._segment_path = lambda: "element-array"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray, ['key'], name, value)


                    class BlockArray(Entity):
                        """
                        block array
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\:  :py:class:`StatsCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.StatsCounter>`
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: data
                        
                        	data
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray, self).__init__()

                            self.yang_name = "block-array"
                            self.yang_parent_name = "element-array"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'StatsCounter', '')])),
                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.type = None
                            self.count = None
                            self.data = None
                            self._segment_path = lambda: "block-array"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray, ['type', 'count', 'data'], name, value)


    class NodeTypeSets(Entity):
        """
        Node and/or interface type specific view of
        interface summary data
        
        .. attribute:: node_type_set
        
        	Summary data for all interfaces on a particular node
        	**type**\: list of  		 :py:class:`NodeTypeSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Interfaces.NodeTypeSets, self).__init__()

            self.yang_name = "node-type-sets"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node-type-set", ("node_type_set", Interfaces.NodeTypeSets.NodeTypeSet))])
            self._leafs = OrderedDict()

            self.node_type_set = YList(self)
            self._segment_path = lambda: "node-type-sets"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.NodeTypeSets, [], name, value)


        class NodeTypeSet(Entity):
            """
            Summary data for all interfaces on a particular
            node
            
            .. attribute:: node_name
            
            	The location to filter on
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: type_set_name
            
            	The interface type to filter on
            	**type**\:  :py:class:`InterfaceTypeSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.InterfaceTypeSet>`
            
            .. attribute:: interface_summary
            
            	Interface summary information
            	**type**\:  :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.NodeTypeSets.NodeTypeSet, self).__init__()

                self.yang_name = "node-type-set"
                self.yang_parent_name = "node-type-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-summary", ("interface_summary", Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('type_set_name', (YLeaf(YType.enumeration, 'type-set-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'InterfaceTypeSet', '')])),
                ])
                self.node_name = None
                self.type_set_name = None

                self.interface_summary = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary()
                self.interface_summary.parent = self
                self._children_name_map["interface_summary"] = "interface-summary"
                self._segment_path = lambda: "node-type-set"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/node-type-sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.NodeTypeSets.NodeTypeSet, ['node_name', 'type_set_name'], name, value)


            class InterfaceSummary(Entity):
                """
                Interface summary information
                
                .. attribute:: interface_counts
                
                	Counts for all interfaces
                	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts>`
                
                .. attribute:: interface_type
                
                	List of per interface type summary information
                	**type**\: list of  		 :py:class:`InterfaceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary, self).__init__()

                    self.yang_name = "interface-summary"
                    self.yang_parent_name = "node-type-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-counts", ("interface_counts", Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts)), ("interface-type", ("interface_type", Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType))])
                    self._leafs = OrderedDict()

                    self.interface_counts = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts()
                    self.interface_counts.parent = self
                    self._children_name_map["interface_counts"] = "interface-counts"

                    self.interface_type = YList(self)
                    self._segment_path = lambda: "interface-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/node-type-sets/node-type-set/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary, [], name, value)


                class InterfaceCounts(Entity):
                    """
                    Counts for all interfaces
                    
                    .. attribute:: interface_count
                    
                    	Number of interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up_interface_count
                    
                    	Number of interfaces in UP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: down_interface_count
                    
                    	Number of interfaces in DOWN state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: admin_down_interface_count
                    
                    	Number of interfaces in an ADMINDOWN state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts, self).__init__()

                        self.yang_name = "interface-counts"
                        self.yang_parent_name = "interface-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                            ('up_interface_count', (YLeaf(YType.uint32, 'up-interface-count'), ['int'])),
                            ('down_interface_count', (YLeaf(YType.uint32, 'down-interface-count'), ['int'])),
                            ('admin_down_interface_count', (YLeaf(YType.uint32, 'admin-down-interface-count'), ['int'])),
                        ])
                        self.interface_count = None
                        self.up_interface_count = None
                        self.down_interface_count = None
                        self.admin_down_interface_count = None
                        self._segment_path = lambda: "interface-counts"
                        self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/node-type-sets/node-type-set/interface-summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts, [u'interface_count', u'up_interface_count', u'down_interface_count', u'admin_down_interface_count'], name, value)


                class InterfaceType(Entity):
                    """
                    List of per interface type summary information
                    
                    .. attribute:: interface_counts
                    
                    	Counts for interfaces of this type
                    	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts>`
                    
                    .. attribute:: interface_type_name
                    
                    	Name of the interface type
                    	**type**\: str
                    
                    .. attribute:: interface_type_description
                    
                    	Description of the interface type
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType, self).__init__()

                        self.yang_name = "interface-type"
                        self.yang_parent_name = "interface-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-counts", ("interface_counts", Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts))])
                        self._leafs = OrderedDict([
                            ('interface_type_name', (YLeaf(YType.str, 'interface-type-name'), ['str'])),
                            ('interface_type_description', (YLeaf(YType.str, 'interface-type-description'), ['str'])),
                        ])
                        self.interface_type_name = None
                        self.interface_type_description = None

                        self.interface_counts = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts()
                        self.interface_counts.parent = self
                        self._children_name_map["interface_counts"] = "interface-counts"
                        self._segment_path = lambda: "interface-type"
                        self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/node-type-sets/node-type-set/interface-summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType, [u'interface_type_name', u'interface_type_description'], name, value)


                    class InterfaceCounts(Entity):
                        """
                        Counts for interfaces of this type
                        
                        .. attribute:: interface_count
                        
                        	Number of interfaces
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: up_interface_count
                        
                        	Number of interfaces in UP state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: down_interface_count
                        
                        	Number of interfaces in DOWN state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_down_interface_count
                        
                        	Number of interfaces in an ADMINDOWN state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts, self).__init__()

                            self.yang_name = "interface-counts"
                            self.yang_parent_name = "interface-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                                ('up_interface_count', (YLeaf(YType.uint32, 'up-interface-count'), ['int'])),
                                ('down_interface_count', (YLeaf(YType.uint32, 'down-interface-count'), ['int'])),
                                ('admin_down_interface_count', (YLeaf(YType.uint32, 'admin-down-interface-count'), ['int'])),
                            ])
                            self.interface_count = None
                            self.up_interface_count = None
                            self.down_interface_count = None
                            self.admin_down_interface_count = None
                            self._segment_path = lambda: "interface-counts"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/node-type-sets/node-type-set/interface-summary/interface-type/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts, [u'interface_count', u'up_interface_count', u'down_interface_count', u'admin_down_interface_count'], name, value)


    class InterfaceBriefs(Entity):
        """
        Brief operational data for interfaces
        
        .. attribute:: interface_brief
        
        	Brief operational attributes for a particular interface
        	**type**\: list of  		 :py:class:`InterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceBriefs.InterfaceBrief>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Interfaces.InterfaceBriefs, self).__init__()

            self.yang_name = "interface-briefs"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-brief", ("interface_brief", Interfaces.InterfaceBriefs.InterfaceBrief))])
            self._leafs = OrderedDict()

            self.interface_brief = YList(self)
            self._segment_path = lambda: "interface-briefs"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.InterfaceBriefs, [], name, value)


        class InterfaceBrief(Entity):
            """
            Brief operational attributes for a particular
            interface
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: interface
            
            	Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: parent_interface
            
            	Parent Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: type
            
            	Interface type
            	**type**\: str
            
            .. attribute:: state
            
            	Operational state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: actual_state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: line_state
            
            	Line protocol state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: actual_line_state
            
            	Line protocol state with no translation of error disable or shutdown
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: encapsulation
            
            	Interface encapsulation
            	**type**\: str
            
            .. attribute:: encapsulation_type_string
            
            	Interface encapsulation description string
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: mtu
            
            	MTU in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: sub_interface_mtu_overhead
            
            	Subif MTU overhead
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2_transport
            
            	L2 transport
            	**type**\: bool
            
            .. attribute:: bandwidth
            
            	Interface bandwidth (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.InterfaceBriefs.InterfaceBrief, self).__init__()

                self.yang_name = "interface-brief"
                self.yang_parent_name = "interface-briefs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('actual_state', (YLeaf(YType.enumeration, 'actual-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('actual_line_state', (YLeaf(YType.enumeration, 'actual-line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('encapsulation', (YLeaf(YType.str, 'encapsulation'), ['str'])),
                    ('encapsulation_type_string', (YLeaf(YType.str, 'encapsulation-type-string'), ['str'])),
                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                    ('sub_interface_mtu_overhead', (YLeaf(YType.uint32, 'sub-interface-mtu-overhead'), ['int'])),
                    ('l2_transport', (YLeaf(YType.boolean, 'l2-transport'), ['bool'])),
                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                ])
                self.interface_name = None
                self.interface = None
                self.parent_interface = None
                self.type = None
                self.state = None
                self.actual_state = None
                self.line_state = None
                self.actual_line_state = None
                self.encapsulation = None
                self.encapsulation_type_string = None
                self.mtu = None
                self.sub_interface_mtu_overhead = None
                self.l2_transport = None
                self.bandwidth = None
                self._segment_path = lambda: "interface-brief" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interface-briefs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.InterfaceBriefs.InterfaceBrief, ['interface_name', u'interface', u'parent_interface', u'type', u'state', u'actual_state', u'line_state', u'actual_line_state', u'encapsulation', u'encapsulation_type_string', u'mtu', u'sub_interface_mtu_overhead', u'l2_transport', u'bandwidth'], name, value)


    class InventorySummary(Entity):
        """
        Inventory summary information
        
        .. attribute:: interface_counts
        
        	Counts for all interfaces
        	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceCounts>`
        
        .. attribute:: interface_type
        
        	List of per interface type summary information
        	**type**\: list of  		 :py:class:`InterfaceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceType>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Interfaces.InventorySummary, self).__init__()

            self.yang_name = "inventory-summary"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-counts", ("interface_counts", Interfaces.InventorySummary.InterfaceCounts)), ("interface-type", ("interface_type", Interfaces.InventorySummary.InterfaceType))])
            self._leafs = OrderedDict()

            self.interface_counts = Interfaces.InventorySummary.InterfaceCounts()
            self.interface_counts.parent = self
            self._children_name_map["interface_counts"] = "interface-counts"

            self.interface_type = YList(self)
            self._segment_path = lambda: "inventory-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.InventorySummary, [], name, value)


        class InterfaceCounts(Entity):
            """
            Counts for all interfaces
            
            .. attribute:: interface_count
            
            	Number of interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_interface_count
            
            	Number of interfaces in UP state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: down_interface_count
            
            	Number of interfaces in DOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: admin_down_interface_count
            
            	Number of interfaces in an ADMINDOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.InventorySummary.InterfaceCounts, self).__init__()

                self.yang_name = "interface-counts"
                self.yang_parent_name = "inventory-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                    ('up_interface_count', (YLeaf(YType.uint32, 'up-interface-count'), ['int'])),
                    ('down_interface_count', (YLeaf(YType.uint32, 'down-interface-count'), ['int'])),
                    ('admin_down_interface_count', (YLeaf(YType.uint32, 'admin-down-interface-count'), ['int'])),
                ])
                self.interface_count = None
                self.up_interface_count = None
                self.down_interface_count = None
                self.admin_down_interface_count = None
                self._segment_path = lambda: "interface-counts"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/inventory-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.InventorySummary.InterfaceCounts, [u'interface_count', u'up_interface_count', u'down_interface_count', u'admin_down_interface_count'], name, value)


        class InterfaceType(Entity):
            """
            List of per interface type summary information
            
            .. attribute:: interface_counts
            
            	Counts for interfaces of this type
            	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceType.InterfaceCounts>`
            
            .. attribute:: interface_type_name
            
            	Name of the interface type
            	**type**\: str
            
            .. attribute:: interface_type_description
            
            	Description of the interface type
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.InventorySummary.InterfaceType, self).__init__()

                self.yang_name = "interface-type"
                self.yang_parent_name = "inventory-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-counts", ("interface_counts", Interfaces.InventorySummary.InterfaceType.InterfaceCounts))])
                self._leafs = OrderedDict([
                    ('interface_type_name', (YLeaf(YType.str, 'interface-type-name'), ['str'])),
                    ('interface_type_description', (YLeaf(YType.str, 'interface-type-description'), ['str'])),
                ])
                self.interface_type_name = None
                self.interface_type_description = None

                self.interface_counts = Interfaces.InventorySummary.InterfaceType.InterfaceCounts()
                self.interface_counts.parent = self
                self._children_name_map["interface_counts"] = "interface-counts"
                self._segment_path = lambda: "interface-type"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/inventory-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.InventorySummary.InterfaceType, [u'interface_type_name', u'interface_type_description'], name, value)


            class InterfaceCounts(Entity):
                """
                Counts for interfaces of this type
                
                .. attribute:: interface_count
                
                	Number of interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_interface_count
                
                	Number of interfaces in UP state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_interface_count
                
                	Number of interfaces in DOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: admin_down_interface_count
                
                	Number of interfaces in an ADMINDOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InventorySummary.InterfaceType.InterfaceCounts, self).__init__()

                    self.yang_name = "interface-counts"
                    self.yang_parent_name = "interface-type"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                        ('up_interface_count', (YLeaf(YType.uint32, 'up-interface-count'), ['int'])),
                        ('down_interface_count', (YLeaf(YType.uint32, 'down-interface-count'), ['int'])),
                        ('admin_down_interface_count', (YLeaf(YType.uint32, 'admin-down-interface-count'), ['int'])),
                    ])
                    self.interface_count = None
                    self.up_interface_count = None
                    self.down_interface_count = None
                    self.admin_down_interface_count = None
                    self._segment_path = lambda: "interface-counts"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/inventory-summary/interface-type/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InventorySummary.InterfaceType.InterfaceCounts, [u'interface_count', u'up_interface_count', u'down_interface_count', u'admin_down_interface_count'], name, value)


    class Interfaces_(Entity):
        """
        Descriptions for interfaces
        
        .. attribute:: interface
        
        	Description for a particular interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.Interfaces_.Interface>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Interfaces.Interfaces_, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Interfaces.Interfaces_.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.Interfaces_, [], name, value)


        class Interface(Entity):
            """
            Description for a particular interface
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: interface
            
            	Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: line_state
            
            	Line protocol state with no translation of error disable or shutdown
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum>`
            
            .. attribute:: description
            
            	Interface description string
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.Interfaces_.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper', 'ImStateEnum', '')])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.interface_name = None
                self.interface = None
                self.state = None
                self.line_state = None
                self.description = None
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interfaces_.Interface, ['interface_name', 'interface', 'state', 'line_state', 'description'], name, value)


    class InterfaceSummary(Entity):
        """
        Interface summary information
        
        .. attribute:: interface_counts
        
        	Counts for all interfaces
        	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceCounts>`
        
        .. attribute:: interface_type
        
        	List of per interface type summary information
        	**type**\: list of  		 :py:class:`InterfaceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceType>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Interfaces.InterfaceSummary, self).__init__()

            self.yang_name = "interface-summary"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-counts", ("interface_counts", Interfaces.InterfaceSummary.InterfaceCounts)), ("interface-type", ("interface_type", Interfaces.InterfaceSummary.InterfaceType))])
            self._leafs = OrderedDict()

            self.interface_counts = Interfaces.InterfaceSummary.InterfaceCounts()
            self.interface_counts.parent = self
            self._children_name_map["interface_counts"] = "interface-counts"

            self.interface_type = YList(self)
            self._segment_path = lambda: "interface-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.InterfaceSummary, [], name, value)


        class InterfaceCounts(Entity):
            """
            Counts for all interfaces
            
            .. attribute:: interface_count
            
            	Number of interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_interface_count
            
            	Number of interfaces in UP state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: down_interface_count
            
            	Number of interfaces in DOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: admin_down_interface_count
            
            	Number of interfaces in an ADMINDOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.InterfaceSummary.InterfaceCounts, self).__init__()

                self.yang_name = "interface-counts"
                self.yang_parent_name = "interface-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                    ('up_interface_count', (YLeaf(YType.uint32, 'up-interface-count'), ['int'])),
                    ('down_interface_count', (YLeaf(YType.uint32, 'down-interface-count'), ['int'])),
                    ('admin_down_interface_count', (YLeaf(YType.uint32, 'admin-down-interface-count'), ['int'])),
                ])
                self.interface_count = None
                self.up_interface_count = None
                self.down_interface_count = None
                self.admin_down_interface_count = None
                self._segment_path = lambda: "interface-counts"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interface-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.InterfaceSummary.InterfaceCounts, [u'interface_count', u'up_interface_count', u'down_interface_count', u'admin_down_interface_count'], name, value)


        class InterfaceType(Entity):
            """
            List of per interface type summary information
            
            .. attribute:: interface_counts
            
            	Counts for interfaces of this type
            	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts>`
            
            .. attribute:: interface_type_name
            
            	Name of the interface type
            	**type**\: str
            
            .. attribute:: interface_type_description
            
            	Description of the interface type
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Interfaces.InterfaceSummary.InterfaceType, self).__init__()

                self.yang_name = "interface-type"
                self.yang_parent_name = "interface-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-counts", ("interface_counts", Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts))])
                self._leafs = OrderedDict([
                    ('interface_type_name', (YLeaf(YType.str, 'interface-type-name'), ['str'])),
                    ('interface_type_description', (YLeaf(YType.str, 'interface-type-description'), ['str'])),
                ])
                self.interface_type_name = None
                self.interface_type_description = None

                self.interface_counts = Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts()
                self.interface_counts.parent = self
                self._children_name_map["interface_counts"] = "interface-counts"
                self._segment_path = lambda: "interface-type"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interface-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.InterfaceSummary.InterfaceType, [u'interface_type_name', u'interface_type_description'], name, value)


            class InterfaceCounts(Entity):
                """
                Counts for interfaces of this type
                
                .. attribute:: interface_count
                
                	Number of interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_interface_count
                
                	Number of interfaces in UP state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_interface_count
                
                	Number of interfaces in DOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: admin_down_interface_count
                
                	Number of interfaces in an ADMINDOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts, self).__init__()

                    self.yang_name = "interface-counts"
                    self.yang_parent_name = "interface-type"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                        ('up_interface_count', (YLeaf(YType.uint32, 'up-interface-count'), ['int'])),
                        ('down_interface_count', (YLeaf(YType.uint32, 'down-interface-count'), ['int'])),
                        ('admin_down_interface_count', (YLeaf(YType.uint32, 'admin-down-interface-count'), ['int'])),
                    ])
                    self.interface_count = None
                    self.up_interface_count = None
                    self.down_interface_count = None
                    self.admin_down_interface_count = None
                    self._segment_path = lambda: "interface-counts"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/interface-summary/interface-type/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts, [u'interface_count', u'up_interface_count', u'down_interface_count', u'admin_down_interface_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Interfaces()
        return self._top_entity

