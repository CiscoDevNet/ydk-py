""" Cisco_IOS_XR_icpe_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package operational data.

This module contains definitions
for the following management objects\:
  nv\-satellite\: Satellite operational information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IcpeGcoOperControlReason(Enum):
    """
    IcpeGcoOperControlReason

    Icpe gco oper control reason

    .. data:: icpe_gco_oper_control_reason_unknown_error = 0

    	Unknown error

    .. data:: icpe_gco_oper_control_reason_wrong_chassis_type = 1

    	Wrong chassis type

    .. data:: icpe_gco_oper_control_reason_wrong_chassis_serial = 2

    	Wrong chassis serial

    .. data:: icpe_gco_oper_control_reason_needs_to_upgrade = 3

    	Needs to upgrade

    .. data:: icpe_gco_oper_control_reason_none = 4

    	None

    """

    icpe_gco_oper_control_reason_unknown_error = Enum.YLeaf(0, "icpe-gco-oper-control-reason-unknown-error")

    icpe_gco_oper_control_reason_wrong_chassis_type = Enum.YLeaf(1, "icpe-gco-oper-control-reason-wrong-chassis-type")

    icpe_gco_oper_control_reason_wrong_chassis_serial = Enum.YLeaf(2, "icpe-gco-oper-control-reason-wrong-chassis-serial")

    icpe_gco_oper_control_reason_needs_to_upgrade = Enum.YLeaf(3, "icpe-gco-oper-control-reason-needs-to-upgrade")

    icpe_gco_oper_control_reason_none = Enum.YLeaf(4, "icpe-gco-oper-control-reason-none")


class IcpeInstallPkgSupp(Enum):
    """
    IcpeInstallPkgSupp

    Icpe install pkg supp

    .. data:: icpe_install_pkg_supp_unknown = 0

    	Unknown

    .. data:: icpe_install_pkg_supp_not_supported = 1

    	Not supported

    .. data:: icpe_install_pkg_supp_supported = 2

    	Supported

    """

    icpe_install_pkg_supp_unknown = Enum.YLeaf(0, "icpe-install-pkg-supp-unknown")

    icpe_install_pkg_supp_not_supported = Enum.YLeaf(1, "icpe-install-pkg-supp-not-supported")

    icpe_install_pkg_supp_supported = Enum.YLeaf(2, "icpe-install-pkg-supp-supported")


class IcpeInstallSatState(Enum):
    """
    IcpeInstallSatState

    Icpe install sat state

    .. data:: icpe_install_sat_state_unknown = 0

    	Unknown

    .. data:: icpe_install_sat_state_not_initiat_ed = 1

    	Not initiated

    .. data:: icpe_install_sat_state_transferring = 2

    	Transferring

    .. data:: icpe_install_sat_state_activating = 3

    	Activating

    .. data:: icpe_install_sat_state_updating = 4

    	Updating

    .. data:: icpe_install_sat_state_deactivating = 5

    	Deactivating

    .. data:: icpe_install_sat_state_removing = 6

    	Removing

    .. data:: icpe_install_sat_state_success = 7

    	Success

    .. data:: icpe_install_sat_state_failure = 8

    	Failure

    .. data:: icpe_install_sat_state_multiple_ops = 9

    	Multiple ops

    .. data:: icpe_install_sat_state_aborted = 10

    	Aborted

    .. data:: icpe_install_sat_state_protocol_version = 11

    	Protocol version

    .. data:: icpe_install_sat_state_pkg_not_present = 12

    	Pkg not present

    .. data:: icpe_install_sat_state_no_image = 13

    	No image

    .. data:: icpe_install_sat_state_no_such_file = 14

    	No such file

    """

    icpe_install_sat_state_unknown = Enum.YLeaf(0, "icpe-install-sat-state-unknown")

    icpe_install_sat_state_not_initiat_ed = Enum.YLeaf(1, "icpe-install-sat-state-not-initiat-ed")

    icpe_install_sat_state_transferring = Enum.YLeaf(2, "icpe-install-sat-state-transferring")

    icpe_install_sat_state_activating = Enum.YLeaf(3, "icpe-install-sat-state-activating")

    icpe_install_sat_state_updating = Enum.YLeaf(4, "icpe-install-sat-state-updating")

    icpe_install_sat_state_deactivating = Enum.YLeaf(5, "icpe-install-sat-state-deactivating")

    icpe_install_sat_state_removing = Enum.YLeaf(6, "icpe-install-sat-state-removing")

    icpe_install_sat_state_success = Enum.YLeaf(7, "icpe-install-sat-state-success")

    icpe_install_sat_state_failure = Enum.YLeaf(8, "icpe-install-sat-state-failure")

    icpe_install_sat_state_multiple_ops = Enum.YLeaf(9, "icpe-install-sat-state-multiple-ops")

    icpe_install_sat_state_aborted = Enum.YLeaf(10, "icpe-install-sat-state-aborted")

    icpe_install_sat_state_protocol_version = Enum.YLeaf(11, "icpe-install-sat-state-protocol-version")

    icpe_install_sat_state_pkg_not_present = Enum.YLeaf(12, "icpe-install-sat-state-pkg-not-present")

    icpe_install_sat_state_no_image = Enum.YLeaf(13, "icpe-install-sat-state-no-image")

    icpe_install_sat_state_no_such_file = Enum.YLeaf(14, "icpe-install-sat-state-no-such-file")


class IcpeOperConflict(Enum):
    """
    IcpeOperConflict

    Icpe oper conflict

    .. data:: icpe_oper_conflict_not_calculated = 0

    	Not calculated

    .. data:: icpe_oper_conflict_no_conflict = 1

    	No conflict

    .. data:: icpe_oper_conflict_satellite_not_configured = 2

    	Satellite not configured

    .. data:: icpe_oper_conflict_satellite_no_type = 3

    	Satellite no type

    .. data:: icpe_oper_conflict_satellite_id_invalid = 4

    	Satellite id invalid

    .. data:: icpe_oper_conflict_satellite_no_ipv4_addr = 5

    	Satellite no ipv4 addr

    .. data:: icpe_oper_conflict_satellite_conflicting_ipv4_addr = 6

    	Satellite conflicting ipv4 addr

    .. data:: icpe_oper_conflict_no_configured_links = 7

    	No configured links

    .. data:: icpe_oper_conflict_no_discovered_links = 8

    	No discovered links

    .. data:: icpe_oper_conflict_invalid_ports = 9

    	Invalid ports

    .. data:: icpe_oper_conflict_ports_overlap = 10

    	Ports overlap

    .. data:: icpe_oper_conflict_waiting_for_ipv4_addr = 11

    	Waiting for ipv4 addr

    .. data:: icpe_oper_conflict_waiting_for_vrf = 12

    	Waiting for VRF

    .. data:: icpe_oper_conflict_different_ipv4_addr = 13

    	Different ipv4 addr

    .. data:: icpe_oper_conflict_different_vrf = 14

    	Different VRF

    .. data:: icpe_oper_conflict_satellite_link_ipv4_overlap = 15

    	Satellite link ipv4 overlap

    .. data:: icpe_oper_conflict_waiting_for_ident = 16

    	Waiting for ident

    .. data:: icpe_oper_conflict_multiple_ids = 17

    	Multiple ids

    .. data:: icpe_oper_conflict_multiple_satellites = 18

    	Multiple satellites

    .. data:: icpe_oper_conflict_ident_rejected = 19

    	Ident rejected

    .. data:: icpe_oper_conflict_interface_down = 20

    	Interface down

    .. data:: icpe_oper_conflict_auto_ip_unavailable = 21

    	Auto IP unavailable

    .. data:: icpe_oper_conflict_satellite_auto_ip_link_manual_ip = 22

    	Satellite auto IP link manual IP

    .. data:: icpe_oper_conflict_link_auto_ip_satellite_manual_ip = 23

    	Link auto IP satellite manual IP

    .. data:: icpe_oper_conflict_serial_num_mismatch = 24

    	Serial num mismatch

    .. data:: icpe_oper_conflict_satellite_not_identified = 25

    	Satellite not identified

    .. data:: icpe_oper_conflict_satellite_unsupported_type = 26

    	Satellite unsupported type

    .. data:: icpe_oper_conflict_satellite_partition_unsupported = 27

    	Satellite partition unsupported

    .. data:: icpe_oper_conflict_satellite_no_serial_number = 28

    	Satellite no serial number

    .. data:: icpe_oper_conflict_satellite_conflicting_serial_number = 29

    	Satellite conflicting serial number

    .. data:: icpe_oper_conflict_satellite_link_waiting_for_arp = 30

    	Satellite link waiting for arp

    .. data:: icpe_oper_conflict_host_pe_isolated_split_brain = 31

    	Host PE isolated split brain

    .. data:: icpe_oper_conflict_fabric_iccp_group_inconsistent = 32

    	Fabric ICCP group inconsistent

    .. data:: icpe_oper_conflict_invalid_iccp_group = 33

    	Invalid ICCP group

    .. data:: icpe_oper_conflict_port_rejected = 34

    	Port rejected

    .. data:: icpe_oper_conflict_satellite_icl_not_supported = 35

    	Satellite ICL not supported

    .. data:: icpe_oper_conflict_multiple_serial_number = 36

    	Multiple serial number

    .. data:: icpe_oper_conflict_multiple_mac_address = 37

    	Multiple MAC address

    """

    icpe_oper_conflict_not_calculated = Enum.YLeaf(0, "icpe-oper-conflict-not-calculated")

    icpe_oper_conflict_no_conflict = Enum.YLeaf(1, "icpe-oper-conflict-no-conflict")

    icpe_oper_conflict_satellite_not_configured = Enum.YLeaf(2, "icpe-oper-conflict-satellite-not-configured")

    icpe_oper_conflict_satellite_no_type = Enum.YLeaf(3, "icpe-oper-conflict-satellite-no-type")

    icpe_oper_conflict_satellite_id_invalid = Enum.YLeaf(4, "icpe-oper-conflict-satellite-id-invalid")

    icpe_oper_conflict_satellite_no_ipv4_addr = Enum.YLeaf(5, "icpe-oper-conflict-satellite-no-ipv4-addr")

    icpe_oper_conflict_satellite_conflicting_ipv4_addr = Enum.YLeaf(6, "icpe-oper-conflict-satellite-conflicting-ipv4-addr")

    icpe_oper_conflict_no_configured_links = Enum.YLeaf(7, "icpe-oper-conflict-no-configured-links")

    icpe_oper_conflict_no_discovered_links = Enum.YLeaf(8, "icpe-oper-conflict-no-discovered-links")

    icpe_oper_conflict_invalid_ports = Enum.YLeaf(9, "icpe-oper-conflict-invalid-ports")

    icpe_oper_conflict_ports_overlap = Enum.YLeaf(10, "icpe-oper-conflict-ports-overlap")

    icpe_oper_conflict_waiting_for_ipv4_addr = Enum.YLeaf(11, "icpe-oper-conflict-waiting-for-ipv4-addr")

    icpe_oper_conflict_waiting_for_vrf = Enum.YLeaf(12, "icpe-oper-conflict-waiting-for-vrf")

    icpe_oper_conflict_different_ipv4_addr = Enum.YLeaf(13, "icpe-oper-conflict-different-ipv4-addr")

    icpe_oper_conflict_different_vrf = Enum.YLeaf(14, "icpe-oper-conflict-different-vrf")

    icpe_oper_conflict_satellite_link_ipv4_overlap = Enum.YLeaf(15, "icpe-oper-conflict-satellite-link-ipv4-overlap")

    icpe_oper_conflict_waiting_for_ident = Enum.YLeaf(16, "icpe-oper-conflict-waiting-for-ident")

    icpe_oper_conflict_multiple_ids = Enum.YLeaf(17, "icpe-oper-conflict-multiple-ids")

    icpe_oper_conflict_multiple_satellites = Enum.YLeaf(18, "icpe-oper-conflict-multiple-satellites")

    icpe_oper_conflict_ident_rejected = Enum.YLeaf(19, "icpe-oper-conflict-ident-rejected")

    icpe_oper_conflict_interface_down = Enum.YLeaf(20, "icpe-oper-conflict-interface-down")

    icpe_oper_conflict_auto_ip_unavailable = Enum.YLeaf(21, "icpe-oper-conflict-auto-ip-unavailable")

    icpe_oper_conflict_satellite_auto_ip_link_manual_ip = Enum.YLeaf(22, "icpe-oper-conflict-satellite-auto-ip-link-manual-ip")

    icpe_oper_conflict_link_auto_ip_satellite_manual_ip = Enum.YLeaf(23, "icpe-oper-conflict-link-auto-ip-satellite-manual-ip")

    icpe_oper_conflict_serial_num_mismatch = Enum.YLeaf(24, "icpe-oper-conflict-serial-num-mismatch")

    icpe_oper_conflict_satellite_not_identified = Enum.YLeaf(25, "icpe-oper-conflict-satellite-not-identified")

    icpe_oper_conflict_satellite_unsupported_type = Enum.YLeaf(26, "icpe-oper-conflict-satellite-unsupported-type")

    icpe_oper_conflict_satellite_partition_unsupported = Enum.YLeaf(27, "icpe-oper-conflict-satellite-partition-unsupported")

    icpe_oper_conflict_satellite_no_serial_number = Enum.YLeaf(28, "icpe-oper-conflict-satellite-no-serial-number")

    icpe_oper_conflict_satellite_conflicting_serial_number = Enum.YLeaf(29, "icpe-oper-conflict-satellite-conflicting-serial-number")

    icpe_oper_conflict_satellite_link_waiting_for_arp = Enum.YLeaf(30, "icpe-oper-conflict-satellite-link-waiting-for-arp")

    icpe_oper_conflict_host_pe_isolated_split_brain = Enum.YLeaf(31, "icpe-oper-conflict-host-pe-isolated-split-brain")

    icpe_oper_conflict_fabric_iccp_group_inconsistent = Enum.YLeaf(32, "icpe-oper-conflict-fabric-iccp-group-inconsistent")

    icpe_oper_conflict_invalid_iccp_group = Enum.YLeaf(33, "icpe-oper-conflict-invalid-iccp-group")

    icpe_oper_conflict_port_rejected = Enum.YLeaf(34, "icpe-oper-conflict-port-rejected")

    icpe_oper_conflict_satellite_icl_not_supported = Enum.YLeaf(35, "icpe-oper-conflict-satellite-icl-not-supported")

    icpe_oper_conflict_multiple_serial_number = Enum.YLeaf(36, "icpe-oper-conflict-multiple-serial-number")

    icpe_oper_conflict_multiple_mac_address = Enum.YLeaf(37, "icpe-oper-conflict-multiple-mac-address")


class IcpeOperDiscdLinkState(Enum):
    """
    IcpeOperDiscdLinkState

    Icpe oper discd link state

    .. data:: icpe_oper_discd_link_state_stopped = 0

    	Stopped

    .. data:: icpe_oper_discd_link_state_probing = 1

    	Probing

    .. data:: icpe_oper_discd_link_state_configuring = 2

    	Configuring

    .. data:: icpe_oper_discd_link_state_ready = 3

    	Ready

    """

    icpe_oper_discd_link_state_stopped = Enum.YLeaf(0, "icpe-oper-discd-link-state-stopped")

    icpe_oper_discd_link_state_probing = Enum.YLeaf(1, "icpe-oper-discd-link-state-probing")

    icpe_oper_discd_link_state_configuring = Enum.YLeaf(2, "icpe-oper-discd-link-state-configuring")

    icpe_oper_discd_link_state_ready = Enum.YLeaf(3, "icpe-oper-discd-link-state-ready")


class IcpeOperFabricPort(Enum):
    """
    IcpeOperFabricPort

    Icpe oper fabric port

    .. data:: icpe_oper_fabric_port_unknown = 0

    	Unknown

    .. data:: icpe_oper_fabric_port_n_v_fabric_gig_e = 1

    	n v fabric- gig e

    .. data:: icpe_oper_fabric_port_n_v_fabric_ten_gig_e = 2

    	n v fabric- ten gig e

    .. data:: icpe_oper_fabric_port_n_v_fabric_hundred_gig_e = 3

    	n v fabric- hundred gig e

    """

    icpe_oper_fabric_port_unknown = Enum.YLeaf(0, "icpe-oper-fabric-port-unknown")

    icpe_oper_fabric_port_n_v_fabric_gig_e = Enum.YLeaf(1, "icpe-oper-fabric-port-n-v-fabric-gig-e")

    icpe_oper_fabric_port_n_v_fabric_ten_gig_e = Enum.YLeaf(2, "icpe-oper-fabric-port-n-v-fabric-ten-gig-e")

    icpe_oper_fabric_port_n_v_fabric_hundred_gig_e = Enum.YLeaf(3, "icpe-oper-fabric-port-n-v-fabric-hundred-gig-e")


class IcpeOperInstallState(Enum):
    """
    IcpeOperInstallState

    Icpe oper install state

    .. data:: icpe_oper_install_state_stable = 0

    	Stable

    .. data:: icpe_oper_install_state_transferring = 1

    	Transferring

    .. data:: icpe_oper_install_state_transferred = 2

    	Transferred

    .. data:: icpe_oper_install_state_installing = 3

    	Installing

    .. data:: icpe_oper_install_state_in_progress = 4

    	In progress

    """

    icpe_oper_install_state_stable = Enum.YLeaf(0, "icpe-oper-install-state-stable")

    icpe_oper_install_state_transferring = Enum.YLeaf(1, "icpe-oper-install-state-transferring")

    icpe_oper_install_state_transferred = Enum.YLeaf(2, "icpe-oper-install-state-transferred")

    icpe_oper_install_state_installing = Enum.YLeaf(3, "icpe-oper-install-state-installing")

    icpe_oper_install_state_in_progress = Enum.YLeaf(4, "icpe-oper-install-state-in-progress")


class IcpeOperMultichassisRedundancy(Enum):
    """
    IcpeOperMultichassisRedundancy

    Icpe oper multichassis redundancy

    .. data:: icpe_oper_multi_chassis_redundancy_not_redundant = 0

    	Not redundant

    .. data:: icpe_oper_multi_chassis_redundancy_active = 1

    	Active

    .. data:: icpe_oper_multi_chassis_redundancy_standby = 2

    	Standby

    """

    icpe_oper_multi_chassis_redundancy_not_redundant = Enum.YLeaf(0, "icpe-oper-multi-chassis-redundancy-not-redundant")

    icpe_oper_multi_chassis_redundancy_active = Enum.YLeaf(1, "icpe-oper-multi-chassis-redundancy-active")

    icpe_oper_multi_chassis_redundancy_standby = Enum.YLeaf(2, "icpe-oper-multi-chassis-redundancy-standby")


class IcpeOperPort(Enum):
    """
    IcpeOperPort

    Icpe oper port

    .. data:: icpe_oper_port_unknown = 0

    	Unknown

    .. data:: icpe_oper_port_gigabit_ethernet = 1

    	Gigabit ethernet

    .. data:: icpe_oper_port_ten_gig_e = 2

    	Ten gig e

    """

    icpe_oper_port_unknown = Enum.YLeaf(0, "icpe-oper-port-unknown")

    icpe_oper_port_gigabit_ethernet = Enum.YLeaf(1, "icpe-oper-port-gigabit-ethernet")

    icpe_oper_port_ten_gig_e = Enum.YLeaf(2, "icpe-oper-port-ten-gig-e")


class IcpeOperSdacpSessState(Enum):
    """
    IcpeOperSdacpSessState

    Icpe oper sdacp sess state

    .. data:: icpe_oper_sdacp_sess_state_not_created = 0

    	Not created

    .. data:: icpe_oper_sdacp_sess_state_created = 1

    	Created

    .. data:: icpe_oper_sdacp_sess_state_authentication_not_ok = 2

    	Authentication not OK

    .. data:: icpe_oper_sdacp_sess_state_authentication_ok = 3

    	Authentication OK

    .. data:: icpe_oper_sdacp_sess_state_version_not_ok = 4

    	Version not OK

    .. data:: icpe_oper_sdacp_sess_state_up = 5

    	Up

    .. data:: icpe_oper_sdacp_sess_state_issu = 6

    	ISSU

    """

    icpe_oper_sdacp_sess_state_not_created = Enum.YLeaf(0, "icpe-oper-sdacp-sess-state-not-created")

    icpe_oper_sdacp_sess_state_created = Enum.YLeaf(1, "icpe-oper-sdacp-sess-state-created")

    icpe_oper_sdacp_sess_state_authentication_not_ok = Enum.YLeaf(2, "icpe-oper-sdacp-sess-state-authentication-not-ok")

    icpe_oper_sdacp_sess_state_authentication_ok = Enum.YLeaf(3, "icpe-oper-sdacp-sess-state-authentication-ok")

    icpe_oper_sdacp_sess_state_version_not_ok = Enum.YLeaf(4, "icpe-oper-sdacp-sess-state-version-not-ok")

    icpe_oper_sdacp_sess_state_up = Enum.YLeaf(5, "icpe-oper-sdacp-sess-state-up")

    icpe_oper_sdacp_sess_state_issu = Enum.YLeaf(6, "icpe-oper-sdacp-sess-state-issu")


class IcpeOperTopoRemoteSource(Enum):
    """
    IcpeOperTopoRemoteSource

    Icpe oper topo remote source

    .. data:: icpe_oper_topo_remote_source_unknown = 0

    	Unknown

    .. data:: icpe_oper_topo_remote_source_remote_icl_id = 1

    	Remote ICL ID

    .. data:: icpe_oper_topo_remote_source_remote_satellite_mac = 2

    	Remote satellite MAC

    .. data:: icpe_oper_topo_remote_source_remote_host_mac = 3

    	Remote host MAC

    .. data:: icpe_oper_topo_remote_source_direct_satellite = 4

    	Direct satellite

    .. data:: icpe_oper_topo_remote_source_direct_host = 5

    	Direct host

    """

    icpe_oper_topo_remote_source_unknown = Enum.YLeaf(0, "icpe-oper-topo-remote-source-unknown")

    icpe_oper_topo_remote_source_remote_icl_id = Enum.YLeaf(1, "icpe-oper-topo-remote-source-remote-icl-id")

    icpe_oper_topo_remote_source_remote_satellite_mac = Enum.YLeaf(2, "icpe-oper-topo-remote-source-remote-satellite-mac")

    icpe_oper_topo_remote_source_remote_host_mac = Enum.YLeaf(3, "icpe-oper-topo-remote-source-remote-host-mac")

    icpe_oper_topo_remote_source_direct_satellite = Enum.YLeaf(4, "icpe-oper-topo-remote-source-direct-satellite")

    icpe_oper_topo_remote_source_direct_host = Enum.YLeaf(5, "icpe-oper-topo-remote-source-direct-host")


class IcpeOperVerCheckState(Enum):
    """
    IcpeOperVerCheckState

    Icpe oper ver check state

    .. data:: icpe_oper_ver_check_state_unknown = 0

    	Unknown

    .. data:: icpe_oper_ver_check_state_not_compatible = 1

    	Not compatible

    .. data:: icpe_oper_ver_check_state_current_version = 2

    	Current version

    .. data:: icpe_oper_ver_check_state_compatible_older = 3

    	Compatible older

    .. data:: icpe_oper_ver_check_state_compatible_newer = 4

    	Compatible newer

    """

    icpe_oper_ver_check_state_unknown = Enum.YLeaf(0, "icpe-oper-ver-check-state-unknown")

    icpe_oper_ver_check_state_not_compatible = Enum.YLeaf(1, "icpe-oper-ver-check-state-not-compatible")

    icpe_oper_ver_check_state_current_version = Enum.YLeaf(2, "icpe-oper-ver-check-state-current-version")

    icpe_oper_ver_check_state_compatible_older = Enum.YLeaf(3, "icpe-oper-ver-check-state-compatible-older")

    icpe_oper_ver_check_state_compatible_newer = Enum.YLeaf(4, "icpe-oper-ver-check-state-compatible-newer")


class IcpeOpmArbitrationFsmState(Enum):
    """
    IcpeOpmArbitrationFsmState

    Icpe opm arbitration fsm state

    .. data:: icpe_opm_arbitration_fsm_state_unarbitrated = 0

    	Unarbitrated

    .. data:: icpe_opm_arbitration_fsm_state_waiting = 1

    	Waiting

    .. data:: icpe_opm_arbitration_fsm_state_arbitrating = 2

    	Arbitrating

    .. data:: icpe_opm_arbitration_fsm_state_arbitrated = 3

    	Arbitrated

    """

    icpe_opm_arbitration_fsm_state_unarbitrated = Enum.YLeaf(0, "icpe-opm-arbitration-fsm-state-unarbitrated")

    icpe_opm_arbitration_fsm_state_waiting = Enum.YLeaf(1, "icpe-opm-arbitration-fsm-state-waiting")

    icpe_opm_arbitration_fsm_state_arbitrating = Enum.YLeaf(2, "icpe-opm-arbitration-fsm-state-arbitrating")

    icpe_opm_arbitration_fsm_state_arbitrated = Enum.YLeaf(3, "icpe-opm-arbitration-fsm-state-arbitrated")


class IcpeOpmAuthFsmState(Enum):
    """
    IcpeOpmAuthFsmState

    Icpe opm auth fsm state

    .. data:: icpe_opm_auth_fsm_state_unauth = 0

    	Unauth

    .. data:: icpe_opm_auth_fsm_state_waiting = 1

    	Waiting

    .. data:: icpe_opm_auth_fsm_state_waiting_for_auth = 2

    	Waiting for auth

    .. data:: icpe_opm_auth_fsm_state_waiting_for_reply = 3

    	Waiting for reply

    .. data:: icpe_opm_auth_fsm_state_authed = 4

    	Authed

    """

    icpe_opm_auth_fsm_state_unauth = Enum.YLeaf(0, "icpe-opm-auth-fsm-state-unauth")

    icpe_opm_auth_fsm_state_waiting = Enum.YLeaf(1, "icpe-opm-auth-fsm-state-waiting")

    icpe_opm_auth_fsm_state_waiting_for_auth = Enum.YLeaf(2, "icpe-opm-auth-fsm-state-waiting-for-auth")

    icpe_opm_auth_fsm_state_waiting_for_reply = Enum.YLeaf(3, "icpe-opm-auth-fsm-state-waiting-for-reply")

    icpe_opm_auth_fsm_state_authed = Enum.YLeaf(4, "icpe-opm-auth-fsm-state-authed")


class IcpeOpmChanFsmState(Enum):
    """
    IcpeOpmChanFsmState

    Icpe opm chan fsm state

    .. data:: icpe_opm_chan_fsm_state_down = 0

    	Down

    .. data:: icpe_opm_chan_fsm_state_closed = 1

    	Closed

    .. data:: icpe_opm_chan_fsm_state_opening = 2

    	Opening

    .. data:: icpe_opm_chan_fsm_state_opened = 3

    	Opened

    .. data:: icpe_opm_chan_fsm_state_open = 4

    	Open

    """

    icpe_opm_chan_fsm_state_down = Enum.YLeaf(0, "icpe-opm-chan-fsm-state-down")

    icpe_opm_chan_fsm_state_closed = Enum.YLeaf(1, "icpe-opm-chan-fsm-state-closed")

    icpe_opm_chan_fsm_state_opening = Enum.YLeaf(2, "icpe-opm-chan-fsm-state-opening")

    icpe_opm_chan_fsm_state_opened = Enum.YLeaf(3, "icpe-opm-chan-fsm-state-opened")

    icpe_opm_chan_fsm_state_open = Enum.YLeaf(4, "icpe-opm-chan-fsm-state-open")


class IcpeOpmController(Enum):
    """
    IcpeOpmController

    Icpe opm controller

    .. data:: icpe_opm_controller_unknown = 0

    	Unknown

    .. data:: icpe_opm_controller_primary = 1

    	Primary

    .. data:: icpe_opm_controller_secondary = 2

    	Secondary

    """

    icpe_opm_controller_unknown = Enum.YLeaf(0, "icpe-opm-controller-unknown")

    icpe_opm_controller_primary = Enum.YLeaf(1, "icpe-opm-controller-primary")

    icpe_opm_controller_secondary = Enum.YLeaf(2, "icpe-opm-controller-secondary")


class IcpeOpmResyncFsmState(Enum):
    """
    IcpeOpmResyncFsmState

    Icpe opm resync fsm state

    .. data:: icpe_opm_resync_fsm_state_not_open = 0

    	Not open

    .. data:: icpe_opm_resync_fsm_state_stable = 1

    	Stable

    .. data:: icpe_opm_resync_fsm_state_in_resync = 2

    	In resync

    .. data:: icpe_opm_resync_fsm_state_queued = 3

    	Queued

    .. data:: icpe_opm_resync_fsm_state_resync_req = 4

    	Resync req

    """

    icpe_opm_resync_fsm_state_not_open = Enum.YLeaf(0, "icpe-opm-resync-fsm-state-not-open")

    icpe_opm_resync_fsm_state_stable = Enum.YLeaf(1, "icpe-opm-resync-fsm-state-stable")

    icpe_opm_resync_fsm_state_in_resync = Enum.YLeaf(2, "icpe-opm-resync-fsm-state-in-resync")

    icpe_opm_resync_fsm_state_queued = Enum.YLeaf(3, "icpe-opm-resync-fsm-state-queued")

    icpe_opm_resync_fsm_state_resync_req = Enum.YLeaf(4, "icpe-opm-resync-fsm-state-resync-req")


class IcpeOpmSessState(Enum):
    """
    IcpeOpmSessState

    Icpe opm sess state

    .. data:: icpe_opm_sess_state_disconnected = 0

    	Disconnected

    .. data:: icpe_opm_sess_state_connecting = 1

    	Connecting

    .. data:: icpe_opm_sess_state_authenticating = 2

    	Authenticating

    .. data:: icpe_opm_sess_state_arbitrating = 3

    	Arbitrating

    .. data:: icpe_opm_sess_state_waiting_for_resyncs = 4

    	Waiting for resyncs

    .. data:: icpe_opm_sess_state_connected = 5

    	Connected

    """

    icpe_opm_sess_state_disconnected = Enum.YLeaf(0, "icpe-opm-sess-state-disconnected")

    icpe_opm_sess_state_connecting = Enum.YLeaf(1, "icpe-opm-sess-state-connecting")

    icpe_opm_sess_state_authenticating = Enum.YLeaf(2, "icpe-opm-sess-state-authenticating")

    icpe_opm_sess_state_arbitrating = Enum.YLeaf(3, "icpe-opm-sess-state-arbitrating")

    icpe_opm_sess_state_waiting_for_resyncs = Enum.YLeaf(4, "icpe-opm-sess-state-waiting-for-resyncs")

    icpe_opm_sess_state_connected = Enum.YLeaf(5, "icpe-opm-sess-state-connected")


class IcpeOpmSyncFsmState(Enum):
    """
    IcpeOpmSyncFsmState

    Icpe opm sync fsm state

    .. data:: icpe_opm_sync_fsm_state_split_brain = 0

    	Split brain

    .. data:: icpe_opm_sync_fsm_state_waiting = 1

    	Waiting

    .. data:: icpe_opm_sync_fsm_state_whole_brain = 2

    	Whole brain

    """

    icpe_opm_sync_fsm_state_split_brain = Enum.YLeaf(0, "icpe-opm-sync-fsm-state-split-brain")

    icpe_opm_sync_fsm_state_waiting = Enum.YLeaf(1, "icpe-opm-sync-fsm-state-waiting")

    icpe_opm_sync_fsm_state_whole_brain = Enum.YLeaf(2, "icpe-opm-sync-fsm-state-whole-brain")


class IcpeOpmTransportState(Enum):
    """
    IcpeOpmTransportState

    Icpe opm transport state

    .. data:: icpe_opm_transport_state_disconnected = 0

    	Disconnected

    .. data:: icpe_opm_transport_state_iccp_unavailable = 1

    	ICCP unavailable

    .. data:: icpe_opm_transport_state_no_member_present = 2

    	No member present

    .. data:: icpe_opm_transport_state_member_down = 3

    	Member down

    .. data:: icpe_opm_transport_state_member_not_reachable = 4

    	Member not reachable

    .. data:: icpe_opm_transport_state_waiting_for_app_connect = 5

    	Waiting for app connect

    .. data:: icpe_opm_transport_state_waiting_for_app_connect_response = 6

    	Waiting for app connect response

    .. data:: icpe_opm_transport_state_connected = 7

    	Connected

    """

    icpe_opm_transport_state_disconnected = Enum.YLeaf(0, "icpe-opm-transport-state-disconnected")

    icpe_opm_transport_state_iccp_unavailable = Enum.YLeaf(1, "icpe-opm-transport-state-iccp-unavailable")

    icpe_opm_transport_state_no_member_present = Enum.YLeaf(2, "icpe-opm-transport-state-no-member-present")

    icpe_opm_transport_state_member_down = Enum.YLeaf(3, "icpe-opm-transport-state-member-down")

    icpe_opm_transport_state_member_not_reachable = Enum.YLeaf(4, "icpe-opm-transport-state-member-not-reachable")

    icpe_opm_transport_state_waiting_for_app_connect = Enum.YLeaf(5, "icpe-opm-transport-state-waiting-for-app-connect")

    icpe_opm_transport_state_waiting_for_app_connect_response = Enum.YLeaf(6, "icpe-opm-transport-state-waiting-for-app-connect-response")

    icpe_opm_transport_state_connected = Enum.YLeaf(7, "icpe-opm-transport-state-connected")


class IcpeOpticalSyncState(Enum):
    """
    IcpeOpticalSyncState

    Icpe optical sync state

    .. data:: icpe_optical_sync_state_unknown = 0

    	Unknown

    .. data:: icpe_optical_sync_state_syncing = 1

    	Syncing

    .. data:: icpe_optical_sync_state_synced = 2

    	Synced

    .. data:: icpe_optical_sync_state_not_connected = 3

    	Not connected

    """

    icpe_optical_sync_state_unknown = Enum.YLeaf(0, "icpe-optical-sync-state-unknown")

    icpe_optical_sync_state_syncing = Enum.YLeaf(1, "icpe-optical-sync-state-syncing")

    icpe_optical_sync_state_synced = Enum.YLeaf(2, "icpe-optical-sync-state-synced")

    icpe_optical_sync_state_not_connected = Enum.YLeaf(3, "icpe-optical-sync-state-not-connected")



class NvSatellite(Entity):
    """
    Satellite operational information
    
    .. attribute:: icpe_dpms
    
    	ICPE DPM operational information table
    	**type**\:   :py:class:`IcpeDpms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms>`
    
    .. attribute:: install
    
    	Satellite Install Information
    	**type**\:   :py:class:`Install <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install>`
    
    .. attribute:: install_op_statuses
    
    	Detailed breakdown of install status table
    	**type**\:   :py:class:`InstallOpStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses>`
    
    .. attribute:: install_progresses
    
    	Current percentage of install table
    	**type**\:   :py:class:`InstallProgresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallProgresses>`
    
    .. attribute:: install_shows
    
    	Detailed breakdown of install status table
    	**type**\:   :py:class:`InstallShows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallShows>`
    
    .. attribute:: install_statuses
    
    	Detailed breakdown of install status table
    	**type**\:   :py:class:`InstallStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallStatuses>`
    
    .. attribute:: reload_op_statuses
    
    	Detailed breakdown of reload status table
    	**type**\:   :py:class:`ReloadOpStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadOpStatuses>`
    
    .. attribute:: reload_statuses
    
    	Detailed breakdown of reload status table
    	**type**\:   :py:class:`ReloadStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses>`
    
    .. attribute:: satellite_priorities
    
    	Satellite priority information table
    	**type**\:   :py:class:`SatellitePriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatellitePriorities>`
    
    .. attribute:: satellite_properties
    
    	ICPE GCO operational information
    	**type**\:   :py:class:`SatelliteProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteProperties>`
    
    .. attribute:: satellite_statuses
    
    	Satellite status information table
    	**type**\:   :py:class:`SatelliteStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses>`
    
    .. attribute:: satellite_topologies
    
    	Satellite Topology Information table
    	**type**\:   :py:class:`SatelliteTopologies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies>`
    
    .. attribute:: satellite_versions
    
    	Satellite remote version information table
    	**type**\:   :py:class:`SatelliteVersions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions>`
    
    .. attribute:: sdacp_controls
    
    	SDAC Protocol Discovery information table
    	**type**\:   :py:class:`SdacpControls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls>`
    
    .. attribute:: sdacp_discovery2s
    
    	ICPE Configured interface state information table
    	**type**\:   :py:class:`SdacpDiscovery2S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S>`
    
    .. attribute:: sdacp_redundancies
    
    	nV Satellite Redundancy Protocol Information table
    	**type**\:   :py:class:`SdacpRedundancies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies>`
    
    

    """

    _prefix = 'icpe-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(NvSatellite, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellite"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-oper"

        self.icpe_dpms = NvSatellite.IcpeDpms()
        self.icpe_dpms.parent = self
        self._children_name_map["icpe_dpms"] = "icpe-dpms"
        self._children_yang_names.add("icpe-dpms")

        self.install = NvSatellite.Install()
        self.install.parent = self
        self._children_name_map["install"] = "install"
        self._children_yang_names.add("install")

        self.install_op_statuses = NvSatellite.InstallOpStatuses()
        self.install_op_statuses.parent = self
        self._children_name_map["install_op_statuses"] = "install-op-statuses"
        self._children_yang_names.add("install-op-statuses")

        self.install_progresses = NvSatellite.InstallProgresses()
        self.install_progresses.parent = self
        self._children_name_map["install_progresses"] = "install-progresses"
        self._children_yang_names.add("install-progresses")

        self.install_shows = NvSatellite.InstallShows()
        self.install_shows.parent = self
        self._children_name_map["install_shows"] = "install-shows"
        self._children_yang_names.add("install-shows")

        self.install_statuses = NvSatellite.InstallStatuses()
        self.install_statuses.parent = self
        self._children_name_map["install_statuses"] = "install-statuses"
        self._children_yang_names.add("install-statuses")

        self.reload_op_statuses = NvSatellite.ReloadOpStatuses()
        self.reload_op_statuses.parent = self
        self._children_name_map["reload_op_statuses"] = "reload-op-statuses"
        self._children_yang_names.add("reload-op-statuses")

        self.reload_statuses = NvSatellite.ReloadStatuses()
        self.reload_statuses.parent = self
        self._children_name_map["reload_statuses"] = "reload-statuses"
        self._children_yang_names.add("reload-statuses")

        self.satellite_priorities = NvSatellite.SatellitePriorities()
        self.satellite_priorities.parent = self
        self._children_name_map["satellite_priorities"] = "satellite-priorities"
        self._children_yang_names.add("satellite-priorities")

        self.satellite_properties = NvSatellite.SatelliteProperties()
        self.satellite_properties.parent = self
        self._children_name_map["satellite_properties"] = "satellite-properties"
        self._children_yang_names.add("satellite-properties")

        self.satellite_statuses = NvSatellite.SatelliteStatuses()
        self.satellite_statuses.parent = self
        self._children_name_map["satellite_statuses"] = "satellite-statuses"
        self._children_yang_names.add("satellite-statuses")

        self.satellite_topologies = NvSatellite.SatelliteTopologies()
        self.satellite_topologies.parent = self
        self._children_name_map["satellite_topologies"] = "satellite-topologies"
        self._children_yang_names.add("satellite-topologies")

        self.satellite_versions = NvSatellite.SatelliteVersions()
        self.satellite_versions.parent = self
        self._children_name_map["satellite_versions"] = "satellite-versions"
        self._children_yang_names.add("satellite-versions")

        self.sdacp_controls = NvSatellite.SdacpControls()
        self.sdacp_controls.parent = self
        self._children_name_map["sdacp_controls"] = "sdacp-controls"
        self._children_yang_names.add("sdacp-controls")

        self.sdacp_discovery2s = NvSatellite.SdacpDiscovery2S()
        self.sdacp_discovery2s.parent = self
        self._children_name_map["sdacp_discovery2s"] = "sdacp-discovery2s"
        self._children_yang_names.add("sdacp-discovery2s")

        self.sdacp_redundancies = NvSatellite.SdacpRedundancies()
        self.sdacp_redundancies.parent = self
        self._children_name_map["sdacp_redundancies"] = "sdacp-redundancies"
        self._children_yang_names.add("sdacp-redundancies")


    class ReloadOpStatuses(Entity):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_op_status
        
        	Detailed breakdown of reload status
        	**type**\: list of    :py:class:`ReloadOpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadOpStatuses.ReloadOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.ReloadOpStatuses, self).__init__()

            self.yang_name = "reload-op-statuses"
            self.yang_parent_name = "nv-satellite"

            self.reload_op_status = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.ReloadOpStatuses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.ReloadOpStatuses, self).__setattr__(name, value)


        class ReloadOpStatus(Entity):
            """
            Detailed breakdown of reload status
            
            .. attribute:: operation_id  <key>
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\:  str
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reload_failed
            
            	Sats reload failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloaded
            
            	Sats reloaded
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloading
            
            	Sats reloading
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.ReloadOpStatuses.ReloadOpStatus, self).__init__()

                self.yang_name = "reload-op-status"
                self.yang_parent_name = "reload-op-statuses"

                self.operation_id = YLeaf(YType.uint32, "operation-id")

                self.operation_id_xr = YLeaf(YType.uint32, "operation-id-xr")

                self.satellite_range = YLeaf(YType.str, "satellite-range")

                self.sats_not_initiated = YLeafList(YType.uint16, "sats-not-initiated")

                self.sats_reload_failed = YLeafList(YType.uint16, "sats-reload-failed")

                self.sats_reloaded = YLeafList(YType.uint16, "sats-reloaded")

                self.sats_reloading = YLeafList(YType.uint16, "sats-reloading")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("operation_id",
                                "operation_id_xr",
                                "satellite_range",
                                "sats_not_initiated",
                                "sats_reload_failed",
                                "sats_reloaded",
                                "sats_reloading") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.ReloadOpStatuses.ReloadOpStatus, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.ReloadOpStatuses.ReloadOpStatus, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_reload_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_reloaded.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_reloading.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.operation_id.is_set or
                    self.operation_id_xr.is_set or
                    self.satellite_range.is_set)

            def has_operation(self):
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_reload_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_reloaded.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_reloading.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.operation_id.yfilter != YFilter.not_set or
                    self.operation_id_xr.yfilter != YFilter.not_set or
                    self.satellite_range.yfilter != YFilter.not_set or
                    self.sats_not_initiated.yfilter != YFilter.not_set or
                    self.sats_reload_failed.yfilter != YFilter.not_set or
                    self.sats_reloaded.yfilter != YFilter.not_set or
                    self.sats_reloading.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "reload-op-status" + "[operation-id='" + self.operation_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/reload-op-statuses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id.get_name_leafdata())
                if (self.operation_id_xr.is_set or self.operation_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id_xr.get_name_leafdata())
                if (self.satellite_range.is_set or self.satellite_range.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range.get_name_leafdata())

                leaf_name_data.extend(self.sats_not_initiated.get_name_leafdata())

                leaf_name_data.extend(self.sats_reload_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_reloaded.get_name_leafdata())

                leaf_name_data.extend(self.sats_reloading.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "operation-id" or name == "operation-id-xr" or name == "satellite-range" or name == "sats-not-initiated" or name == "sats-reload-failed" or name == "sats-reloaded" or name == "sats-reloading"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "operation-id"):
                    self.operation_id = value
                    self.operation_id.value_namespace = name_space
                    self.operation_id.value_namespace_prefix = name_space_prefix
                if(value_path == "operation-id-xr"):
                    self.operation_id_xr = value
                    self.operation_id_xr.value_namespace = name_space
                    self.operation_id_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-range"):
                    self.satellite_range = value
                    self.satellite_range.value_namespace = name_space
                    self.satellite_range.value_namespace_prefix = name_space_prefix
                if(value_path == "sats-not-initiated"):
                    self.sats_not_initiated.append(value)
                if(value_path == "sats-reload-failed"):
                    self.sats_reload_failed.append(value)
                if(value_path == "sats-reloaded"):
                    self.sats_reloaded.append(value)
                if(value_path == "sats-reloading"):
                    self.sats_reloading.append(value)

        def has_data(self):
            for c in self.reload_op_status:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.reload_op_status:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "reload-op-statuses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "reload-op-status"):
                for c in self.reload_op_status:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.ReloadOpStatuses.ReloadOpStatus()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.reload_op_status.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "reload-op-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InstallStatuses(Entity):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_status
        
        	Detailed breakdown of install status
        	**type**\: list of    :py:class:`InstallStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallStatuses.InstallStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallStatuses, self).__init__()

            self.yang_name = "install-statuses"
            self.yang_parent_name = "nv-satellite"

            self.install_status = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.InstallStatuses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.InstallStatuses, self).__setattr__(name, value)


        class InstallStatus(Entity):
            """
            Detailed breakdown of install status
            
            .. attribute:: satellite_range  <key>
            
            	Satellite range
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: operation_id
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range_xr
            
            	Satellite range
            	**type**\:  str
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_aborted
            
            	Sats deactivate aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_failed
            
            	Sats deactivate failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivating
            
            	Sats deactivating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_aborted
            
            	Sats remove aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_failed
            
            	Sats remove failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_removing
            
            	Sats removing
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_aborted
            
            	Sats update aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_failed
            
            	Sats update failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_updating
            
            	Sats updating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallStatuses.InstallStatus, self).__init__()

                self.yang_name = "install-status"
                self.yang_parent_name = "install-statuses"

                self.satellite_range = YLeaf(YType.str, "satellite-range")

                self.operation_id = YLeaf(YType.uint32, "operation-id")

                self.satellite_range_xr = YLeaf(YType.str, "satellite-range-xr")

                self.sats_activate_aborted = YLeafList(YType.uint16, "sats-activate-aborted")

                self.sats_activate_failed = YLeafList(YType.uint16, "sats-activate-failed")

                self.sats_activating = YLeafList(YType.uint16, "sats-activating")

                self.sats_completed = YLeafList(YType.uint16, "sats-completed")

                self.sats_deactivate_aborted = YLeafList(YType.uint16, "sats-deactivate-aborted")

                self.sats_deactivate_failed = YLeafList(YType.uint16, "sats-deactivate-failed")

                self.sats_deactivating = YLeafList(YType.uint16, "sats-deactivating")

                self.sats_no_operation = YLeafList(YType.uint16, "sats-no-operation")

                self.sats_not_initiated = YLeafList(YType.uint16, "sats-not-initiated")

                self.sats_remove_aborted = YLeafList(YType.uint16, "sats-remove-aborted")

                self.sats_remove_failed = YLeafList(YType.uint16, "sats-remove-failed")

                self.sats_removing = YLeafList(YType.uint16, "sats-removing")

                self.sats_transfer_aborted = YLeafList(YType.uint16, "sats-transfer-aborted")

                self.sats_transfer_failed = YLeafList(YType.uint16, "sats-transfer-failed")

                self.sats_transferring = YLeafList(YType.uint16, "sats-transferring")

                self.sats_update_aborted = YLeafList(YType.uint16, "sats-update-aborted")

                self.sats_update_failed = YLeafList(YType.uint16, "sats-update-failed")

                self.sats_updating = YLeafList(YType.uint16, "sats-updating")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("satellite_range",
                                "operation_id",
                                "satellite_range_xr",
                                "sats_activate_aborted",
                                "sats_activate_failed",
                                "sats_activating",
                                "sats_completed",
                                "sats_deactivate_aborted",
                                "sats_deactivate_failed",
                                "sats_deactivating",
                                "sats_no_operation",
                                "sats_not_initiated",
                                "sats_remove_aborted",
                                "sats_remove_failed",
                                "sats_removing",
                                "sats_transfer_aborted",
                                "sats_transfer_failed",
                                "sats_transferring",
                                "sats_update_aborted",
                                "sats_update_failed",
                                "sats_updating") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.InstallStatuses.InstallStatus, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.InstallStatuses.InstallStatus, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.sats_activate_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activate_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_completed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivate_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivate_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_no_operation.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_remove_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_remove_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_removing.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transfer_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transfer_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transferring.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_update_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_update_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_updating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.satellite_range.is_set or
                    self.operation_id.is_set or
                    self.satellite_range_xr.is_set)

            def has_operation(self):
                for leaf in self.sats_activate_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activate_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activating.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_completed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivate_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivate_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivating.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_no_operation.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_remove_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_remove_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_removing.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transfer_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transfer_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transferring.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_update_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_update_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_updating.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.satellite_range.yfilter != YFilter.not_set or
                    self.operation_id.yfilter != YFilter.not_set or
                    self.satellite_range_xr.yfilter != YFilter.not_set or
                    self.sats_activate_aborted.yfilter != YFilter.not_set or
                    self.sats_activate_failed.yfilter != YFilter.not_set or
                    self.sats_activating.yfilter != YFilter.not_set or
                    self.sats_completed.yfilter != YFilter.not_set or
                    self.sats_deactivate_aborted.yfilter != YFilter.not_set or
                    self.sats_deactivate_failed.yfilter != YFilter.not_set or
                    self.sats_deactivating.yfilter != YFilter.not_set or
                    self.sats_no_operation.yfilter != YFilter.not_set or
                    self.sats_not_initiated.yfilter != YFilter.not_set or
                    self.sats_remove_aborted.yfilter != YFilter.not_set or
                    self.sats_remove_failed.yfilter != YFilter.not_set or
                    self.sats_removing.yfilter != YFilter.not_set or
                    self.sats_transfer_aborted.yfilter != YFilter.not_set or
                    self.sats_transfer_failed.yfilter != YFilter.not_set or
                    self.sats_transferring.yfilter != YFilter.not_set or
                    self.sats_update_aborted.yfilter != YFilter.not_set or
                    self.sats_update_failed.yfilter != YFilter.not_set or
                    self.sats_updating.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "install-status" + "[satellite-range='" + self.satellite_range.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-statuses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.satellite_range.is_set or self.satellite_range.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range.get_name_leafdata())
                if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id.get_name_leafdata())
                if (self.satellite_range_xr.is_set or self.satellite_range_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range_xr.get_name_leafdata())

                leaf_name_data.extend(self.sats_activate_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_activate_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_activating.get_name_leafdata())

                leaf_name_data.extend(self.sats_completed.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivate_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivate_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivating.get_name_leafdata())

                leaf_name_data.extend(self.sats_no_operation.get_name_leafdata())

                leaf_name_data.extend(self.sats_not_initiated.get_name_leafdata())

                leaf_name_data.extend(self.sats_remove_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_remove_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_removing.get_name_leafdata())

                leaf_name_data.extend(self.sats_transfer_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_transfer_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_transferring.get_name_leafdata())

                leaf_name_data.extend(self.sats_update_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_update_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_updating.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "satellite-range" or name == "operation-id" or name == "satellite-range-xr" or name == "sats-activate-aborted" or name == "sats-activate-failed" or name == "sats-activating" or name == "sats-completed" or name == "sats-deactivate-aborted" or name == "sats-deactivate-failed" or name == "sats-deactivating" or name == "sats-no-operation" or name == "sats-not-initiated" or name == "sats-remove-aborted" or name == "sats-remove-failed" or name == "sats-removing" or name == "sats-transfer-aborted" or name == "sats-transfer-failed" or name == "sats-transferring" or name == "sats-update-aborted" or name == "sats-update-failed" or name == "sats-updating"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "satellite-range"):
                    self.satellite_range = value
                    self.satellite_range.value_namespace = name_space
                    self.satellite_range.value_namespace_prefix = name_space_prefix
                if(value_path == "operation-id"):
                    self.operation_id = value
                    self.operation_id.value_namespace = name_space
                    self.operation_id.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-range-xr"):
                    self.satellite_range_xr = value
                    self.satellite_range_xr.value_namespace = name_space
                    self.satellite_range_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "sats-activate-aborted"):
                    self.sats_activate_aborted.append(value)
                if(value_path == "sats-activate-failed"):
                    self.sats_activate_failed.append(value)
                if(value_path == "sats-activating"):
                    self.sats_activating.append(value)
                if(value_path == "sats-completed"):
                    self.sats_completed.append(value)
                if(value_path == "sats-deactivate-aborted"):
                    self.sats_deactivate_aborted.append(value)
                if(value_path == "sats-deactivate-failed"):
                    self.sats_deactivate_failed.append(value)
                if(value_path == "sats-deactivating"):
                    self.sats_deactivating.append(value)
                if(value_path == "sats-no-operation"):
                    self.sats_no_operation.append(value)
                if(value_path == "sats-not-initiated"):
                    self.sats_not_initiated.append(value)
                if(value_path == "sats-remove-aborted"):
                    self.sats_remove_aborted.append(value)
                if(value_path == "sats-remove-failed"):
                    self.sats_remove_failed.append(value)
                if(value_path == "sats-removing"):
                    self.sats_removing.append(value)
                if(value_path == "sats-transfer-aborted"):
                    self.sats_transfer_aborted.append(value)
                if(value_path == "sats-transfer-failed"):
                    self.sats_transfer_failed.append(value)
                if(value_path == "sats-transferring"):
                    self.sats_transferring.append(value)
                if(value_path == "sats-update-aborted"):
                    self.sats_update_aborted.append(value)
                if(value_path == "sats-update-failed"):
                    self.sats_update_failed.append(value)
                if(value_path == "sats-updating"):
                    self.sats_updating.append(value)

        def has_data(self):
            for c in self.install_status:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.install_status:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "install-statuses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "install-status"):
                for c in self.install_status:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.InstallStatuses.InstallStatus()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.install_status.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "install-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SdacpRedundancies(Entity):
        """
        nV Satellite Redundancy Protocol Information
        table
        
        .. attribute:: sdacp_redundancy
        
        	nV Satellite Redundancy Protocol Information
        	**type**\: list of    :py:class:`SdacpRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SdacpRedundancies, self).__init__()

            self.yang_name = "sdacp-redundancies"
            self.yang_parent_name = "nv-satellite"

            self.sdacp_redundancy = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SdacpRedundancies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SdacpRedundancies, self).__setattr__(name, value)


        class SdacpRedundancy(Entity):
            """
            nV Satellite Redundancy Protocol Information
            
            .. attribute:: iccp_group  <key>
            
            	ICCP group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: arbitration_state
            
            	Arbitration state
            	**type**\:   :py:class:`IcpeOpmArbitrationFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmArbitrationFsmState>`
            
            .. attribute:: authentication_state
            
            	Authentication state
            	**type**\:   :py:class:`IcpeOpmAuthFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmAuthFsmState>`
            
            .. attribute:: channel
            
            	Channels on this session table
            	**type**\: list of    :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel>`
            
            .. attribute:: iccp_group_xr
            
            	ICCP group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: isolated
            
            	Isolated
            	**type**\:  bool
            
            .. attribute:: primacy
            
            	Primacy
            	**type**\:   :py:class:`IcpeOpmController <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmController>`
            
            .. attribute:: protocol_state
            
            	Protocol state
            	**type**\:   :py:class:`IcpeOpmSessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSessState>`
            
            .. attribute:: protocol_state_timestamp
            
            	Timestamp
            	**type**\:   :py:class:`ProtocolStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp>`
            
            .. attribute:: synchronization_state
            
            	Synchronization state
            	**type**\:   :py:class:`IcpeOpmSyncFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSyncFsmState>`
            
            .. attribute:: system_mac
            
            	System MAC
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: transport_state
            
            	Transport state
            	**type**\:   :py:class:`IcpeOpmTransportState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmTransportState>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SdacpRedundancies.SdacpRedundancy, self).__init__()

                self.yang_name = "sdacp-redundancy"
                self.yang_parent_name = "sdacp-redundancies"

                self.iccp_group = YLeaf(YType.uint32, "iccp-group")

                self.arbitration_state = YLeaf(YType.enumeration, "arbitration-state")

                self.authentication_state = YLeaf(YType.enumeration, "authentication-state")

                self.iccp_group_xr = YLeaf(YType.uint32, "iccp-group-xr")

                self.isolated = YLeaf(YType.boolean, "isolated")

                self.primacy = YLeaf(YType.enumeration, "primacy")

                self.protocol_state = YLeaf(YType.enumeration, "protocol-state")

                self.synchronization_state = YLeaf(YType.enumeration, "synchronization-state")

                self.system_mac = YLeaf(YType.str, "system-mac")

                self.transport_state = YLeaf(YType.enumeration, "transport-state")

                self.protocol_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp()
                self.protocol_state_timestamp.parent = self
                self._children_name_map["protocol_state_timestamp"] = "protocol-state-timestamp"
                self._children_yang_names.add("protocol-state-timestamp")

                self.channel = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("iccp_group",
                                "arbitration_state",
                                "authentication_state",
                                "iccp_group_xr",
                                "isolated",
                                "primacy",
                                "protocol_state",
                                "synchronization_state",
                                "system_mac",
                                "transport_state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SdacpRedundancies.SdacpRedundancy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SdacpRedundancies.SdacpRedundancy, self).__setattr__(name, value)


            class ProtocolStateTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp, self).__init__()

                    self.yang_name = "protocol-state-timestamp"
                    self.yang_parent_name = "sdacp-redundancy"

                    self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                    self.seconds = YLeaf(YType.uint32, "seconds")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nanoseconds",
                                    "seconds") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nanoseconds.is_set or
                        self.seconds.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nanoseconds.yfilter != YFilter.not_set or
                        self.seconds.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protocol-state-timestamp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                    if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nanoseconds" or name == "seconds"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nanoseconds"):
                        self.nanoseconds = value
                        self.nanoseconds.value_namespace = name_space
                        self.nanoseconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds"):
                        self.seconds = value
                        self.seconds.value_namespace = name_space
                        self.seconds.value_namespace_prefix = name_space_prefix


            class Channel(Entity):
                """
                Channels on this session table
                
                .. attribute:: chan_state
                
                	Chan state
                	**type**\:   :py:class:`IcpeOpmChanFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmChanFsmState>`
                
                .. attribute:: channel_id
                
                	Channel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: channel_state_timestamp
                
                	Timestamp
                	**type**\:   :py:class:`ChannelStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp>`
                
                .. attribute:: control_messages_received
                
                	Control messages received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_sent
                
                	Control messages sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_received
                
                	Normal messages received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_sent
                
                	Normal messages sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: resync_state
                
                	Resync state
                	**type**\:   :py:class:`IcpeOpmResyncFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmResyncFsmState>`
                
                .. attribute:: resync_state_timestamp
                
                	Timestamp
                	**type**\:   :py:class:`ResyncStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel, self).__init__()

                    self.yang_name = "channel"
                    self.yang_parent_name = "sdacp-redundancy"

                    self.chan_state = YLeaf(YType.enumeration, "chan-state")

                    self.channel_id = YLeaf(YType.uint32, "channel-id")

                    self.control_messages_received = YLeaf(YType.uint64, "control-messages-received")

                    self.control_messages_sent = YLeaf(YType.uint64, "control-messages-sent")

                    self.normal_messages_received = YLeaf(YType.uint64, "normal-messages-received")

                    self.normal_messages_sent = YLeaf(YType.uint64, "normal-messages-sent")

                    self.resync_state = YLeaf(YType.enumeration, "resync-state")

                    self.channel_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp()
                    self.channel_state_timestamp.parent = self
                    self._children_name_map["channel_state_timestamp"] = "channel-state-timestamp"
                    self._children_yang_names.add("channel-state-timestamp")

                    self.resync_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp()
                    self.resync_state_timestamp.parent = self
                    self._children_name_map["resync_state_timestamp"] = "resync-state-timestamp"
                    self._children_yang_names.add("resync-state-timestamp")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("chan_state",
                                    "channel_id",
                                    "control_messages_received",
                                    "control_messages_sent",
                                    "normal_messages_received",
                                    "normal_messages_sent",
                                    "resync_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel, self).__setattr__(name, value)


                class ChannelStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp, self).__init__()

                        self.yang_name = "channel-state-timestamp"
                        self.yang_parent_name = "channel"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "channel-state-timestamp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class ResyncStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp, self).__init__()

                        self.yang_name = "resync-state-timestamp"
                        self.yang_parent_name = "channel"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resync-state-timestamp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.chan_state.is_set or
                        self.channel_id.is_set or
                        self.control_messages_received.is_set or
                        self.control_messages_sent.is_set or
                        self.normal_messages_received.is_set or
                        self.normal_messages_sent.is_set or
                        self.resync_state.is_set or
                        (self.channel_state_timestamp is not None and self.channel_state_timestamp.has_data()) or
                        (self.resync_state_timestamp is not None and self.resync_state_timestamp.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.chan_state.yfilter != YFilter.not_set or
                        self.channel_id.yfilter != YFilter.not_set or
                        self.control_messages_received.yfilter != YFilter.not_set or
                        self.control_messages_sent.yfilter != YFilter.not_set or
                        self.normal_messages_received.yfilter != YFilter.not_set or
                        self.normal_messages_sent.yfilter != YFilter.not_set or
                        self.resync_state.yfilter != YFilter.not_set or
                        (self.channel_state_timestamp is not None and self.channel_state_timestamp.has_operation()) or
                        (self.resync_state_timestamp is not None and self.resync_state_timestamp.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "channel" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.chan_state.is_set or self.chan_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.chan_state.get_name_leafdata())
                    if (self.channel_id.is_set or self.channel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.channel_id.get_name_leafdata())
                    if (self.control_messages_received.is_set or self.control_messages_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.control_messages_received.get_name_leafdata())
                    if (self.control_messages_sent.is_set or self.control_messages_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.control_messages_sent.get_name_leafdata())
                    if (self.normal_messages_received.is_set or self.normal_messages_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.normal_messages_received.get_name_leafdata())
                    if (self.normal_messages_sent.is_set or self.normal_messages_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.normal_messages_sent.get_name_leafdata())
                    if (self.resync_state.is_set or self.resync_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resync_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "channel-state-timestamp"):
                        if (self.channel_state_timestamp is None):
                            self.channel_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp()
                            self.channel_state_timestamp.parent = self
                            self._children_name_map["channel_state_timestamp"] = "channel-state-timestamp"
                        return self.channel_state_timestamp

                    if (child_yang_name == "resync-state-timestamp"):
                        if (self.resync_state_timestamp is None):
                            self.resync_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp()
                            self.resync_state_timestamp.parent = self
                            self._children_name_map["resync_state_timestamp"] = "resync-state-timestamp"
                        return self.resync_state_timestamp

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "channel-state-timestamp" or name == "resync-state-timestamp" or name == "chan-state" or name == "channel-id" or name == "control-messages-received" or name == "control-messages-sent" or name == "normal-messages-received" or name == "normal-messages-sent" or name == "resync-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "chan-state"):
                        self.chan_state = value
                        self.chan_state.value_namespace = name_space
                        self.chan_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "channel-id"):
                        self.channel_id = value
                        self.channel_id.value_namespace = name_space
                        self.channel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "control-messages-received"):
                        self.control_messages_received = value
                        self.control_messages_received.value_namespace = name_space
                        self.control_messages_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "control-messages-sent"):
                        self.control_messages_sent = value
                        self.control_messages_sent.value_namespace = name_space
                        self.control_messages_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "normal-messages-received"):
                        self.normal_messages_received = value
                        self.normal_messages_received.value_namespace = name_space
                        self.normal_messages_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "normal-messages-sent"):
                        self.normal_messages_sent = value
                        self.normal_messages_sent.value_namespace = name_space
                        self.normal_messages_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "resync-state"):
                        self.resync_state = value
                        self.resync_state.value_namespace = name_space
                        self.resync_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.channel:
                    if (c.has_data()):
                        return True
                return (
                    self.iccp_group.is_set or
                    self.arbitration_state.is_set or
                    self.authentication_state.is_set or
                    self.iccp_group_xr.is_set or
                    self.isolated.is_set or
                    self.primacy.is_set or
                    self.protocol_state.is_set or
                    self.synchronization_state.is_set or
                    self.system_mac.is_set or
                    self.transport_state.is_set or
                    (self.protocol_state_timestamp is not None and self.protocol_state_timestamp.has_data()))

            def has_operation(self):
                for c in self.channel:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.iccp_group.yfilter != YFilter.not_set or
                    self.arbitration_state.yfilter != YFilter.not_set or
                    self.authentication_state.yfilter != YFilter.not_set or
                    self.iccp_group_xr.yfilter != YFilter.not_set or
                    self.isolated.yfilter != YFilter.not_set or
                    self.primacy.yfilter != YFilter.not_set or
                    self.protocol_state.yfilter != YFilter.not_set or
                    self.synchronization_state.yfilter != YFilter.not_set or
                    self.system_mac.yfilter != YFilter.not_set or
                    self.transport_state.yfilter != YFilter.not_set or
                    (self.protocol_state_timestamp is not None and self.protocol_state_timestamp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sdacp-redundancy" + "[iccp-group='" + self.iccp_group.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/sdacp-redundancies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.iccp_group.is_set or self.iccp_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iccp_group.get_name_leafdata())
                if (self.arbitration_state.is_set or self.arbitration_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.arbitration_state.get_name_leafdata())
                if (self.authentication_state.is_set or self.authentication_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authentication_state.get_name_leafdata())
                if (self.iccp_group_xr.is_set or self.iccp_group_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iccp_group_xr.get_name_leafdata())
                if (self.isolated.is_set or self.isolated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.isolated.get_name_leafdata())
                if (self.primacy.is_set or self.primacy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.primacy.get_name_leafdata())
                if (self.protocol_state.is_set or self.protocol_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.protocol_state.get_name_leafdata())
                if (self.synchronization_state.is_set or self.synchronization_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.synchronization_state.get_name_leafdata())
                if (self.system_mac.is_set or self.system_mac.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.system_mac.get_name_leafdata())
                if (self.transport_state.is_set or self.transport_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transport_state.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "channel"):
                    for c in self.channel:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.channel.append(c)
                    return c

                if (child_yang_name == "protocol-state-timestamp"):
                    if (self.protocol_state_timestamp is None):
                        self.protocol_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp()
                        self.protocol_state_timestamp.parent = self
                        self._children_name_map["protocol_state_timestamp"] = "protocol-state-timestamp"
                    return self.protocol_state_timestamp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "channel" or name == "protocol-state-timestamp" or name == "iccp-group" or name == "arbitration-state" or name == "authentication-state" or name == "iccp-group-xr" or name == "isolated" or name == "primacy" or name == "protocol-state" or name == "synchronization-state" or name == "system-mac" or name == "transport-state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "iccp-group"):
                    self.iccp_group = value
                    self.iccp_group.value_namespace = name_space
                    self.iccp_group.value_namespace_prefix = name_space_prefix
                if(value_path == "arbitration-state"):
                    self.arbitration_state = value
                    self.arbitration_state.value_namespace = name_space
                    self.arbitration_state.value_namespace_prefix = name_space_prefix
                if(value_path == "authentication-state"):
                    self.authentication_state = value
                    self.authentication_state.value_namespace = name_space
                    self.authentication_state.value_namespace_prefix = name_space_prefix
                if(value_path == "iccp-group-xr"):
                    self.iccp_group_xr = value
                    self.iccp_group_xr.value_namespace = name_space
                    self.iccp_group_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "isolated"):
                    self.isolated = value
                    self.isolated.value_namespace = name_space
                    self.isolated.value_namespace_prefix = name_space_prefix
                if(value_path == "primacy"):
                    self.primacy = value
                    self.primacy.value_namespace = name_space
                    self.primacy.value_namespace_prefix = name_space_prefix
                if(value_path == "protocol-state"):
                    self.protocol_state = value
                    self.protocol_state.value_namespace = name_space
                    self.protocol_state.value_namespace_prefix = name_space_prefix
                if(value_path == "synchronization-state"):
                    self.synchronization_state = value
                    self.synchronization_state.value_namespace = name_space
                    self.synchronization_state.value_namespace_prefix = name_space_prefix
                if(value_path == "system-mac"):
                    self.system_mac = value
                    self.system_mac.value_namespace = name_space
                    self.system_mac.value_namespace_prefix = name_space_prefix
                if(value_path == "transport-state"):
                    self.transport_state = value
                    self.transport_state.value_namespace = name_space
                    self.transport_state.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sdacp_redundancy:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sdacp_redundancy:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sdacp-redundancies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sdacp-redundancy"):
                for c in self.sdacp_redundancy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SdacpRedundancies.SdacpRedundancy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sdacp_redundancy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sdacp-redundancy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InstallShows(Entity):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_show
        
        	Detailed breakdown of install status
        	**type**\: list of    :py:class:`InstallShow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallShows.InstallShow>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallShows, self).__init__()

            self.yang_name = "install-shows"
            self.yang_parent_name = "nv-satellite"

            self.install_show = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.InstallShows, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.InstallShows, self).__setattr__(name, value)


        class InstallShow(Entity):
            """
            Detailed breakdown of install status
            
            .. attribute:: operation_id  <key>
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: end_time
            
            	End time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: name_string
            
            	Name strings
            	**type**\:  list of str
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_type
            
            	Operation type
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: progress_percentage
            
            	Progress percentage
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: percentage
            
            .. attribute:: ref_state
            
            	Ref state
            	**type**\:   :py:class:`IcpeInstallSatState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeInstallSatState>`
            
            .. attribute:: satellite
            
            	Breakdown per satellite table
            	**type**\: list of    :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallShows.InstallShow.Satellite>`
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\:  str
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_aborted
            
            	Sats deactivate aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_failed
            
            	Sats deactivate failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivating
            
            	Sats deactivating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_aborted
            
            	Sats remove aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_failed
            
            	Sats remove failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_removing
            
            	Sats removing
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_aborted
            
            	Sats update aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_failed
            
            	Sats update failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_updating
            
            	Sats updating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: start_time
            
            	Start time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallShows.InstallShow, self).__init__()

                self.yang_name = "install-show"
                self.yang_parent_name = "install-shows"

                self.operation_id = YLeaf(YType.uint32, "operation-id")

                self.end_time = YLeaf(YType.uint32, "end-time")

                self.name_string = YLeafList(YType.str, "name-string")

                self.operation_id_xr = YLeaf(YType.uint32, "operation-id-xr")

                self.operation_type = YLeaf(YType.uint16, "operation-type")

                self.progress_percentage = YLeaf(YType.uint16, "progress-percentage")

                self.ref_state = YLeaf(YType.enumeration, "ref-state")

                self.satellite_range = YLeaf(YType.str, "satellite-range")

                self.sats_activate_aborted = YLeafList(YType.uint16, "sats-activate-aborted")

                self.sats_activate_failed = YLeafList(YType.uint16, "sats-activate-failed")

                self.sats_activating = YLeafList(YType.uint16, "sats-activating")

                self.sats_completed = YLeafList(YType.uint16, "sats-completed")

                self.sats_deactivate_aborted = YLeafList(YType.uint16, "sats-deactivate-aborted")

                self.sats_deactivate_failed = YLeafList(YType.uint16, "sats-deactivate-failed")

                self.sats_deactivating = YLeafList(YType.uint16, "sats-deactivating")

                self.sats_no_operation = YLeafList(YType.uint16, "sats-no-operation")

                self.sats_not_initiated = YLeafList(YType.uint16, "sats-not-initiated")

                self.sats_remove_aborted = YLeafList(YType.uint16, "sats-remove-aborted")

                self.sats_remove_failed = YLeafList(YType.uint16, "sats-remove-failed")

                self.sats_removing = YLeafList(YType.uint16, "sats-removing")

                self.sats_transfer_aborted = YLeafList(YType.uint16, "sats-transfer-aborted")

                self.sats_transfer_failed = YLeafList(YType.uint16, "sats-transfer-failed")

                self.sats_transferring = YLeafList(YType.uint16, "sats-transferring")

                self.sats_update_aborted = YLeafList(YType.uint16, "sats-update-aborted")

                self.sats_update_failed = YLeafList(YType.uint16, "sats-update-failed")

                self.sats_updating = YLeafList(YType.uint16, "sats-updating")

                self.start_time = YLeaf(YType.uint32, "start-time")

                self.satellite = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("operation_id",
                                "end_time",
                                "name_string",
                                "operation_id_xr",
                                "operation_type",
                                "progress_percentage",
                                "ref_state",
                                "satellite_range",
                                "sats_activate_aborted",
                                "sats_activate_failed",
                                "sats_activating",
                                "sats_completed",
                                "sats_deactivate_aborted",
                                "sats_deactivate_failed",
                                "sats_deactivating",
                                "sats_no_operation",
                                "sats_not_initiated",
                                "sats_remove_aborted",
                                "sats_remove_failed",
                                "sats_removing",
                                "sats_transfer_aborted",
                                "sats_transfer_failed",
                                "sats_transferring",
                                "sats_update_aborted",
                                "sats_update_failed",
                                "sats_updating",
                                "start_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.InstallShows.InstallShow, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.InstallShows.InstallShow, self).__setattr__(name, value)


            class Satellite(Entity):
                """
                Breakdown per satellite table
                
                .. attribute:: end_time
                
                	End time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: info
                
                	Info
                	**type**\:  str
                
                .. attribute:: percentage
                
                	Percentage
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**units**\: percentage
                
                .. attribute:: retries
                
                	Retries
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: start_time
                
                	Start time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State
                	**type**\:   :py:class:`IcpeInstallSatState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeInstallSatState>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.InstallShows.InstallShow.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "install-show"

                    self.end_time = YLeaf(YType.uint32, "end-time")

                    self.info = YLeaf(YType.str, "info")

                    self.percentage = YLeaf(YType.uint16, "percentage")

                    self.retries = YLeaf(YType.uint16, "retries")

                    self.satellite_id = YLeaf(YType.uint16, "satellite-id")

                    self.start_time = YLeaf(YType.uint32, "start-time")

                    self.state = YLeaf(YType.enumeration, "state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("end_time",
                                    "info",
                                    "percentage",
                                    "retries",
                                    "satellite_id",
                                    "start_time",
                                    "state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.InstallShows.InstallShow.Satellite, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.InstallShows.InstallShow.Satellite, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.end_time.is_set or
                        self.info.is_set or
                        self.percentage.is_set or
                        self.retries.is_set or
                        self.satellite_id.is_set or
                        self.start_time.is_set or
                        self.state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.end_time.yfilter != YFilter.not_set or
                        self.info.yfilter != YFilter.not_set or
                        self.percentage.yfilter != YFilter.not_set or
                        self.retries.yfilter != YFilter.not_set or
                        self.satellite_id.yfilter != YFilter.not_set or
                        self.start_time.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "satellite" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.end_time.is_set or self.end_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.end_time.get_name_leafdata())
                    if (self.info.is_set or self.info.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.info.get_name_leafdata())
                    if (self.percentage.is_set or self.percentage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.percentage.get_name_leafdata())
                    if (self.retries.is_set or self.retries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retries.get_name_leafdata())
                    if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_id.get_name_leafdata())
                    if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_time.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "end-time" or name == "info" or name == "percentage" or name == "retries" or name == "satellite-id" or name == "start-time" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "end-time"):
                        self.end_time = value
                        self.end_time.value_namespace = name_space
                        self.end_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "info"):
                        self.info = value
                        self.info.value_namespace = name_space
                        self.info.value_namespace_prefix = name_space_prefix
                    if(value_path == "percentage"):
                        self.percentage = value
                        self.percentage.value_namespace = name_space
                        self.percentage.value_namespace_prefix = name_space_prefix
                    if(value_path == "retries"):
                        self.retries = value
                        self.retries.value_namespace = name_space
                        self.retries.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-id"):
                        self.satellite_id = value
                        self.satellite_id.value_namespace = name_space
                        self.satellite_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-time"):
                        self.start_time = value
                        self.start_time.value_namespace = name_space
                        self.start_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.satellite:
                    if (c.has_data()):
                        return True
                for leaf in self.name_string.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activate_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activate_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_completed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivate_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivate_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_no_operation.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_remove_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_remove_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_removing.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transfer_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transfer_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transferring.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_update_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_update_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_updating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.operation_id.is_set or
                    self.end_time.is_set or
                    self.operation_id_xr.is_set or
                    self.operation_type.is_set or
                    self.progress_percentage.is_set or
                    self.ref_state.is_set or
                    self.satellite_range.is_set or
                    self.start_time.is_set)

            def has_operation(self):
                for c in self.satellite:
                    if (c.has_operation()):
                        return True
                for leaf in self.name_string.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activate_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activate_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activating.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_completed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivate_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivate_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivating.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_no_operation.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_remove_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_remove_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_removing.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transfer_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transfer_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transferring.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_update_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_update_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_updating.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.operation_id.yfilter != YFilter.not_set or
                    self.end_time.yfilter != YFilter.not_set or
                    self.name_string.yfilter != YFilter.not_set or
                    self.operation_id_xr.yfilter != YFilter.not_set or
                    self.operation_type.yfilter != YFilter.not_set or
                    self.progress_percentage.yfilter != YFilter.not_set or
                    self.ref_state.yfilter != YFilter.not_set or
                    self.satellite_range.yfilter != YFilter.not_set or
                    self.sats_activate_aborted.yfilter != YFilter.not_set or
                    self.sats_activate_failed.yfilter != YFilter.not_set or
                    self.sats_activating.yfilter != YFilter.not_set or
                    self.sats_completed.yfilter != YFilter.not_set or
                    self.sats_deactivate_aborted.yfilter != YFilter.not_set or
                    self.sats_deactivate_failed.yfilter != YFilter.not_set or
                    self.sats_deactivating.yfilter != YFilter.not_set or
                    self.sats_no_operation.yfilter != YFilter.not_set or
                    self.sats_not_initiated.yfilter != YFilter.not_set or
                    self.sats_remove_aborted.yfilter != YFilter.not_set or
                    self.sats_remove_failed.yfilter != YFilter.not_set or
                    self.sats_removing.yfilter != YFilter.not_set or
                    self.sats_transfer_aborted.yfilter != YFilter.not_set or
                    self.sats_transfer_failed.yfilter != YFilter.not_set or
                    self.sats_transferring.yfilter != YFilter.not_set or
                    self.sats_update_aborted.yfilter != YFilter.not_set or
                    self.sats_update_failed.yfilter != YFilter.not_set or
                    self.sats_updating.yfilter != YFilter.not_set or
                    self.start_time.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "install-show" + "[operation-id='" + self.operation_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-shows/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id.get_name_leafdata())
                if (self.end_time.is_set or self.end_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.end_time.get_name_leafdata())
                if (self.operation_id_xr.is_set or self.operation_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id_xr.get_name_leafdata())
                if (self.operation_type.is_set or self.operation_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_type.get_name_leafdata())
                if (self.progress_percentage.is_set or self.progress_percentage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.progress_percentage.get_name_leafdata())
                if (self.ref_state.is_set or self.ref_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ref_state.get_name_leafdata())
                if (self.satellite_range.is_set or self.satellite_range.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range.get_name_leafdata())
                if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.start_time.get_name_leafdata())

                leaf_name_data.extend(self.name_string.get_name_leafdata())

                leaf_name_data.extend(self.sats_activate_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_activate_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_activating.get_name_leafdata())

                leaf_name_data.extend(self.sats_completed.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivate_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivate_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivating.get_name_leafdata())

                leaf_name_data.extend(self.sats_no_operation.get_name_leafdata())

                leaf_name_data.extend(self.sats_not_initiated.get_name_leafdata())

                leaf_name_data.extend(self.sats_remove_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_remove_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_removing.get_name_leafdata())

                leaf_name_data.extend(self.sats_transfer_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_transfer_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_transferring.get_name_leafdata())

                leaf_name_data.extend(self.sats_update_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_update_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_updating.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "satellite"):
                    for c in self.satellite:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.InstallShows.InstallShow.Satellite()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.satellite.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "satellite" or name == "operation-id" or name == "end-time" or name == "name-string" or name == "operation-id-xr" or name == "operation-type" or name == "progress-percentage" or name == "ref-state" or name == "satellite-range" or name == "sats-activate-aborted" or name == "sats-activate-failed" or name == "sats-activating" or name == "sats-completed" or name == "sats-deactivate-aborted" or name == "sats-deactivate-failed" or name == "sats-deactivating" or name == "sats-no-operation" or name == "sats-not-initiated" or name == "sats-remove-aborted" or name == "sats-remove-failed" or name == "sats-removing" or name == "sats-transfer-aborted" or name == "sats-transfer-failed" or name == "sats-transferring" or name == "sats-update-aborted" or name == "sats-update-failed" or name == "sats-updating" or name == "start-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "operation-id"):
                    self.operation_id = value
                    self.operation_id.value_namespace = name_space
                    self.operation_id.value_namespace_prefix = name_space_prefix
                if(value_path == "end-time"):
                    self.end_time = value
                    self.end_time.value_namespace = name_space
                    self.end_time.value_namespace_prefix = name_space_prefix
                if(value_path == "name-string"):
                    self.name_string.append(value)
                if(value_path == "operation-id-xr"):
                    self.operation_id_xr = value
                    self.operation_id_xr.value_namespace = name_space
                    self.operation_id_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "operation-type"):
                    self.operation_type = value
                    self.operation_type.value_namespace = name_space
                    self.operation_type.value_namespace_prefix = name_space_prefix
                if(value_path == "progress-percentage"):
                    self.progress_percentage = value
                    self.progress_percentage.value_namespace = name_space
                    self.progress_percentage.value_namespace_prefix = name_space_prefix
                if(value_path == "ref-state"):
                    self.ref_state = value
                    self.ref_state.value_namespace = name_space
                    self.ref_state.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-range"):
                    self.satellite_range = value
                    self.satellite_range.value_namespace = name_space
                    self.satellite_range.value_namespace_prefix = name_space_prefix
                if(value_path == "sats-activate-aborted"):
                    self.sats_activate_aborted.append(value)
                if(value_path == "sats-activate-failed"):
                    self.sats_activate_failed.append(value)
                if(value_path == "sats-activating"):
                    self.sats_activating.append(value)
                if(value_path == "sats-completed"):
                    self.sats_completed.append(value)
                if(value_path == "sats-deactivate-aborted"):
                    self.sats_deactivate_aborted.append(value)
                if(value_path == "sats-deactivate-failed"):
                    self.sats_deactivate_failed.append(value)
                if(value_path == "sats-deactivating"):
                    self.sats_deactivating.append(value)
                if(value_path == "sats-no-operation"):
                    self.sats_no_operation.append(value)
                if(value_path == "sats-not-initiated"):
                    self.sats_not_initiated.append(value)
                if(value_path == "sats-remove-aborted"):
                    self.sats_remove_aborted.append(value)
                if(value_path == "sats-remove-failed"):
                    self.sats_remove_failed.append(value)
                if(value_path == "sats-removing"):
                    self.sats_removing.append(value)
                if(value_path == "sats-transfer-aborted"):
                    self.sats_transfer_aborted.append(value)
                if(value_path == "sats-transfer-failed"):
                    self.sats_transfer_failed.append(value)
                if(value_path == "sats-transferring"):
                    self.sats_transferring.append(value)
                if(value_path == "sats-update-aborted"):
                    self.sats_update_aborted.append(value)
                if(value_path == "sats-update-failed"):
                    self.sats_update_failed.append(value)
                if(value_path == "sats-updating"):
                    self.sats_updating.append(value)
                if(value_path == "start-time"):
                    self.start_time = value
                    self.start_time.value_namespace = name_space
                    self.start_time.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.install_show:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.install_show:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "install-shows" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "install-show"):
                for c in self.install_show:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.InstallShows.InstallShow()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.install_show.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "install-show"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SatelliteStatuses(Entity):
        """
        Satellite status information table
        
        .. attribute:: satellite_status
        
        	Satellite status information
        	**type**\: list of    :py:class:`SatelliteStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteStatuses, self).__init__()

            self.yang_name = "satellite-statuses"
            self.yang_parent_name = "nv-satellite"

            self.satellite_status = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SatelliteStatuses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SatelliteStatuses, self).__setattr__(name, value)


        class SatelliteStatus(Entity):
            """
            Satellite status information
            
            .. attribute:: satellite_id  <key>
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: candidate_fabric_ports
            
            	Candidate Fabric Ports on this Satellite
            	**type**\:   :py:class:`CandidateFabricPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts>`
            
            .. attribute:: cfgd_timeout
            
            	Cfgd timeout
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: configured_link
            
            	Configured Links on this Satellite table
            	**type**\: list of    :py:class:`ConfiguredLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink>`
            
            .. attribute:: configured_serial_number
            
            	Configured serial number
            	**type**\:  str
            
            .. attribute:: configured_serial_number_present
            
            	Configured serial number present
            	**type**\:  bool
            
            .. attribute:: conflict_context
            
            	Conflict context
            	**type**\:  str
            
            .. attribute:: conflict_reason
            
            	Conflict reason
            	**type**\:   :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
            
            .. attribute:: description
            
            	Description
            	**type**\:  str
            
            .. attribute:: description_present
            
            	Description present
            	**type**\:  bool
            
            .. attribute:: ethernet_fabric_supported
            
            	Ethernet fabric supported
            	**type**\:  bool
            
            .. attribute:: host_treating_as_active
            
            	Host treating as active
            	**type**\:  bool
            
            .. attribute:: install_state
            
            	Install state
            	**type**\:   :py:class:`IcpeOperInstallState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperInstallState>`
            
            .. attribute:: ip_address
            
            	IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ip_address_auto
            
            	IP address auto
            	**type**\:  bool
            
            .. attribute:: ip_address_present
            
            	IP address present
            	**type**\:  bool
            
            .. attribute:: ipv6_address
            
            	IPV6 address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address_present
            
            	IPV6 address present
            	**type**\:  bool
            
            .. attribute:: mac_address
            
            	MAC address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: mac_address_present
            
            	MAC address present
            	**type**\:  bool
            
            .. attribute:: optical_status
            
            	Optical Satellite Status
            	**type**\:   :py:class:`OpticalStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus>`
            
            .. attribute:: optical_supported
            
            	Optical supported
            	**type**\:  bool
            
            .. attribute:: password
            
            	Password
            	**type**\:  str
            
            .. attribute:: password_error
            
            	Password error
            	**type**\:  str
            
            .. attribute:: received_host_name
            
            	Received hostname
            	**type**\:  str
            
            .. attribute:: received_serial_number
            
            	Received serial number
            	**type**\:  str
            
            .. attribute:: received_serial_number_present
            
            	Received serial number present
            	**type**\:  bool
            
            .. attribute:: recovery_delay_time_left
            
            	Recovery delay time left
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: redundancy_iccp_group
            
            	Redundancy ICCP group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: redundancy_out_of_sync_timestamp
            
            	Timestamp
            	**type**\:   :py:class:`RedundancyOutOfSyncTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp>`
            
            .. attribute:: remote_version
            
            	Remote version
            	**type**\:  list of str
            
            .. attribute:: remote_version_present
            
            	Remote version present
            	**type**\:  bool
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_treating_as_active
            
            	Satellite treating as active
            	**type**\:  bool
            
            .. attribute:: sdacp_session_failure_reason
            
            	SDACP session failure reason
            	**type**\:   :py:class:`IcpeGcoOperControlReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeGcoOperControlReason>`
            
            .. attribute:: sdacp_session_state
            
            	SDACP session state
            	**type**\:   :py:class:`IcpeOperSdacpSessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperSdacpSessState>`
            
            .. attribute:: timeout_warning
            
            	Timeout warning
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: type
            
            	Type
            	**type**\:  str
            
            .. attribute:: version_check_state
            
            	Version check state
            	**type**\:   :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            .. attribute:: vrfid
            
            	VRFID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteStatuses.SatelliteStatus, self).__init__()

                self.yang_name = "satellite-status"
                self.yang_parent_name = "satellite-statuses"

                self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                self.cfgd_timeout = YLeaf(YType.uint32, "cfgd-timeout")

                self.configured_serial_number = YLeaf(YType.str, "configured-serial-number")

                self.configured_serial_number_present = YLeaf(YType.boolean, "configured-serial-number-present")

                self.conflict_context = YLeaf(YType.str, "conflict-context")

                self.conflict_reason = YLeaf(YType.enumeration, "conflict-reason")

                self.description = YLeaf(YType.str, "description")

                self.description_present = YLeaf(YType.boolean, "description-present")

                self.ethernet_fabric_supported = YLeaf(YType.boolean, "ethernet-fabric-supported")

                self.host_treating_as_active = YLeaf(YType.boolean, "host-treating-as-active")

                self.install_state = YLeaf(YType.enumeration, "install-state")

                self.ip_address = YLeaf(YType.str, "ip-address")

                self.ip_address_auto = YLeaf(YType.boolean, "ip-address-auto")

                self.ip_address_present = YLeaf(YType.boolean, "ip-address-present")

                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                self.ipv6_address_present = YLeaf(YType.boolean, "ipv6-address-present")

                self.mac_address = YLeaf(YType.str, "mac-address")

                self.mac_address_present = YLeaf(YType.boolean, "mac-address-present")

                self.optical_supported = YLeaf(YType.boolean, "optical-supported")

                self.password = YLeaf(YType.str, "password")

                self.password_error = YLeaf(YType.str, "password-error")

                self.received_host_name = YLeaf(YType.str, "received-host-name")

                self.received_serial_number = YLeaf(YType.str, "received-serial-number")

                self.received_serial_number_present = YLeaf(YType.boolean, "received-serial-number-present")

                self.recovery_delay_time_left = YLeaf(YType.uint16, "recovery-delay-time-left")

                self.redundancy_iccp_group = YLeaf(YType.uint32, "redundancy-iccp-group")

                self.remote_version = YLeafList(YType.str, "remote-version")

                self.remote_version_present = YLeaf(YType.boolean, "remote-version-present")

                self.satellite_id_xr = YLeaf(YType.uint32, "satellite-id-xr")

                self.satellite_treating_as_active = YLeaf(YType.boolean, "satellite-treating-as-active")

                self.sdacp_session_failure_reason = YLeaf(YType.enumeration, "sdacp-session-failure-reason")

                self.sdacp_session_state = YLeaf(YType.enumeration, "sdacp-session-state")

                self.timeout_warning = YLeaf(YType.uint32, "timeout-warning")

                self.type = YLeaf(YType.str, "type")

                self.version_check_state = YLeaf(YType.enumeration, "version-check-state")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrfid = YLeaf(YType.uint32, "vrfid")

                self.candidate_fabric_ports = NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts()
                self.candidate_fabric_ports.parent = self
                self._children_name_map["candidate_fabric_ports"] = "candidate-fabric-ports"
                self._children_yang_names.add("candidate-fabric-ports")

                self.optical_status = NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus()
                self.optical_status.parent = self
                self._children_name_map["optical_status"] = "optical-status"
                self._children_yang_names.add("optical-status")

                self.redundancy_out_of_sync_timestamp = NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp()
                self.redundancy_out_of_sync_timestamp.parent = self
                self._children_name_map["redundancy_out_of_sync_timestamp"] = "redundancy-out-of-sync-timestamp"
                self._children_yang_names.add("redundancy-out-of-sync-timestamp")

                self.configured_link = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("satellite_id",
                                "cfgd_timeout",
                                "configured_serial_number",
                                "configured_serial_number_present",
                                "conflict_context",
                                "conflict_reason",
                                "description",
                                "description_present",
                                "ethernet_fabric_supported",
                                "host_treating_as_active",
                                "install_state",
                                "ip_address",
                                "ip_address_auto",
                                "ip_address_present",
                                "ipv6_address",
                                "ipv6_address_present",
                                "mac_address",
                                "mac_address_present",
                                "optical_supported",
                                "password",
                                "password_error",
                                "received_host_name",
                                "received_serial_number",
                                "received_serial_number_present",
                                "recovery_delay_time_left",
                                "redundancy_iccp_group",
                                "remote_version",
                                "remote_version_present",
                                "satellite_id_xr",
                                "satellite_treating_as_active",
                                "sdacp_session_failure_reason",
                                "sdacp_session_state",
                                "timeout_warning",
                                "type",
                                "version_check_state",
                                "vrf_name",
                                "vrfid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SatelliteStatuses.SatelliteStatus, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus, self).__setattr__(name, value)


            class CandidateFabricPorts(Entity):
                """
                Candidate Fabric Ports on this Satellite
                
                .. attribute:: channel_up
                
                	Channel up
                	**type**\:  bool
                
                .. attribute:: configured_port
                
                	Configured Candidate Fabric Ports table
                	**type**\: list of    :py:class:`ConfiguredPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort>`
                
                .. attribute:: current_port
                
                	Current Candidate Fabric Ports on this Satellite table
                	**type**\: list of    :py:class:`CurrentPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort>`
                
                .. attribute:: error_string
                
                	Error string
                	**type**\:  str
                
                .. attribute:: out_of_sync
                
                	Out of sync
                	**type**\:  bool
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts, self).__init__()

                    self.yang_name = "candidate-fabric-ports"
                    self.yang_parent_name = "satellite-status"

                    self.channel_up = YLeaf(YType.boolean, "channel-up")

                    self.error_string = YLeaf(YType.str, "error-string")

                    self.out_of_sync = YLeaf(YType.boolean, "out-of-sync")

                    self.configured_port = YList(self)
                    self.current_port = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("channel_up",
                                    "error_string",
                                    "out_of_sync") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts, self).__setattr__(name, value)


                class ConfiguredPort(Entity):
                    """
                    Configured Candidate Fabric Ports table
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:   :py:class:`IcpeOperFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPort>`
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: valid
                    
                    	Valid
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort, self).__init__()

                        self.yang_name = "configured-port"
                        self.yang_parent_name = "candidate-fabric-ports"

                        self.port = YLeaf(YType.uint16, "port")

                        self.port_type = YLeaf(YType.enumeration, "port-type")

                        self.slot = YLeaf(YType.uint16, "slot")

                        self.subslot = YLeaf(YType.uint16, "subslot")

                        self.valid = YLeaf(YType.boolean, "valid")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("port",
                                        "port_type",
                                        "slot",
                                        "subslot",
                                        "valid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.port.is_set or
                            self.port_type.is_set or
                            self.slot.is_set or
                            self.subslot.is_set or
                            self.valid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set or
                            self.port_type.yfilter != YFilter.not_set or
                            self.slot.yfilter != YFilter.not_set or
                            self.subslot.yfilter != YFilter.not_set or
                            self.valid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "configured-port" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())
                        if (self.port_type.is_set or self.port_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_type.get_name_leafdata())
                        if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot.get_name_leafdata())
                        if (self.subslot.is_set or self.subslot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subslot.get_name_leafdata())
                        if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.valid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "port" or name == "port-type" or name == "slot" or name == "subslot" or name == "valid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-type"):
                            self.port_type = value
                            self.port_type.value_namespace = name_space
                            self.port_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "slot"):
                            self.slot = value
                            self.slot.value_namespace = name_space
                            self.slot.value_namespace_prefix = name_space_prefix
                        if(value_path == "subslot"):
                            self.subslot = value
                            self.subslot.value_namespace = name_space
                            self.subslot.value_namespace_prefix = name_space_prefix
                        if(value_path == "valid"):
                            self.valid = value
                            self.valid.value_namespace = name_space
                            self.valid.value_namespace_prefix = name_space_prefix


                class CurrentPort(Entity):
                    """
                    Current Candidate Fabric Ports on this Satellite
                    table
                    
                    .. attribute:: permanent
                    
                    	Permanent
                    	**type**\:  bool
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:   :py:class:`IcpeOperFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPort>`
                    
                    .. attribute:: requested
                    
                    	Requested
                    	**type**\:  bool
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort, self).__init__()

                        self.yang_name = "current-port"
                        self.yang_parent_name = "candidate-fabric-ports"

                        self.permanent = YLeaf(YType.boolean, "permanent")

                        self.port = YLeaf(YType.uint16, "port")

                        self.port_type = YLeaf(YType.enumeration, "port-type")

                        self.requested = YLeaf(YType.boolean, "requested")

                        self.slot = YLeaf(YType.uint16, "slot")

                        self.subslot = YLeaf(YType.uint16, "subslot")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("permanent",
                                        "port",
                                        "port_type",
                                        "requested",
                                        "slot",
                                        "subslot") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.permanent.is_set or
                            self.port.is_set or
                            self.port_type.is_set or
                            self.requested.is_set or
                            self.slot.is_set or
                            self.subslot.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.permanent.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set or
                            self.port_type.yfilter != YFilter.not_set or
                            self.requested.yfilter != YFilter.not_set or
                            self.slot.yfilter != YFilter.not_set or
                            self.subslot.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "current-port" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.permanent.is_set or self.permanent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.permanent.get_name_leafdata())
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())
                        if (self.port_type.is_set or self.port_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_type.get_name_leafdata())
                        if (self.requested.is_set or self.requested.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.requested.get_name_leafdata())
                        if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot.get_name_leafdata())
                        if (self.subslot.is_set or self.subslot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subslot.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "permanent" or name == "port" or name == "port-type" or name == "requested" or name == "slot" or name == "subslot"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "permanent"):
                            self.permanent = value
                            self.permanent.value_namespace = name_space
                            self.permanent.value_namespace_prefix = name_space_prefix
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-type"):
                            self.port_type = value
                            self.port_type.value_namespace = name_space
                            self.port_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "requested"):
                            self.requested = value
                            self.requested.value_namespace = name_space
                            self.requested.value_namespace_prefix = name_space_prefix
                        if(value_path == "slot"):
                            self.slot = value
                            self.slot.value_namespace = name_space
                            self.slot.value_namespace_prefix = name_space_prefix
                        if(value_path == "subslot"):
                            self.subslot = value
                            self.subslot.value_namespace = name_space
                            self.subslot.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.configured_port:
                        if (c.has_data()):
                            return True
                    for c in self.current_port:
                        if (c.has_data()):
                            return True
                    return (
                        self.channel_up.is_set or
                        self.error_string.is_set or
                        self.out_of_sync.is_set)

                def has_operation(self):
                    for c in self.configured_port:
                        if (c.has_operation()):
                            return True
                    for c in self.current_port:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.channel_up.yfilter != YFilter.not_set or
                        self.error_string.yfilter != YFilter.not_set or
                        self.out_of_sync.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "candidate-fabric-ports" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.channel_up.is_set or self.channel_up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.channel_up.get_name_leafdata())
                    if (self.error_string.is_set or self.error_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error_string.get_name_leafdata())
                    if (self.out_of_sync.is_set or self.out_of_sync.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_sync.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "configured-port"):
                        for c in self.configured_port:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.configured_port.append(c)
                        return c

                    if (child_yang_name == "current-port"):
                        for c in self.current_port:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.current_port.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "configured-port" or name == "current-port" or name == "channel-up" or name == "error-string" or name == "out-of-sync"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "channel-up"):
                        self.channel_up = value
                        self.channel_up.value_namespace = name_space
                        self.channel_up.value_namespace_prefix = name_space_prefix
                    if(value_path == "error-string"):
                        self.error_string = value
                        self.error_string.value_namespace = name_space
                        self.error_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-sync"):
                        self.out_of_sync = value
                        self.out_of_sync.value_namespace = name_space
                        self.out_of_sync.value_namespace_prefix = name_space_prefix


            class OpticalStatus(Entity):
                """
                Optical Satellite Status
                
                .. attribute:: application
                
                	Application State table
                	**type**\: list of    :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application>`
                
                .. attribute:: chassis_sync_state
                
                	Chassis sync state
                	**type**\:   :py:class:`IcpeOpticalSyncState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncState>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus, self).__init__()

                    self.yang_name = "optical-status"
                    self.yang_parent_name = "satellite-status"

                    self.chassis_sync_state = YLeaf(YType.enumeration, "chassis-sync-state")

                    self.application = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("chassis_sync_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus, self).__setattr__(name, value)


                class Application(Entity):
                    """
                    Application State table
                    
                    .. attribute:: name
                    
                    	Name
                    	**type**\:  str
                    
                    .. attribute:: sync_state
                    
                    	Sync state
                    	**type**\:   :py:class:`IcpeOpticalSyncState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncState>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application, self).__init__()

                        self.yang_name = "application"
                        self.yang_parent_name = "optical-status"

                        self.name = YLeaf(YType.str, "name")

                        self.sync_state = YLeaf(YType.enumeration, "sync-state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name",
                                        "sync_state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.sync_state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.sync_state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "application" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.sync_state.is_set or self.sync_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sync_state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name" or name == "sync-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "sync-state"):
                            self.sync_state = value
                            self.sync_state.value_namespace = name_space
                            self.sync_state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.application:
                        if (c.has_data()):
                            return True
                    return self.chassis_sync_state.is_set

                def has_operation(self):
                    for c in self.application:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.chassis_sync_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optical-status" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.chassis_sync_state.is_set or self.chassis_sync_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.chassis_sync_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "application"):
                        for c in self.application:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.application.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "application" or name == "chassis-sync-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "chassis-sync-state"):
                        self.chassis_sync_state = value
                        self.chassis_sync_state.value_namespace = name_space
                        self.chassis_sync_state.value_namespace_prefix = name_space_prefix


            class RedundancyOutOfSyncTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp, self).__init__()

                    self.yang_name = "redundancy-out-of-sync-timestamp"
                    self.yang_parent_name = "satellite-status"

                    self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                    self.seconds = YLeaf(YType.uint32, "seconds")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nanoseconds",
                                    "seconds") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nanoseconds.is_set or
                        self.seconds.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nanoseconds.yfilter != YFilter.not_set or
                        self.seconds.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "redundancy-out-of-sync-timestamp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                    if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nanoseconds" or name == "seconds"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nanoseconds"):
                        self.nanoseconds = value
                        self.nanoseconds.value_namespace = name_space
                        self.nanoseconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds"):
                        self.seconds = value
                        self.seconds.value_namespace = name_space
                        self.seconds.value_namespace_prefix = name_space_prefix


            class ConfiguredLink(Entity):
                """
                Configured Links on this Satellite table
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\:  str
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:   :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                
                .. attribute:: discovered_link
                
                	Discovered Links table
                	**type**\: list of    :py:class:`DiscoveredLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink>`
                
                .. attribute:: interface_handle
                
                	Interface handle
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: ip_address
                
                	IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ip_address_auto
                
                	IP address auto
                	**type**\:  bool
                
                .. attribute:: min_links_satisfied
                
                	Min links satisfied
                	**type**\:  bool
                
                .. attribute:: minimum_preferred_links
                
                	Minimum preferred links
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: minimum_required_links
                
                	Minimum required links
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_active_links
                
                	Number active links
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_range
                
                	Port ranges table
                	**type**\: list of    :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange>`
                
                .. attribute:: required_min_links_satisfied
                
                	Required min links satisfied
                	**type**\:  bool
                
                .. attribute:: vrf_id
                
                	VRF ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_id_present
                
                	VRF ID present
                	**type**\:  bool
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink, self).__init__()

                    self.yang_name = "configured-link"
                    self.yang_parent_name = "satellite-status"

                    self.conflict_context = YLeaf(YType.str, "conflict-context")

                    self.conflict_reason = YLeaf(YType.enumeration, "conflict-reason")

                    self.interface_handle = YLeaf(YType.str, "interface-handle")

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.ip_address_auto = YLeaf(YType.boolean, "ip-address-auto")

                    self.min_links_satisfied = YLeaf(YType.boolean, "min-links-satisfied")

                    self.minimum_preferred_links = YLeaf(YType.uint32, "minimum-preferred-links")

                    self.minimum_required_links = YLeaf(YType.uint32, "minimum-required-links")

                    self.number_active_links = YLeaf(YType.uint32, "number-active-links")

                    self.required_min_links_satisfied = YLeaf(YType.boolean, "required-min-links-satisfied")

                    self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                    self.vrf_id_present = YLeaf(YType.boolean, "vrf-id-present")

                    self.discovered_link = YList(self)
                    self.port_range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("conflict_context",
                                    "conflict_reason",
                                    "interface_handle",
                                    "ip_address",
                                    "ip_address_auto",
                                    "min_links_satisfied",
                                    "minimum_preferred_links",
                                    "minimum_required_links",
                                    "number_active_links",
                                    "required_min_links_satisfied",
                                    "vrf_id",
                                    "vrf_id_present") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink, self).__setattr__(name, value)


                class PortRange(Entity):
                    """
                    Port ranges table
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\:  str
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:   :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                    
                    .. attribute:: high_port
                    
                    	High port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: low_port
                    
                    	Low port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:   :py:class:`IcpeOperPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperPort>`
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange, self).__init__()

                        self.yang_name = "port-range"
                        self.yang_parent_name = "configured-link"

                        self.conflict_context = YLeaf(YType.str, "conflict-context")

                        self.conflict_reason = YLeaf(YType.enumeration, "conflict-reason")

                        self.high_port = YLeaf(YType.uint32, "high-port")

                        self.low_port = YLeaf(YType.uint32, "low-port")

                        self.port_type = YLeaf(YType.enumeration, "port-type")

                        self.slot = YLeaf(YType.uint32, "slot")

                        self.subslot = YLeaf(YType.uint32, "subslot")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("conflict_context",
                                        "conflict_reason",
                                        "high_port",
                                        "low_port",
                                        "port_type",
                                        "slot",
                                        "subslot") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.conflict_context.is_set or
                            self.conflict_reason.is_set or
                            self.high_port.is_set or
                            self.low_port.is_set or
                            self.port_type.is_set or
                            self.slot.is_set or
                            self.subslot.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.conflict_context.yfilter != YFilter.not_set or
                            self.conflict_reason.yfilter != YFilter.not_set or
                            self.high_port.yfilter != YFilter.not_set or
                            self.low_port.yfilter != YFilter.not_set or
                            self.port_type.yfilter != YFilter.not_set or
                            self.slot.yfilter != YFilter.not_set or
                            self.subslot.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.conflict_context.is_set or self.conflict_context.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_context.get_name_leafdata())
                        if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                        if (self.high_port.is_set or self.high_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.high_port.get_name_leafdata())
                        if (self.low_port.is_set or self.low_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.low_port.get_name_leafdata())
                        if (self.port_type.is_set or self.port_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_type.get_name_leafdata())
                        if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot.get_name_leafdata())
                        if (self.subslot.is_set or self.subslot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subslot.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "conflict-context" or name == "conflict-reason" or name == "high-port" or name == "low-port" or name == "port-type" or name == "slot" or name == "subslot"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "conflict-context"):
                            self.conflict_context = value
                            self.conflict_context.value_namespace = name_space
                            self.conflict_context.value_namespace_prefix = name_space_prefix
                        if(value_path == "conflict-reason"):
                            self.conflict_reason = value
                            self.conflict_reason.value_namespace = name_space
                            self.conflict_reason.value_namespace_prefix = name_space_prefix
                        if(value_path == "high-port"):
                            self.high_port = value
                            self.high_port.value_namespace = name_space
                            self.high_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "low-port"):
                            self.low_port = value
                            self.low_port.value_namespace = name_space
                            self.low_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-type"):
                            self.port_type = value
                            self.port_type.value_namespace = name_space
                            self.port_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "slot"):
                            self.slot = value
                            self.slot.value_namespace = name_space
                            self.slot.value_namespace_prefix = name_space_prefix
                        if(value_path == "subslot"):
                            self.subslot = value
                            self.subslot.value_namespace = name_space
                            self.subslot.value_namespace_prefix = name_space_prefix


                class DiscoveredLink(Entity):
                    """
                    Discovered Links table
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\:  str
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:   :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:   :py:class:`IcpeOperDiscdLinkState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperDiscdLinkState>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink, self).__init__()

                        self.yang_name = "discovered-link"
                        self.yang_parent_name = "configured-link"

                        self.conflict_context = YLeaf(YType.str, "conflict-context")

                        self.conflict_reason = YLeaf(YType.enumeration, "conflict-reason")

                        self.interface_handle = YLeaf(YType.str, "interface-handle")

                        self.state = YLeaf(YType.enumeration, "state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("conflict_context",
                                        "conflict_reason",
                                        "interface_handle",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.conflict_context.is_set or
                            self.conflict_reason.is_set or
                            self.interface_handle.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.conflict_context.yfilter != YFilter.not_set or
                            self.conflict_reason.yfilter != YFilter.not_set or
                            self.interface_handle.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "discovered-link" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.conflict_context.is_set or self.conflict_context.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_context.get_name_leafdata())
                        if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                        if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_handle.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "conflict-context" or name == "conflict-reason" or name == "interface-handle" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "conflict-context"):
                            self.conflict_context = value
                            self.conflict_context.value_namespace = name_space
                            self.conflict_context.value_namespace_prefix = name_space_prefix
                        if(value_path == "conflict-reason"):
                            self.conflict_reason = value
                            self.conflict_reason.value_namespace = name_space
                            self.conflict_reason.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-handle"):
                            self.interface_handle = value
                            self.interface_handle.value_namespace = name_space
                            self.interface_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.discovered_link:
                        if (c.has_data()):
                            return True
                    for c in self.port_range:
                        if (c.has_data()):
                            return True
                    return (
                        self.conflict_context.is_set or
                        self.conflict_reason.is_set or
                        self.interface_handle.is_set or
                        self.ip_address.is_set or
                        self.ip_address_auto.is_set or
                        self.min_links_satisfied.is_set or
                        self.minimum_preferred_links.is_set or
                        self.minimum_required_links.is_set or
                        self.number_active_links.is_set or
                        self.required_min_links_satisfied.is_set or
                        self.vrf_id.is_set or
                        self.vrf_id_present.is_set)

                def has_operation(self):
                    for c in self.discovered_link:
                        if (c.has_operation()):
                            return True
                    for c in self.port_range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.conflict_context.yfilter != YFilter.not_set or
                        self.conflict_reason.yfilter != YFilter.not_set or
                        self.interface_handle.yfilter != YFilter.not_set or
                        self.ip_address.yfilter != YFilter.not_set or
                        self.ip_address_auto.yfilter != YFilter.not_set or
                        self.min_links_satisfied.yfilter != YFilter.not_set or
                        self.minimum_preferred_links.yfilter != YFilter.not_set or
                        self.minimum_required_links.yfilter != YFilter.not_set or
                        self.number_active_links.yfilter != YFilter.not_set or
                        self.required_min_links_satisfied.yfilter != YFilter.not_set or
                        self.vrf_id.yfilter != YFilter.not_set or
                        self.vrf_id_present.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configured-link" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.conflict_context.is_set or self.conflict_context.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conflict_context.get_name_leafdata())
                    if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                    if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_handle.get_name_leafdata())
                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address.get_name_leafdata())
                    if (self.ip_address_auto.is_set or self.ip_address_auto.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address_auto.get_name_leafdata())
                    if (self.min_links_satisfied.is_set or self.min_links_satisfied.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_links_satisfied.get_name_leafdata())
                    if (self.minimum_preferred_links.is_set or self.minimum_preferred_links.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minimum_preferred_links.get_name_leafdata())
                    if (self.minimum_required_links.is_set or self.minimum_required_links.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minimum_required_links.get_name_leafdata())
                    if (self.number_active_links.is_set or self.number_active_links.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_active_links.get_name_leafdata())
                    if (self.required_min_links_satisfied.is_set or self.required_min_links_satisfied.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.required_min_links_satisfied.get_name_leafdata())
                    if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_id.get_name_leafdata())
                    if (self.vrf_id_present.is_set or self.vrf_id_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_id_present.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "discovered-link"):
                        for c in self.discovered_link:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.discovered_link.append(c)
                        return c

                    if (child_yang_name == "port-range"):
                        for c in self.port_range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.port_range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discovered-link" or name == "port-range" or name == "conflict-context" or name == "conflict-reason" or name == "interface-handle" or name == "ip-address" or name == "ip-address-auto" or name == "min-links-satisfied" or name == "minimum-preferred-links" or name == "minimum-required-links" or name == "number-active-links" or name == "required-min-links-satisfied" or name == "vrf-id" or name == "vrf-id-present"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "conflict-context"):
                        self.conflict_context = value
                        self.conflict_context.value_namespace = name_space
                        self.conflict_context.value_namespace_prefix = name_space_prefix
                    if(value_path == "conflict-reason"):
                        self.conflict_reason = value
                        self.conflict_reason.value_namespace = name_space
                        self.conflict_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-handle"):
                        self.interface_handle = value
                        self.interface_handle.value_namespace = name_space
                        self.interface_handle.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address"):
                        self.ip_address = value
                        self.ip_address.value_namespace = name_space
                        self.ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address-auto"):
                        self.ip_address_auto = value
                        self.ip_address_auto.value_namespace = name_space
                        self.ip_address_auto.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-links-satisfied"):
                        self.min_links_satisfied = value
                        self.min_links_satisfied.value_namespace = name_space
                        self.min_links_satisfied.value_namespace_prefix = name_space_prefix
                    if(value_path == "minimum-preferred-links"):
                        self.minimum_preferred_links = value
                        self.minimum_preferred_links.value_namespace = name_space
                        self.minimum_preferred_links.value_namespace_prefix = name_space_prefix
                    if(value_path == "minimum-required-links"):
                        self.minimum_required_links = value
                        self.minimum_required_links.value_namespace = name_space
                        self.minimum_required_links.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-active-links"):
                        self.number_active_links = value
                        self.number_active_links.value_namespace = name_space
                        self.number_active_links.value_namespace_prefix = name_space_prefix
                    if(value_path == "required-min-links-satisfied"):
                        self.required_min_links_satisfied = value
                        self.required_min_links_satisfied.value_namespace = name_space
                        self.required_min_links_satisfied.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-id"):
                        self.vrf_id = value
                        self.vrf_id.value_namespace = name_space
                        self.vrf_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-id-present"):
                        self.vrf_id_present = value
                        self.vrf_id_present.value_namespace = name_space
                        self.vrf_id_present.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.configured_link:
                    if (c.has_data()):
                        return True
                for leaf in self.remote_version.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.satellite_id.is_set or
                    self.cfgd_timeout.is_set or
                    self.configured_serial_number.is_set or
                    self.configured_serial_number_present.is_set or
                    self.conflict_context.is_set or
                    self.conflict_reason.is_set or
                    self.description.is_set or
                    self.description_present.is_set or
                    self.ethernet_fabric_supported.is_set or
                    self.host_treating_as_active.is_set or
                    self.install_state.is_set or
                    self.ip_address.is_set or
                    self.ip_address_auto.is_set or
                    self.ip_address_present.is_set or
                    self.ipv6_address.is_set or
                    self.ipv6_address_present.is_set or
                    self.mac_address.is_set or
                    self.mac_address_present.is_set or
                    self.optical_supported.is_set or
                    self.password.is_set or
                    self.password_error.is_set or
                    self.received_host_name.is_set or
                    self.received_serial_number.is_set or
                    self.received_serial_number_present.is_set or
                    self.recovery_delay_time_left.is_set or
                    self.redundancy_iccp_group.is_set or
                    self.remote_version_present.is_set or
                    self.satellite_id_xr.is_set or
                    self.satellite_treating_as_active.is_set or
                    self.sdacp_session_failure_reason.is_set or
                    self.sdacp_session_state.is_set or
                    self.timeout_warning.is_set or
                    self.type.is_set or
                    self.version_check_state.is_set or
                    self.vrf_name.is_set or
                    self.vrfid.is_set or
                    (self.candidate_fabric_ports is not None and self.candidate_fabric_ports.has_data()) or
                    (self.optical_status is not None and self.optical_status.has_data()) or
                    (self.redundancy_out_of_sync_timestamp is not None and self.redundancy_out_of_sync_timestamp.has_data()))

            def has_operation(self):
                for c in self.configured_link:
                    if (c.has_operation()):
                        return True
                for leaf in self.remote_version.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.satellite_id.yfilter != YFilter.not_set or
                    self.cfgd_timeout.yfilter != YFilter.not_set or
                    self.configured_serial_number.yfilter != YFilter.not_set or
                    self.configured_serial_number_present.yfilter != YFilter.not_set or
                    self.conflict_context.yfilter != YFilter.not_set or
                    self.conflict_reason.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.description_present.yfilter != YFilter.not_set or
                    self.ethernet_fabric_supported.yfilter != YFilter.not_set or
                    self.host_treating_as_active.yfilter != YFilter.not_set or
                    self.install_state.yfilter != YFilter.not_set or
                    self.ip_address.yfilter != YFilter.not_set or
                    self.ip_address_auto.yfilter != YFilter.not_set or
                    self.ip_address_present.yfilter != YFilter.not_set or
                    self.ipv6_address.yfilter != YFilter.not_set or
                    self.ipv6_address_present.yfilter != YFilter.not_set or
                    self.mac_address.yfilter != YFilter.not_set or
                    self.mac_address_present.yfilter != YFilter.not_set or
                    self.optical_supported.yfilter != YFilter.not_set or
                    self.password.yfilter != YFilter.not_set or
                    self.password_error.yfilter != YFilter.not_set or
                    self.received_host_name.yfilter != YFilter.not_set or
                    self.received_serial_number.yfilter != YFilter.not_set or
                    self.received_serial_number_present.yfilter != YFilter.not_set or
                    self.recovery_delay_time_left.yfilter != YFilter.not_set or
                    self.redundancy_iccp_group.yfilter != YFilter.not_set or
                    self.remote_version.yfilter != YFilter.not_set or
                    self.remote_version_present.yfilter != YFilter.not_set or
                    self.satellite_id_xr.yfilter != YFilter.not_set or
                    self.satellite_treating_as_active.yfilter != YFilter.not_set or
                    self.sdacp_session_failure_reason.yfilter != YFilter.not_set or
                    self.sdacp_session_state.yfilter != YFilter.not_set or
                    self.timeout_warning.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.version_check_state.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.vrfid.yfilter != YFilter.not_set or
                    (self.candidate_fabric_ports is not None and self.candidate_fabric_ports.has_operation()) or
                    (self.optical_status is not None and self.optical_status.has_operation()) or
                    (self.redundancy_out_of_sync_timestamp is not None and self.redundancy_out_of_sync_timestamp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "satellite-status" + "[satellite-id='" + self.satellite_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-statuses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id.get_name_leafdata())
                if (self.cfgd_timeout.is_set or self.cfgd_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfgd_timeout.get_name_leafdata())
                if (self.configured_serial_number.is_set or self.configured_serial_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configured_serial_number.get_name_leafdata())
                if (self.configured_serial_number_present.is_set or self.configured_serial_number_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configured_serial_number_present.get_name_leafdata())
                if (self.conflict_context.is_set or self.conflict_context.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.conflict_context.get_name_leafdata())
                if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.description_present.is_set or self.description_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description_present.get_name_leafdata())
                if (self.ethernet_fabric_supported.is_set or self.ethernet_fabric_supported.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ethernet_fabric_supported.get_name_leafdata())
                if (self.host_treating_as_active.is_set or self.host_treating_as_active.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_treating_as_active.get_name_leafdata())
                if (self.install_state.is_set or self.install_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.install_state.get_name_leafdata())
                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip_address.get_name_leafdata())
                if (self.ip_address_auto.is_set or self.ip_address_auto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip_address_auto.get_name_leafdata())
                if (self.ip_address_present.is_set or self.ip_address_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip_address_present.get_name_leafdata())
                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                if (self.ipv6_address_present.is_set or self.ipv6_address_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6_address_present.get_name_leafdata())
                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                if (self.mac_address_present.is_set or self.mac_address_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_address_present.get_name_leafdata())
                if (self.optical_supported.is_set or self.optical_supported.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.optical_supported.get_name_leafdata())
                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.password.get_name_leafdata())
                if (self.password_error.is_set or self.password_error.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.password_error.get_name_leafdata())
                if (self.received_host_name.is_set or self.received_host_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_host_name.get_name_leafdata())
                if (self.received_serial_number.is_set or self.received_serial_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_serial_number.get_name_leafdata())
                if (self.received_serial_number_present.is_set or self.received_serial_number_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_serial_number_present.get_name_leafdata())
                if (self.recovery_delay_time_left.is_set or self.recovery_delay_time_left.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.recovery_delay_time_left.get_name_leafdata())
                if (self.redundancy_iccp_group.is_set or self.redundancy_iccp_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.redundancy_iccp_group.get_name_leafdata())
                if (self.remote_version_present.is_set or self.remote_version_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_version_present.get_name_leafdata())
                if (self.satellite_id_xr.is_set or self.satellite_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id_xr.get_name_leafdata())
                if (self.satellite_treating_as_active.is_set or self.satellite_treating_as_active.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_treating_as_active.get_name_leafdata())
                if (self.sdacp_session_failure_reason.is_set or self.sdacp_session_failure_reason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sdacp_session_failure_reason.get_name_leafdata())
                if (self.sdacp_session_state.is_set or self.sdacp_session_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sdacp_session_state.get_name_leafdata())
                if (self.timeout_warning.is_set or self.timeout_warning.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout_warning.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.version_check_state.is_set or self.version_check_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version_check_state.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.vrfid.is_set or self.vrfid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrfid.get_name_leafdata())

                leaf_name_data.extend(self.remote_version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "candidate-fabric-ports"):
                    if (self.candidate_fabric_ports is None):
                        self.candidate_fabric_ports = NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts()
                        self.candidate_fabric_ports.parent = self
                        self._children_name_map["candidate_fabric_ports"] = "candidate-fabric-ports"
                    return self.candidate_fabric_ports

                if (child_yang_name == "configured-link"):
                    for c in self.configured_link:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.configured_link.append(c)
                    return c

                if (child_yang_name == "optical-status"):
                    if (self.optical_status is None):
                        self.optical_status = NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus()
                        self.optical_status.parent = self
                        self._children_name_map["optical_status"] = "optical-status"
                    return self.optical_status

                if (child_yang_name == "redundancy-out-of-sync-timestamp"):
                    if (self.redundancy_out_of_sync_timestamp is None):
                        self.redundancy_out_of_sync_timestamp = NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp()
                        self.redundancy_out_of_sync_timestamp.parent = self
                        self._children_name_map["redundancy_out_of_sync_timestamp"] = "redundancy-out-of-sync-timestamp"
                    return self.redundancy_out_of_sync_timestamp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate-fabric-ports" or name == "configured-link" or name == "optical-status" or name == "redundancy-out-of-sync-timestamp" or name == "satellite-id" or name == "cfgd-timeout" or name == "configured-serial-number" or name == "configured-serial-number-present" or name == "conflict-context" or name == "conflict-reason" or name == "description" or name == "description-present" or name == "ethernet-fabric-supported" or name == "host-treating-as-active" or name == "install-state" or name == "ip-address" or name == "ip-address-auto" or name == "ip-address-present" or name == "ipv6-address" or name == "ipv6-address-present" or name == "mac-address" or name == "mac-address-present" or name == "optical-supported" or name == "password" or name == "password-error" or name == "received-host-name" or name == "received-serial-number" or name == "received-serial-number-present" or name == "recovery-delay-time-left" or name == "redundancy-iccp-group" or name == "remote-version" or name == "remote-version-present" or name == "satellite-id-xr" or name == "satellite-treating-as-active" or name == "sdacp-session-failure-reason" or name == "sdacp-session-state" or name == "timeout-warning" or name == "type" or name == "version-check-state" or name == "vrf-name" or name == "vrfid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "satellite-id"):
                    self.satellite_id = value
                    self.satellite_id.value_namespace = name_space
                    self.satellite_id.value_namespace_prefix = name_space_prefix
                if(value_path == "cfgd-timeout"):
                    self.cfgd_timeout = value
                    self.cfgd_timeout.value_namespace = name_space
                    self.cfgd_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "configured-serial-number"):
                    self.configured_serial_number = value
                    self.configured_serial_number.value_namespace = name_space
                    self.configured_serial_number.value_namespace_prefix = name_space_prefix
                if(value_path == "configured-serial-number-present"):
                    self.configured_serial_number_present = value
                    self.configured_serial_number_present.value_namespace = name_space
                    self.configured_serial_number_present.value_namespace_prefix = name_space_prefix
                if(value_path == "conflict-context"):
                    self.conflict_context = value
                    self.conflict_context.value_namespace = name_space
                    self.conflict_context.value_namespace_prefix = name_space_prefix
                if(value_path == "conflict-reason"):
                    self.conflict_reason = value
                    self.conflict_reason.value_namespace = name_space
                    self.conflict_reason.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "description-present"):
                    self.description_present = value
                    self.description_present.value_namespace = name_space
                    self.description_present.value_namespace_prefix = name_space_prefix
                if(value_path == "ethernet-fabric-supported"):
                    self.ethernet_fabric_supported = value
                    self.ethernet_fabric_supported.value_namespace = name_space
                    self.ethernet_fabric_supported.value_namespace_prefix = name_space_prefix
                if(value_path == "host-treating-as-active"):
                    self.host_treating_as_active = value
                    self.host_treating_as_active.value_namespace = name_space
                    self.host_treating_as_active.value_namespace_prefix = name_space_prefix
                if(value_path == "install-state"):
                    self.install_state = value
                    self.install_state.value_namespace = name_space
                    self.install_state.value_namespace_prefix = name_space_prefix
                if(value_path == "ip-address"):
                    self.ip_address = value
                    self.ip_address.value_namespace = name_space
                    self.ip_address.value_namespace_prefix = name_space_prefix
                if(value_path == "ip-address-auto"):
                    self.ip_address_auto = value
                    self.ip_address_auto.value_namespace = name_space
                    self.ip_address_auto.value_namespace_prefix = name_space_prefix
                if(value_path == "ip-address-present"):
                    self.ip_address_present = value
                    self.ip_address_present.value_namespace = name_space
                    self.ip_address_present.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6-address"):
                    self.ipv6_address = value
                    self.ipv6_address.value_namespace = name_space
                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6-address-present"):
                    self.ipv6_address_present = value
                    self.ipv6_address_present.value_namespace = name_space
                    self.ipv6_address_present.value_namespace_prefix = name_space_prefix
                if(value_path == "mac-address"):
                    self.mac_address = value
                    self.mac_address.value_namespace = name_space
                    self.mac_address.value_namespace_prefix = name_space_prefix
                if(value_path == "mac-address-present"):
                    self.mac_address_present = value
                    self.mac_address_present.value_namespace = name_space
                    self.mac_address_present.value_namespace_prefix = name_space_prefix
                if(value_path == "optical-supported"):
                    self.optical_supported = value
                    self.optical_supported.value_namespace = name_space
                    self.optical_supported.value_namespace_prefix = name_space_prefix
                if(value_path == "password"):
                    self.password = value
                    self.password.value_namespace = name_space
                    self.password.value_namespace_prefix = name_space_prefix
                if(value_path == "password-error"):
                    self.password_error = value
                    self.password_error.value_namespace = name_space
                    self.password_error.value_namespace_prefix = name_space_prefix
                if(value_path == "received-host-name"):
                    self.received_host_name = value
                    self.received_host_name.value_namespace = name_space
                    self.received_host_name.value_namespace_prefix = name_space_prefix
                if(value_path == "received-serial-number"):
                    self.received_serial_number = value
                    self.received_serial_number.value_namespace = name_space
                    self.received_serial_number.value_namespace_prefix = name_space_prefix
                if(value_path == "received-serial-number-present"):
                    self.received_serial_number_present = value
                    self.received_serial_number_present.value_namespace = name_space
                    self.received_serial_number_present.value_namespace_prefix = name_space_prefix
                if(value_path == "recovery-delay-time-left"):
                    self.recovery_delay_time_left = value
                    self.recovery_delay_time_left.value_namespace = name_space
                    self.recovery_delay_time_left.value_namespace_prefix = name_space_prefix
                if(value_path == "redundancy-iccp-group"):
                    self.redundancy_iccp_group = value
                    self.redundancy_iccp_group.value_namespace = name_space
                    self.redundancy_iccp_group.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-version"):
                    self.remote_version.append(value)
                if(value_path == "remote-version-present"):
                    self.remote_version_present = value
                    self.remote_version_present.value_namespace = name_space
                    self.remote_version_present.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-id-xr"):
                    self.satellite_id_xr = value
                    self.satellite_id_xr.value_namespace = name_space
                    self.satellite_id_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-treating-as-active"):
                    self.satellite_treating_as_active = value
                    self.satellite_treating_as_active.value_namespace = name_space
                    self.satellite_treating_as_active.value_namespace_prefix = name_space_prefix
                if(value_path == "sdacp-session-failure-reason"):
                    self.sdacp_session_failure_reason = value
                    self.sdacp_session_failure_reason.value_namespace = name_space
                    self.sdacp_session_failure_reason.value_namespace_prefix = name_space_prefix
                if(value_path == "sdacp-session-state"):
                    self.sdacp_session_state = value
                    self.sdacp_session_state.value_namespace = name_space
                    self.sdacp_session_state.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout-warning"):
                    self.timeout_warning = value
                    self.timeout_warning.value_namespace = name_space
                    self.timeout_warning.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "version-check-state"):
                    self.version_check_state = value
                    self.version_check_state.value_namespace = name_space
                    self.version_check_state.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrfid"):
                    self.vrfid = value
                    self.vrfid.value_namespace = name_space
                    self.vrfid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.satellite_status:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.satellite_status:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "satellite-statuses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "satellite-status"):
                for c in self.satellite_status:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SatelliteStatuses.SatelliteStatus()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.satellite_status.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "satellite-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SatellitePriorities(Entity):
        """
        Satellite priority information table
        
        .. attribute:: satellite_priority
        
        	Satellite priority information
        	**type**\: list of    :py:class:`SatellitePriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatellitePriorities.SatellitePriority>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatellitePriorities, self).__init__()

            self.yang_name = "satellite-priorities"
            self.yang_parent_name = "nv-satellite"

            self.satellite_priority = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SatellitePriorities, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SatellitePriorities, self).__setattr__(name, value)


        class SatellitePriority(Entity):
            """
            Satellite priority information
            
            .. attribute:: satellite_id  <key>
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: best_path_hops
            
            	Best path hops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: configured_priority
            
            	Configured priority
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: host_priority
            
            	Host priority
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: multichassis_redundancy
            
            	Multichassis redundancy
            	**type**\:   :py:class:`IcpeOperMultichassisRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperMultichassisRedundancy>`
            
            .. attribute:: partner_priority
            
            	Partner priority
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rgid
            
            	RG ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatellitePriorities.SatellitePriority, self).__init__()

                self.yang_name = "satellite-priority"
                self.yang_parent_name = "satellite-priorities"

                self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                self.best_path_hops = YLeaf(YType.uint32, "best-path-hops")

                self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                self.host_priority = YLeaf(YType.uint64, "host-priority")

                self.multichassis_redundancy = YLeaf(YType.enumeration, "multichassis-redundancy")

                self.partner_priority = YLeaf(YType.uint64, "partner-priority")

                self.rgid = YLeaf(YType.uint32, "rgid")

                self.satellite_id_xr = YLeaf(YType.uint32, "satellite-id-xr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("satellite_id",
                                "best_path_hops",
                                "configured_priority",
                                "host_priority",
                                "multichassis_redundancy",
                                "partner_priority",
                                "rgid",
                                "satellite_id_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SatellitePriorities.SatellitePriority, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SatellitePriorities.SatellitePriority, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.satellite_id.is_set or
                    self.best_path_hops.is_set or
                    self.configured_priority.is_set or
                    self.host_priority.is_set or
                    self.multichassis_redundancy.is_set or
                    self.partner_priority.is_set or
                    self.rgid.is_set or
                    self.satellite_id_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.satellite_id.yfilter != YFilter.not_set or
                    self.best_path_hops.yfilter != YFilter.not_set or
                    self.configured_priority.yfilter != YFilter.not_set or
                    self.host_priority.yfilter != YFilter.not_set or
                    self.multichassis_redundancy.yfilter != YFilter.not_set or
                    self.partner_priority.yfilter != YFilter.not_set or
                    self.rgid.yfilter != YFilter.not_set or
                    self.satellite_id_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "satellite-priority" + "[satellite-id='" + self.satellite_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-priorities/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id.get_name_leafdata())
                if (self.best_path_hops.is_set or self.best_path_hops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.best_path_hops.get_name_leafdata())
                if (self.configured_priority.is_set or self.configured_priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configured_priority.get_name_leafdata())
                if (self.host_priority.is_set or self.host_priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_priority.get_name_leafdata())
                if (self.multichassis_redundancy.is_set or self.multichassis_redundancy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multichassis_redundancy.get_name_leafdata())
                if (self.partner_priority.is_set or self.partner_priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.partner_priority.get_name_leafdata())
                if (self.rgid.is_set or self.rgid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rgid.get_name_leafdata())
                if (self.satellite_id_xr.is_set or self.satellite_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "satellite-id" or name == "best-path-hops" or name == "configured-priority" or name == "host-priority" or name == "multichassis-redundancy" or name == "partner-priority" or name == "rgid" or name == "satellite-id-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "satellite-id"):
                    self.satellite_id = value
                    self.satellite_id.value_namespace = name_space
                    self.satellite_id.value_namespace_prefix = name_space_prefix
                if(value_path == "best-path-hops"):
                    self.best_path_hops = value
                    self.best_path_hops.value_namespace = name_space
                    self.best_path_hops.value_namespace_prefix = name_space_prefix
                if(value_path == "configured-priority"):
                    self.configured_priority = value
                    self.configured_priority.value_namespace = name_space
                    self.configured_priority.value_namespace_prefix = name_space_prefix
                if(value_path == "host-priority"):
                    self.host_priority = value
                    self.host_priority.value_namespace = name_space
                    self.host_priority.value_namespace_prefix = name_space_prefix
                if(value_path == "multichassis-redundancy"):
                    self.multichassis_redundancy = value
                    self.multichassis_redundancy.value_namespace = name_space
                    self.multichassis_redundancy.value_namespace_prefix = name_space_prefix
                if(value_path == "partner-priority"):
                    self.partner_priority = value
                    self.partner_priority.value_namespace = name_space
                    self.partner_priority.value_namespace_prefix = name_space_prefix
                if(value_path == "rgid"):
                    self.rgid = value
                    self.rgid.value_namespace = name_space
                    self.rgid.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-id-xr"):
                    self.satellite_id_xr = value
                    self.satellite_id_xr.value_namespace = name_space
                    self.satellite_id_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.satellite_priority:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.satellite_priority:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "satellite-priorities" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "satellite-priority"):
                for c in self.satellite_priority:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SatellitePriorities.SatellitePriority()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.satellite_priority.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "satellite-priority"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SatelliteVersions(Entity):
        """
        Satellite remote version information table
        
        .. attribute:: satellite_version
        
        	Satellite remote version information
        	**type**\: list of    :py:class:`SatelliteVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteVersions, self).__init__()

            self.yang_name = "satellite-versions"
            self.yang_parent_name = "nv-satellite"

            self.satellite_version = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SatelliteVersions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SatelliteVersions, self).__setattr__(name, value)


        class SatelliteVersion(Entity):
            """
            Satellite remote version information
            
            .. attribute:: satellite_id  <key>
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: active_version
            
            	Satellite active version information
            	**type**\:   :py:class:`ActiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion>`
            
            .. attribute:: committed_version
            
            	Satellite committed version information
            	**type**\:   :py:class:`CommittedVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion>`
            
            .. attribute:: remote_version
            
            	Remote version
            	**type**\:  list of str
            
            .. attribute:: remote_version_present
            
            	Remote version present
            	**type**\:  bool
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: transferred_version
            
            	Satellite transferred version information
            	**type**\:   :py:class:`TransferredVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion>`
            
            .. attribute:: version_check_state
            
            	Version check state
            	**type**\:   :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteVersions.SatelliteVersion, self).__init__()

                self.yang_name = "satellite-version"
                self.yang_parent_name = "satellite-versions"

                self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                self.remote_version = YLeafList(YType.str, "remote-version")

                self.remote_version_present = YLeaf(YType.boolean, "remote-version-present")

                self.satellite_id_xr = YLeaf(YType.uint32, "satellite-id-xr")

                self.version_check_state = YLeaf(YType.enumeration, "version-check-state")

                self.active_version = NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion()
                self.active_version.parent = self
                self._children_name_map["active_version"] = "active-version"
                self._children_yang_names.add("active-version")

                self.committed_version = NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion()
                self.committed_version.parent = self
                self._children_name_map["committed_version"] = "committed-version"
                self._children_yang_names.add("committed-version")

                self.transferred_version = NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion()
                self.transferred_version.parent = self
                self._children_name_map["transferred_version"] = "transferred-version"
                self._children_yang_names.add("transferred-version")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("satellite_id",
                                "remote_version",
                                "remote_version_present",
                                "satellite_id_xr",
                                "version_check_state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SatelliteVersions.SatelliteVersion, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SatelliteVersions.SatelliteVersion, self).__setattr__(name, value)


            class ActiveVersion(Entity):
                """
                Satellite active version information
                
                .. attribute:: remote_version
                
                	Remote version
                	**type**\:  list of str
                
                .. attribute:: remote_version_present
                
                	Remote version present
                	**type**\:  bool
                
                .. attribute:: version_check_state
                
                	Version check state
                	**type**\:   :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion, self).__init__()

                    self.yang_name = "active-version"
                    self.yang_parent_name = "satellite-version"

                    self.remote_version = YLeafList(YType.str, "remote-version")

                    self.remote_version_present = YLeaf(YType.boolean, "remote-version-present")

                    self.version_check_state = YLeaf(YType.enumeration, "version-check-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("remote_version",
                                    "remote_version_present",
                                    "version_check_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.remote_version.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.remote_version_present.is_set or
                        self.version_check_state.is_set)

                def has_operation(self):
                    for leaf in self.remote_version.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.remote_version.yfilter != YFilter.not_set or
                        self.remote_version_present.yfilter != YFilter.not_set or
                        self.version_check_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "active-version" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.remote_version_present.is_set or self.remote_version_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_version_present.get_name_leafdata())
                    if (self.version_check_state.is_set or self.version_check_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version_check_state.get_name_leafdata())

                    leaf_name_data.extend(self.remote_version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-version" or name == "remote-version-present" or name == "version-check-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "remote-version"):
                        self.remote_version.append(value)
                    if(value_path == "remote-version-present"):
                        self.remote_version_present = value
                        self.remote_version_present.value_namespace = name_space
                        self.remote_version_present.value_namespace_prefix = name_space_prefix
                    if(value_path == "version-check-state"):
                        self.version_check_state = value
                        self.version_check_state.value_namespace = name_space
                        self.version_check_state.value_namespace_prefix = name_space_prefix


            class TransferredVersion(Entity):
                """
                Satellite transferred version information
                
                .. attribute:: remote_version
                
                	Remote version
                	**type**\:  list of str
                
                .. attribute:: remote_version_present
                
                	Remote version present
                	**type**\:  bool
                
                .. attribute:: version_check_state
                
                	Version check state
                	**type**\:   :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion, self).__init__()

                    self.yang_name = "transferred-version"
                    self.yang_parent_name = "satellite-version"

                    self.remote_version = YLeafList(YType.str, "remote-version")

                    self.remote_version_present = YLeaf(YType.boolean, "remote-version-present")

                    self.version_check_state = YLeaf(YType.enumeration, "version-check-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("remote_version",
                                    "remote_version_present",
                                    "version_check_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.remote_version.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.remote_version_present.is_set or
                        self.version_check_state.is_set)

                def has_operation(self):
                    for leaf in self.remote_version.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.remote_version.yfilter != YFilter.not_set or
                        self.remote_version_present.yfilter != YFilter.not_set or
                        self.version_check_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transferred-version" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.remote_version_present.is_set or self.remote_version_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_version_present.get_name_leafdata())
                    if (self.version_check_state.is_set or self.version_check_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version_check_state.get_name_leafdata())

                    leaf_name_data.extend(self.remote_version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-version" or name == "remote-version-present" or name == "version-check-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "remote-version"):
                        self.remote_version.append(value)
                    if(value_path == "remote-version-present"):
                        self.remote_version_present = value
                        self.remote_version_present.value_namespace = name_space
                        self.remote_version_present.value_namespace_prefix = name_space_prefix
                    if(value_path == "version-check-state"):
                        self.version_check_state = value
                        self.version_check_state.value_namespace = name_space
                        self.version_check_state.value_namespace_prefix = name_space_prefix


            class CommittedVersion(Entity):
                """
                Satellite committed version information
                
                .. attribute:: remote_version
                
                	Remote version
                	**type**\:  list of str
                
                .. attribute:: remote_version_present
                
                	Remote version present
                	**type**\:  bool
                
                .. attribute:: version_check_state
                
                	Version check state
                	**type**\:   :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion, self).__init__()

                    self.yang_name = "committed-version"
                    self.yang_parent_name = "satellite-version"

                    self.remote_version = YLeafList(YType.str, "remote-version")

                    self.remote_version_present = YLeaf(YType.boolean, "remote-version-present")

                    self.version_check_state = YLeaf(YType.enumeration, "version-check-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("remote_version",
                                    "remote_version_present",
                                    "version_check_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.remote_version.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.remote_version_present.is_set or
                        self.version_check_state.is_set)

                def has_operation(self):
                    for leaf in self.remote_version.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.remote_version.yfilter != YFilter.not_set or
                        self.remote_version_present.yfilter != YFilter.not_set or
                        self.version_check_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "committed-version" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.remote_version_present.is_set or self.remote_version_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_version_present.get_name_leafdata())
                    if (self.version_check_state.is_set or self.version_check_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version_check_state.get_name_leafdata())

                    leaf_name_data.extend(self.remote_version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-version" or name == "remote-version-present" or name == "version-check-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "remote-version"):
                        self.remote_version.append(value)
                    if(value_path == "remote-version-present"):
                        self.remote_version_present = value
                        self.remote_version_present.value_namespace = name_space
                        self.remote_version_present.value_namespace_prefix = name_space_prefix
                    if(value_path == "version-check-state"):
                        self.version_check_state = value
                        self.version_check_state.value_namespace = name_space
                        self.version_check_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for leaf in self.remote_version.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.satellite_id.is_set or
                    self.remote_version_present.is_set or
                    self.satellite_id_xr.is_set or
                    self.version_check_state.is_set or
                    (self.active_version is not None and self.active_version.has_data()) or
                    (self.committed_version is not None and self.committed_version.has_data()) or
                    (self.transferred_version is not None and self.transferred_version.has_data()))

            def has_operation(self):
                for leaf in self.remote_version.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.satellite_id.yfilter != YFilter.not_set or
                    self.remote_version.yfilter != YFilter.not_set or
                    self.remote_version_present.yfilter != YFilter.not_set or
                    self.satellite_id_xr.yfilter != YFilter.not_set or
                    self.version_check_state.yfilter != YFilter.not_set or
                    (self.active_version is not None and self.active_version.has_operation()) or
                    (self.committed_version is not None and self.committed_version.has_operation()) or
                    (self.transferred_version is not None and self.transferred_version.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "satellite-version" + "[satellite-id='" + self.satellite_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-versions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id.get_name_leafdata())
                if (self.remote_version_present.is_set or self.remote_version_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_version_present.get_name_leafdata())
                if (self.satellite_id_xr.is_set or self.satellite_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id_xr.get_name_leafdata())
                if (self.version_check_state.is_set or self.version_check_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version_check_state.get_name_leafdata())

                leaf_name_data.extend(self.remote_version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "active-version"):
                    if (self.active_version is None):
                        self.active_version = NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion()
                        self.active_version.parent = self
                        self._children_name_map["active_version"] = "active-version"
                    return self.active_version

                if (child_yang_name == "committed-version"):
                    if (self.committed_version is None):
                        self.committed_version = NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion()
                        self.committed_version.parent = self
                        self._children_name_map["committed_version"] = "committed-version"
                    return self.committed_version

                if (child_yang_name == "transferred-version"):
                    if (self.transferred_version is None):
                        self.transferred_version = NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion()
                        self.transferred_version.parent = self
                        self._children_name_map["transferred_version"] = "transferred-version"
                    return self.transferred_version

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active-version" or name == "committed-version" or name == "transferred-version" or name == "satellite-id" or name == "remote-version" or name == "remote-version-present" or name == "satellite-id-xr" or name == "version-check-state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "satellite-id"):
                    self.satellite_id = value
                    self.satellite_id.value_namespace = name_space
                    self.satellite_id.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-version"):
                    self.remote_version.append(value)
                if(value_path == "remote-version-present"):
                    self.remote_version_present = value
                    self.remote_version_present.value_namespace = name_space
                    self.remote_version_present.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-id-xr"):
                    self.satellite_id_xr = value
                    self.satellite_id_xr.value_namespace = name_space
                    self.satellite_id_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "version-check-state"):
                    self.version_check_state = value
                    self.version_check_state.value_namespace = name_space
                    self.version_check_state.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.satellite_version:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.satellite_version:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "satellite-versions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "satellite-version"):
                for c in self.satellite_version:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SatelliteVersions.SatelliteVersion()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.satellite_version.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "satellite-version"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SatelliteTopologies(Entity):
        """
        Satellite Topology Information table
        
        .. attribute:: satellite_topology
        
        	Satellite Topology Information
        	**type**\: list of    :py:class:`SatelliteTopology <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteTopologies, self).__init__()

            self.yang_name = "satellite-topologies"
            self.yang_parent_name = "nv-satellite"

            self.satellite_topology = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SatelliteTopologies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SatelliteTopologies, self).__setattr__(name, value)


        class SatelliteTopology(Entity):
            """
            Satellite Topology Information
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: discovered_link
            
            	Discovered Links table
            	**type**\: list of    :py:class:`DiscoveredLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink>`
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: is_physical
            
            	Is physical
            	**type**\:  bool
            
            .. attribute:: redundancy_iccp_group
            
            	Redundancy ICCP group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ring_whole
            
            	Ring whole
            	**type**\:  bool
            
            .. attribute:: satellite
            
            	Satellite table
            	**type**\: list of    :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteTopologies.SatelliteTopology, self).__init__()

                self.yang_name = "satellite-topology"
                self.yang_parent_name = "satellite-topologies"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_handle = YLeaf(YType.str, "interface-handle")

                self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                self.is_physical = YLeaf(YType.boolean, "is-physical")

                self.redundancy_iccp_group = YLeaf(YType.uint32, "redundancy-iccp-group")

                self.ring_whole = YLeaf(YType.boolean, "ring-whole")

                self.discovered_link = YList(self)
                self.satellite = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "interface_handle",
                                "interface_name_xr",
                                "is_physical",
                                "redundancy_iccp_group",
                                "ring_whole") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SatelliteTopologies.SatelliteTopology, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SatelliteTopologies.SatelliteTopology, self).__setattr__(name, value)


            class DiscoveredLink(Entity):
                """
                Discovered Links table
                
                .. attribute:: discovery_running
                
                	Discovery running
                	**type**\:  bool
                
                .. attribute:: interface_handle
                
                	Interface handle
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink, self).__init__()

                    self.yang_name = "discovered-link"
                    self.yang_parent_name = "satellite-topology"

                    self.discovery_running = YLeaf(YType.boolean, "discovery-running")

                    self.interface_handle = YLeaf(YType.str, "interface-handle")

                    self.interface_name = YLeaf(YType.str, "interface-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discovery_running",
                                    "interface_handle",
                                    "interface_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.discovery_running.is_set or
                        self.interface_handle.is_set or
                        self.interface_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discovery_running.yfilter != YFilter.not_set or
                        self.interface_handle.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "discovered-link" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discovery_running.is_set or self.discovery_running.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discovery_running.get_name_leafdata())
                    if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_handle.get_name_leafdata())
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discovery-running" or name == "interface-handle" or name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discovery-running"):
                        self.discovery_running = value
                        self.discovery_running.value_namespace = name_space
                        self.discovery_running.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-handle"):
                        self.interface_handle = value
                        self.interface_handle.value_namespace = name_space
                        self.interface_handle.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix


            class Satellite(Entity):
                """
                Satellite table
                
                .. attribute:: configured
                
                	Configured
                	**type**\:  bool
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\:  str
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:   :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                
                .. attribute:: display_name
                
                	Display name
                	**type**\:  str
                
                .. attribute:: fabric_link
                
                	Local Satellite Fabric Link table
                	**type**\: list of    :py:class:`FabricLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink>`
                
                .. attribute:: mac_address
                
                	MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: num_hops
                
                	Num hops
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: received_serial_number
                
                	Received serial number
                	**type**\:  str
                
                .. attribute:: received_serial_number_present
                
                	Received serial number present
                	**type**\:  bool
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Type
                	**type**\:  str
                
                .. attribute:: vlan_id
                
                	VLAN ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "satellite-topology"

                    self.configured = YLeaf(YType.boolean, "configured")

                    self.conflict_context = YLeaf(YType.str, "conflict-context")

                    self.conflict_reason = YLeaf(YType.enumeration, "conflict-reason")

                    self.display_name = YLeaf(YType.str, "display-name")

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.num_hops = YLeaf(YType.uint16, "num-hops")

                    self.received_serial_number = YLeaf(YType.str, "received-serial-number")

                    self.received_serial_number_present = YLeaf(YType.boolean, "received-serial-number-present")

                    self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                    self.type = YLeaf(YType.str, "type")

                    self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                    self.fabric_link = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("configured",
                                    "conflict_context",
                                    "conflict_reason",
                                    "display_name",
                                    "mac_address",
                                    "num_hops",
                                    "received_serial_number",
                                    "received_serial_number_present",
                                    "satellite_id",
                                    "type",
                                    "vlan_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite, self).__setattr__(name, value)


                class FabricLink(Entity):
                    """
                    Local Satellite Fabric Link table
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\:  bool
                    
                    .. attribute:: display_name
                    
                    	Display name
                    	**type**\:  str
                    
                    .. attribute:: icl_id
                    
                    	ICL ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: obsolete
                    
                    	Obsolete
                    	**type**\:  bool
                    
                    .. attribute:: redundant
                    
                    	Redundant
                    	**type**\:  bool
                    
                    .. attribute:: remote_device
                    
                    	Remote Device table
                    	**type**\: list of    :py:class:`RemoteDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink, self).__init__()

                        self.yang_name = "fabric-link"
                        self.yang_parent_name = "satellite"

                        self.active = YLeaf(YType.boolean, "active")

                        self.display_name = YLeaf(YType.str, "display-name")

                        self.icl_id = YLeaf(YType.uint32, "icl-id")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.obsolete = YLeaf(YType.boolean, "obsolete")

                        self.redundant = YLeaf(YType.boolean, "redundant")

                        self.remote_device = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active",
                                        "display_name",
                                        "icl_id",
                                        "interface_name",
                                        "obsolete",
                                        "redundant") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink, self).__setattr__(name, value)


                    class RemoteDevice(Entity):
                        """
                        Remote Device table
                        
                        .. attribute:: icl_id
                        
                        	ICL ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  str
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: remote_is_local_host
                        
                        	Remote is local host
                        	**type**\:  bool
                        
                        .. attribute:: remote_is_satellite
                        
                        	Remote is satellite
                        	**type**\:  bool
                        
                        .. attribute:: source
                        
                        	Source
                        	**type**\:   :py:class:`IcpeOperTopoRemoteSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperTopoRemoteSource>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice, self).__init__()

                            self.yang_name = "remote-device"
                            self.yang_parent_name = "fabric-link"

                            self.icl_id = YLeaf(YType.uint32, "icl-id")

                            self.interface_handle = YLeaf(YType.str, "interface-handle")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.remote_is_local_host = YLeaf(YType.boolean, "remote-is-local-host")

                            self.remote_is_satellite = YLeaf(YType.boolean, "remote-is-satellite")

                            self.source = YLeaf(YType.enumeration, "source")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("icl_id",
                                            "interface_handle",
                                            "interface_name",
                                            "mac_address",
                                            "remote_is_local_host",
                                            "remote_is_satellite",
                                            "source") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.icl_id.is_set or
                                self.interface_handle.is_set or
                                self.interface_name.is_set or
                                self.mac_address.is_set or
                                self.remote_is_local_host.is_set or
                                self.remote_is_satellite.is_set or
                                self.source.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.icl_id.yfilter != YFilter.not_set or
                                self.interface_handle.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.mac_address.yfilter != YFilter.not_set or
                                self.remote_is_local_host.yfilter != YFilter.not_set or
                                self.remote_is_satellite.yfilter != YFilter.not_set or
                                self.source.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "remote-device" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.icl_id.is_set or self.icl_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.icl_id.get_name_leafdata())
                            if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_handle.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_address.get_name_leafdata())
                            if (self.remote_is_local_host.is_set or self.remote_is_local_host.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_is_local_host.get_name_leafdata())
                            if (self.remote_is_satellite.is_set or self.remote_is_satellite.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_is_satellite.get_name_leafdata())
                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "icl-id" or name == "interface-handle" or name == "interface-name" or name == "mac-address" or name == "remote-is-local-host" or name == "remote-is-satellite" or name == "source"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "icl-id"):
                                self.icl_id = value
                                self.icl_id.value_namespace = name_space
                                self.icl_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-handle"):
                                self.interface_handle = value
                                self.interface_handle.value_namespace = name_space
                                self.interface_handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "mac-address"):
                                self.mac_address = value
                                self.mac_address.value_namespace = name_space
                                self.mac_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-is-local-host"):
                                self.remote_is_local_host = value
                                self.remote_is_local_host.value_namespace = name_space
                                self.remote_is_local_host.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-is-satellite"):
                                self.remote_is_satellite = value
                                self.remote_is_satellite.value_namespace = name_space
                                self.remote_is_satellite.value_namespace_prefix = name_space_prefix
                            if(value_path == "source"):
                                self.source = value
                                self.source.value_namespace = name_space
                                self.source.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.remote_device:
                            if (c.has_data()):
                                return True
                        return (
                            self.active.is_set or
                            self.display_name.is_set or
                            self.icl_id.is_set or
                            self.interface_name.is_set or
                            self.obsolete.is_set or
                            self.redundant.is_set)

                    def has_operation(self):
                        for c in self.remote_device:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active.yfilter != YFilter.not_set or
                            self.display_name.yfilter != YFilter.not_set or
                            self.icl_id.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.obsolete.yfilter != YFilter.not_set or
                            self.redundant.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fabric-link" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active.get_name_leafdata())
                        if (self.display_name.is_set or self.display_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.display_name.get_name_leafdata())
                        if (self.icl_id.is_set or self.icl_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.icl_id.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.obsolete.is_set or self.obsolete.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.obsolete.get_name_leafdata())
                        if (self.redundant.is_set or self.redundant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.redundant.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "remote-device"):
                            for c in self.remote_device:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.remote_device.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "remote-device" or name == "active" or name == "display-name" or name == "icl-id" or name == "interface-name" or name == "obsolete" or name == "redundant"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active"):
                            self.active = value
                            self.active.value_namespace = name_space
                            self.active.value_namespace_prefix = name_space_prefix
                        if(value_path == "display-name"):
                            self.display_name = value
                            self.display_name.value_namespace = name_space
                            self.display_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "icl-id"):
                            self.icl_id = value
                            self.icl_id.value_namespace = name_space
                            self.icl_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "obsolete"):
                            self.obsolete = value
                            self.obsolete.value_namespace = name_space
                            self.obsolete.value_namespace_prefix = name_space_prefix
                        if(value_path == "redundant"):
                            self.redundant = value
                            self.redundant.value_namespace = name_space
                            self.redundant.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.fabric_link:
                        if (c.has_data()):
                            return True
                    return (
                        self.configured.is_set or
                        self.conflict_context.is_set or
                        self.conflict_reason.is_set or
                        self.display_name.is_set or
                        self.mac_address.is_set or
                        self.num_hops.is_set or
                        self.received_serial_number.is_set or
                        self.received_serial_number_present.is_set or
                        self.satellite_id.is_set or
                        self.type.is_set or
                        self.vlan_id.is_set)

                def has_operation(self):
                    for c in self.fabric_link:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.configured.yfilter != YFilter.not_set or
                        self.conflict_context.yfilter != YFilter.not_set or
                        self.conflict_reason.yfilter != YFilter.not_set or
                        self.display_name.yfilter != YFilter.not_set or
                        self.mac_address.yfilter != YFilter.not_set or
                        self.num_hops.yfilter != YFilter.not_set or
                        self.received_serial_number.yfilter != YFilter.not_set or
                        self.received_serial_number_present.yfilter != YFilter.not_set or
                        self.satellite_id.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.vlan_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "satellite" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.configured.is_set or self.configured.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured.get_name_leafdata())
                    if (self.conflict_context.is_set or self.conflict_context.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conflict_context.get_name_leafdata())
                    if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                    if (self.display_name.is_set or self.display_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.display_name.get_name_leafdata())
                    if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_address.get_name_leafdata())
                    if (self.num_hops.is_set or self.num_hops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_hops.get_name_leafdata())
                    if (self.received_serial_number.is_set or self.received_serial_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_serial_number.get_name_leafdata())
                    if (self.received_serial_number_present.is_set or self.received_serial_number_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_serial_number_present.get_name_leafdata())
                    if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_id.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vlan_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fabric-link"):
                        for c in self.fabric_link:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.fabric_link.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fabric-link" or name == "configured" or name == "conflict-context" or name == "conflict-reason" or name == "display-name" or name == "mac-address" or name == "num-hops" or name == "received-serial-number" or name == "received-serial-number-present" or name == "satellite-id" or name == "type" or name == "vlan-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "configured"):
                        self.configured = value
                        self.configured.value_namespace = name_space
                        self.configured.value_namespace_prefix = name_space_prefix
                    if(value_path == "conflict-context"):
                        self.conflict_context = value
                        self.conflict_context.value_namespace = name_space
                        self.conflict_context.value_namespace_prefix = name_space_prefix
                    if(value_path == "conflict-reason"):
                        self.conflict_reason = value
                        self.conflict_reason.value_namespace = name_space
                        self.conflict_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "display-name"):
                        self.display_name = value
                        self.display_name.value_namespace = name_space
                        self.display_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-address"):
                        self.mac_address = value
                        self.mac_address.value_namespace = name_space
                        self.mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-hops"):
                        self.num_hops = value
                        self.num_hops.value_namespace = name_space
                        self.num_hops.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-serial-number"):
                        self.received_serial_number = value
                        self.received_serial_number.value_namespace = name_space
                        self.received_serial_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-serial-number-present"):
                        self.received_serial_number_present = value
                        self.received_serial_number_present.value_namespace = name_space
                        self.received_serial_number_present.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-id"):
                        self.satellite_id = value
                        self.satellite_id.value_namespace = name_space
                        self.satellite_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "vlan-id"):
                        self.vlan_id = value
                        self.vlan_id.value_namespace = name_space
                        self.vlan_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.discovered_link:
                    if (c.has_data()):
                        return True
                for c in self.satellite:
                    if (c.has_data()):
                        return True
                return (
                    self.interface_name.is_set or
                    self.interface_handle.is_set or
                    self.interface_name_xr.is_set or
                    self.is_physical.is_set or
                    self.redundancy_iccp_group.is_set or
                    self.ring_whole.is_set)

            def has_operation(self):
                for c in self.discovered_link:
                    if (c.has_operation()):
                        return True
                for c in self.satellite:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.interface_handle.yfilter != YFilter.not_set or
                    self.interface_name_xr.yfilter != YFilter.not_set or
                    self.is_physical.yfilter != YFilter.not_set or
                    self.redundancy_iccp_group.yfilter != YFilter.not_set or
                    self.ring_whole.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "satellite-topology" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-topologies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_handle.get_name_leafdata())
                if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                if (self.is_physical.is_set or self.is_physical.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_physical.get_name_leafdata())
                if (self.redundancy_iccp_group.is_set or self.redundancy_iccp_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.redundancy_iccp_group.get_name_leafdata())
                if (self.ring_whole.is_set or self.ring_whole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ring_whole.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "discovered-link"):
                    for c in self.discovered_link:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.discovered_link.append(c)
                    return c

                if (child_yang_name == "satellite"):
                    for c in self.satellite:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.satellite.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "discovered-link" or name == "satellite" or name == "interface-name" or name == "interface-handle" or name == "interface-name-xr" or name == "is-physical" or name == "redundancy-iccp-group" or name == "ring-whole"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-handle"):
                    self.interface_handle = value
                    self.interface_handle.value_namespace = name_space
                    self.interface_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name-xr"):
                    self.interface_name_xr = value
                    self.interface_name_xr.value_namespace = name_space
                    self.interface_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "is-physical"):
                    self.is_physical = value
                    self.is_physical.value_namespace = name_space
                    self.is_physical.value_namespace_prefix = name_space_prefix
                if(value_path == "redundancy-iccp-group"):
                    self.redundancy_iccp_group = value
                    self.redundancy_iccp_group.value_namespace = name_space
                    self.redundancy_iccp_group.value_namespace_prefix = name_space_prefix
                if(value_path == "ring-whole"):
                    self.ring_whole = value
                    self.ring_whole.value_namespace = name_space
                    self.ring_whole.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.satellite_topology:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.satellite_topology:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "satellite-topologies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "satellite-topology"):
                for c in self.satellite_topology:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SatelliteTopologies.SatelliteTopology()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.satellite_topology.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "satellite-topology"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InstallProgresses(Entity):
        """
        Current percentage of install table
        
        .. attribute:: install_progress
        
        	Current percentage of install
        	**type**\: list of    :py:class:`InstallProgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallProgresses.InstallProgress>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallProgresses, self).__init__()

            self.yang_name = "install-progresses"
            self.yang_parent_name = "nv-satellite"

            self.install_progress = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.InstallProgresses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.InstallProgresses, self).__setattr__(name, value)


        class InstallProgress(Entity):
            """
            Current percentage of install
            
            .. attribute:: progress_percentage  <key>
            
            	Progress percentage
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: percentage
            
            .. attribute:: progress_percentage_xr
            
            	Progress percentage
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: percentage
            
            .. attribute:: satellite_count
            
            	Satellite count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallProgresses.InstallProgress, self).__init__()

                self.yang_name = "install-progress"
                self.yang_parent_name = "install-progresses"

                self.progress_percentage = YLeaf(YType.uint32, "progress-percentage")

                self.progress_percentage_xr = YLeaf(YType.uint16, "progress-percentage-xr")

                self.satellite_count = YLeaf(YType.uint32, "satellite-count")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("progress_percentage",
                                "progress_percentage_xr",
                                "satellite_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.InstallProgresses.InstallProgress, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.InstallProgresses.InstallProgress, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.progress_percentage.is_set or
                    self.progress_percentage_xr.is_set or
                    self.satellite_count.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.progress_percentage.yfilter != YFilter.not_set or
                    self.progress_percentage_xr.yfilter != YFilter.not_set or
                    self.satellite_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "install-progress" + "[progress-percentage='" + self.progress_percentage.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-progresses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.progress_percentage.is_set or self.progress_percentage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.progress_percentage.get_name_leafdata())
                if (self.progress_percentage_xr.is_set or self.progress_percentage_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.progress_percentage_xr.get_name_leafdata())
                if (self.satellite_count.is_set or self.satellite_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "progress-percentage" or name == "progress-percentage-xr" or name == "satellite-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "progress-percentage"):
                    self.progress_percentage = value
                    self.progress_percentage.value_namespace = name_space
                    self.progress_percentage.value_namespace_prefix = name_space_prefix
                if(value_path == "progress-percentage-xr"):
                    self.progress_percentage_xr = value
                    self.progress_percentage_xr.value_namespace = name_space
                    self.progress_percentage_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-count"):
                    self.satellite_count = value
                    self.satellite_count.value_namespace = name_space
                    self.satellite_count.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.install_progress:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.install_progress:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "install-progresses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "install-progress"):
                for c in self.install_progress:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.InstallProgresses.InstallProgress()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.install_progress.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "install-progress"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class ReloadStatuses(Entity):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_status
        
        	Detailed breakdown of reload status
        	**type**\: list of    :py:class:`ReloadStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses.ReloadStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.ReloadStatuses, self).__init__()

            self.yang_name = "reload-statuses"
            self.yang_parent_name = "nv-satellite"

            self.reload_status = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.ReloadStatuses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.ReloadStatuses, self).__setattr__(name, value)


        class ReloadStatus(Entity):
            """
            Detailed breakdown of reload status
            
            .. attribute:: satellite_range  <key>
            
            	Satellite range
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: satellite_range_xr
            
            	Satellite range
            	**type**\:  str
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reload_failed
            
            	Sats reload failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloaded
            
            	Sats reloaded
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloading
            
            	Sats reloading
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.ReloadStatuses.ReloadStatus, self).__init__()

                self.yang_name = "reload-status"
                self.yang_parent_name = "reload-statuses"

                self.satellite_range = YLeaf(YType.str, "satellite-range")

                self.satellite_range_xr = YLeaf(YType.str, "satellite-range-xr")

                self.sats_not_initiated = YLeafList(YType.uint16, "sats-not-initiated")

                self.sats_reload_failed = YLeafList(YType.uint16, "sats-reload-failed")

                self.sats_reloaded = YLeafList(YType.uint16, "sats-reloaded")

                self.sats_reloading = YLeafList(YType.uint16, "sats-reloading")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("satellite_range",
                                "satellite_range_xr",
                                "sats_not_initiated",
                                "sats_reload_failed",
                                "sats_reloaded",
                                "sats_reloading") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.ReloadStatuses.ReloadStatus, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.ReloadStatuses.ReloadStatus, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_reload_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_reloaded.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_reloading.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.satellite_range.is_set or
                    self.satellite_range_xr.is_set)

            def has_operation(self):
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_reload_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_reloaded.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_reloading.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.satellite_range.yfilter != YFilter.not_set or
                    self.satellite_range_xr.yfilter != YFilter.not_set or
                    self.sats_not_initiated.yfilter != YFilter.not_set or
                    self.sats_reload_failed.yfilter != YFilter.not_set or
                    self.sats_reloaded.yfilter != YFilter.not_set or
                    self.sats_reloading.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "reload-status" + "[satellite-range='" + self.satellite_range.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/reload-statuses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.satellite_range.is_set or self.satellite_range.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range.get_name_leafdata())
                if (self.satellite_range_xr.is_set or self.satellite_range_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range_xr.get_name_leafdata())

                leaf_name_data.extend(self.sats_not_initiated.get_name_leafdata())

                leaf_name_data.extend(self.sats_reload_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_reloaded.get_name_leafdata())

                leaf_name_data.extend(self.sats_reloading.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "satellite-range" or name == "satellite-range-xr" or name == "sats-not-initiated" or name == "sats-reload-failed" or name == "sats-reloaded" or name == "sats-reloading"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "satellite-range"):
                    self.satellite_range = value
                    self.satellite_range.value_namespace = name_space
                    self.satellite_range.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-range-xr"):
                    self.satellite_range_xr = value
                    self.satellite_range_xr.value_namespace = name_space
                    self.satellite_range_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "sats-not-initiated"):
                    self.sats_not_initiated.append(value)
                if(value_path == "sats-reload-failed"):
                    self.sats_reload_failed.append(value)
                if(value_path == "sats-reloaded"):
                    self.sats_reloaded.append(value)
                if(value_path == "sats-reloading"):
                    self.sats_reloading.append(value)

        def has_data(self):
            for c in self.reload_status:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.reload_status:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "reload-statuses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "reload-status"):
                for c in self.reload_status:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.ReloadStatuses.ReloadStatus()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.reload_status.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "reload-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Install(Entity):
        """
        Satellite Install Information
        
        .. attribute:: satellite_software_versions
        
        	Satellite Software Package Information table
        	**type**\:   :py:class:`SatelliteSoftwareVersions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.Install, self).__init__()

            self.yang_name = "install"
            self.yang_parent_name = "nv-satellite"

            self.satellite_software_versions = NvSatellite.Install.SatelliteSoftwareVersions()
            self.satellite_software_versions.parent = self
            self._children_name_map["satellite_software_versions"] = "satellite-software-versions"
            self._children_yang_names.add("satellite-software-versions")


        class SatelliteSoftwareVersions(Entity):
            """
            Satellite Software Package Information table
            
            .. attribute:: satellite_software_version
            
            	Satellite Software Package Information
            	**type**\: list of    :py:class:`SatelliteSoftwareVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.Install.SatelliteSoftwareVersions, self).__init__()

                self.yang_name = "satellite-software-versions"
                self.yang_parent_name = "install"

                self.satellite_software_version = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.Install.SatelliteSoftwareVersions, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.Install.SatelliteSoftwareVersions, self).__setattr__(name, value)


            class SatelliteSoftwareVersion(Entity):
                """
                Satellite Software Package Information
                
                .. attribute:: satellite_id  <key>
                
                	Satellite ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: install_package_info
                
                	Package Data on this Satellite
                	**type**\:   :py:class:`InstallPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo>`
                
                .. attribute:: package_support
                
                	Package support
                	**type**\:   :py:class:`IcpeInstallPkgSupp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeInstallPkgSupp>`
                
                .. attribute:: satellite_id_xr
                
                	Satellite ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion, self).__init__()

                    self.yang_name = "satellite-software-version"
                    self.yang_parent_name = "satellite-software-versions"

                    self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                    self.package_support = YLeaf(YType.enumeration, "package-support")

                    self.satellite_id_xr = YLeaf(YType.uint32, "satellite-id-xr")

                    self.install_package_info = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo()
                    self.install_package_info.parent = self
                    self._children_name_map["install_package_info"] = "install-package-info"
                    self._children_yang_names.add("install-package-info")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("satellite_id",
                                    "package_support",
                                    "satellite_id_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion, self).__setattr__(name, value)


                class InstallPackageInfo(Entity):
                    """
                    Package Data on this Satellite
                    
                    .. attribute:: active_packages
                    
                    	Active Packages running on this Satellite
                    	**type**\:   :py:class:`ActivePackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages>`
                    
                    .. attribute:: committed_packages
                    
                    	Committed Packages running on this Satellite
                    	**type**\:   :py:class:`CommittedPackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages>`
                    
                    .. attribute:: inactive_packages
                    
                    	Inactive Packages on this Satellite
                    	**type**\:   :py:class:`InactivePackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo, self).__init__()

                        self.yang_name = "install-package-info"
                        self.yang_parent_name = "satellite-software-version"

                        self.active_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages()
                        self.active_packages.parent = self
                        self._children_name_map["active_packages"] = "active-packages"
                        self._children_yang_names.add("active-packages")

                        self.committed_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages()
                        self.committed_packages.parent = self
                        self._children_name_map["committed_packages"] = "committed-packages"
                        self._children_yang_names.add("committed-packages")

                        self.inactive_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages()
                        self.inactive_packages.parent = self
                        self._children_name_map["inactive_packages"] = "inactive-packages"
                        self._children_yang_names.add("inactive-packages")


                    class ActivePackages(Entity):
                        """
                        Active Packages running on this Satellite
                        
                        .. attribute:: package
                        
                        	A package on this Satellite table
                        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages, self).__init__()

                            self.yang_name = "active-packages"
                            self.yang_parent_name = "install-package-info"

                            self.package = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages, self).__setattr__(name, value)


                        class Package(Entity):
                            """
                            A package on this Satellite table
                            
                            .. attribute:: is_base_image
                            
                            	Is base image
                            	**type**\:  bool
                            
                            .. attribute:: name
                            
                            	Name
                            	**type**\:  str
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'icpe-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "active-packages"

                                self.is_base_image = YLeaf(YType.boolean, "is-base-image")

                                self.name = YLeaf(YType.str, "name")

                                self.version = YLeaf(YType.str, "version")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_base_image",
                                                "name",
                                                "version") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.is_base_image.is_set or
                                    self.name.is_set or
                                    self.version.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_base_image.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    self.version.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "package" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_base_image.is_set or self.is_base_image.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_base_image.get_name_leafdata())
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())
                                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.version.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "is-base-image" or name == "name" or name == "version"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-base-image"):
                                    self.is_base_image = value
                                    self.is_base_image.value_namespace = name_space
                                    self.is_base_image.value_namespace_prefix = name_space_prefix
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix
                                if(value_path == "version"):
                                    self.version = value
                                    self.version.value_namespace = name_space
                                    self.version.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.package:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.package:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "active-packages" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "package"):
                                for c in self.package:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.package.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "package"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class InactivePackages(Entity):
                        """
                        Inactive Packages on this Satellite
                        
                        .. attribute:: package
                        
                        	A package on this Satellite table
                        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages, self).__init__()

                            self.yang_name = "inactive-packages"
                            self.yang_parent_name = "install-package-info"

                            self.package = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages, self).__setattr__(name, value)


                        class Package(Entity):
                            """
                            A package on this Satellite table
                            
                            .. attribute:: is_base_image
                            
                            	Is base image
                            	**type**\:  bool
                            
                            .. attribute:: name
                            
                            	Name
                            	**type**\:  str
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'icpe-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "inactive-packages"

                                self.is_base_image = YLeaf(YType.boolean, "is-base-image")

                                self.name = YLeaf(YType.str, "name")

                                self.version = YLeaf(YType.str, "version")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_base_image",
                                                "name",
                                                "version") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.is_base_image.is_set or
                                    self.name.is_set or
                                    self.version.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_base_image.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    self.version.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "package" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_base_image.is_set or self.is_base_image.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_base_image.get_name_leafdata())
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())
                                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.version.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "is-base-image" or name == "name" or name == "version"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-base-image"):
                                    self.is_base_image = value
                                    self.is_base_image.value_namespace = name_space
                                    self.is_base_image.value_namespace_prefix = name_space_prefix
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix
                                if(value_path == "version"):
                                    self.version = value
                                    self.version.value_namespace = name_space
                                    self.version.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.package:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.package:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "inactive-packages" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "package"):
                                for c in self.package:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.package.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "package"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class CommittedPackages(Entity):
                        """
                        Committed Packages running on this Satellite
                        
                        .. attribute:: package
                        
                        	A package on this Satellite table
                        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages, self).__init__()

                            self.yang_name = "committed-packages"
                            self.yang_parent_name = "install-package-info"

                            self.package = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages, self).__setattr__(name, value)


                        class Package(Entity):
                            """
                            A package on this Satellite table
                            
                            .. attribute:: is_base_image
                            
                            	Is base image
                            	**type**\:  bool
                            
                            .. attribute:: name
                            
                            	Name
                            	**type**\:  str
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'icpe-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "committed-packages"

                                self.is_base_image = YLeaf(YType.boolean, "is-base-image")

                                self.name = YLeaf(YType.str, "name")

                                self.version = YLeaf(YType.str, "version")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_base_image",
                                                "name",
                                                "version") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.is_base_image.is_set or
                                    self.name.is_set or
                                    self.version.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_base_image.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    self.version.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "package" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_base_image.is_set or self.is_base_image.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_base_image.get_name_leafdata())
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())
                                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.version.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "is-base-image" or name == "name" or name == "version"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-base-image"):
                                    self.is_base_image = value
                                    self.is_base_image.value_namespace = name_space
                                    self.is_base_image.value_namespace_prefix = name_space_prefix
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix
                                if(value_path == "version"):
                                    self.version = value
                                    self.version.value_namespace = name_space
                                    self.version.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.package:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.package:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "committed-packages" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "package"):
                                for c in self.package:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.package.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "package"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.active_packages is not None and self.active_packages.has_data()) or
                            (self.committed_packages is not None and self.committed_packages.has_data()) or
                            (self.inactive_packages is not None and self.inactive_packages.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.active_packages is not None and self.active_packages.has_operation()) or
                            (self.committed_packages is not None and self.committed_packages.has_operation()) or
                            (self.inactive_packages is not None and self.inactive_packages.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "install-package-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "active-packages"):
                            if (self.active_packages is None):
                                self.active_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages()
                                self.active_packages.parent = self
                                self._children_name_map["active_packages"] = "active-packages"
                            return self.active_packages

                        if (child_yang_name == "committed-packages"):
                            if (self.committed_packages is None):
                                self.committed_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages()
                                self.committed_packages.parent = self
                                self._children_name_map["committed_packages"] = "committed-packages"
                            return self.committed_packages

                        if (child_yang_name == "inactive-packages"):
                            if (self.inactive_packages is None):
                                self.inactive_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages()
                                self.inactive_packages.parent = self
                                self._children_name_map["inactive_packages"] = "inactive-packages"
                            return self.inactive_packages

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-packages" or name == "committed-packages" or name == "inactive-packages"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.satellite_id.is_set or
                        self.package_support.is_set or
                        self.satellite_id_xr.is_set or
                        (self.install_package_info is not None and self.install_package_info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.satellite_id.yfilter != YFilter.not_set or
                        self.package_support.yfilter != YFilter.not_set or
                        self.satellite_id_xr.yfilter != YFilter.not_set or
                        (self.install_package_info is not None and self.install_package_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "satellite-software-version" + "[satellite-id='" + self.satellite_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install/satellite-software-versions/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_id.get_name_leafdata())
                    if (self.package_support.is_set or self.package_support.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.package_support.get_name_leafdata())
                    if (self.satellite_id_xr.is_set or self.satellite_id_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_id_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "install-package-info"):
                        if (self.install_package_info is None):
                            self.install_package_info = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo()
                            self.install_package_info.parent = self
                            self._children_name_map["install_package_info"] = "install-package-info"
                        return self.install_package_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "install-package-info" or name == "satellite-id" or name == "package-support" or name == "satellite-id-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "satellite-id"):
                        self.satellite_id = value
                        self.satellite_id.value_namespace = name_space
                        self.satellite_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "package-support"):
                        self.package_support = value
                        self.package_support.value_namespace = name_space
                        self.package_support.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-id-xr"):
                        self.satellite_id_xr = value
                        self.satellite_id_xr.value_namespace = name_space
                        self.satellite_id_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.satellite_software_version:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.satellite_software_version:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "satellite-software-versions" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "satellite-software-version"):
                    for c in self.satellite_software_version:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.satellite_software_version.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "satellite-software-version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.satellite_software_versions is not None and self.satellite_software_versions.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.satellite_software_versions is not None and self.satellite_software_versions.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "install" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "satellite-software-versions"):
                if (self.satellite_software_versions is None):
                    self.satellite_software_versions = NvSatellite.Install.SatelliteSoftwareVersions()
                    self.satellite_software_versions.parent = self
                    self._children_name_map["satellite_software_versions"] = "satellite-software-versions"
                return self.satellite_software_versions

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "satellite-software-versions"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InstallOpStatuses(Entity):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_op_status
        
        	Detailed breakdown of install status
        	**type**\: list of    :py:class:`InstallOpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses.InstallOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallOpStatuses, self).__init__()

            self.yang_name = "install-op-statuses"
            self.yang_parent_name = "nv-satellite"

            self.install_op_status = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.InstallOpStatuses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.InstallOpStatuses, self).__setattr__(name, value)


        class InstallOpStatus(Entity):
            """
            Detailed breakdown of install status
            
            .. attribute:: operation_id  <key>
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\:  str
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_aborted
            
            	Sats deactivate aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_failed
            
            	Sats deactivate failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivating
            
            	Sats deactivating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_aborted
            
            	Sats remove aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_failed
            
            	Sats remove failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_removing
            
            	Sats removing
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_aborted
            
            	Sats update aborted
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_failed
            
            	Sats update failed
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_updating
            
            	Sats updating
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallOpStatuses.InstallOpStatus, self).__init__()

                self.yang_name = "install-op-status"
                self.yang_parent_name = "install-op-statuses"

                self.operation_id = YLeaf(YType.uint32, "operation-id")

                self.operation_id_xr = YLeaf(YType.uint32, "operation-id-xr")

                self.satellite_range = YLeaf(YType.str, "satellite-range")

                self.sats_activate_aborted = YLeafList(YType.uint16, "sats-activate-aborted")

                self.sats_activate_failed = YLeafList(YType.uint16, "sats-activate-failed")

                self.sats_activating = YLeafList(YType.uint16, "sats-activating")

                self.sats_completed = YLeafList(YType.uint16, "sats-completed")

                self.sats_deactivate_aborted = YLeafList(YType.uint16, "sats-deactivate-aborted")

                self.sats_deactivate_failed = YLeafList(YType.uint16, "sats-deactivate-failed")

                self.sats_deactivating = YLeafList(YType.uint16, "sats-deactivating")

                self.sats_no_operation = YLeafList(YType.uint16, "sats-no-operation")

                self.sats_not_initiated = YLeafList(YType.uint16, "sats-not-initiated")

                self.sats_remove_aborted = YLeafList(YType.uint16, "sats-remove-aborted")

                self.sats_remove_failed = YLeafList(YType.uint16, "sats-remove-failed")

                self.sats_removing = YLeafList(YType.uint16, "sats-removing")

                self.sats_transfer_aborted = YLeafList(YType.uint16, "sats-transfer-aborted")

                self.sats_transfer_failed = YLeafList(YType.uint16, "sats-transfer-failed")

                self.sats_transferring = YLeafList(YType.uint16, "sats-transferring")

                self.sats_update_aborted = YLeafList(YType.uint16, "sats-update-aborted")

                self.sats_update_failed = YLeafList(YType.uint16, "sats-update-failed")

                self.sats_updating = YLeafList(YType.uint16, "sats-updating")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("operation_id",
                                "operation_id_xr",
                                "satellite_range",
                                "sats_activate_aborted",
                                "sats_activate_failed",
                                "sats_activating",
                                "sats_completed",
                                "sats_deactivate_aborted",
                                "sats_deactivate_failed",
                                "sats_deactivating",
                                "sats_no_operation",
                                "sats_not_initiated",
                                "sats_remove_aborted",
                                "sats_remove_failed",
                                "sats_removing",
                                "sats_transfer_aborted",
                                "sats_transfer_failed",
                                "sats_transferring",
                                "sats_update_aborted",
                                "sats_update_failed",
                                "sats_updating") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.InstallOpStatuses.InstallOpStatus, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.InstallOpStatuses.InstallOpStatus, self).__setattr__(name, value)

            def has_data(self):
                for leaf in self.sats_activate_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activate_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_activating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_completed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivate_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivate_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_deactivating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_no_operation.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_remove_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_remove_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_removing.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transfer_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transfer_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_transferring.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_update_aborted.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_update_failed.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.sats_updating.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.operation_id.is_set or
                    self.operation_id_xr.is_set or
                    self.satellite_range.is_set)

            def has_operation(self):
                for leaf in self.sats_activate_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activate_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_activating.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_completed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivate_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivate_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_deactivating.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_no_operation.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_not_initiated.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_remove_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_remove_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_removing.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transfer_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transfer_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_transferring.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_update_aborted.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_update_failed.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.sats_updating.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.operation_id.yfilter != YFilter.not_set or
                    self.operation_id_xr.yfilter != YFilter.not_set or
                    self.satellite_range.yfilter != YFilter.not_set or
                    self.sats_activate_aborted.yfilter != YFilter.not_set or
                    self.sats_activate_failed.yfilter != YFilter.not_set or
                    self.sats_activating.yfilter != YFilter.not_set or
                    self.sats_completed.yfilter != YFilter.not_set or
                    self.sats_deactivate_aborted.yfilter != YFilter.not_set or
                    self.sats_deactivate_failed.yfilter != YFilter.not_set or
                    self.sats_deactivating.yfilter != YFilter.not_set or
                    self.sats_no_operation.yfilter != YFilter.not_set or
                    self.sats_not_initiated.yfilter != YFilter.not_set or
                    self.sats_remove_aborted.yfilter != YFilter.not_set or
                    self.sats_remove_failed.yfilter != YFilter.not_set or
                    self.sats_removing.yfilter != YFilter.not_set or
                    self.sats_transfer_aborted.yfilter != YFilter.not_set or
                    self.sats_transfer_failed.yfilter != YFilter.not_set or
                    self.sats_transferring.yfilter != YFilter.not_set or
                    self.sats_update_aborted.yfilter != YFilter.not_set or
                    self.sats_update_failed.yfilter != YFilter.not_set or
                    self.sats_updating.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "install-op-status" + "[operation-id='" + self.operation_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-op-statuses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.operation_id.is_set or self.operation_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id.get_name_leafdata())
                if (self.operation_id_xr.is_set or self.operation_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_id_xr.get_name_leafdata())
                if (self.satellite_range.is_set or self.satellite_range.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_range.get_name_leafdata())

                leaf_name_data.extend(self.sats_activate_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_activate_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_activating.get_name_leafdata())

                leaf_name_data.extend(self.sats_completed.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivate_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivate_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_deactivating.get_name_leafdata())

                leaf_name_data.extend(self.sats_no_operation.get_name_leafdata())

                leaf_name_data.extend(self.sats_not_initiated.get_name_leafdata())

                leaf_name_data.extend(self.sats_remove_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_remove_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_removing.get_name_leafdata())

                leaf_name_data.extend(self.sats_transfer_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_transfer_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_transferring.get_name_leafdata())

                leaf_name_data.extend(self.sats_update_aborted.get_name_leafdata())

                leaf_name_data.extend(self.sats_update_failed.get_name_leafdata())

                leaf_name_data.extend(self.sats_updating.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "operation-id" or name == "operation-id-xr" or name == "satellite-range" or name == "sats-activate-aborted" or name == "sats-activate-failed" or name == "sats-activating" or name == "sats-completed" or name == "sats-deactivate-aborted" or name == "sats-deactivate-failed" or name == "sats-deactivating" or name == "sats-no-operation" or name == "sats-not-initiated" or name == "sats-remove-aborted" or name == "sats-remove-failed" or name == "sats-removing" or name == "sats-transfer-aborted" or name == "sats-transfer-failed" or name == "sats-transferring" or name == "sats-update-aborted" or name == "sats-update-failed" or name == "sats-updating"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "operation-id"):
                    self.operation_id = value
                    self.operation_id.value_namespace = name_space
                    self.operation_id.value_namespace_prefix = name_space_prefix
                if(value_path == "operation-id-xr"):
                    self.operation_id_xr = value
                    self.operation_id_xr.value_namespace = name_space
                    self.operation_id_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-range"):
                    self.satellite_range = value
                    self.satellite_range.value_namespace = name_space
                    self.satellite_range.value_namespace_prefix = name_space_prefix
                if(value_path == "sats-activate-aborted"):
                    self.sats_activate_aborted.append(value)
                if(value_path == "sats-activate-failed"):
                    self.sats_activate_failed.append(value)
                if(value_path == "sats-activating"):
                    self.sats_activating.append(value)
                if(value_path == "sats-completed"):
                    self.sats_completed.append(value)
                if(value_path == "sats-deactivate-aborted"):
                    self.sats_deactivate_aborted.append(value)
                if(value_path == "sats-deactivate-failed"):
                    self.sats_deactivate_failed.append(value)
                if(value_path == "sats-deactivating"):
                    self.sats_deactivating.append(value)
                if(value_path == "sats-no-operation"):
                    self.sats_no_operation.append(value)
                if(value_path == "sats-not-initiated"):
                    self.sats_not_initiated.append(value)
                if(value_path == "sats-remove-aborted"):
                    self.sats_remove_aborted.append(value)
                if(value_path == "sats-remove-failed"):
                    self.sats_remove_failed.append(value)
                if(value_path == "sats-removing"):
                    self.sats_removing.append(value)
                if(value_path == "sats-transfer-aborted"):
                    self.sats_transfer_aborted.append(value)
                if(value_path == "sats-transfer-failed"):
                    self.sats_transfer_failed.append(value)
                if(value_path == "sats-transferring"):
                    self.sats_transferring.append(value)
                if(value_path == "sats-update-aborted"):
                    self.sats_update_aborted.append(value)
                if(value_path == "sats-update-failed"):
                    self.sats_update_failed.append(value)
                if(value_path == "sats-updating"):
                    self.sats_updating.append(value)

        def has_data(self):
            for c in self.install_op_status:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.install_op_status:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "install-op-statuses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "install-op-status"):
                for c in self.install_op_status:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.InstallOpStatuses.InstallOpStatus()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.install_op_status.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "install-op-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SatelliteProperties(Entity):
        """
        ICPE GCO operational information
        
        .. attribute:: id_ranges
        
        	Satellite ID range table
        	**type**\:   :py:class:`IdRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteProperties.IdRanges>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteProperties, self).__init__()

            self.yang_name = "satellite-properties"
            self.yang_parent_name = "nv-satellite"

            self.id_ranges = NvSatellite.SatelliteProperties.IdRanges()
            self.id_ranges.parent = self
            self._children_name_map["id_ranges"] = "id-ranges"
            self._children_yang_names.add("id-ranges")


        class IdRanges(Entity):
            """
            Satellite ID range table
            
            .. attribute:: id_range
            
            	Satellite ID range
            	**type**\: list of    :py:class:`IdRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteProperties.IdRanges.IdRange>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteProperties.IdRanges, self).__init__()

                self.yang_name = "id-ranges"
                self.yang_parent_name = "satellite-properties"

                self.id_range = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SatelliteProperties.IdRanges, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SatelliteProperties.IdRanges, self).__setattr__(name, value)


            class IdRange(Entity):
                """
                Satellite ID range
                
                .. attribute:: sat_id_range  <key>
                
                	Sat ID range
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: max
                
                	Max
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                .. attribute:: min
                
                	Min
                	**type**\:  int
                
                	**range:** 0..2147483647
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteProperties.IdRanges.IdRange, self).__init__()

                    self.yang_name = "id-range"
                    self.yang_parent_name = "id-ranges"

                    self.sat_id_range = YLeaf(YType.str, "sat-id-range")

                    self.max = YLeaf(YType.uint32, "max")

                    self.min = YLeaf(YType.uint32, "min")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("sat_id_range",
                                    "max",
                                    "min") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SatelliteProperties.IdRanges.IdRange, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SatelliteProperties.IdRanges.IdRange, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.sat_id_range.is_set or
                        self.max.is_set or
                        self.min.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.sat_id_range.yfilter != YFilter.not_set or
                        self.max.yfilter != YFilter.not_set or
                        self.min.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "id-range" + "[sat-id-range='" + self.sat_id_range.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-properties/id-ranges/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.sat_id_range.is_set or self.sat_id_range.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sat_id_range.get_name_leafdata())
                    if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max.get_name_leafdata())
                    if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sat-id-range" or name == "max" or name == "min"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "sat-id-range"):
                        self.sat_id_range = value
                        self.sat_id_range.value_namespace = name_space
                        self.sat_id_range.value_namespace_prefix = name_space_prefix
                    if(value_path == "max"):
                        self.max = value
                        self.max.value_namespace = name_space
                        self.max.value_namespace_prefix = name_space_prefix
                    if(value_path == "min"):
                        self.min = value
                        self.min.value_namespace = name_space
                        self.min.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.id_range:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.id_range:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "id-ranges" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-properties/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "id-range"):
                    for c in self.id_range:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SatelliteProperties.IdRanges.IdRange()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.id_range.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "id-range"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.id_ranges is not None and self.id_ranges.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.id_ranges is not None and self.id_ranges.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "satellite-properties" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "id-ranges"):
                if (self.id_ranges is None):
                    self.id_ranges = NvSatellite.SatelliteProperties.IdRanges()
                    self.id_ranges.parent = self
                    self._children_name_map["id_ranges"] = "id-ranges"
                return self.id_ranges

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "id-ranges"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SdacpDiscovery2S(Entity):
        """
        ICPE Configured interface state information
        table
        
        .. attribute:: sdacp_discovery2
        
        	ICPE Configured interface state information
        	**type**\: list of    :py:class:`SdacpDiscovery2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2>`
        
        

        """

        _prefix = 'icpe-sdacp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SdacpDiscovery2S, self).__init__()

            self.yang_name = "sdacp-discovery2s"
            self.yang_parent_name = "nv-satellite"

            self.sdacp_discovery2 = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SdacpDiscovery2S, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SdacpDiscovery2S, self).__setattr__(name, value)


        class SdacpDiscovery2(Entity):
            """
            ICPE Configured interface state information
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface
            
            	ICPE Discovery interface state information table
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface>`
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: satellite
            
            	ICPE Satellite state information table
            	**type**\: list of    :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite>`
            
            

            """

            _prefix = 'icpe-sdacp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2, self).__init__()

                self.yang_name = "sdacp-discovery2"
                self.yang_parent_name = "sdacp-discovery2s"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                self.interface = YList(self)
                self.satellite = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "interface_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2, self).__setattr__(name, value)


            class Interface(Entity):
                """
                ICPE Discovery interface state information table
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: interface_status
                
                	Interface status
                	**type**\:   :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "sdacp-discovery2"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface_status = YLeaf(YType.enumeration, "interface-status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "interface_status") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.interface_status.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.interface_status.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.interface_status.is_set or self.interface_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_status.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "interface-status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-status"):
                        self.interface_status = value
                        self.interface_status.value_namespace = name_space
                        self.interface_status.value_namespace_prefix = name_space_prefix


            class Satellite(Entity):
                """
                ICPE Satellite state information table
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: host_ip_address
                
                	Host IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface
                
                	ICPE Discovered satellite state information table
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface>`
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: satellite_ip_address
                
                	Satellite IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: satellite_status
                
                	Satellite status
                	**type**\:   :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "sdacp-discovery2"

                    self.conflict_reason = YLeaf(YType.uint32, "conflict-reason")

                    self.host_ip_address = YLeaf(YType.str, "host-ip-address")

                    self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                    self.satellite_ip_address = YLeaf(YType.str, "satellite-ip-address")

                    self.satellite_status = YLeaf(YType.enumeration, "satellite-status")

                    self.interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("conflict_reason",
                                    "host_ip_address",
                                    "satellite_id",
                                    "satellite_ip_address",
                                    "satellite_status") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    ICPE Discovered satellite state information
                    table
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: satellite_chassis_mac
                    
                    	Satellite chassis MAC
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: satellite_chassis_vendor
                    
                    	Satellite chassis vendor
                    	**type**\:  str
                    
                    .. attribute:: satellite_interface_id
                    
                    	Satellite interface ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: satellite_interface_mac
                    
                    	Satellite interface MAC
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: satellite_module_vendor
                    
                    	Satellite module vendor
                    	**type**\:  str
                    
                    .. attribute:: satellite_serial_id
                    
                    	Satellite serial id
                    	**type**\:  str
                    
                    .. attribute:: satellite_status
                    
                    	Satellite status
                    	**type**\:   :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "satellite"

                        self.conflict_reason = YLeaf(YType.uint32, "conflict-reason")

                        self.interface_handle = YLeaf(YType.str, "interface-handle")

                        self.satellite_chassis_mac = YLeaf(YType.str, "satellite-chassis-mac")

                        self.satellite_chassis_vendor = YLeaf(YType.str, "satellite-chassis-vendor")

                        self.satellite_interface_id = YLeaf(YType.uint32, "satellite-interface-id")

                        self.satellite_interface_mac = YLeaf(YType.str, "satellite-interface-mac")

                        self.satellite_module_vendor = YLeaf(YType.str, "satellite-module-vendor")

                        self.satellite_serial_id = YLeaf(YType.str, "satellite-serial-id")

                        self.satellite_status = YLeaf(YType.enumeration, "satellite-status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("conflict_reason",
                                        "interface_handle",
                                        "satellite_chassis_mac",
                                        "satellite_chassis_vendor",
                                        "satellite_interface_id",
                                        "satellite_interface_mac",
                                        "satellite_module_vendor",
                                        "satellite_serial_id",
                                        "satellite_status") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.conflict_reason.is_set or
                            self.interface_handle.is_set or
                            self.satellite_chassis_mac.is_set or
                            self.satellite_chassis_vendor.is_set or
                            self.satellite_interface_id.is_set or
                            self.satellite_interface_mac.is_set or
                            self.satellite_module_vendor.is_set or
                            self.satellite_serial_id.is_set or
                            self.satellite_status.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.conflict_reason.yfilter != YFilter.not_set or
                            self.interface_handle.yfilter != YFilter.not_set or
                            self.satellite_chassis_mac.yfilter != YFilter.not_set or
                            self.satellite_chassis_vendor.yfilter != YFilter.not_set or
                            self.satellite_interface_id.yfilter != YFilter.not_set or
                            self.satellite_interface_mac.yfilter != YFilter.not_set or
                            self.satellite_module_vendor.yfilter != YFilter.not_set or
                            self.satellite_serial_id.yfilter != YFilter.not_set or
                            self.satellite_status.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                        if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_handle.get_name_leafdata())
                        if (self.satellite_chassis_mac.is_set or self.satellite_chassis_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_chassis_mac.get_name_leafdata())
                        if (self.satellite_chassis_vendor.is_set or self.satellite_chassis_vendor.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_chassis_vendor.get_name_leafdata())
                        if (self.satellite_interface_id.is_set or self.satellite_interface_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_interface_id.get_name_leafdata())
                        if (self.satellite_interface_mac.is_set or self.satellite_interface_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_interface_mac.get_name_leafdata())
                        if (self.satellite_module_vendor.is_set or self.satellite_module_vendor.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_module_vendor.get_name_leafdata())
                        if (self.satellite_serial_id.is_set or self.satellite_serial_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_serial_id.get_name_leafdata())
                        if (self.satellite_status.is_set or self.satellite_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.satellite_status.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "conflict-reason" or name == "interface-handle" or name == "satellite-chassis-mac" or name == "satellite-chassis-vendor" or name == "satellite-interface-id" or name == "satellite-interface-mac" or name == "satellite-module-vendor" or name == "satellite-serial-id" or name == "satellite-status"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "conflict-reason"):
                            self.conflict_reason = value
                            self.conflict_reason.value_namespace = name_space
                            self.conflict_reason.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-handle"):
                            self.interface_handle = value
                            self.interface_handle.value_namespace = name_space
                            self.interface_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-chassis-mac"):
                            self.satellite_chassis_mac = value
                            self.satellite_chassis_mac.value_namespace = name_space
                            self.satellite_chassis_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-chassis-vendor"):
                            self.satellite_chassis_vendor = value
                            self.satellite_chassis_vendor.value_namespace = name_space
                            self.satellite_chassis_vendor.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-interface-id"):
                            self.satellite_interface_id = value
                            self.satellite_interface_id.value_namespace = name_space
                            self.satellite_interface_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-interface-mac"):
                            self.satellite_interface_mac = value
                            self.satellite_interface_mac.value_namespace = name_space
                            self.satellite_interface_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-module-vendor"):
                            self.satellite_module_vendor = value
                            self.satellite_module_vendor.value_namespace = name_space
                            self.satellite_module_vendor.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-serial-id"):
                            self.satellite_serial_id = value
                            self.satellite_serial_id.value_namespace = name_space
                            self.satellite_serial_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "satellite-status"):
                            self.satellite_status = value
                            self.satellite_status.value_namespace = name_space
                            self.satellite_status.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return (
                        self.conflict_reason.is_set or
                        self.host_ip_address.is_set or
                        self.satellite_id.is_set or
                        self.satellite_ip_address.is_set or
                        self.satellite_status.is_set)

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.conflict_reason.yfilter != YFilter.not_set or
                        self.host_ip_address.yfilter != YFilter.not_set or
                        self.satellite_id.yfilter != YFilter.not_set or
                        self.satellite_ip_address.yfilter != YFilter.not_set or
                        self.satellite_status.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "satellite" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                    if (self.host_ip_address.is_set or self.host_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_ip_address.get_name_leafdata())
                    if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_id.get_name_leafdata())
                    if (self.satellite_ip_address.is_set or self.satellite_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_ip_address.get_name_leafdata())
                    if (self.satellite_status.is_set or self.satellite_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_status.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface" or name == "conflict-reason" or name == "host-ip-address" or name == "satellite-id" or name == "satellite-ip-address" or name == "satellite-status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "conflict-reason"):
                        self.conflict_reason = value
                        self.conflict_reason.value_namespace = name_space
                        self.conflict_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-ip-address"):
                        self.host_ip_address = value
                        self.host_ip_address.value_namespace = name_space
                        self.host_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-id"):
                        self.satellite_id = value
                        self.satellite_id.value_namespace = name_space
                        self.satellite_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-ip-address"):
                        self.satellite_ip_address = value
                        self.satellite_ip_address.value_namespace = name_space
                        self.satellite_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-status"):
                        self.satellite_status = value
                        self.satellite_status.value_namespace = name_space
                        self.satellite_status.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                for c in self.satellite:
                    if (c.has_data()):
                        return True
                return (
                    self.interface_name.is_set or
                    self.interface_name_xr.is_set)

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                for c in self.satellite:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.interface_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sdacp-discovery2" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                if (child_yang_name == "satellite"):
                    for c in self.satellite:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.satellite.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface" or name == "satellite" or name == "interface-name" or name == "interface-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name-xr"):
                    self.interface_name_xr = value
                    self.interface_name_xr.value_namespace = name_space
                    self.interface_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sdacp_discovery2:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sdacp_discovery2:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sdacp-discovery2"):
                for c in self.sdacp_discovery2:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SdacpDiscovery2S.SdacpDiscovery2()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sdacp_discovery2.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sdacp-discovery2"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class IcpeDpms(Entity):
        """
        ICPE DPM operational information table
        
        .. attribute:: icpe_dpm
        
        	ICPE DPM operational information
        	**type**\: list of    :py:class:`IcpeDpm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms.IcpeDpm>`
        
        

        """

        _prefix = 'icpe-sdacp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.IcpeDpms, self).__init__()

            self.yang_name = "icpe-dpms"
            self.yang_parent_name = "nv-satellite"

            self.icpe_dpm = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.IcpeDpms, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.IcpeDpms, self).__setattr__(name, value)


        class IcpeDpm(Entity):
            """
            ICPE DPM operational information
            
            .. attribute:: discovery_interface  <key>
            
            	Discovery interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: ack_packets_sent
            
            	Ack packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: configuration_packets_sent
            
            	Configuration packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: discovery_interface_handle
            
            	Discovery interface handle
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: discovery_interface_status
            
            	Discovery interface status
            	**type**\:   :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
            
            .. attribute:: discovery_interface_xr
            
            	Discovery interface
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: host_ack_packets_received
            
            	Host ack packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: host_ack_packets_sent
            
            	Host ack packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ident_packets_received
            
            	Ident packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_packets_received
            
            	Invalid packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: los_packets_received
            
            	Los packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: probe_packets_sent
            
            	Probe packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ready_packets_received
            
            	Ready packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: reject_packets_sent
            
            	Reject packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: remote_host
            
            	ICPE DPM remote host operational information table
            	**type**\: list of    :py:class:`RemoteHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms.IcpeDpm.RemoteHost>`
            
            .. attribute:: satellite
            
            	ICPE DPM satellite operational information table
            	**type**\: list of    :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms.IcpeDpm.Satellite>`
            
            .. attribute:: secs_since_pkts_cleaned
            
            	Secs since pkts cleaned
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            

            """

            _prefix = 'icpe-sdacp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.IcpeDpms.IcpeDpm, self).__init__()

                self.yang_name = "icpe-dpm"
                self.yang_parent_name = "icpe-dpms"

                self.discovery_interface = YLeaf(YType.str, "discovery-interface")

                self.ack_packets_sent = YLeaf(YType.uint64, "ack-packets-sent")

                self.configuration_packets_sent = YLeaf(YType.uint64, "configuration-packets-sent")

                self.discovery_interface_handle = YLeaf(YType.str, "discovery-interface-handle")

                self.discovery_interface_status = YLeaf(YType.enumeration, "discovery-interface-status")

                self.discovery_interface_xr = YLeaf(YType.str, "discovery-interface-xr")

                self.host_ack_packets_received = YLeaf(YType.uint64, "host-ack-packets-received")

                self.host_ack_packets_sent = YLeaf(YType.uint64, "host-ack-packets-sent")

                self.ident_packets_received = YLeaf(YType.uint64, "ident-packets-received")

                self.invalid_packets_received = YLeaf(YType.uint64, "invalid-packets-received")

                self.los_packets_received = YLeaf(YType.uint64, "los-packets-received")

                self.probe_packets_sent = YLeaf(YType.uint64, "probe-packets-sent")

                self.ready_packets_received = YLeaf(YType.uint64, "ready-packets-received")

                self.reject_packets_sent = YLeaf(YType.uint64, "reject-packets-sent")

                self.secs_since_pkts_cleaned = YLeaf(YType.uint64, "secs-since-pkts-cleaned")

                self.remote_host = YList(self)
                self.satellite = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("discovery_interface",
                                "ack_packets_sent",
                                "configuration_packets_sent",
                                "discovery_interface_handle",
                                "discovery_interface_status",
                                "discovery_interface_xr",
                                "host_ack_packets_received",
                                "host_ack_packets_sent",
                                "ident_packets_received",
                                "invalid_packets_received",
                                "los_packets_received",
                                "probe_packets_sent",
                                "ready_packets_received",
                                "reject_packets_sent",
                                "secs_since_pkts_cleaned") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.IcpeDpms.IcpeDpm, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.IcpeDpms.IcpeDpm, self).__setattr__(name, value)


            class Satellite(Entity):
                """
                ICPE DPM satellite operational information table
                
                .. attribute:: ack_packets_sent
                
                	Ack packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: configuration_packets_sent
                
                	Configuration packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_timeout
                
                	Current timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: deleting
                
                	Deleting
                	**type**\:  bool
                
                .. attribute:: discovery_protocol_state
                
                	Discovery protocol state
                	**type**\:   :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                
                .. attribute:: host_chassis_mac
                
                	Host chassis MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: host_chassis_type
                
                	Host chassis type
                	**type**\:  str
                
                .. attribute:: host_chassis_vendor
                
                	Host chassis vendor
                	**type**\:  str
                
                .. attribute:: host_ip_address
                
                	Host IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ident_packets_received
                
                	Ident packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ifmgr_state
                
                	Ifmgr state
                	**type**\:  bool
                
                .. attribute:: invalid_packets_received
                
                	Invalid packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: is_queued_for_efd
                
                	Is queued for EFD
                	**type**\:  bool
                
                .. attribute:: is_queued_for_oc
                
                	Is queued for OC
                	**type**\:  bool
                
                .. attribute:: last_imdr_state
                
                	Last IMDR state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: legacy
                
                	Legacy
                	**type**\:  bool
                
                .. attribute:: los_packets_received
                
                	Los packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ready_packets_received
                
                	Ready packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: received_sys_mac
                
                	Received sys MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: reject_packets_sent
                
                	Reject packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: satellite_chassis_mac
                
                	Satellite chassis MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: satellite_chassis_type
                
                	Satellite chassis type
                	**type**\:  str
                
                .. attribute:: satellite_chassis_vendor
                
                	Satellite chassis vendor
                	**type**\:  str
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: satellite_interface_id
                
                	Satellite interface ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: satellite_interface_mac
                
                	Satellite interface MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: satellite_ip_address
                
                	Satellite IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: satellite_module_mac
                
                	Satellite module MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: satellite_module_type
                
                	Satellite module type
                	**type**\:  str
                
                .. attribute:: satellite_module_vendor
                
                	Satellite module vendor
                	**type**\:  str
                
                .. attribute:: satellite_serial_id
                
                	Satellite serial id
                	**type**\:  str
                
                .. attribute:: secs_since_pkts_cleaned
                
                	Secs since pkts cleaned
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.IcpeDpms.IcpeDpm.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "icpe-dpm"

                    self.ack_packets_sent = YLeaf(YType.uint64, "ack-packets-sent")

                    self.configuration_packets_sent = YLeaf(YType.uint64, "configuration-packets-sent")

                    self.conflict_reason = YLeaf(YType.uint32, "conflict-reason")

                    self.current_timeout = YLeaf(YType.uint32, "current-timeout")

                    self.deleting = YLeaf(YType.boolean, "deleting")

                    self.discovery_protocol_state = YLeaf(YType.enumeration, "discovery-protocol-state")

                    self.host_chassis_mac = YLeaf(YType.str, "host-chassis-mac")

                    self.host_chassis_type = YLeaf(YType.str, "host-chassis-type")

                    self.host_chassis_vendor = YLeaf(YType.str, "host-chassis-vendor")

                    self.host_ip_address = YLeaf(YType.str, "host-ip-address")

                    self.ident_packets_received = YLeaf(YType.uint64, "ident-packets-received")

                    self.ifmgr_state = YLeaf(YType.boolean, "ifmgr-state")

                    self.invalid_packets_received = YLeaf(YType.uint64, "invalid-packets-received")

                    self.is_queued_for_efd = YLeaf(YType.boolean, "is-queued-for-efd")

                    self.is_queued_for_oc = YLeaf(YType.boolean, "is-queued-for-oc")

                    self.last_imdr_state = YLeaf(YType.uint32, "last-imdr-state")

                    self.legacy = YLeaf(YType.boolean, "legacy")

                    self.los_packets_received = YLeaf(YType.uint64, "los-packets-received")

                    self.ready_packets_received = YLeaf(YType.uint64, "ready-packets-received")

                    self.received_sys_mac = YLeaf(YType.str, "received-sys-mac")

                    self.reject_packets_sent = YLeaf(YType.uint64, "reject-packets-sent")

                    self.satellite_chassis_mac = YLeaf(YType.str, "satellite-chassis-mac")

                    self.satellite_chassis_type = YLeaf(YType.str, "satellite-chassis-type")

                    self.satellite_chassis_vendor = YLeaf(YType.str, "satellite-chassis-vendor")

                    self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                    self.satellite_interface_id = YLeaf(YType.uint32, "satellite-interface-id")

                    self.satellite_interface_mac = YLeaf(YType.str, "satellite-interface-mac")

                    self.satellite_ip_address = YLeaf(YType.str, "satellite-ip-address")

                    self.satellite_module_mac = YLeaf(YType.str, "satellite-module-mac")

                    self.satellite_module_type = YLeaf(YType.str, "satellite-module-type")

                    self.satellite_module_vendor = YLeaf(YType.str, "satellite-module-vendor")

                    self.satellite_serial_id = YLeaf(YType.str, "satellite-serial-id")

                    self.secs_since_pkts_cleaned = YLeaf(YType.uint64, "secs-since-pkts-cleaned")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ack_packets_sent",
                                    "configuration_packets_sent",
                                    "conflict_reason",
                                    "current_timeout",
                                    "deleting",
                                    "discovery_protocol_state",
                                    "host_chassis_mac",
                                    "host_chassis_type",
                                    "host_chassis_vendor",
                                    "host_ip_address",
                                    "ident_packets_received",
                                    "ifmgr_state",
                                    "invalid_packets_received",
                                    "is_queued_for_efd",
                                    "is_queued_for_oc",
                                    "last_imdr_state",
                                    "legacy",
                                    "los_packets_received",
                                    "ready_packets_received",
                                    "received_sys_mac",
                                    "reject_packets_sent",
                                    "satellite_chassis_mac",
                                    "satellite_chassis_type",
                                    "satellite_chassis_vendor",
                                    "satellite_id",
                                    "satellite_interface_id",
                                    "satellite_interface_mac",
                                    "satellite_ip_address",
                                    "satellite_module_mac",
                                    "satellite_module_type",
                                    "satellite_module_vendor",
                                    "satellite_serial_id",
                                    "secs_since_pkts_cleaned") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.IcpeDpms.IcpeDpm.Satellite, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.IcpeDpms.IcpeDpm.Satellite, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ack_packets_sent.is_set or
                        self.configuration_packets_sent.is_set or
                        self.conflict_reason.is_set or
                        self.current_timeout.is_set or
                        self.deleting.is_set or
                        self.discovery_protocol_state.is_set or
                        self.host_chassis_mac.is_set or
                        self.host_chassis_type.is_set or
                        self.host_chassis_vendor.is_set or
                        self.host_ip_address.is_set or
                        self.ident_packets_received.is_set or
                        self.ifmgr_state.is_set or
                        self.invalid_packets_received.is_set or
                        self.is_queued_for_efd.is_set or
                        self.is_queued_for_oc.is_set or
                        self.last_imdr_state.is_set or
                        self.legacy.is_set or
                        self.los_packets_received.is_set or
                        self.ready_packets_received.is_set or
                        self.received_sys_mac.is_set or
                        self.reject_packets_sent.is_set or
                        self.satellite_chassis_mac.is_set or
                        self.satellite_chassis_type.is_set or
                        self.satellite_chassis_vendor.is_set or
                        self.satellite_id.is_set or
                        self.satellite_interface_id.is_set or
                        self.satellite_interface_mac.is_set or
                        self.satellite_ip_address.is_set or
                        self.satellite_module_mac.is_set or
                        self.satellite_module_type.is_set or
                        self.satellite_module_vendor.is_set or
                        self.satellite_serial_id.is_set or
                        self.secs_since_pkts_cleaned.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ack_packets_sent.yfilter != YFilter.not_set or
                        self.configuration_packets_sent.yfilter != YFilter.not_set or
                        self.conflict_reason.yfilter != YFilter.not_set or
                        self.current_timeout.yfilter != YFilter.not_set or
                        self.deleting.yfilter != YFilter.not_set or
                        self.discovery_protocol_state.yfilter != YFilter.not_set or
                        self.host_chassis_mac.yfilter != YFilter.not_set or
                        self.host_chassis_type.yfilter != YFilter.not_set or
                        self.host_chassis_vendor.yfilter != YFilter.not_set or
                        self.host_ip_address.yfilter != YFilter.not_set or
                        self.ident_packets_received.yfilter != YFilter.not_set or
                        self.ifmgr_state.yfilter != YFilter.not_set or
                        self.invalid_packets_received.yfilter != YFilter.not_set or
                        self.is_queued_for_efd.yfilter != YFilter.not_set or
                        self.is_queued_for_oc.yfilter != YFilter.not_set or
                        self.last_imdr_state.yfilter != YFilter.not_set or
                        self.legacy.yfilter != YFilter.not_set or
                        self.los_packets_received.yfilter != YFilter.not_set or
                        self.ready_packets_received.yfilter != YFilter.not_set or
                        self.received_sys_mac.yfilter != YFilter.not_set or
                        self.reject_packets_sent.yfilter != YFilter.not_set or
                        self.satellite_chassis_mac.yfilter != YFilter.not_set or
                        self.satellite_chassis_type.yfilter != YFilter.not_set or
                        self.satellite_chassis_vendor.yfilter != YFilter.not_set or
                        self.satellite_id.yfilter != YFilter.not_set or
                        self.satellite_interface_id.yfilter != YFilter.not_set or
                        self.satellite_interface_mac.yfilter != YFilter.not_set or
                        self.satellite_ip_address.yfilter != YFilter.not_set or
                        self.satellite_module_mac.yfilter != YFilter.not_set or
                        self.satellite_module_type.yfilter != YFilter.not_set or
                        self.satellite_module_vendor.yfilter != YFilter.not_set or
                        self.satellite_serial_id.yfilter != YFilter.not_set or
                        self.secs_since_pkts_cleaned.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "satellite" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ack_packets_sent.is_set or self.ack_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ack_packets_sent.get_name_leafdata())
                    if (self.configuration_packets_sent.is_set or self.configuration_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configuration_packets_sent.get_name_leafdata())
                    if (self.conflict_reason.is_set or self.conflict_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conflict_reason.get_name_leafdata())
                    if (self.current_timeout.is_set or self.current_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_timeout.get_name_leafdata())
                    if (self.deleting.is_set or self.deleting.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.deleting.get_name_leafdata())
                    if (self.discovery_protocol_state.is_set or self.discovery_protocol_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discovery_protocol_state.get_name_leafdata())
                    if (self.host_chassis_mac.is_set or self.host_chassis_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_chassis_mac.get_name_leafdata())
                    if (self.host_chassis_type.is_set or self.host_chassis_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_chassis_type.get_name_leafdata())
                    if (self.host_chassis_vendor.is_set or self.host_chassis_vendor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_chassis_vendor.get_name_leafdata())
                    if (self.host_ip_address.is_set or self.host_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_ip_address.get_name_leafdata())
                    if (self.ident_packets_received.is_set or self.ident_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ident_packets_received.get_name_leafdata())
                    if (self.ifmgr_state.is_set or self.ifmgr_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ifmgr_state.get_name_leafdata())
                    if (self.invalid_packets_received.is_set or self.invalid_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_packets_received.get_name_leafdata())
                    if (self.is_queued_for_efd.is_set or self.is_queued_for_efd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_queued_for_efd.get_name_leafdata())
                    if (self.is_queued_for_oc.is_set or self.is_queued_for_oc.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_queued_for_oc.get_name_leafdata())
                    if (self.last_imdr_state.is_set or self.last_imdr_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_imdr_state.get_name_leafdata())
                    if (self.legacy.is_set or self.legacy.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.legacy.get_name_leafdata())
                    if (self.los_packets_received.is_set or self.los_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.los_packets_received.get_name_leafdata())
                    if (self.ready_packets_received.is_set or self.ready_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ready_packets_received.get_name_leafdata())
                    if (self.received_sys_mac.is_set or self.received_sys_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_sys_mac.get_name_leafdata())
                    if (self.reject_packets_sent.is_set or self.reject_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reject_packets_sent.get_name_leafdata())
                    if (self.satellite_chassis_mac.is_set or self.satellite_chassis_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_chassis_mac.get_name_leafdata())
                    if (self.satellite_chassis_type.is_set or self.satellite_chassis_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_chassis_type.get_name_leafdata())
                    if (self.satellite_chassis_vendor.is_set or self.satellite_chassis_vendor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_chassis_vendor.get_name_leafdata())
                    if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_id.get_name_leafdata())
                    if (self.satellite_interface_id.is_set or self.satellite_interface_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_interface_id.get_name_leafdata())
                    if (self.satellite_interface_mac.is_set or self.satellite_interface_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_interface_mac.get_name_leafdata())
                    if (self.satellite_ip_address.is_set or self.satellite_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_ip_address.get_name_leafdata())
                    if (self.satellite_module_mac.is_set or self.satellite_module_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_module_mac.get_name_leafdata())
                    if (self.satellite_module_type.is_set or self.satellite_module_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_module_type.get_name_leafdata())
                    if (self.satellite_module_vendor.is_set or self.satellite_module_vendor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_module_vendor.get_name_leafdata())
                    if (self.satellite_serial_id.is_set or self.satellite_serial_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.satellite_serial_id.get_name_leafdata())
                    if (self.secs_since_pkts_cleaned.is_set or self.secs_since_pkts_cleaned.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secs_since_pkts_cleaned.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ack-packets-sent" or name == "configuration-packets-sent" or name == "conflict-reason" or name == "current-timeout" or name == "deleting" or name == "discovery-protocol-state" or name == "host-chassis-mac" or name == "host-chassis-type" or name == "host-chassis-vendor" or name == "host-ip-address" or name == "ident-packets-received" or name == "ifmgr-state" or name == "invalid-packets-received" or name == "is-queued-for-efd" or name == "is-queued-for-oc" or name == "last-imdr-state" or name == "legacy" or name == "los-packets-received" or name == "ready-packets-received" or name == "received-sys-mac" or name == "reject-packets-sent" or name == "satellite-chassis-mac" or name == "satellite-chassis-type" or name == "satellite-chassis-vendor" or name == "satellite-id" or name == "satellite-interface-id" or name == "satellite-interface-mac" or name == "satellite-ip-address" or name == "satellite-module-mac" or name == "satellite-module-type" or name == "satellite-module-vendor" or name == "satellite-serial-id" or name == "secs-since-pkts-cleaned"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ack-packets-sent"):
                        self.ack_packets_sent = value
                        self.ack_packets_sent.value_namespace = name_space
                        self.ack_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "configuration-packets-sent"):
                        self.configuration_packets_sent = value
                        self.configuration_packets_sent.value_namespace = name_space
                        self.configuration_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "conflict-reason"):
                        self.conflict_reason = value
                        self.conflict_reason.value_namespace = name_space
                        self.conflict_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-timeout"):
                        self.current_timeout = value
                        self.current_timeout.value_namespace = name_space
                        self.current_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "deleting"):
                        self.deleting = value
                        self.deleting.value_namespace = name_space
                        self.deleting.value_namespace_prefix = name_space_prefix
                    if(value_path == "discovery-protocol-state"):
                        self.discovery_protocol_state = value
                        self.discovery_protocol_state.value_namespace = name_space
                        self.discovery_protocol_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-chassis-mac"):
                        self.host_chassis_mac = value
                        self.host_chassis_mac.value_namespace = name_space
                        self.host_chassis_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-chassis-type"):
                        self.host_chassis_type = value
                        self.host_chassis_type.value_namespace = name_space
                        self.host_chassis_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-chassis-vendor"):
                        self.host_chassis_vendor = value
                        self.host_chassis_vendor.value_namespace = name_space
                        self.host_chassis_vendor.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-ip-address"):
                        self.host_ip_address = value
                        self.host_ip_address.value_namespace = name_space
                        self.host_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "ident-packets-received"):
                        self.ident_packets_received = value
                        self.ident_packets_received.value_namespace = name_space
                        self.ident_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "ifmgr-state"):
                        self.ifmgr_state = value
                        self.ifmgr_state.value_namespace = name_space
                        self.ifmgr_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-packets-received"):
                        self.invalid_packets_received = value
                        self.invalid_packets_received.value_namespace = name_space
                        self.invalid_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-queued-for-efd"):
                        self.is_queued_for_efd = value
                        self.is_queued_for_efd.value_namespace = name_space
                        self.is_queued_for_efd.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-queued-for-oc"):
                        self.is_queued_for_oc = value
                        self.is_queued_for_oc.value_namespace = name_space
                        self.is_queued_for_oc.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-imdr-state"):
                        self.last_imdr_state = value
                        self.last_imdr_state.value_namespace = name_space
                        self.last_imdr_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "legacy"):
                        self.legacy = value
                        self.legacy.value_namespace = name_space
                        self.legacy.value_namespace_prefix = name_space_prefix
                    if(value_path == "los-packets-received"):
                        self.los_packets_received = value
                        self.los_packets_received.value_namespace = name_space
                        self.los_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "ready-packets-received"):
                        self.ready_packets_received = value
                        self.ready_packets_received.value_namespace = name_space
                        self.ready_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-sys-mac"):
                        self.received_sys_mac = value
                        self.received_sys_mac.value_namespace = name_space
                        self.received_sys_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "reject-packets-sent"):
                        self.reject_packets_sent = value
                        self.reject_packets_sent.value_namespace = name_space
                        self.reject_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-chassis-mac"):
                        self.satellite_chassis_mac = value
                        self.satellite_chassis_mac.value_namespace = name_space
                        self.satellite_chassis_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-chassis-type"):
                        self.satellite_chassis_type = value
                        self.satellite_chassis_type.value_namespace = name_space
                        self.satellite_chassis_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-chassis-vendor"):
                        self.satellite_chassis_vendor = value
                        self.satellite_chassis_vendor.value_namespace = name_space
                        self.satellite_chassis_vendor.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-id"):
                        self.satellite_id = value
                        self.satellite_id.value_namespace = name_space
                        self.satellite_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-interface-id"):
                        self.satellite_interface_id = value
                        self.satellite_interface_id.value_namespace = name_space
                        self.satellite_interface_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-interface-mac"):
                        self.satellite_interface_mac = value
                        self.satellite_interface_mac.value_namespace = name_space
                        self.satellite_interface_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-ip-address"):
                        self.satellite_ip_address = value
                        self.satellite_ip_address.value_namespace = name_space
                        self.satellite_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-module-mac"):
                        self.satellite_module_mac = value
                        self.satellite_module_mac.value_namespace = name_space
                        self.satellite_module_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-module-type"):
                        self.satellite_module_type = value
                        self.satellite_module_type.value_namespace = name_space
                        self.satellite_module_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-module-vendor"):
                        self.satellite_module_vendor = value
                        self.satellite_module_vendor.value_namespace = name_space
                        self.satellite_module_vendor.value_namespace_prefix = name_space_prefix
                    if(value_path == "satellite-serial-id"):
                        self.satellite_serial_id = value
                        self.satellite_serial_id.value_namespace = name_space
                        self.satellite_serial_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "secs-since-pkts-cleaned"):
                        self.secs_since_pkts_cleaned = value
                        self.secs_since_pkts_cleaned.value_namespace = name_space
                        self.secs_since_pkts_cleaned.value_namespace_prefix = name_space_prefix


            class RemoteHost(Entity):
                """
                ICPE DPM remote host operational information
                table
                
                .. attribute:: current_timeout
                
                	Current timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discovery_protocol_state
                
                	Discovery protocol state
                	**type**\:   :py:class:`DpmProtoHostState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoHostState>`
                
                .. attribute:: host_ack_packets_received
                
                	Host ack packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: host_ack_packets_sent
                
                	Host ack packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: host_chassis_mac
                
                	Host chassis MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: host_interface_mac
                
                	Host interface MAC
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: route_length
                
                	Route length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: secs_since_pkts_cleaned
                
                	Secs since pkts cleaned
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.IcpeDpms.IcpeDpm.RemoteHost, self).__init__()

                    self.yang_name = "remote-host"
                    self.yang_parent_name = "icpe-dpm"

                    self.current_timeout = YLeaf(YType.uint32, "current-timeout")

                    self.discovery_protocol_state = YLeaf(YType.enumeration, "discovery-protocol-state")

                    self.host_ack_packets_received = YLeaf(YType.uint64, "host-ack-packets-received")

                    self.host_ack_packets_sent = YLeaf(YType.uint64, "host-ack-packets-sent")

                    self.host_chassis_mac = YLeaf(YType.str, "host-chassis-mac")

                    self.host_interface_mac = YLeaf(YType.str, "host-interface-mac")

                    self.route_length = YLeaf(YType.uint32, "route-length")

                    self.secs_since_pkts_cleaned = YLeaf(YType.uint64, "secs-since-pkts-cleaned")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("current_timeout",
                                    "discovery_protocol_state",
                                    "host_ack_packets_received",
                                    "host_ack_packets_sent",
                                    "host_chassis_mac",
                                    "host_interface_mac",
                                    "route_length",
                                    "secs_since_pkts_cleaned") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.IcpeDpms.IcpeDpm.RemoteHost, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.IcpeDpms.IcpeDpm.RemoteHost, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.current_timeout.is_set or
                        self.discovery_protocol_state.is_set or
                        self.host_ack_packets_received.is_set or
                        self.host_ack_packets_sent.is_set or
                        self.host_chassis_mac.is_set or
                        self.host_interface_mac.is_set or
                        self.route_length.is_set or
                        self.secs_since_pkts_cleaned.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.current_timeout.yfilter != YFilter.not_set or
                        self.discovery_protocol_state.yfilter != YFilter.not_set or
                        self.host_ack_packets_received.yfilter != YFilter.not_set or
                        self.host_ack_packets_sent.yfilter != YFilter.not_set or
                        self.host_chassis_mac.yfilter != YFilter.not_set or
                        self.host_interface_mac.yfilter != YFilter.not_set or
                        self.route_length.yfilter != YFilter.not_set or
                        self.secs_since_pkts_cleaned.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "remote-host" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.current_timeout.is_set or self.current_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_timeout.get_name_leafdata())
                    if (self.discovery_protocol_state.is_set or self.discovery_protocol_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discovery_protocol_state.get_name_leafdata())
                    if (self.host_ack_packets_received.is_set or self.host_ack_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_ack_packets_received.get_name_leafdata())
                    if (self.host_ack_packets_sent.is_set or self.host_ack_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_ack_packets_sent.get_name_leafdata())
                    if (self.host_chassis_mac.is_set or self.host_chassis_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_chassis_mac.get_name_leafdata())
                    if (self.host_interface_mac.is_set or self.host_interface_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_interface_mac.get_name_leafdata())
                    if (self.route_length.is_set or self.route_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_length.get_name_leafdata())
                    if (self.secs_since_pkts_cleaned.is_set or self.secs_since_pkts_cleaned.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secs_since_pkts_cleaned.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "current-timeout" or name == "discovery-protocol-state" or name == "host-ack-packets-received" or name == "host-ack-packets-sent" or name == "host-chassis-mac" or name == "host-interface-mac" or name == "route-length" or name == "secs-since-pkts-cleaned"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "current-timeout"):
                        self.current_timeout = value
                        self.current_timeout.value_namespace = name_space
                        self.current_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "discovery-protocol-state"):
                        self.discovery_protocol_state = value
                        self.discovery_protocol_state.value_namespace = name_space
                        self.discovery_protocol_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-ack-packets-received"):
                        self.host_ack_packets_received = value
                        self.host_ack_packets_received.value_namespace = name_space
                        self.host_ack_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-ack-packets-sent"):
                        self.host_ack_packets_sent = value
                        self.host_ack_packets_sent.value_namespace = name_space
                        self.host_ack_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-chassis-mac"):
                        self.host_chassis_mac = value
                        self.host_chassis_mac.value_namespace = name_space
                        self.host_chassis_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "host-interface-mac"):
                        self.host_interface_mac = value
                        self.host_interface_mac.value_namespace = name_space
                        self.host_interface_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-length"):
                        self.route_length = value
                        self.route_length.value_namespace = name_space
                        self.route_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "secs-since-pkts-cleaned"):
                        self.secs_since_pkts_cleaned = value
                        self.secs_since_pkts_cleaned.value_namespace = name_space
                        self.secs_since_pkts_cleaned.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.remote_host:
                    if (c.has_data()):
                        return True
                for c in self.satellite:
                    if (c.has_data()):
                        return True
                return (
                    self.discovery_interface.is_set or
                    self.ack_packets_sent.is_set or
                    self.configuration_packets_sent.is_set or
                    self.discovery_interface_handle.is_set or
                    self.discovery_interface_status.is_set or
                    self.discovery_interface_xr.is_set or
                    self.host_ack_packets_received.is_set or
                    self.host_ack_packets_sent.is_set or
                    self.ident_packets_received.is_set or
                    self.invalid_packets_received.is_set or
                    self.los_packets_received.is_set or
                    self.probe_packets_sent.is_set or
                    self.ready_packets_received.is_set or
                    self.reject_packets_sent.is_set or
                    self.secs_since_pkts_cleaned.is_set)

            def has_operation(self):
                for c in self.remote_host:
                    if (c.has_operation()):
                        return True
                for c in self.satellite:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.discovery_interface.yfilter != YFilter.not_set or
                    self.ack_packets_sent.yfilter != YFilter.not_set or
                    self.configuration_packets_sent.yfilter != YFilter.not_set or
                    self.discovery_interface_handle.yfilter != YFilter.not_set or
                    self.discovery_interface_status.yfilter != YFilter.not_set or
                    self.discovery_interface_xr.yfilter != YFilter.not_set or
                    self.host_ack_packets_received.yfilter != YFilter.not_set or
                    self.host_ack_packets_sent.yfilter != YFilter.not_set or
                    self.ident_packets_received.yfilter != YFilter.not_set or
                    self.invalid_packets_received.yfilter != YFilter.not_set or
                    self.los_packets_received.yfilter != YFilter.not_set or
                    self.probe_packets_sent.yfilter != YFilter.not_set or
                    self.ready_packets_received.yfilter != YFilter.not_set or
                    self.reject_packets_sent.yfilter != YFilter.not_set or
                    self.secs_since_pkts_cleaned.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "icpe-dpm" + "[discovery-interface='" + self.discovery_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.discovery_interface.is_set or self.discovery_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discovery_interface.get_name_leafdata())
                if (self.ack_packets_sent.is_set or self.ack_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ack_packets_sent.get_name_leafdata())
                if (self.configuration_packets_sent.is_set or self.configuration_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configuration_packets_sent.get_name_leafdata())
                if (self.discovery_interface_handle.is_set or self.discovery_interface_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discovery_interface_handle.get_name_leafdata())
                if (self.discovery_interface_status.is_set or self.discovery_interface_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discovery_interface_status.get_name_leafdata())
                if (self.discovery_interface_xr.is_set or self.discovery_interface_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discovery_interface_xr.get_name_leafdata())
                if (self.host_ack_packets_received.is_set or self.host_ack_packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_ack_packets_received.get_name_leafdata())
                if (self.host_ack_packets_sent.is_set or self.host_ack_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_ack_packets_sent.get_name_leafdata())
                if (self.ident_packets_received.is_set or self.ident_packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ident_packets_received.get_name_leafdata())
                if (self.invalid_packets_received.is_set or self.invalid_packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.invalid_packets_received.get_name_leafdata())
                if (self.los_packets_received.is_set or self.los_packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.los_packets_received.get_name_leafdata())
                if (self.probe_packets_sent.is_set or self.probe_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.probe_packets_sent.get_name_leafdata())
                if (self.ready_packets_received.is_set or self.ready_packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ready_packets_received.get_name_leafdata())
                if (self.reject_packets_sent.is_set or self.reject_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.reject_packets_sent.get_name_leafdata())
                if (self.secs_since_pkts_cleaned.is_set or self.secs_since_pkts_cleaned.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.secs_since_pkts_cleaned.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "remote-host"):
                    for c in self.remote_host:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.IcpeDpms.IcpeDpm.RemoteHost()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.remote_host.append(c)
                    return c

                if (child_yang_name == "satellite"):
                    for c in self.satellite:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.IcpeDpms.IcpeDpm.Satellite()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.satellite.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "remote-host" or name == "satellite" or name == "discovery-interface" or name == "ack-packets-sent" or name == "configuration-packets-sent" or name == "discovery-interface-handle" or name == "discovery-interface-status" or name == "discovery-interface-xr" or name == "host-ack-packets-received" or name == "host-ack-packets-sent" or name == "ident-packets-received" or name == "invalid-packets-received" or name == "los-packets-received" or name == "probe-packets-sent" or name == "ready-packets-received" or name == "reject-packets-sent" or name == "secs-since-pkts-cleaned"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "discovery-interface"):
                    self.discovery_interface = value
                    self.discovery_interface.value_namespace = name_space
                    self.discovery_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "ack-packets-sent"):
                    self.ack_packets_sent = value
                    self.ack_packets_sent.value_namespace = name_space
                    self.ack_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "configuration-packets-sent"):
                    self.configuration_packets_sent = value
                    self.configuration_packets_sent.value_namespace = name_space
                    self.configuration_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "discovery-interface-handle"):
                    self.discovery_interface_handle = value
                    self.discovery_interface_handle.value_namespace = name_space
                    self.discovery_interface_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "discovery-interface-status"):
                    self.discovery_interface_status = value
                    self.discovery_interface_status.value_namespace = name_space
                    self.discovery_interface_status.value_namespace_prefix = name_space_prefix
                if(value_path == "discovery-interface-xr"):
                    self.discovery_interface_xr = value
                    self.discovery_interface_xr.value_namespace = name_space
                    self.discovery_interface_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "host-ack-packets-received"):
                    self.host_ack_packets_received = value
                    self.host_ack_packets_received.value_namespace = name_space
                    self.host_ack_packets_received.value_namespace_prefix = name_space_prefix
                if(value_path == "host-ack-packets-sent"):
                    self.host_ack_packets_sent = value
                    self.host_ack_packets_sent.value_namespace = name_space
                    self.host_ack_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "ident-packets-received"):
                    self.ident_packets_received = value
                    self.ident_packets_received.value_namespace = name_space
                    self.ident_packets_received.value_namespace_prefix = name_space_prefix
                if(value_path == "invalid-packets-received"):
                    self.invalid_packets_received = value
                    self.invalid_packets_received.value_namespace = name_space
                    self.invalid_packets_received.value_namespace_prefix = name_space_prefix
                if(value_path == "los-packets-received"):
                    self.los_packets_received = value
                    self.los_packets_received.value_namespace = name_space
                    self.los_packets_received.value_namespace_prefix = name_space_prefix
                if(value_path == "probe-packets-sent"):
                    self.probe_packets_sent = value
                    self.probe_packets_sent.value_namespace = name_space
                    self.probe_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "ready-packets-received"):
                    self.ready_packets_received = value
                    self.ready_packets_received.value_namespace = name_space
                    self.ready_packets_received.value_namespace_prefix = name_space_prefix
                if(value_path == "reject-packets-sent"):
                    self.reject_packets_sent = value
                    self.reject_packets_sent.value_namespace = name_space
                    self.reject_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "secs-since-pkts-cleaned"):
                    self.secs_since_pkts_cleaned = value
                    self.secs_since_pkts_cleaned.value_namespace = name_space
                    self.secs_since_pkts_cleaned.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.icpe_dpm:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.icpe_dpm:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "icpe-dpm"):
                for c in self.icpe_dpm:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.IcpeDpms.IcpeDpm()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.icpe_dpm.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "icpe-dpm"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SdacpControls(Entity):
        """
        SDAC Protocol Discovery information table
        
        .. attribute:: sdacp_control
        
        	SDAC Protocol Discovery information
        	**type**\: list of    :py:class:`SdacpControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl>`
        
        

        """

        _prefix = 'icpe-sdacp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SdacpControls, self).__init__()

            self.yang_name = "sdacp-controls"
            self.yang_parent_name = "nv-satellite"

            self.sdacp_control = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellite.SdacpControls, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellite.SdacpControls, self).__setattr__(name, value)


        class SdacpControl(Entity):
            """
            SDAC Protocol Discovery information
            
            .. attribute:: satellite_id  <key>
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: channel
            
            	Channels on satellite table
            	**type**\: list of    :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel>`
            
            .. attribute:: control_protocol_state
            
            	Control protocol state
            	**type**\:   :py:class:`IcpeCpmControlFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.IcpeCpmControlFsmState>`
            
            .. attribute:: ip_address_auto
            
            	IP address auto
            	**type**\:  bool
            
            .. attribute:: protocol_state_timestamp
            
            	Timestamp
            	**type**\:   :py:class:`ProtocolStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp>`
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_ip_address
            
            	Satellite IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: transport_error
            
            	Transport error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: transport_error_timestamp
            
            	Timestamp
            	**type**\:   :py:class:`TransportErrorTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'icpe-sdacp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SdacpControls.SdacpControl, self).__init__()

                self.yang_name = "sdacp-control"
                self.yang_parent_name = "sdacp-controls"

                self.satellite_id = YLeaf(YType.uint32, "satellite-id")

                self.control_protocol_state = YLeaf(YType.enumeration, "control-protocol-state")

                self.ip_address_auto = YLeaf(YType.boolean, "ip-address-auto")

                self.satellite_id_xr = YLeaf(YType.uint32, "satellite-id-xr")

                self.satellite_ip_address = YLeaf(YType.str, "satellite-ip-address")

                self.transport_error = YLeaf(YType.uint32, "transport-error")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.protocol_state_timestamp = NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp()
                self.protocol_state_timestamp.parent = self
                self._children_name_map["protocol_state_timestamp"] = "protocol-state-timestamp"
                self._children_yang_names.add("protocol-state-timestamp")

                self.transport_error_timestamp = NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp()
                self.transport_error_timestamp.parent = self
                self._children_name_map["transport_error_timestamp"] = "transport-error-timestamp"
                self._children_yang_names.add("transport-error-timestamp")

                self.channel = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("satellite_id",
                                "control_protocol_state",
                                "ip_address_auto",
                                "satellite_id_xr",
                                "satellite_ip_address",
                                "transport_error",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellite.SdacpControls.SdacpControl, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellite.SdacpControls.SdacpControl, self).__setattr__(name, value)


            class ProtocolStateTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp, self).__init__()

                    self.yang_name = "protocol-state-timestamp"
                    self.yang_parent_name = "sdacp-control"

                    self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                    self.seconds = YLeaf(YType.uint32, "seconds")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nanoseconds",
                                    "seconds") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nanoseconds.is_set or
                        self.seconds.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nanoseconds.yfilter != YFilter.not_set or
                        self.seconds.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protocol-state-timestamp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                    if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nanoseconds" or name == "seconds"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nanoseconds"):
                        self.nanoseconds = value
                        self.nanoseconds.value_namespace = name_space
                        self.nanoseconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds"):
                        self.seconds = value
                        self.seconds.value_namespace = name_space
                        self.seconds.value_namespace_prefix = name_space_prefix


            class TransportErrorTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp, self).__init__()

                    self.yang_name = "transport-error-timestamp"
                    self.yang_parent_name = "sdacp-control"

                    self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                    self.seconds = YLeaf(YType.uint32, "seconds")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nanoseconds",
                                    "seconds") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nanoseconds.is_set or
                        self.seconds.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nanoseconds.yfilter != YFilter.not_set or
                        self.seconds.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transport-error-timestamp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                    if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nanoseconds" or name == "seconds"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nanoseconds"):
                        self.nanoseconds = value
                        self.nanoseconds.value_namespace = name_space
                        self.nanoseconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds"):
                        self.seconds = value
                        self.seconds.value_namespace = name_space
                        self.seconds.value_namespace_prefix = name_space_prefix


            class Channel(Entity):
                """
                Channels on satellite table
                
                .. attribute:: capabilities
                
                	Capabilities
                	**type**\:   :py:class:`Capabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities>`
                
                .. attribute:: channel_id
                
                	Channel ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: channel_state
                
                	Channel state
                	**type**\:   :py:class:`IcpeCpmChanFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.IcpeCpmChanFsmState>`
                
                .. attribute:: channel_state_timestamp
                
                	Timestamp
                	**type**\:   :py:class:`ChannelStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp>`
                
                .. attribute:: control_messages_dropped
                
                	Control messages dropped
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_received
                
                	Control messages received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_sent
                
                	Control messages sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_dropped
                
                	Normal messages dropped
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_received
                
                	Normal messages received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_sent
                
                	Normal messages sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: resync_state
                
                	Resync state
                	**type**\:   :py:class:`IcpeCpmChannelResyncState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.IcpeCpmChannelResyncState>`
                
                .. attribute:: resync_state_timestamp
                
                	Timestamp
                	**type**\:   :py:class:`ResyncStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp>`
                
                .. attribute:: secs_since_last_cleared
                
                	Secs since last cleared
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                .. attribute:: version
                
                	Version
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpControls.SdacpControl.Channel, self).__init__()

                    self.yang_name = "channel"
                    self.yang_parent_name = "sdacp-control"

                    self.channel_id = YLeaf(YType.uint16, "channel-id")

                    self.channel_state = YLeaf(YType.enumeration, "channel-state")

                    self.control_messages_dropped = YLeaf(YType.uint64, "control-messages-dropped")

                    self.control_messages_received = YLeaf(YType.uint64, "control-messages-received")

                    self.control_messages_sent = YLeaf(YType.uint64, "control-messages-sent")

                    self.normal_messages_dropped = YLeaf(YType.uint64, "normal-messages-dropped")

                    self.normal_messages_received = YLeaf(YType.uint64, "normal-messages-received")

                    self.normal_messages_sent = YLeaf(YType.uint64, "normal-messages-sent")

                    self.resync_state = YLeaf(YType.enumeration, "resync-state")

                    self.secs_since_last_cleared = YLeaf(YType.uint64, "secs-since-last-cleared")

                    self.version = YLeaf(YType.uint16, "version")

                    self.capabilities = NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities()
                    self.capabilities.parent = self
                    self._children_name_map["capabilities"] = "capabilities"
                    self._children_yang_names.add("capabilities")

                    self.channel_state_timestamp = NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp()
                    self.channel_state_timestamp.parent = self
                    self._children_name_map["channel_state_timestamp"] = "channel-state-timestamp"
                    self._children_yang_names.add("channel-state-timestamp")

                    self.resync_state_timestamp = NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp()
                    self.resync_state_timestamp.parent = self
                    self._children_name_map["resync_state_timestamp"] = "resync-state-timestamp"
                    self._children_yang_names.add("resync-state-timestamp")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("channel_id",
                                    "channel_state",
                                    "control_messages_dropped",
                                    "control_messages_received",
                                    "control_messages_sent",
                                    "normal_messages_dropped",
                                    "normal_messages_received",
                                    "normal_messages_sent",
                                    "resync_state",
                                    "secs_since_last_cleared",
                                    "version") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellite.SdacpControls.SdacpControl.Channel, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellite.SdacpControls.SdacpControl.Channel, self).__setattr__(name, value)


                class Capabilities(Entity):
                    """
                    Capabilities
                    
                    .. attribute:: tl_vs
                    
                    	Capability TLVs table
                    	**type**\: list of    :py:class:`TlVs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs>`
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities, self).__init__()

                        self.yang_name = "capabilities"
                        self.yang_parent_name = "channel"

                        self.tl_vs = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities, self).__setattr__(name, value)


                    class TlVs(Entity):
                        """
                        Capability TLVs table
                        
                        .. attribute:: debug
                        
                        	Debug
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: value
                        
                        	Value
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'icpe-sdacp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs, self).__init__()

                            self.yang_name = "tl-vs"
                            self.yang_parent_name = "capabilities"

                            self.debug = YLeaf(YType.str, "debug")

                            self.type = YLeaf(YType.uint32, "type")

                            self.value = YLeafList(YType.uint8, "value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("debug",
                                            "type",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.value.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return (
                                self.debug.is_set or
                                self.type.is_set)

                        def has_operation(self):
                            for leaf in self.value.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.debug.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tl-vs" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.debug.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            leaf_name_data.extend(self.value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "debug" or name == "type" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "debug"):
                                self.debug = value
                                self.debug.value_namespace = name_space
                                self.debug.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value.append(value)

                    def has_data(self):
                        for c in self.tl_vs:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.tl_vs:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "capabilities" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "tl-vs"):
                            for c in self.tl_vs:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.tl_vs.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tl-vs"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ResyncStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp, self).__init__()

                        self.yang_name = "resync-state-timestamp"
                        self.yang_parent_name = "channel"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resync-state-timestamp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class ChannelStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp, self).__init__()

                        self.yang_name = "channel-state-timestamp"
                        self.yang_parent_name = "channel"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "channel-state-timestamp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.channel_id.is_set or
                        self.channel_state.is_set or
                        self.control_messages_dropped.is_set or
                        self.control_messages_received.is_set or
                        self.control_messages_sent.is_set or
                        self.normal_messages_dropped.is_set or
                        self.normal_messages_received.is_set or
                        self.normal_messages_sent.is_set or
                        self.resync_state.is_set or
                        self.secs_since_last_cleared.is_set or
                        self.version.is_set or
                        (self.capabilities is not None and self.capabilities.has_data()) or
                        (self.channel_state_timestamp is not None and self.channel_state_timestamp.has_data()) or
                        (self.resync_state_timestamp is not None and self.resync_state_timestamp.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.channel_id.yfilter != YFilter.not_set or
                        self.channel_state.yfilter != YFilter.not_set or
                        self.control_messages_dropped.yfilter != YFilter.not_set or
                        self.control_messages_received.yfilter != YFilter.not_set or
                        self.control_messages_sent.yfilter != YFilter.not_set or
                        self.normal_messages_dropped.yfilter != YFilter.not_set or
                        self.normal_messages_received.yfilter != YFilter.not_set or
                        self.normal_messages_sent.yfilter != YFilter.not_set or
                        self.resync_state.yfilter != YFilter.not_set or
                        self.secs_since_last_cleared.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        (self.capabilities is not None and self.capabilities.has_operation()) or
                        (self.channel_state_timestamp is not None and self.channel_state_timestamp.has_operation()) or
                        (self.resync_state_timestamp is not None and self.resync_state_timestamp.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "channel" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.channel_id.is_set or self.channel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.channel_id.get_name_leafdata())
                    if (self.channel_state.is_set or self.channel_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.channel_state.get_name_leafdata())
                    if (self.control_messages_dropped.is_set or self.control_messages_dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.control_messages_dropped.get_name_leafdata())
                    if (self.control_messages_received.is_set or self.control_messages_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.control_messages_received.get_name_leafdata())
                    if (self.control_messages_sent.is_set or self.control_messages_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.control_messages_sent.get_name_leafdata())
                    if (self.normal_messages_dropped.is_set or self.normal_messages_dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.normal_messages_dropped.get_name_leafdata())
                    if (self.normal_messages_received.is_set or self.normal_messages_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.normal_messages_received.get_name_leafdata())
                    if (self.normal_messages_sent.is_set or self.normal_messages_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.normal_messages_sent.get_name_leafdata())
                    if (self.resync_state.is_set or self.resync_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resync_state.get_name_leafdata())
                    if (self.secs_since_last_cleared.is_set or self.secs_since_last_cleared.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secs_since_last_cleared.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "capabilities"):
                        if (self.capabilities is None):
                            self.capabilities = NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities()
                            self.capabilities.parent = self
                            self._children_name_map["capabilities"] = "capabilities"
                        return self.capabilities

                    if (child_yang_name == "channel-state-timestamp"):
                        if (self.channel_state_timestamp is None):
                            self.channel_state_timestamp = NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp()
                            self.channel_state_timestamp.parent = self
                            self._children_name_map["channel_state_timestamp"] = "channel-state-timestamp"
                        return self.channel_state_timestamp

                    if (child_yang_name == "resync-state-timestamp"):
                        if (self.resync_state_timestamp is None):
                            self.resync_state_timestamp = NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp()
                            self.resync_state_timestamp.parent = self
                            self._children_name_map["resync_state_timestamp"] = "resync-state-timestamp"
                        return self.resync_state_timestamp

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "capabilities" or name == "channel-state-timestamp" or name == "resync-state-timestamp" or name == "channel-id" or name == "channel-state" or name == "control-messages-dropped" or name == "control-messages-received" or name == "control-messages-sent" or name == "normal-messages-dropped" or name == "normal-messages-received" or name == "normal-messages-sent" or name == "resync-state" or name == "secs-since-last-cleared" or name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "channel-id"):
                        self.channel_id = value
                        self.channel_id.value_namespace = name_space
                        self.channel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "channel-state"):
                        self.channel_state = value
                        self.channel_state.value_namespace = name_space
                        self.channel_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "control-messages-dropped"):
                        self.control_messages_dropped = value
                        self.control_messages_dropped.value_namespace = name_space
                        self.control_messages_dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "control-messages-received"):
                        self.control_messages_received = value
                        self.control_messages_received.value_namespace = name_space
                        self.control_messages_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "control-messages-sent"):
                        self.control_messages_sent = value
                        self.control_messages_sent.value_namespace = name_space
                        self.control_messages_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "normal-messages-dropped"):
                        self.normal_messages_dropped = value
                        self.normal_messages_dropped.value_namespace = name_space
                        self.normal_messages_dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "normal-messages-received"):
                        self.normal_messages_received = value
                        self.normal_messages_received.value_namespace = name_space
                        self.normal_messages_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "normal-messages-sent"):
                        self.normal_messages_sent = value
                        self.normal_messages_sent.value_namespace = name_space
                        self.normal_messages_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "resync-state"):
                        self.resync_state = value
                        self.resync_state.value_namespace = name_space
                        self.resync_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "secs-since-last-cleared"):
                        self.secs_since_last_cleared = value
                        self.secs_since_last_cleared.value_namespace = name_space
                        self.secs_since_last_cleared.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.channel:
                    if (c.has_data()):
                        return True
                return (
                    self.satellite_id.is_set or
                    self.control_protocol_state.is_set or
                    self.ip_address_auto.is_set or
                    self.satellite_id_xr.is_set or
                    self.satellite_ip_address.is_set or
                    self.transport_error.is_set or
                    self.vrf_name.is_set or
                    (self.protocol_state_timestamp is not None and self.protocol_state_timestamp.has_data()) or
                    (self.transport_error_timestamp is not None and self.transport_error_timestamp.has_data()))

            def has_operation(self):
                for c in self.channel:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.satellite_id.yfilter != YFilter.not_set or
                    self.control_protocol_state.yfilter != YFilter.not_set or
                    self.ip_address_auto.yfilter != YFilter.not_set or
                    self.satellite_id_xr.yfilter != YFilter.not_set or
                    self.satellite_ip_address.yfilter != YFilter.not_set or
                    self.transport_error.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.protocol_state_timestamp is not None and self.protocol_state_timestamp.has_operation()) or
                    (self.transport_error_timestamp is not None and self.transport_error_timestamp.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sdacp-control" + "[satellite-id='" + self.satellite_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id.get_name_leafdata())
                if (self.control_protocol_state.is_set or self.control_protocol_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.control_protocol_state.get_name_leafdata())
                if (self.ip_address_auto.is_set or self.ip_address_auto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip_address_auto.get_name_leafdata())
                if (self.satellite_id_xr.is_set or self.satellite_id_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_id_xr.get_name_leafdata())
                if (self.satellite_ip_address.is_set or self.satellite_ip_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.satellite_ip_address.get_name_leafdata())
                if (self.transport_error.is_set or self.transport_error.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transport_error.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "channel"):
                    for c in self.channel:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellite.SdacpControls.SdacpControl.Channel()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.channel.append(c)
                    return c

                if (child_yang_name == "protocol-state-timestamp"):
                    if (self.protocol_state_timestamp is None):
                        self.protocol_state_timestamp = NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp()
                        self.protocol_state_timestamp.parent = self
                        self._children_name_map["protocol_state_timestamp"] = "protocol-state-timestamp"
                    return self.protocol_state_timestamp

                if (child_yang_name == "transport-error-timestamp"):
                    if (self.transport_error_timestamp is None):
                        self.transport_error_timestamp = NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp()
                        self.transport_error_timestamp.parent = self
                        self._children_name_map["transport_error_timestamp"] = "transport-error-timestamp"
                    return self.transport_error_timestamp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "channel" or name == "protocol-state-timestamp" or name == "transport-error-timestamp" or name == "satellite-id" or name == "control-protocol-state" or name == "ip-address-auto" or name == "satellite-id-xr" or name == "satellite-ip-address" or name == "transport-error" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "satellite-id"):
                    self.satellite_id = value
                    self.satellite_id.value_namespace = name_space
                    self.satellite_id.value_namespace_prefix = name_space_prefix
                if(value_path == "control-protocol-state"):
                    self.control_protocol_state = value
                    self.control_protocol_state.value_namespace = name_space
                    self.control_protocol_state.value_namespace_prefix = name_space_prefix
                if(value_path == "ip-address-auto"):
                    self.ip_address_auto = value
                    self.ip_address_auto.value_namespace = name_space
                    self.ip_address_auto.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-id-xr"):
                    self.satellite_id_xr = value
                    self.satellite_id_xr.value_namespace = name_space
                    self.satellite_id_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "satellite-ip-address"):
                    self.satellite_ip_address = value
                    self.satellite_ip_address.value_namespace = name_space
                    self.satellite_ip_address.value_namespace_prefix = name_space_prefix
                if(value_path == "transport-error"):
                    self.transport_error = value
                    self.transport_error.value_namespace = name_space
                    self.transport_error.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sdacp_control:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sdacp_control:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sdacp-control"):
                for c in self.sdacp_control:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvSatellite.SdacpControls.SdacpControl()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sdacp_control.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sdacp-control"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.icpe_dpms is not None and self.icpe_dpms.has_data()) or
            (self.install is not None and self.install.has_data()) or
            (self.install_op_statuses is not None and self.install_op_statuses.has_data()) or
            (self.install_progresses is not None and self.install_progresses.has_data()) or
            (self.install_shows is not None and self.install_shows.has_data()) or
            (self.install_statuses is not None and self.install_statuses.has_data()) or
            (self.reload_op_statuses is not None and self.reload_op_statuses.has_data()) or
            (self.reload_statuses is not None and self.reload_statuses.has_data()) or
            (self.satellite_priorities is not None and self.satellite_priorities.has_data()) or
            (self.satellite_properties is not None and self.satellite_properties.has_data()) or
            (self.satellite_statuses is not None and self.satellite_statuses.has_data()) or
            (self.satellite_topologies is not None and self.satellite_topologies.has_data()) or
            (self.satellite_versions is not None and self.satellite_versions.has_data()) or
            (self.sdacp_controls is not None and self.sdacp_controls.has_data()) or
            (self.sdacp_discovery2s is not None and self.sdacp_discovery2s.has_data()) or
            (self.sdacp_redundancies is not None and self.sdacp_redundancies.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.icpe_dpms is not None and self.icpe_dpms.has_operation()) or
            (self.install is not None and self.install.has_operation()) or
            (self.install_op_statuses is not None and self.install_op_statuses.has_operation()) or
            (self.install_progresses is not None and self.install_progresses.has_operation()) or
            (self.install_shows is not None and self.install_shows.has_operation()) or
            (self.install_statuses is not None and self.install_statuses.has_operation()) or
            (self.reload_op_statuses is not None and self.reload_op_statuses.has_operation()) or
            (self.reload_statuses is not None and self.reload_statuses.has_operation()) or
            (self.satellite_priorities is not None and self.satellite_priorities.has_operation()) or
            (self.satellite_properties is not None and self.satellite_properties.has_operation()) or
            (self.satellite_statuses is not None and self.satellite_statuses.has_operation()) or
            (self.satellite_topologies is not None and self.satellite_topologies.has_operation()) or
            (self.satellite_versions is not None and self.satellite_versions.has_operation()) or
            (self.sdacp_controls is not None and self.sdacp_controls.has_operation()) or
            (self.sdacp_discovery2s is not None and self.sdacp_discovery2s.has_operation()) or
            (self.sdacp_redundancies is not None and self.sdacp_redundancies.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-icpe-infra-oper:nv-satellite" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "icpe-dpms"):
            if (self.icpe_dpms is None):
                self.icpe_dpms = NvSatellite.IcpeDpms()
                self.icpe_dpms.parent = self
                self._children_name_map["icpe_dpms"] = "icpe-dpms"
            return self.icpe_dpms

        if (child_yang_name == "install"):
            if (self.install is None):
                self.install = NvSatellite.Install()
                self.install.parent = self
                self._children_name_map["install"] = "install"
            return self.install

        if (child_yang_name == "install-op-statuses"):
            if (self.install_op_statuses is None):
                self.install_op_statuses = NvSatellite.InstallOpStatuses()
                self.install_op_statuses.parent = self
                self._children_name_map["install_op_statuses"] = "install-op-statuses"
            return self.install_op_statuses

        if (child_yang_name == "install-progresses"):
            if (self.install_progresses is None):
                self.install_progresses = NvSatellite.InstallProgresses()
                self.install_progresses.parent = self
                self._children_name_map["install_progresses"] = "install-progresses"
            return self.install_progresses

        if (child_yang_name == "install-shows"):
            if (self.install_shows is None):
                self.install_shows = NvSatellite.InstallShows()
                self.install_shows.parent = self
                self._children_name_map["install_shows"] = "install-shows"
            return self.install_shows

        if (child_yang_name == "install-statuses"):
            if (self.install_statuses is None):
                self.install_statuses = NvSatellite.InstallStatuses()
                self.install_statuses.parent = self
                self._children_name_map["install_statuses"] = "install-statuses"
            return self.install_statuses

        if (child_yang_name == "reload-op-statuses"):
            if (self.reload_op_statuses is None):
                self.reload_op_statuses = NvSatellite.ReloadOpStatuses()
                self.reload_op_statuses.parent = self
                self._children_name_map["reload_op_statuses"] = "reload-op-statuses"
            return self.reload_op_statuses

        if (child_yang_name == "reload-statuses"):
            if (self.reload_statuses is None):
                self.reload_statuses = NvSatellite.ReloadStatuses()
                self.reload_statuses.parent = self
                self._children_name_map["reload_statuses"] = "reload-statuses"
            return self.reload_statuses

        if (child_yang_name == "satellite-priorities"):
            if (self.satellite_priorities is None):
                self.satellite_priorities = NvSatellite.SatellitePriorities()
                self.satellite_priorities.parent = self
                self._children_name_map["satellite_priorities"] = "satellite-priorities"
            return self.satellite_priorities

        if (child_yang_name == "satellite-properties"):
            if (self.satellite_properties is None):
                self.satellite_properties = NvSatellite.SatelliteProperties()
                self.satellite_properties.parent = self
                self._children_name_map["satellite_properties"] = "satellite-properties"
            return self.satellite_properties

        if (child_yang_name == "satellite-statuses"):
            if (self.satellite_statuses is None):
                self.satellite_statuses = NvSatellite.SatelliteStatuses()
                self.satellite_statuses.parent = self
                self._children_name_map["satellite_statuses"] = "satellite-statuses"
            return self.satellite_statuses

        if (child_yang_name == "satellite-topologies"):
            if (self.satellite_topologies is None):
                self.satellite_topologies = NvSatellite.SatelliteTopologies()
                self.satellite_topologies.parent = self
                self._children_name_map["satellite_topologies"] = "satellite-topologies"
            return self.satellite_topologies

        if (child_yang_name == "satellite-versions"):
            if (self.satellite_versions is None):
                self.satellite_versions = NvSatellite.SatelliteVersions()
                self.satellite_versions.parent = self
                self._children_name_map["satellite_versions"] = "satellite-versions"
            return self.satellite_versions

        if (child_yang_name == "sdacp-controls"):
            if (self.sdacp_controls is None):
                self.sdacp_controls = NvSatellite.SdacpControls()
                self.sdacp_controls.parent = self
                self._children_name_map["sdacp_controls"] = "sdacp-controls"
            return self.sdacp_controls

        if (child_yang_name == "sdacp-discovery2s"):
            if (self.sdacp_discovery2s is None):
                self.sdacp_discovery2s = NvSatellite.SdacpDiscovery2S()
                self.sdacp_discovery2s.parent = self
                self._children_name_map["sdacp_discovery2s"] = "sdacp-discovery2s"
            return self.sdacp_discovery2s

        if (child_yang_name == "sdacp-redundancies"):
            if (self.sdacp_redundancies is None):
                self.sdacp_redundancies = NvSatellite.SdacpRedundancies()
                self.sdacp_redundancies.parent = self
                self._children_name_map["sdacp_redundancies"] = "sdacp-redundancies"
            return self.sdacp_redundancies

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "icpe-dpms" or name == "install" or name == "install-op-statuses" or name == "install-progresses" or name == "install-shows" or name == "install-statuses" or name == "reload-op-statuses" or name == "reload-statuses" or name == "satellite-priorities" or name == "satellite-properties" or name == "satellite-statuses" or name == "satellite-topologies" or name == "satellite-versions" or name == "sdacp-controls" or name == "sdacp-discovery2s" or name == "sdacp-redundancies"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NvSatellite()
        return self._top_entity

