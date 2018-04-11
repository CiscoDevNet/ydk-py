""" Cisco_IOS_XR_icpe_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package operational data.

This module contains definitions
for the following management objects\:
  nv\-satellite\: Satellite operational information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IcpeGcoOperControlReason(Enum):
    """
    IcpeGcoOperControlReason (Enum Class)

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
    IcpeInstallPkgSupp (Enum Class)

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
    IcpeInstallSatState (Enum Class)

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

    .. data:: icpe_install_sat_state_sat_uncfgd = 15

    	Sat uncfgd

    .. data:: icpe_install_sat_state_processing = 16

    	Processing

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

    icpe_install_sat_state_sat_uncfgd = Enum.YLeaf(15, "icpe-install-sat-state-sat-uncfgd")

    icpe_install_sat_state_processing = Enum.YLeaf(16, "icpe-install-sat-state-processing")


class IcpeOperConflict(Enum):
    """
    IcpeOperConflict (Enum Class)

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
    IcpeOperDiscdLinkState (Enum Class)

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
    IcpeOperFabricPort (Enum Class)

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
    IcpeOperInstallState (Enum Class)

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
    IcpeOperMultichassisRedundancy (Enum Class)

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
    IcpeOperPort (Enum Class)

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
    IcpeOperSdacpSessState (Enum Class)

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
    IcpeOperTopoRemoteSource (Enum Class)

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
    IcpeOperVerCheckState (Enum Class)

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
    IcpeOpmArbitrationFsmState (Enum Class)

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
    IcpeOpmAuthFsmState (Enum Class)

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
    IcpeOpmChanFsmState (Enum Class)

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
    IcpeOpmController (Enum Class)

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
    IcpeOpmResyncFsmState (Enum Class)

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
    IcpeOpmSessState (Enum Class)

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
    IcpeOpmSyncFsmState (Enum Class)

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
    IcpeOpmTransportState (Enum Class)

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
    IcpeOpticalSyncState (Enum Class)

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
    
    .. attribute:: reload_op_statuses
    
    	Detailed breakdown of reload status table
    	**type**\:  :py:class:`ReloadOpStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadOpStatuses>`
    
    .. attribute:: sdacp_redundancies
    
    	nV Satellite Redundancy Protocol Information table
    	**type**\:  :py:class:`SdacpRedundancies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies>`
    
    .. attribute:: install_shows
    
    	Detailed breakdown of install status table
    	**type**\:  :py:class:`InstallShows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallShows>`
    
    .. attribute:: satellite_statuses
    
    	Satellite status information table
    	**type**\:  :py:class:`SatelliteStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses>`
    
    .. attribute:: satellite_priorities
    
    	Satellite priority information table
    	**type**\:  :py:class:`SatellitePriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatellitePriorities>`
    
    .. attribute:: satellite_versions
    
    	Satellite remote version information table
    	**type**\:  :py:class:`SatelliteVersions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions>`
    
    .. attribute:: satellite_topologies
    
    	Satellite Topology Information table
    	**type**\:  :py:class:`SatelliteTopologies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies>`
    
    .. attribute:: install_reference_info
    
    	Satellite Install Reference Information
    	**type**\:  :py:class:`InstallReferenceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallReferenceInfo>`
    
    .. attribute:: install_op_progresses
    
    	Current percentage of install table
    	**type**\:  :py:class:`InstallOpProgresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpProgresses>`
    
    .. attribute:: reload_statuses
    
    	Detailed breakdown of reload status table
    	**type**\:  :py:class:`ReloadStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses>`
    
    .. attribute:: install
    
    	Satellite Install Information
    	**type**\:  :py:class:`Install <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install>`
    
    .. attribute:: install_op_statuses
    
    	Detailed breakdown of install status table
    	**type**\:  :py:class:`InstallOpStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses>`
    
    .. attribute:: satellite_properties
    
    	ICPE GCO operational information
    	**type**\:  :py:class:`SatelliteProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteProperties>`
    
    .. attribute:: sdacp_discovery2s
    
    	ICPE Configured interface state information table
    	**type**\:  :py:class:`SdacpDiscovery2S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S>`
    
    .. attribute:: icpe_dpms
    
    	ICPE DPM operational information table
    	**type**\:  :py:class:`IcpeDpms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms>`
    
    .. attribute:: sdacp_controls
    
    	SDAC Protocol Discovery information table
    	**type**\:  :py:class:`SdacpControls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls>`
    
    

    """

    _prefix = 'icpe-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(NvSatellite, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellite"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("reload-op-statuses", ("reload_op_statuses", NvSatellite.ReloadOpStatuses)), ("sdacp-redundancies", ("sdacp_redundancies", NvSatellite.SdacpRedundancies)), ("install-shows", ("install_shows", NvSatellite.InstallShows)), ("satellite-statuses", ("satellite_statuses", NvSatellite.SatelliteStatuses)), ("satellite-priorities", ("satellite_priorities", NvSatellite.SatellitePriorities)), ("satellite-versions", ("satellite_versions", NvSatellite.SatelliteVersions)), ("satellite-topologies", ("satellite_topologies", NvSatellite.SatelliteTopologies)), ("install-reference-info", ("install_reference_info", NvSatellite.InstallReferenceInfo)), ("install-op-progresses", ("install_op_progresses", NvSatellite.InstallOpProgresses)), ("reload-statuses", ("reload_statuses", NvSatellite.ReloadStatuses)), ("install", ("install", NvSatellite.Install)), ("install-op-statuses", ("install_op_statuses", NvSatellite.InstallOpStatuses)), ("satellite-properties", ("satellite_properties", NvSatellite.SatelliteProperties)), ("Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s", ("sdacp_discovery2s", NvSatellite.SdacpDiscovery2S)), ("Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms", ("icpe_dpms", NvSatellite.IcpeDpms)), ("Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls", ("sdacp_controls", NvSatellite.SdacpControls))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.reload_op_statuses = NvSatellite.ReloadOpStatuses()
        self.reload_op_statuses.parent = self
        self._children_name_map["reload_op_statuses"] = "reload-op-statuses"
        self._children_yang_names.add("reload-op-statuses")

        self.sdacp_redundancies = NvSatellite.SdacpRedundancies()
        self.sdacp_redundancies.parent = self
        self._children_name_map["sdacp_redundancies"] = "sdacp-redundancies"
        self._children_yang_names.add("sdacp-redundancies")

        self.install_shows = NvSatellite.InstallShows()
        self.install_shows.parent = self
        self._children_name_map["install_shows"] = "install-shows"
        self._children_yang_names.add("install-shows")

        self.satellite_statuses = NvSatellite.SatelliteStatuses()
        self.satellite_statuses.parent = self
        self._children_name_map["satellite_statuses"] = "satellite-statuses"
        self._children_yang_names.add("satellite-statuses")

        self.satellite_priorities = NvSatellite.SatellitePriorities()
        self.satellite_priorities.parent = self
        self._children_name_map["satellite_priorities"] = "satellite-priorities"
        self._children_yang_names.add("satellite-priorities")

        self.satellite_versions = NvSatellite.SatelliteVersions()
        self.satellite_versions.parent = self
        self._children_name_map["satellite_versions"] = "satellite-versions"
        self._children_yang_names.add("satellite-versions")

        self.satellite_topologies = NvSatellite.SatelliteTopologies()
        self.satellite_topologies.parent = self
        self._children_name_map["satellite_topologies"] = "satellite-topologies"
        self._children_yang_names.add("satellite-topologies")

        self.install_reference_info = NvSatellite.InstallReferenceInfo()
        self.install_reference_info.parent = self
        self._children_name_map["install_reference_info"] = "install-reference-info"
        self._children_yang_names.add("install-reference-info")

        self.install_op_progresses = NvSatellite.InstallOpProgresses()
        self.install_op_progresses.parent = self
        self._children_name_map["install_op_progresses"] = "install-op-progresses"
        self._children_yang_names.add("install-op-progresses")

        self.reload_statuses = NvSatellite.ReloadStatuses()
        self.reload_statuses.parent = self
        self._children_name_map["reload_statuses"] = "reload-statuses"
        self._children_yang_names.add("reload-statuses")

        self.install = NvSatellite.Install()
        self.install.parent = self
        self._children_name_map["install"] = "install"
        self._children_yang_names.add("install")

        self.install_op_statuses = NvSatellite.InstallOpStatuses()
        self.install_op_statuses.parent = self
        self._children_name_map["install_op_statuses"] = "install-op-statuses"
        self._children_yang_names.add("install-op-statuses")

        self.satellite_properties = NvSatellite.SatelliteProperties()
        self.satellite_properties.parent = self
        self._children_name_map["satellite_properties"] = "satellite-properties"
        self._children_yang_names.add("satellite-properties")

        self.sdacp_discovery2s = NvSatellite.SdacpDiscovery2S()
        self.sdacp_discovery2s.parent = self
        self._children_name_map["sdacp_discovery2s"] = "Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s"
        self._children_yang_names.add("Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s")

        self.icpe_dpms = NvSatellite.IcpeDpms()
        self.icpe_dpms.parent = self
        self._children_name_map["icpe_dpms"] = "Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms"
        self._children_yang_names.add("Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms")

        self.sdacp_controls = NvSatellite.SdacpControls()
        self.sdacp_controls.parent = self
        self._children_name_map["sdacp_controls"] = "Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls"
        self._children_yang_names.add("Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls")
        self._segment_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite"


    class ReloadOpStatuses(Entity):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_op_status
        
        	Detailed breakdown of reload status
        	**type**\: list of  		 :py:class:`ReloadOpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadOpStatuses.ReloadOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.ReloadOpStatuses, self).__init__()

            self.yang_name = "reload-op-statuses"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("reload-op-status", ("reload_op_status", NvSatellite.ReloadOpStatuses.ReloadOpStatus))])
            self._leafs = OrderedDict()

            self.reload_op_status = YList(self)
            self._segment_path = lambda: "reload-op-statuses"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.ReloadOpStatuses, [], name, value)


        class ReloadOpStatus(Entity):
            """
            Detailed breakdown of reload status
            
            .. attribute:: operation_id  (key)
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloading
            
            	Sats reloading
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloaded
            
            	Sats reloaded
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reload_failed
            
            	Sats reload failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.ReloadOpStatuses.ReloadOpStatus, self).__init__()

                self.yang_name = "reload-op-status"
                self.yang_parent_name = "reload-op-statuses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['operation_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('operation_id', YLeaf(YType.uint32, 'operation-id')),
                    ('operation_id_xr', YLeaf(YType.uint32, 'operation-id-xr')),
                    ('satellite_range', YLeaf(YType.str, 'satellite-range')),
                    ('sats_not_initiated', YLeafList(YType.uint16, 'sats-not-initiated')),
                    ('sats_reloading', YLeafList(YType.uint16, 'sats-reloading')),
                    ('sats_reloaded', YLeafList(YType.uint16, 'sats-reloaded')),
                    ('sats_reload_failed', YLeafList(YType.uint16, 'sats-reload-failed')),
                ])
                self.operation_id = None
                self.operation_id_xr = None
                self.satellite_range = None
                self.sats_not_initiated = []
                self.sats_reloading = []
                self.sats_reloaded = []
                self.sats_reload_failed = []
                self._segment_path = lambda: "reload-op-status" + "[operation-id='" + str(self.operation_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/reload-op-statuses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.ReloadOpStatuses.ReloadOpStatus, ['operation_id', 'operation_id_xr', 'satellite_range', 'sats_not_initiated', 'sats_reloading', 'sats_reloaded', 'sats_reload_failed'], name, value)


    class SdacpRedundancies(Entity):
        """
        nV Satellite Redundancy Protocol Information
        table
        
        .. attribute:: sdacp_redundancy
        
        	nV Satellite Redundancy Protocol Information
        	**type**\: list of  		 :py:class:`SdacpRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SdacpRedundancies, self).__init__()

            self.yang_name = "sdacp-redundancies"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sdacp-redundancy", ("sdacp_redundancy", NvSatellite.SdacpRedundancies.SdacpRedundancy))])
            self._leafs = OrderedDict()

            self.sdacp_redundancy = YList(self)
            self._segment_path = lambda: "sdacp-redundancies"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SdacpRedundancies, [], name, value)


        class SdacpRedundancy(Entity):
            """
            nV Satellite Redundancy Protocol Information
            
            .. attribute:: iccp_group  (key)
            
            	ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocol_state_timestamp
            
            	Timestamp
            	**type**\:  :py:class:`ProtocolStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp>`
            
            .. attribute:: iccp_group_xr
            
            	ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocol_state
            
            	Protocol state
            	**type**\:  :py:class:`IcpeOpmSessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSessState>`
            
            .. attribute:: transport_state
            
            	Transport state
            	**type**\:  :py:class:`IcpeOpmTransportState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmTransportState>`
            
            .. attribute:: authentication_state
            
            	Authentication state
            	**type**\:  :py:class:`IcpeOpmAuthFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmAuthFsmState>`
            
            .. attribute:: arbitration_state
            
            	Arbitration state
            	**type**\:  :py:class:`IcpeOpmArbitrationFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmArbitrationFsmState>`
            
            .. attribute:: synchronization_state
            
            	Synchronization state
            	**type**\:  :py:class:`IcpeOpmSyncFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSyncFsmState>`
            
            .. attribute:: primacy
            
            	Primacy
            	**type**\:  :py:class:`IcpeOpmController <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmController>`
            
            .. attribute:: system_mac
            
            	System MAC
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: isolated
            
            	Isolated
            	**type**\: bool
            
            .. attribute:: channel
            
            	Channels on this session table
            	**type**\: list of  		 :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SdacpRedundancies.SdacpRedundancy, self).__init__()

                self.yang_name = "sdacp-redundancy"
                self.yang_parent_name = "sdacp-redundancies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['iccp_group']
                self._child_container_classes = OrderedDict([("protocol-state-timestamp", ("protocol_state_timestamp", NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp))])
                self._child_list_classes = OrderedDict([("channel", ("channel", NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel))])
                self._leafs = OrderedDict([
                    ('iccp_group', YLeaf(YType.uint32, 'iccp-group')),
                    ('iccp_group_xr', YLeaf(YType.uint32, 'iccp-group-xr')),
                    ('protocol_state', YLeaf(YType.enumeration, 'protocol-state')),
                    ('transport_state', YLeaf(YType.enumeration, 'transport-state')),
                    ('authentication_state', YLeaf(YType.enumeration, 'authentication-state')),
                    ('arbitration_state', YLeaf(YType.enumeration, 'arbitration-state')),
                    ('synchronization_state', YLeaf(YType.enumeration, 'synchronization-state')),
                    ('primacy', YLeaf(YType.enumeration, 'primacy')),
                    ('system_mac', YLeaf(YType.str, 'system-mac')),
                    ('isolated', YLeaf(YType.boolean, 'isolated')),
                ])
                self.iccp_group = None
                self.iccp_group_xr = None
                self.protocol_state = None
                self.transport_state = None
                self.authentication_state = None
                self.arbitration_state = None
                self.synchronization_state = None
                self.primacy = None
                self.system_mac = None
                self.isolated = None

                self.protocol_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp()
                self.protocol_state_timestamp.parent = self
                self._children_name_map["protocol_state_timestamp"] = "protocol-state-timestamp"
                self._children_yang_names.add("protocol-state-timestamp")

                self.channel = YList(self)
                self._segment_path = lambda: "sdacp-redundancy" + "[iccp-group='" + str(self.iccp_group) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/sdacp-redundancies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SdacpRedundancies.SdacpRedundancy, ['iccp_group', 'iccp_group_xr', 'protocol_state', 'transport_state', 'authentication_state', 'arbitration_state', 'synchronization_state', 'primacy', 'system_mac', 'isolated'], name, value)


            class ProtocolStateTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp, self).__init__()

                    self.yang_name = "protocol-state-timestamp"
                    self.yang_parent_name = "sdacp-redundancy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                        ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                    ])
                    self.seconds = None
                    self.nanoseconds = None
                    self._segment_path = lambda: "protocol-state-timestamp"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp, ['seconds', 'nanoseconds'], name, value)


            class Channel(Entity):
                """
                Channels on this session table
                
                .. attribute:: channel_state_timestamp
                
                	Timestamp
                	**type**\:  :py:class:`ChannelStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp>`
                
                .. attribute:: resync_state_timestamp
                
                	Timestamp
                	**type**\:  :py:class:`ResyncStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp>`
                
                .. attribute:: channel_id
                
                	Channel ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: chan_state
                
                	Chan state
                	**type**\:  :py:class:`IcpeOpmChanFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmChanFsmState>`
                
                .. attribute:: resync_state
                
                	Resync state
                	**type**\:  :py:class:`IcpeOpmResyncFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmResyncFsmState>`
                
                .. attribute:: control_messages_sent
                
                	Control messages sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_sent
                
                	Normal messages sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_received
                
                	Control messages received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_received
                
                	Normal messages received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel, self).__init__()

                    self.yang_name = "channel"
                    self.yang_parent_name = "sdacp-redundancy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("channel-state-timestamp", ("channel_state_timestamp", NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp)), ("resync-state-timestamp", ("resync_state_timestamp", NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('channel_id', YLeaf(YType.uint32, 'channel-id')),
                        ('chan_state', YLeaf(YType.enumeration, 'chan-state')),
                        ('resync_state', YLeaf(YType.enumeration, 'resync-state')),
                        ('control_messages_sent', YLeaf(YType.uint64, 'control-messages-sent')),
                        ('normal_messages_sent', YLeaf(YType.uint64, 'normal-messages-sent')),
                        ('control_messages_received', YLeaf(YType.uint64, 'control-messages-received')),
                        ('normal_messages_received', YLeaf(YType.uint64, 'normal-messages-received')),
                    ])
                    self.channel_id = None
                    self.chan_state = None
                    self.resync_state = None
                    self.control_messages_sent = None
                    self.normal_messages_sent = None
                    self.control_messages_received = None
                    self.normal_messages_received = None

                    self.channel_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp()
                    self.channel_state_timestamp.parent = self
                    self._children_name_map["channel_state_timestamp"] = "channel-state-timestamp"
                    self._children_yang_names.add("channel-state-timestamp")

                    self.resync_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp()
                    self.resync_state_timestamp.parent = self
                    self._children_name_map["resync_state_timestamp"] = "resync-state-timestamp"
                    self._children_yang_names.add("resync-state-timestamp")
                    self._segment_path = lambda: "channel"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel, ['channel_id', 'chan_state', 'resync_state', 'control_messages_sent', 'normal_messages_sent', 'control_messages_received', 'normal_messages_received'], name, value)


                class ChannelStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp, self).__init__()

                        self.yang_name = "channel-state-timestamp"
                        self.yang_parent_name = "channel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', YLeaf(YType.uint32, 'seconds')),
                            ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "channel-state-timestamp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp, ['seconds', 'nanoseconds'], name, value)


                class ResyncStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp, self).__init__()

                        self.yang_name = "resync-state-timestamp"
                        self.yang_parent_name = "channel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', YLeaf(YType.uint32, 'seconds')),
                            ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "resync-state-timestamp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp, ['seconds', 'nanoseconds'], name, value)


    class InstallShows(Entity):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_show
        
        	Detailed breakdown of install status
        	**type**\: list of  		 :py:class:`InstallShow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallShows.InstallShow>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallShows, self).__init__()

            self.yang_name = "install-shows"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("install-show", ("install_show", NvSatellite.InstallShows.InstallShow))])
            self._leafs = OrderedDict()

            self.install_show = YList(self)
            self._segment_path = lambda: "install-shows"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.InstallShows, [], name, value)


        class InstallShow(Entity):
            """
            Detailed breakdown of install status
            
            .. attribute:: operation_id  (key)
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: operation_type
            
            	Operation type
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: progress_percentage
            
            	Progress percentage
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: percentage
            
            .. attribute:: start_time
            
            	Start time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: end_time
            
            	End time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ref_state
            
            	Ref state
            	**type**\:  :py:class:`IcpeInstallSatState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeInstallSatState>`
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_updating
            
            	Sats updating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivating
            
            	Sats deactivating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_removing
            
            	Sats removing
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_failed
            
            	Sats update failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_failed
            
            	Sats deactivate failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_failed
            
            	Sats remove failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_aborted
            
            	Sats update aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_aborted
            
            	Sats deactivate aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_aborted
            
            	Sats remove aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: name_string
            
            	Name strings
            	**type**\: list of str
            
            .. attribute:: satellite
            
            	Breakdown per satellite table
            	**type**\: list of  		 :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallShows.InstallShow.Satellite>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallShows.InstallShow, self).__init__()

                self.yang_name = "install-show"
                self.yang_parent_name = "install-shows"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['operation_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("satellite", ("satellite", NvSatellite.InstallShows.InstallShow.Satellite))])
                self._leafs = OrderedDict([
                    ('operation_id', YLeaf(YType.uint32, 'operation-id')),
                    ('operation_id_xr', YLeaf(YType.uint32, 'operation-id-xr')),
                    ('satellite_range', YLeaf(YType.str, 'satellite-range')),
                    ('operation_type', YLeaf(YType.uint16, 'operation-type')),
                    ('progress_percentage', YLeaf(YType.uint16, 'progress-percentage')),
                    ('start_time', YLeaf(YType.uint32, 'start-time')),
                    ('end_time', YLeaf(YType.uint32, 'end-time')),
                    ('ref_state', YLeaf(YType.enumeration, 'ref-state')),
                    ('sats_not_initiated', YLeafList(YType.uint16, 'sats-not-initiated')),
                    ('sats_transferring', YLeafList(YType.uint16, 'sats-transferring')),
                    ('sats_activating', YLeafList(YType.uint16, 'sats-activating')),
                    ('sats_updating', YLeafList(YType.uint16, 'sats-updating')),
                    ('sats_deactivating', YLeafList(YType.uint16, 'sats-deactivating')),
                    ('sats_removing', YLeafList(YType.uint16, 'sats-removing')),
                    ('sats_transfer_failed', YLeafList(YType.uint16, 'sats-transfer-failed')),
                    ('sats_activate_failed', YLeafList(YType.uint16, 'sats-activate-failed')),
                    ('sats_update_failed', YLeafList(YType.uint16, 'sats-update-failed')),
                    ('sats_deactivate_failed', YLeafList(YType.uint16, 'sats-deactivate-failed')),
                    ('sats_remove_failed', YLeafList(YType.uint16, 'sats-remove-failed')),
                    ('sats_transfer_aborted', YLeafList(YType.uint16, 'sats-transfer-aborted')),
                    ('sats_activate_aborted', YLeafList(YType.uint16, 'sats-activate-aborted')),
                    ('sats_update_aborted', YLeafList(YType.uint16, 'sats-update-aborted')),
                    ('sats_deactivate_aborted', YLeafList(YType.uint16, 'sats-deactivate-aborted')),
                    ('sats_remove_aborted', YLeafList(YType.uint16, 'sats-remove-aborted')),
                    ('sats_no_operation', YLeafList(YType.uint16, 'sats-no-operation')),
                    ('sats_completed', YLeafList(YType.uint16, 'sats-completed')),
                    ('name_string', YLeafList(YType.str, 'name-string')),
                ])
                self.operation_id = None
                self.operation_id_xr = None
                self.satellite_range = None
                self.operation_type = None
                self.progress_percentage = None
                self.start_time = None
                self.end_time = None
                self.ref_state = None
                self.sats_not_initiated = []
                self.sats_transferring = []
                self.sats_activating = []
                self.sats_updating = []
                self.sats_deactivating = []
                self.sats_removing = []
                self.sats_transfer_failed = []
                self.sats_activate_failed = []
                self.sats_update_failed = []
                self.sats_deactivate_failed = []
                self.sats_remove_failed = []
                self.sats_transfer_aborted = []
                self.sats_activate_aborted = []
                self.sats_update_aborted = []
                self.sats_deactivate_aborted = []
                self.sats_remove_aborted = []
                self.sats_no_operation = []
                self.sats_completed = []
                self.name_string = []

                self.satellite = YList(self)
                self._segment_path = lambda: "install-show" + "[operation-id='" + str(self.operation_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-shows/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.InstallShows.InstallShow, ['operation_id', 'operation_id_xr', 'satellite_range', 'operation_type', 'progress_percentage', 'start_time', 'end_time', 'ref_state', 'sats_not_initiated', 'sats_transferring', 'sats_activating', 'sats_updating', 'sats_deactivating', 'sats_removing', 'sats_transfer_failed', 'sats_activate_failed', 'sats_update_failed', 'sats_deactivate_failed', 'sats_remove_failed', 'sats_transfer_aborted', 'sats_activate_aborted', 'sats_update_aborted', 'sats_deactivate_aborted', 'sats_remove_aborted', 'sats_no_operation', 'sats_completed', 'name_string'], name, value)


            class Satellite(Entity):
                """
                Breakdown per satellite table
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`IcpeInstallSatState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeInstallSatState>`
                
                .. attribute:: percentage
                
                	Percentage
                	**type**\: int
                
                	**range:** 0..65535
                
                	**units**\: percentage
                
                .. attribute:: retries
                
                	Retries
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: start_time
                
                	Start time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: end_time
                
                	End time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: info
                
                	Info
                	**type**\: str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.InstallShows.InstallShow.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "install-show"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('satellite_id', YLeaf(YType.uint16, 'satellite-id')),
                        ('state', YLeaf(YType.enumeration, 'state')),
                        ('percentage', YLeaf(YType.uint16, 'percentage')),
                        ('retries', YLeaf(YType.uint16, 'retries')),
                        ('start_time', YLeaf(YType.uint32, 'start-time')),
                        ('end_time', YLeaf(YType.uint32, 'end-time')),
                        ('info', YLeaf(YType.str, 'info')),
                    ])
                    self.satellite_id = None
                    self.state = None
                    self.percentage = None
                    self.retries = None
                    self.start_time = None
                    self.end_time = None
                    self.info = None
                    self._segment_path = lambda: "satellite"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.InstallShows.InstallShow.Satellite, ['satellite_id', 'state', 'percentage', 'retries', 'start_time', 'end_time', 'info'], name, value)


    class SatelliteStatuses(Entity):
        """
        Satellite status information table
        
        .. attribute:: satellite_status
        
        	Satellite status information
        	**type**\: list of  		 :py:class:`SatelliteStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteStatuses, self).__init__()

            self.yang_name = "satellite-statuses"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("satellite-status", ("satellite_status", NvSatellite.SatelliteStatuses.SatelliteStatus))])
            self._leafs = OrderedDict()

            self.satellite_status = YList(self)
            self._segment_path = lambda: "satellite-statuses"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SatelliteStatuses, [], name, value)


        class SatelliteStatus(Entity):
            """
            Satellite status information
            
            .. attribute:: satellite_id  (key)
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 100..65534
            
            .. attribute:: candidate_fabric_ports
            
            	Candidate Fabric Ports on this Satellite
            	**type**\:  :py:class:`CandidateFabricPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts>`
            
            .. attribute:: optical_status
            
            	Optical Satellite Status
            	**type**\:  :py:class:`OpticalStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus>`
            
            .. attribute:: redundancy_out_of_sync_timestamp
            
            	Timestamp
            	**type**\:  :py:class:`RedundancyOutOfSyncTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp>`
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: version_check_state
            
            	Version check state
            	**type**\:  :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
            
            .. attribute:: remote_version_present
            
            	Remote version present
            	**type**\: bool
            
            .. attribute:: type
            
            	Type
            	**type**\: str
            
            .. attribute:: ethernet_fabric_supported
            
            	Ethernet fabric supported
            	**type**\: bool
            
            .. attribute:: optical_supported
            
            	Optical supported
            	**type**\: bool
            
            .. attribute:: ip_address
            
            	IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ip_address_present
            
            	IP address present
            	**type**\: bool
            
            .. attribute:: ip_address_auto
            
            	IP address auto
            	**type**\: bool
            
            .. attribute:: ipv6_address
            
            	IPV6 address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address_present
            
            	IPV6 address present
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: vrfid
            
            	VRFID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: description
            
            	Description
            	**type**\: str
            
            .. attribute:: description_present
            
            	Description present
            	**type**\: bool
            
            .. attribute:: mac_address
            
            	MAC address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: mac_address_present
            
            	MAC address present
            	**type**\: bool
            
            .. attribute:: configured_serial_number
            
            	Configured serial number
            	**type**\: str
            
            .. attribute:: configured_serial_number_present
            
            	Configured serial number present
            	**type**\: bool
            
            .. attribute:: received_serial_number
            
            	Received serial number
            	**type**\: str
            
            .. attribute:: received_serial_number_present
            
            	Received serial number present
            	**type**\: bool
            
            .. attribute:: password
            
            	Password
            	**type**\: str
            
            .. attribute:: password_error
            
            	Password error
            	**type**\: str
            
            .. attribute:: received_host_name
            
            	Received hostname
            	**type**\: str
            
            .. attribute:: cfgd_timeout
            
            	Cfgd timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeout_warning
            
            	Timeout warning
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: conflict_reason
            
            	Conflict reason
            	**type**\:  :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
            
            .. attribute:: conflict_context
            
            	Conflict context
            	**type**\: str
            
            .. attribute:: redundancy_iccp_group
            
            	Redundancy ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: recovery_delay_time_left
            
            	Recovery delay time left
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: host_treating_as_active
            
            	Host treating as active
            	**type**\: bool
            
            .. attribute:: satellite_treating_as_active
            
            	Satellite treating as active
            	**type**\: bool
            
            .. attribute:: sdacp_session_state
            
            	SDACP session state
            	**type**\:  :py:class:`IcpeOperSdacpSessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperSdacpSessState>`
            
            .. attribute:: sdacp_session_failure_reason
            
            	SDACP session failure reason
            	**type**\:  :py:class:`IcpeGcoOperControlReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeGcoOperControlReason>`
            
            .. attribute:: install_state
            
            	Install state
            	**type**\:  :py:class:`IcpeOperInstallState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperInstallState>`
            
            .. attribute:: remote_version
            
            	Remote version
            	**type**\: list of str
            
            .. attribute:: configured_link
            
            	Configured Links on this Satellite table
            	**type**\: list of  		 :py:class:`ConfiguredLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteStatuses.SatelliteStatus, self).__init__()

                self.yang_name = "satellite-status"
                self.yang_parent_name = "satellite-statuses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['satellite_id']
                self._child_container_classes = OrderedDict([("candidate-fabric-ports", ("candidate_fabric_ports", NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts)), ("optical-status", ("optical_status", NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus)), ("redundancy-out-of-sync-timestamp", ("redundancy_out_of_sync_timestamp", NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp))])
                self._child_list_classes = OrderedDict([("configured-link", ("configured_link", NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink))])
                self._leafs = OrderedDict([
                    ('satellite_id', YLeaf(YType.uint32, 'satellite-id')),
                    ('satellite_id_xr', YLeaf(YType.uint16, 'satellite-id-xr')),
                    ('version_check_state', YLeaf(YType.enumeration, 'version-check-state')),
                    ('remote_version_present', YLeaf(YType.boolean, 'remote-version-present')),
                    ('type', YLeaf(YType.str, 'type')),
                    ('ethernet_fabric_supported', YLeaf(YType.boolean, 'ethernet-fabric-supported')),
                    ('optical_supported', YLeaf(YType.boolean, 'optical-supported')),
                    ('ip_address', YLeaf(YType.str, 'ip-address')),
                    ('ip_address_present', YLeaf(YType.boolean, 'ip-address-present')),
                    ('ip_address_auto', YLeaf(YType.boolean, 'ip-address-auto')),
                    ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                    ('ipv6_address_present', YLeaf(YType.boolean, 'ipv6-address-present')),
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('vrfid', YLeaf(YType.uint32, 'vrfid')),
                    ('description', YLeaf(YType.str, 'description')),
                    ('description_present', YLeaf(YType.boolean, 'description-present')),
                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                    ('mac_address_present', YLeaf(YType.boolean, 'mac-address-present')),
                    ('configured_serial_number', YLeaf(YType.str, 'configured-serial-number')),
                    ('configured_serial_number_present', YLeaf(YType.boolean, 'configured-serial-number-present')),
                    ('received_serial_number', YLeaf(YType.str, 'received-serial-number')),
                    ('received_serial_number_present', YLeaf(YType.boolean, 'received-serial-number-present')),
                    ('password', YLeaf(YType.str, 'password')),
                    ('password_error', YLeaf(YType.str, 'password-error')),
                    ('received_host_name', YLeaf(YType.str, 'received-host-name')),
                    ('cfgd_timeout', YLeaf(YType.uint32, 'cfgd-timeout')),
                    ('timeout_warning', YLeaf(YType.uint32, 'timeout-warning')),
                    ('conflict_reason', YLeaf(YType.enumeration, 'conflict-reason')),
                    ('conflict_context', YLeaf(YType.str, 'conflict-context')),
                    ('redundancy_iccp_group', YLeaf(YType.uint32, 'redundancy-iccp-group')),
                    ('recovery_delay_time_left', YLeaf(YType.uint16, 'recovery-delay-time-left')),
                    ('host_treating_as_active', YLeaf(YType.boolean, 'host-treating-as-active')),
                    ('satellite_treating_as_active', YLeaf(YType.boolean, 'satellite-treating-as-active')),
                    ('sdacp_session_state', YLeaf(YType.enumeration, 'sdacp-session-state')),
                    ('sdacp_session_failure_reason', YLeaf(YType.enumeration, 'sdacp-session-failure-reason')),
                    ('install_state', YLeaf(YType.enumeration, 'install-state')),
                    ('remote_version', YLeafList(YType.str, 'remote-version')),
                ])
                self.satellite_id = None
                self.satellite_id_xr = None
                self.version_check_state = None
                self.remote_version_present = None
                self.type = None
                self.ethernet_fabric_supported = None
                self.optical_supported = None
                self.ip_address = None
                self.ip_address_present = None
                self.ip_address_auto = None
                self.ipv6_address = None
                self.ipv6_address_present = None
                self.vrf_name = None
                self.vrfid = None
                self.description = None
                self.description_present = None
                self.mac_address = None
                self.mac_address_present = None
                self.configured_serial_number = None
                self.configured_serial_number_present = None
                self.received_serial_number = None
                self.received_serial_number_present = None
                self.password = None
                self.password_error = None
                self.received_host_name = None
                self.cfgd_timeout = None
                self.timeout_warning = None
                self.conflict_reason = None
                self.conflict_context = None
                self.redundancy_iccp_group = None
                self.recovery_delay_time_left = None
                self.host_treating_as_active = None
                self.satellite_treating_as_active = None
                self.sdacp_session_state = None
                self.sdacp_session_failure_reason = None
                self.install_state = None
                self.remote_version = []

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
                self._segment_path = lambda: "satellite-status" + "[satellite-id='" + str(self.satellite_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-statuses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus, ['satellite_id', 'satellite_id_xr', 'version_check_state', 'remote_version_present', 'type', 'ethernet_fabric_supported', 'optical_supported', 'ip_address', 'ip_address_present', 'ip_address_auto', 'ipv6_address', 'ipv6_address_present', 'vrf_name', 'vrfid', 'description', 'description_present', 'mac_address', 'mac_address_present', 'configured_serial_number', 'configured_serial_number_present', 'received_serial_number', 'received_serial_number_present', 'password', 'password_error', 'received_host_name', 'cfgd_timeout', 'timeout_warning', 'conflict_reason', 'conflict_context', 'redundancy_iccp_group', 'recovery_delay_time_left', 'host_treating_as_active', 'satellite_treating_as_active', 'sdacp_session_state', 'sdacp_session_failure_reason', 'install_state', 'remote_version'], name, value)


            class CandidateFabricPorts(Entity):
                """
                Candidate Fabric Ports on this Satellite
                
                .. attribute:: channel_up
                
                	Channel up
                	**type**\: bool
                
                .. attribute:: out_of_sync
                
                	Out of sync
                	**type**\: bool
                
                .. attribute:: error_string
                
                	Error string
                	**type**\: str
                
                .. attribute:: configured_port
                
                	Configured Candidate Fabric Ports table
                	**type**\: list of  		 :py:class:`ConfiguredPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort>`
                
                .. attribute:: current_port
                
                	Current Candidate Fabric Ports on this Satellite table
                	**type**\: list of  		 :py:class:`CurrentPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts, self).__init__()

                    self.yang_name = "candidate-fabric-ports"
                    self.yang_parent_name = "satellite-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("configured-port", ("configured_port", NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort)), ("current-port", ("current_port", NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort))])
                    self._leafs = OrderedDict([
                        ('channel_up', YLeaf(YType.boolean, 'channel-up')),
                        ('out_of_sync', YLeaf(YType.boolean, 'out-of-sync')),
                        ('error_string', YLeaf(YType.str, 'error-string')),
                    ])
                    self.channel_up = None
                    self.out_of_sync = None
                    self.error_string = None

                    self.configured_port = YList(self)
                    self.current_port = YList(self)
                    self._segment_path = lambda: "candidate-fabric-ports"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts, ['channel_up', 'out_of_sync', 'error_string'], name, value)


                class ConfiguredPort(Entity):
                    """
                    Configured Candidate Fabric Ports table
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:  :py:class:`IcpeOperFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPort>`
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: valid
                    
                    	Valid
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort, self).__init__()

                        self.yang_name = "configured-port"
                        self.yang_parent_name = "candidate-fabric-ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('port_type', YLeaf(YType.enumeration, 'port-type')),
                            ('slot', YLeaf(YType.uint16, 'slot')),
                            ('subslot', YLeaf(YType.uint16, 'subslot')),
                            ('port', YLeaf(YType.uint16, 'port')),
                            ('valid', YLeaf(YType.boolean, 'valid')),
                        ])
                        self.port_type = None
                        self.slot = None
                        self.subslot = None
                        self.port = None
                        self.valid = None
                        self._segment_path = lambda: "configured-port"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort, ['port_type', 'slot', 'subslot', 'port', 'valid'], name, value)


                class CurrentPort(Entity):
                    """
                    Current Candidate Fabric Ports on this Satellite
                    table
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:  :py:class:`IcpeOperFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPort>`
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: permanent
                    
                    	Permanent
                    	**type**\: bool
                    
                    .. attribute:: requested
                    
                    	Requested
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort, self).__init__()

                        self.yang_name = "current-port"
                        self.yang_parent_name = "candidate-fabric-ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('port_type', YLeaf(YType.enumeration, 'port-type')),
                            ('slot', YLeaf(YType.uint16, 'slot')),
                            ('subslot', YLeaf(YType.uint16, 'subslot')),
                            ('port', YLeaf(YType.uint16, 'port')),
                            ('permanent', YLeaf(YType.boolean, 'permanent')),
                            ('requested', YLeaf(YType.boolean, 'requested')),
                        ])
                        self.port_type = None
                        self.slot = None
                        self.subslot = None
                        self.port = None
                        self.permanent = None
                        self.requested = None
                        self._segment_path = lambda: "current-port"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort, ['port_type', 'slot', 'subslot', 'port', 'permanent', 'requested'], name, value)


            class OpticalStatus(Entity):
                """
                Optical Satellite Status
                
                .. attribute:: chassis_sync_state
                
                	Chassis sync state
                	**type**\:  :py:class:`IcpeOpticalSyncState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncState>`
                
                .. attribute:: application
                
                	Application State table
                	**type**\: list of  		 :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus, self).__init__()

                    self.yang_name = "optical-status"
                    self.yang_parent_name = "satellite-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("application", ("application", NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application))])
                    self._leafs = OrderedDict([
                        ('chassis_sync_state', YLeaf(YType.enumeration, 'chassis-sync-state')),
                    ])
                    self.chassis_sync_state = None

                    self.application = YList(self)
                    self._segment_path = lambda: "optical-status"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus, ['chassis_sync_state'], name, value)


                class Application(Entity):
                    """
                    Application State table
                    
                    .. attribute:: name
                    
                    	Name
                    	**type**\: str
                    
                    .. attribute:: sync_state
                    
                    	Sync state
                    	**type**\:  :py:class:`IcpeOpticalSyncState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncState>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application, self).__init__()

                        self.yang_name = "application"
                        self.yang_parent_name = "optical-status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                            ('sync_state', YLeaf(YType.enumeration, 'sync-state')),
                        ])
                        self.name = None
                        self.sync_state = None
                        self._segment_path = lambda: "application"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application, ['name', 'sync_state'], name, value)


            class RedundancyOutOfSyncTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp, self).__init__()

                    self.yang_name = "redundancy-out-of-sync-timestamp"
                    self.yang_parent_name = "satellite-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                        ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                    ])
                    self.seconds = None
                    self.nanoseconds = None
                    self._segment_path = lambda: "redundancy-out-of-sync-timestamp"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp, ['seconds', 'nanoseconds'], name, value)


            class ConfiguredLink(Entity):
                """
                Configured Links on this Satellite table
                
                .. attribute:: interface_handle
                
                	Interface handle
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: ip_address
                
                	IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ip_address_auto
                
                	IP address auto
                	**type**\: bool
                
                .. attribute:: vrf_id_present
                
                	VRF ID present
                	**type**\: bool
                
                .. attribute:: vrf_id
                
                	VRF ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: minimum_preferred_links
                
                	Minimum preferred links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_active_links
                
                	Number active links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_links_satisfied
                
                	Min links satisfied
                	**type**\: bool
                
                .. attribute:: minimum_required_links
                
                	Minimum required links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: required_min_links_satisfied
                
                	Required min links satisfied
                	**type**\: bool
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:  :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\: str
                
                .. attribute:: port_range
                
                	Port ranges table
                	**type**\: list of  		 :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange>`
                
                .. attribute:: discovered_link
                
                	Discovered Links table
                	**type**\: list of  		 :py:class:`DiscoveredLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink, self).__init__()

                    self.yang_name = "configured-link"
                    self.yang_parent_name = "satellite-status"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("port-range", ("port_range", NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange)), ("discovered-link", ("discovered_link", NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink))])
                    self._leafs = OrderedDict([
                        ('interface_handle', YLeaf(YType.str, 'interface-handle')),
                        ('ip_address', YLeaf(YType.str, 'ip-address')),
                        ('ip_address_auto', YLeaf(YType.boolean, 'ip-address-auto')),
                        ('vrf_id_present', YLeaf(YType.boolean, 'vrf-id-present')),
                        ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                        ('minimum_preferred_links', YLeaf(YType.uint32, 'minimum-preferred-links')),
                        ('number_active_links', YLeaf(YType.uint32, 'number-active-links')),
                        ('min_links_satisfied', YLeaf(YType.boolean, 'min-links-satisfied')),
                        ('minimum_required_links', YLeaf(YType.uint32, 'minimum-required-links')),
                        ('required_min_links_satisfied', YLeaf(YType.boolean, 'required-min-links-satisfied')),
                        ('conflict_reason', YLeaf(YType.enumeration, 'conflict-reason')),
                        ('conflict_context', YLeaf(YType.str, 'conflict-context')),
                    ])
                    self.interface_handle = None
                    self.ip_address = None
                    self.ip_address_auto = None
                    self.vrf_id_present = None
                    self.vrf_id = None
                    self.minimum_preferred_links = None
                    self.number_active_links = None
                    self.min_links_satisfied = None
                    self.minimum_required_links = None
                    self.required_min_links_satisfied = None
                    self.conflict_reason = None
                    self.conflict_context = None

                    self.port_range = YList(self)
                    self.discovered_link = YList(self)
                    self._segment_path = lambda: "configured-link"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink, ['interface_handle', 'ip_address', 'ip_address_auto', 'vrf_id_present', 'vrf_id', 'minimum_preferred_links', 'number_active_links', 'min_links_satisfied', 'minimum_required_links', 'required_min_links_satisfied', 'conflict_reason', 'conflict_context'], name, value)


                class PortRange(Entity):
                    """
                    Port ranges table
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: low_port
                    
                    	Low port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: high_port
                    
                    	High port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:  :py:class:`IcpeOperPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperPort>`
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:  :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange, self).__init__()

                        self.yang_name = "port-range"
                        self.yang_parent_name = "configured-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('slot', YLeaf(YType.uint32, 'slot')),
                            ('subslot', YLeaf(YType.uint32, 'subslot')),
                            ('low_port', YLeaf(YType.uint32, 'low-port')),
                            ('high_port', YLeaf(YType.uint32, 'high-port')),
                            ('port_type', YLeaf(YType.enumeration, 'port-type')),
                            ('conflict_reason', YLeaf(YType.enumeration, 'conflict-reason')),
                            ('conflict_context', YLeaf(YType.str, 'conflict-context')),
                        ])
                        self.slot = None
                        self.subslot = None
                        self.low_port = None
                        self.high_port = None
                        self.port_type = None
                        self.conflict_reason = None
                        self.conflict_context = None
                        self._segment_path = lambda: "port-range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange, ['slot', 'subslot', 'low_port', 'high_port', 'port_type', 'conflict_reason', 'conflict_context'], name, value)


                class DiscoveredLink(Entity):
                    """
                    Discovered Links table
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:  :py:class:`IcpeOperDiscdLinkState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperDiscdLinkState>`
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:  :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink, self).__init__()

                        self.yang_name = "discovered-link"
                        self.yang_parent_name = "configured-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_handle', YLeaf(YType.str, 'interface-handle')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('conflict_reason', YLeaf(YType.enumeration, 'conflict-reason')),
                            ('conflict_context', YLeaf(YType.str, 'conflict-context')),
                        ])
                        self.interface_handle = None
                        self.state = None
                        self.conflict_reason = None
                        self.conflict_context = None
                        self._segment_path = lambda: "discovered-link"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink, ['interface_handle', 'state', 'conflict_reason', 'conflict_context'], name, value)


    class SatellitePriorities(Entity):
        """
        Satellite priority information table
        
        .. attribute:: satellite_priority
        
        	Satellite priority information
        	**type**\: list of  		 :py:class:`SatellitePriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatellitePriorities.SatellitePriority>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatellitePriorities, self).__init__()

            self.yang_name = "satellite-priorities"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("satellite-priority", ("satellite_priority", NvSatellite.SatellitePriorities.SatellitePriority))])
            self._leafs = OrderedDict()

            self.satellite_priority = YList(self)
            self._segment_path = lambda: "satellite-priorities"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SatellitePriorities, [], name, value)


        class SatellitePriority(Entity):
            """
            Satellite priority information
            
            .. attribute:: satellite_id  (key)
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 100..65534
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: rgid
            
            	RG ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: best_path_hops
            
            	Best path hops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: configured_priority
            
            	Configured priority
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: host_priority
            
            	Host priority
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: partner_priority
            
            	Partner priority
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: multichassis_redundancy
            
            	Multichassis redundancy
            	**type**\:  :py:class:`IcpeOperMultichassisRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperMultichassisRedundancy>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatellitePriorities.SatellitePriority, self).__init__()

                self.yang_name = "satellite-priority"
                self.yang_parent_name = "satellite-priorities"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['satellite_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('satellite_id', YLeaf(YType.uint32, 'satellite-id')),
                    ('satellite_id_xr', YLeaf(YType.uint16, 'satellite-id-xr')),
                    ('rgid', YLeaf(YType.uint32, 'rgid')),
                    ('best_path_hops', YLeaf(YType.uint32, 'best-path-hops')),
                    ('configured_priority', YLeaf(YType.uint8, 'configured-priority')),
                    ('host_priority', YLeaf(YType.uint64, 'host-priority')),
                    ('partner_priority', YLeaf(YType.uint64, 'partner-priority')),
                    ('multichassis_redundancy', YLeaf(YType.enumeration, 'multichassis-redundancy')),
                ])
                self.satellite_id = None
                self.satellite_id_xr = None
                self.rgid = None
                self.best_path_hops = None
                self.configured_priority = None
                self.host_priority = None
                self.partner_priority = None
                self.multichassis_redundancy = None
                self._segment_path = lambda: "satellite-priority" + "[satellite-id='" + str(self.satellite_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-priorities/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SatellitePriorities.SatellitePriority, ['satellite_id', 'satellite_id_xr', 'rgid', 'best_path_hops', 'configured_priority', 'host_priority', 'partner_priority', 'multichassis_redundancy'], name, value)


    class SatelliteVersions(Entity):
        """
        Satellite remote version information table
        
        .. attribute:: satellite_version
        
        	Satellite remote version information
        	**type**\: list of  		 :py:class:`SatelliteVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteVersions, self).__init__()

            self.yang_name = "satellite-versions"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("satellite-version", ("satellite_version", NvSatellite.SatelliteVersions.SatelliteVersion))])
            self._leafs = OrderedDict()

            self.satellite_version = YList(self)
            self._segment_path = lambda: "satellite-versions"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SatelliteVersions, [], name, value)


        class SatelliteVersion(Entity):
            """
            Satellite remote version information
            
            .. attribute:: satellite_id  (key)
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 100..65534
            
            .. attribute:: active_version
            
            	Satellite active version information
            	**type**\:  :py:class:`ActiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion>`
            
            .. attribute:: transferred_version
            
            	Satellite transferred version information
            	**type**\:  :py:class:`TransferredVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion>`
            
            .. attribute:: committed_version
            
            	Satellite committed version information
            	**type**\:  :py:class:`CommittedVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion>`
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: version_check_state
            
            	Version check state
            	**type**\:  :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
            
            .. attribute:: remote_version_present
            
            	Remote version present
            	**type**\: bool
            
            .. attribute:: remote_version
            
            	Remote version
            	**type**\: list of str
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteVersions.SatelliteVersion, self).__init__()

                self.yang_name = "satellite-version"
                self.yang_parent_name = "satellite-versions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['satellite_id']
                self._child_container_classes = OrderedDict([("active-version", ("active_version", NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion)), ("transferred-version", ("transferred_version", NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion)), ("committed-version", ("committed_version", NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('satellite_id', YLeaf(YType.uint32, 'satellite-id')),
                    ('satellite_id_xr', YLeaf(YType.uint16, 'satellite-id-xr')),
                    ('version_check_state', YLeaf(YType.enumeration, 'version-check-state')),
                    ('remote_version_present', YLeaf(YType.boolean, 'remote-version-present')),
                    ('remote_version', YLeafList(YType.str, 'remote-version')),
                ])
                self.satellite_id = None
                self.satellite_id_xr = None
                self.version_check_state = None
                self.remote_version_present = None
                self.remote_version = []

                self.active_version = NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion()
                self.active_version.parent = self
                self._children_name_map["active_version"] = "active-version"
                self._children_yang_names.add("active-version")

                self.transferred_version = NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion()
                self.transferred_version.parent = self
                self._children_name_map["transferred_version"] = "transferred-version"
                self._children_yang_names.add("transferred-version")

                self.committed_version = NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion()
                self.committed_version.parent = self
                self._children_name_map["committed_version"] = "committed-version"
                self._children_yang_names.add("committed-version")
                self._segment_path = lambda: "satellite-version" + "[satellite-id='" + str(self.satellite_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-versions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SatelliteVersions.SatelliteVersion, ['satellite_id', 'satellite_id_xr', 'version_check_state', 'remote_version_present', 'remote_version'], name, value)


            class ActiveVersion(Entity):
                """
                Satellite active version information
                
                .. attribute:: version_check_state
                
                	Version check state
                	**type**\:  :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
                
                .. attribute:: remote_version_present
                
                	Remote version present
                	**type**\: bool
                
                .. attribute:: remote_version
                
                	Remote version
                	**type**\: list of str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion, self).__init__()

                    self.yang_name = "active-version"
                    self.yang_parent_name = "satellite-version"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('version_check_state', YLeaf(YType.enumeration, 'version-check-state')),
                        ('remote_version_present', YLeaf(YType.boolean, 'remote-version-present')),
                        ('remote_version', YLeafList(YType.str, 'remote-version')),
                    ])
                    self.version_check_state = None
                    self.remote_version_present = None
                    self.remote_version = []
                    self._segment_path = lambda: "active-version"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion, ['version_check_state', 'remote_version_present', 'remote_version'], name, value)


            class TransferredVersion(Entity):
                """
                Satellite transferred version information
                
                .. attribute:: version_check_state
                
                	Version check state
                	**type**\:  :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
                
                .. attribute:: remote_version_present
                
                	Remote version present
                	**type**\: bool
                
                .. attribute:: remote_version
                
                	Remote version
                	**type**\: list of str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion, self).__init__()

                    self.yang_name = "transferred-version"
                    self.yang_parent_name = "satellite-version"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('version_check_state', YLeaf(YType.enumeration, 'version-check-state')),
                        ('remote_version_present', YLeaf(YType.boolean, 'remote-version-present')),
                        ('remote_version', YLeafList(YType.str, 'remote-version')),
                    ])
                    self.version_check_state = None
                    self.remote_version_present = None
                    self.remote_version = []
                    self._segment_path = lambda: "transferred-version"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion, ['version_check_state', 'remote_version_present', 'remote_version'], name, value)


            class CommittedVersion(Entity):
                """
                Satellite committed version information
                
                .. attribute:: version_check_state
                
                	Version check state
                	**type**\:  :py:class:`IcpeOperVerCheckState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState>`
                
                .. attribute:: remote_version_present
                
                	Remote version present
                	**type**\: bool
                
                .. attribute:: remote_version
                
                	Remote version
                	**type**\: list of str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion, self).__init__()

                    self.yang_name = "committed-version"
                    self.yang_parent_name = "satellite-version"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('version_check_state', YLeaf(YType.enumeration, 'version-check-state')),
                        ('remote_version_present', YLeaf(YType.boolean, 'remote-version-present')),
                        ('remote_version', YLeafList(YType.str, 'remote-version')),
                    ])
                    self.version_check_state = None
                    self.remote_version_present = None
                    self.remote_version = []
                    self._segment_path = lambda: "committed-version"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion, ['version_check_state', 'remote_version_present', 'remote_version'], name, value)


    class SatelliteTopologies(Entity):
        """
        Satellite Topology Information table
        
        .. attribute:: satellite_topology
        
        	Satellite Topology Information
        	**type**\: list of  		 :py:class:`SatelliteTopology <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteTopologies, self).__init__()

            self.yang_name = "satellite-topologies"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("satellite-topology", ("satellite_topology", NvSatellite.SatelliteTopologies.SatelliteTopology))])
            self._leafs = OrderedDict()

            self.satellite_topology = YList(self)
            self._segment_path = lambda: "satellite-topologies"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SatelliteTopologies, [], name, value)


        class SatelliteTopology(Entity):
            """
            Satellite Topology Information
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\: str
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: redundancy_iccp_group
            
            	Redundancy ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_physical
            
            	Is physical
            	**type**\: bool
            
            .. attribute:: ring_whole
            
            	Ring whole
            	**type**\: bool
            
            .. attribute:: discovered_link
            
            	Discovered Links table
            	**type**\: list of  		 :py:class:`DiscoveredLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink>`
            
            .. attribute:: satellite
            
            	Satellite table
            	**type**\: list of  		 :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteTopologies.SatelliteTopology, self).__init__()

                self.yang_name = "satellite-topology"
                self.yang_parent_name = "satellite-topologies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("discovered-link", ("discovered_link", NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink)), ("satellite", ("satellite", NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite))])
                self._leafs = OrderedDict([
                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                    ('interface_name_xr', YLeaf(YType.str, 'interface-name-xr')),
                    ('interface_handle', YLeaf(YType.str, 'interface-handle')),
                    ('redundancy_iccp_group', YLeaf(YType.uint32, 'redundancy-iccp-group')),
                    ('is_physical', YLeaf(YType.boolean, 'is-physical')),
                    ('ring_whole', YLeaf(YType.boolean, 'ring-whole')),
                ])
                self.interface_name = None
                self.interface_name_xr = None
                self.interface_handle = None
                self.redundancy_iccp_group = None
                self.is_physical = None
                self.ring_whole = None

                self.discovered_link = YList(self)
                self.satellite = YList(self)
                self._segment_path = lambda: "satellite-topology" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-topologies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SatelliteTopologies.SatelliteTopology, ['interface_name', 'interface_name_xr', 'interface_handle', 'redundancy_iccp_group', 'is_physical', 'ring_whole'], name, value)


            class DiscoveredLink(Entity):
                """
                Discovered Links table
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\: str
                
                .. attribute:: interface_handle
                
                	Interface handle
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: discovery_running
                
                	Discovery running
                	**type**\: bool
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink, self).__init__()

                    self.yang_name = "discovered-link"
                    self.yang_parent_name = "satellite-topology"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('interface_handle', YLeaf(YType.str, 'interface-handle')),
                        ('discovery_running', YLeaf(YType.boolean, 'discovery-running')),
                    ])
                    self.interface_name = None
                    self.interface_handle = None
                    self.discovery_running = None
                    self._segment_path = lambda: "discovered-link"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink, ['interface_name', 'interface_handle', 'discovery_running'], name, value)


            class Satellite(Entity):
                """
                Satellite table
                
                .. attribute:: mac_address
                
                	MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: configured
                
                	Configured
                	**type**\: bool
                
                .. attribute:: num_hops
                
                	Num hops
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: type
                
                	Type
                	**type**\: str
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: received_serial_number
                
                	Received serial number
                	**type**\: str
                
                .. attribute:: received_serial_number_present
                
                	Received serial number present
                	**type**\: bool
                
                .. attribute:: vlan_id
                
                	VLAN ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: display_name
                
                	Display name
                	**type**\: str
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:  :py:class:`IcpeOperConflict <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict>`
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\: str
                
                .. attribute:: fabric_link
                
                	Local Satellite Fabric Link table
                	**type**\: list of  		 :py:class:`FabricLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "satellite-topology"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("fabric-link", ("fabric_link", NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink))])
                    self._leafs = OrderedDict([
                        ('mac_address', YLeaf(YType.str, 'mac-address')),
                        ('configured', YLeaf(YType.boolean, 'configured')),
                        ('num_hops', YLeaf(YType.uint16, 'num-hops')),
                        ('type', YLeaf(YType.str, 'type')),
                        ('satellite_id', YLeaf(YType.uint16, 'satellite-id')),
                        ('received_serial_number', YLeaf(YType.str, 'received-serial-number')),
                        ('received_serial_number_present', YLeaf(YType.boolean, 'received-serial-number-present')),
                        ('vlan_id', YLeaf(YType.uint16, 'vlan-id')),
                        ('display_name', YLeaf(YType.str, 'display-name')),
                        ('conflict_reason', YLeaf(YType.enumeration, 'conflict-reason')),
                        ('conflict_context', YLeaf(YType.str, 'conflict-context')),
                    ])
                    self.mac_address = None
                    self.configured = None
                    self.num_hops = None
                    self.type = None
                    self.satellite_id = None
                    self.received_serial_number = None
                    self.received_serial_number_present = None
                    self.vlan_id = None
                    self.display_name = None
                    self.conflict_reason = None
                    self.conflict_context = None

                    self.fabric_link = YList(self)
                    self._segment_path = lambda: "satellite"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite, ['mac_address', 'configured', 'num_hops', 'type', 'satellite_id', 'received_serial_number', 'received_serial_number_present', 'vlan_id', 'display_name', 'conflict_reason', 'conflict_context'], name, value)


                class FabricLink(Entity):
                    """
                    Local Satellite Fabric Link table
                    
                    .. attribute:: icl_id
                    
                    	ICL ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: display_name
                    
                    	Display name
                    	**type**\: str
                    
                    .. attribute:: redundant
                    
                    	Redundant
                    	**type**\: bool
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\: bool
                    
                    .. attribute:: obsolete
                    
                    	Obsolete
                    	**type**\: bool
                    
                    .. attribute:: remote_device
                    
                    	Remote Device table
                    	**type**\: list of  		 :py:class:`RemoteDevice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink, self).__init__()

                        self.yang_name = "fabric-link"
                        self.yang_parent_name = "satellite"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("remote-device", ("remote_device", NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice))])
                        self._leafs = OrderedDict([
                            ('icl_id', YLeaf(YType.uint32, 'icl-id')),
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('display_name', YLeaf(YType.str, 'display-name')),
                            ('redundant', YLeaf(YType.boolean, 'redundant')),
                            ('active', YLeaf(YType.boolean, 'active')),
                            ('obsolete', YLeaf(YType.boolean, 'obsolete')),
                        ])
                        self.icl_id = None
                        self.interface_name = None
                        self.display_name = None
                        self.redundant = None
                        self.active = None
                        self.obsolete = None

                        self.remote_device = YList(self)
                        self._segment_path = lambda: "fabric-link"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink, ['icl_id', 'interface_name', 'display_name', 'redundant', 'active', 'obsolete'], name, value)


                    class RemoteDevice(Entity):
                        """
                        Remote Device table
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: source
                        
                        	Source
                        	**type**\:  :py:class:`IcpeOperTopoRemoteSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperTopoRemoteSource>`
                        
                        .. attribute:: remote_is_satellite
                        
                        	Remote is satellite
                        	**type**\: bool
                        
                        .. attribute:: remote_is_local_host
                        
                        	Remote is local host
                        	**type**\: bool
                        
                        .. attribute:: icl_id
                        
                        	ICL ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice, self).__init__()

                            self.yang_name = "remote-device"
                            self.yang_parent_name = "fabric-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mac_address', YLeaf(YType.str, 'mac-address')),
                                ('source', YLeaf(YType.enumeration, 'source')),
                                ('remote_is_satellite', YLeaf(YType.boolean, 'remote-is-satellite')),
                                ('remote_is_local_host', YLeaf(YType.boolean, 'remote-is-local-host')),
                                ('icl_id', YLeaf(YType.uint32, 'icl-id')),
                                ('interface_handle', YLeaf(YType.str, 'interface-handle')),
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ])
                            self.mac_address = None
                            self.source = None
                            self.remote_is_satellite = None
                            self.remote_is_local_host = None
                            self.icl_id = None
                            self.interface_handle = None
                            self.interface_name = None
                            self._segment_path = lambda: "remote-device"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice, ['mac_address', 'source', 'remote_is_satellite', 'remote_is_local_host', 'icl_id', 'interface_handle', 'interface_name'], name, value)


    class InstallReferenceInfo(Entity):
        """
        Satellite Install Reference Information
        
        .. attribute:: references
        
        	Install Reference Information table
        	**type**\:  :py:class:`References <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallReferenceInfo.References>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallReferenceInfo, self).__init__()

            self.yang_name = "install-reference-info"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("references", ("references", NvSatellite.InstallReferenceInfo.References))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.references = NvSatellite.InstallReferenceInfo.References()
            self.references.parent = self
            self._children_name_map["references"] = "references"
            self._children_yang_names.add("references")
            self._segment_path = lambda: "install-reference-info"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()


        class References(Entity):
            """
            Install Reference Information table
            
            .. attribute:: reference
            
            	Install Reference Information
            	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallReferenceInfo.References.Reference>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallReferenceInfo.References, self).__init__()

                self.yang_name = "references"
                self.yang_parent_name = "install-reference-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("reference", ("reference", NvSatellite.InstallReferenceInfo.References.Reference))])
                self._leafs = OrderedDict()

                self.reference = YList(self)
                self._segment_path = lambda: "references"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-reference-info/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.InstallReferenceInfo.References, [], name, value)


            class Reference(Entity):
                """
                Install Reference Information
                
                .. attribute:: reference_name  (key)
                
                	Reference name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: reference_name_xr
                
                	Reference name
                	**type**\: str
                
                .. attribute:: reference_file
                
                	Reference files
                	**type**\: list of str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.InstallReferenceInfo.References.Reference, self).__init__()

                    self.yang_name = "reference"
                    self.yang_parent_name = "references"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['reference_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('reference_name', YLeaf(YType.str, 'reference-name')),
                        ('reference_name_xr', YLeaf(YType.str, 'reference-name-xr')),
                        ('reference_file', YLeafList(YType.str, 'reference-file')),
                    ])
                    self.reference_name = None
                    self.reference_name_xr = None
                    self.reference_file = []
                    self._segment_path = lambda: "reference" + "[reference-name='" + str(self.reference_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-reference-info/references/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.InstallReferenceInfo.References.Reference, ['reference_name', 'reference_name_xr', 'reference_file'], name, value)


    class InstallOpProgresses(Entity):
        """
        Current percentage of install table
        
        .. attribute:: install_op_progress
        
        	Current percentage of install
        	**type**\: list of  		 :py:class:`InstallOpProgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpProgresses.InstallOpProgress>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallOpProgresses, self).__init__()

            self.yang_name = "install-op-progresses"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("install-op-progress", ("install_op_progress", NvSatellite.InstallOpProgresses.InstallOpProgress))])
            self._leafs = OrderedDict()

            self.install_op_progress = YList(self)
            self._segment_path = lambda: "install-op-progresses"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.InstallOpProgresses, [], name, value)


        class InstallOpProgress(Entity):
            """
            Current percentage of install
            
            .. attribute:: operation_id  (key)
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: progress_percentage
            
            	Progress percentage
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: percentage
            
            .. attribute:: satellite_count
            
            	Satellite count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallOpProgresses.InstallOpProgress, self).__init__()

                self.yang_name = "install-op-progress"
                self.yang_parent_name = "install-op-progresses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['operation_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('operation_id', YLeaf(YType.uint32, 'operation-id')),
                    ('operation_id_xr', YLeaf(YType.uint32, 'operation-id-xr')),
                    ('progress_percentage', YLeaf(YType.uint16, 'progress-percentage')),
                    ('satellite_count', YLeaf(YType.uint32, 'satellite-count')),
                ])
                self.operation_id = None
                self.operation_id_xr = None
                self.progress_percentage = None
                self.satellite_count = None
                self._segment_path = lambda: "install-op-progress" + "[operation-id='" + str(self.operation_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-op-progresses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.InstallOpProgresses.InstallOpProgress, ['operation_id', 'operation_id_xr', 'progress_percentage', 'satellite_count'], name, value)


    class ReloadStatuses(Entity):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_status
        
        	Detailed breakdown of reload status
        	**type**\: list of  		 :py:class:`ReloadStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses.ReloadStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.ReloadStatuses, self).__init__()

            self.yang_name = "reload-statuses"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("reload-status", ("reload_status", NvSatellite.ReloadStatuses.ReloadStatus))])
            self._leafs = OrderedDict()

            self.reload_status = YList(self)
            self._segment_path = lambda: "reload-statuses"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.ReloadStatuses, [], name, value)


        class ReloadStatus(Entity):
            """
            Detailed breakdown of reload status
            
            .. attribute:: satellite_range  (key)
            
            	Satellite range
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: satellite_range_xr
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloading
            
            	Sats reloading
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloaded
            
            	Sats reloaded
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reload_failed
            
            	Sats reload failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.ReloadStatuses.ReloadStatus, self).__init__()

                self.yang_name = "reload-status"
                self.yang_parent_name = "reload-statuses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['satellite_range']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('satellite_range', YLeaf(YType.str, 'satellite-range')),
                    ('satellite_range_xr', YLeaf(YType.str, 'satellite-range-xr')),
                    ('sats_not_initiated', YLeafList(YType.uint16, 'sats-not-initiated')),
                    ('sats_reloading', YLeafList(YType.uint16, 'sats-reloading')),
                    ('sats_reloaded', YLeafList(YType.uint16, 'sats-reloaded')),
                    ('sats_reload_failed', YLeafList(YType.uint16, 'sats-reload-failed')),
                ])
                self.satellite_range = None
                self.satellite_range_xr = None
                self.sats_not_initiated = []
                self.sats_reloading = []
                self.sats_reloaded = []
                self.sats_reload_failed = []
                self._segment_path = lambda: "reload-status" + "[satellite-range='" + str(self.satellite_range) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/reload-statuses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.ReloadStatuses.ReloadStatus, ['satellite_range', 'satellite_range_xr', 'sats_not_initiated', 'sats_reloading', 'sats_reloaded', 'sats_reload_failed'], name, value)


    class Install(Entity):
        """
        Satellite Install Information
        
        .. attribute:: satellite_software_versions
        
        	Satellite Software Package Information table
        	**type**\:  :py:class:`SatelliteSoftwareVersions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.Install, self).__init__()

            self.yang_name = "install"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("satellite-software-versions", ("satellite_software_versions", NvSatellite.Install.SatelliteSoftwareVersions))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.satellite_software_versions = NvSatellite.Install.SatelliteSoftwareVersions()
            self.satellite_software_versions.parent = self
            self._children_name_map["satellite_software_versions"] = "satellite-software-versions"
            self._children_yang_names.add("satellite-software-versions")
            self._segment_path = lambda: "install"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()


        class SatelliteSoftwareVersions(Entity):
            """
            Satellite Software Package Information table
            
            .. attribute:: satellite_software_version
            
            	Satellite Software Package Information
            	**type**\: list of  		 :py:class:`SatelliteSoftwareVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.Install.SatelliteSoftwareVersions, self).__init__()

                self.yang_name = "satellite-software-versions"
                self.yang_parent_name = "install"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("satellite-software-version", ("satellite_software_version", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion))])
                self._leafs = OrderedDict()

                self.satellite_software_version = YList(self)
                self._segment_path = lambda: "satellite-software-versions"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions, [], name, value)


            class SatelliteSoftwareVersion(Entity):
                """
                Satellite Software Package Information
                
                .. attribute:: satellite_id  (key)
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 100..65534
                
                .. attribute:: install_package_info
                
                	Package Data on this Satellite
                	**type**\:  :py:class:`InstallPackageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo>`
                
                .. attribute:: satellite_id_xr
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: package_support
                
                	Package support
                	**type**\:  :py:class:`IcpeInstallPkgSupp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeInstallPkgSupp>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion, self).__init__()

                    self.yang_name = "satellite-software-version"
                    self.yang_parent_name = "satellite-software-versions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['satellite_id']
                    self._child_container_classes = OrderedDict([("install-package-info", ("install_package_info", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('satellite_id', YLeaf(YType.uint32, 'satellite-id')),
                        ('satellite_id_xr', YLeaf(YType.uint16, 'satellite-id-xr')),
                        ('package_support', YLeaf(YType.enumeration, 'package-support')),
                    ])
                    self.satellite_id = None
                    self.satellite_id_xr = None
                    self.package_support = None

                    self.install_package_info = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo()
                    self.install_package_info.parent = self
                    self._children_name_map["install_package_info"] = "install-package-info"
                    self._children_yang_names.add("install-package-info")
                    self._segment_path = lambda: "satellite-software-version" + "[satellite-id='" + str(self.satellite_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install/satellite-software-versions/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion, ['satellite_id', 'satellite_id_xr', 'package_support'], name, value)


                class InstallPackageInfo(Entity):
                    """
                    Package Data on this Satellite
                    
                    .. attribute:: active_packages
                    
                    	Active Packages running on this Satellite
                    	**type**\:  :py:class:`ActivePackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages>`
                    
                    .. attribute:: inactive_packages
                    
                    	Inactive Packages on this Satellite
                    	**type**\:  :py:class:`InactivePackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages>`
                    
                    .. attribute:: committed_packages
                    
                    	Committed Packages running on this Satellite
                    	**type**\:  :py:class:`CommittedPackages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo, self).__init__()

                        self.yang_name = "install-package-info"
                        self.yang_parent_name = "satellite-software-version"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("active-packages", ("active_packages", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages)), ("inactive-packages", ("inactive_packages", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages)), ("committed-packages", ("committed_packages", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.active_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages()
                        self.active_packages.parent = self
                        self._children_name_map["active_packages"] = "active-packages"
                        self._children_yang_names.add("active-packages")

                        self.inactive_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages()
                        self.inactive_packages.parent = self
                        self._children_name_map["inactive_packages"] = "inactive-packages"
                        self._children_yang_names.add("inactive-packages")

                        self.committed_packages = NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages()
                        self.committed_packages.parent = self
                        self._children_name_map["committed_packages"] = "committed-packages"
                        self._children_yang_names.add("committed-packages")
                        self._segment_path = lambda: "install-package-info"


                    class ActivePackages(Entity):
                        """
                        Active Packages running on this Satellite
                        
                        .. attribute:: package
                        
                        	A package on this Satellite table
                        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages, self).__init__()

                            self.yang_name = "active-packages"
                            self.yang_parent_name = "install-package-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("package", ("package", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package))])
                            self._leafs = OrderedDict()

                            self.package = YList(self)
                            self._segment_path = lambda: "active-packages"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages, [], name, value)


                        class Package(Entity):
                            """
                            A package on this Satellite table
                            
                            .. attribute:: name
                            
                            	Name
                            	**type**\: str
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\: str
                            
                            .. attribute:: is_base_image
                            
                            	Is base image
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'icpe-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "active-packages"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('version', YLeaf(YType.str, 'version')),
                                    ('is_base_image', YLeaf(YType.boolean, 'is-base-image')),
                                ])
                                self.name = None
                                self.version = None
                                self.is_base_image = None
                                self._segment_path = lambda: "package"

                            def __setattr__(self, name, value):
                                self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package, ['name', 'version', 'is_base_image'], name, value)


                    class InactivePackages(Entity):
                        """
                        Inactive Packages on this Satellite
                        
                        .. attribute:: package
                        
                        	A package on this Satellite table
                        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages, self).__init__()

                            self.yang_name = "inactive-packages"
                            self.yang_parent_name = "install-package-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("package", ("package", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package))])
                            self._leafs = OrderedDict()

                            self.package = YList(self)
                            self._segment_path = lambda: "inactive-packages"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages, [], name, value)


                        class Package(Entity):
                            """
                            A package on this Satellite table
                            
                            .. attribute:: name
                            
                            	Name
                            	**type**\: str
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\: str
                            
                            .. attribute:: is_base_image
                            
                            	Is base image
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'icpe-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "inactive-packages"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('version', YLeaf(YType.str, 'version')),
                                    ('is_base_image', YLeaf(YType.boolean, 'is-base-image')),
                                ])
                                self.name = None
                                self.version = None
                                self.is_base_image = None
                                self._segment_path = lambda: "package"

                            def __setattr__(self, name, value):
                                self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package, ['name', 'version', 'is_base_image'], name, value)


                    class CommittedPackages(Entity):
                        """
                        Committed Packages running on this Satellite
                        
                        .. attribute:: package
                        
                        	A package on this Satellite table
                        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages, self).__init__()

                            self.yang_name = "committed-packages"
                            self.yang_parent_name = "install-package-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("package", ("package", NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package))])
                            self._leafs = OrderedDict()

                            self.package = YList(self)
                            self._segment_path = lambda: "committed-packages"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages, [], name, value)


                        class Package(Entity):
                            """
                            A package on this Satellite table
                            
                            .. attribute:: name
                            
                            	Name
                            	**type**\: str
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\: str
                            
                            .. attribute:: is_base_image
                            
                            	Is base image
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'icpe-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package, self).__init__()

                                self.yang_name = "package"
                                self.yang_parent_name = "committed-packages"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('version', YLeaf(YType.str, 'version')),
                                    ('is_base_image', YLeaf(YType.boolean, 'is-base-image')),
                                ])
                                self.name = None
                                self.version = None
                                self.is_base_image = None
                                self._segment_path = lambda: "package"

                            def __setattr__(self, name, value):
                                self._perform_setattr(NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package, ['name', 'version', 'is_base_image'], name, value)


    class InstallOpStatuses(Entity):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_op_status
        
        	Detailed breakdown of install status
        	**type**\: list of  		 :py:class:`InstallOpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses.InstallOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.InstallOpStatuses, self).__init__()

            self.yang_name = "install-op-statuses"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("install-op-status", ("install_op_status", NvSatellite.InstallOpStatuses.InstallOpStatus))])
            self._leafs = OrderedDict()

            self.install_op_status = YList(self)
            self._segment_path = lambda: "install-op-statuses"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.InstallOpStatuses, [], name, value)


        class InstallOpStatus(Entity):
            """
            Detailed breakdown of install status
            
            .. attribute:: operation_id  (key)
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_updating
            
            	Sats updating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivating
            
            	Sats deactivating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_removing
            
            	Sats removing
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_failed
            
            	Sats update failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_failed
            
            	Sats deactivate failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_failed
            
            	Sats remove failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_update_aborted
            
            	Sats update aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_deactivate_aborted
            
            	Sats deactivate aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_remove_aborted
            
            	Sats remove aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.InstallOpStatuses.InstallOpStatus, self).__init__()

                self.yang_name = "install-op-status"
                self.yang_parent_name = "install-op-statuses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['operation_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('operation_id', YLeaf(YType.uint32, 'operation-id')),
                    ('operation_id_xr', YLeaf(YType.uint32, 'operation-id-xr')),
                    ('satellite_range', YLeaf(YType.str, 'satellite-range')),
                    ('sats_not_initiated', YLeafList(YType.uint16, 'sats-not-initiated')),
                    ('sats_transferring', YLeafList(YType.uint16, 'sats-transferring')),
                    ('sats_activating', YLeafList(YType.uint16, 'sats-activating')),
                    ('sats_updating', YLeafList(YType.uint16, 'sats-updating')),
                    ('sats_deactivating', YLeafList(YType.uint16, 'sats-deactivating')),
                    ('sats_removing', YLeafList(YType.uint16, 'sats-removing')),
                    ('sats_transfer_failed', YLeafList(YType.uint16, 'sats-transfer-failed')),
                    ('sats_activate_failed', YLeafList(YType.uint16, 'sats-activate-failed')),
                    ('sats_update_failed', YLeafList(YType.uint16, 'sats-update-failed')),
                    ('sats_deactivate_failed', YLeafList(YType.uint16, 'sats-deactivate-failed')),
                    ('sats_remove_failed', YLeafList(YType.uint16, 'sats-remove-failed')),
                    ('sats_transfer_aborted', YLeafList(YType.uint16, 'sats-transfer-aborted')),
                    ('sats_activate_aborted', YLeafList(YType.uint16, 'sats-activate-aborted')),
                    ('sats_update_aborted', YLeafList(YType.uint16, 'sats-update-aborted')),
                    ('sats_deactivate_aborted', YLeafList(YType.uint16, 'sats-deactivate-aborted')),
                    ('sats_remove_aborted', YLeafList(YType.uint16, 'sats-remove-aborted')),
                    ('sats_no_operation', YLeafList(YType.uint16, 'sats-no-operation')),
                    ('sats_completed', YLeafList(YType.uint16, 'sats-completed')),
                ])
                self.operation_id = None
                self.operation_id_xr = None
                self.satellite_range = None
                self.sats_not_initiated = []
                self.sats_transferring = []
                self.sats_activating = []
                self.sats_updating = []
                self.sats_deactivating = []
                self.sats_removing = []
                self.sats_transfer_failed = []
                self.sats_activate_failed = []
                self.sats_update_failed = []
                self.sats_deactivate_failed = []
                self.sats_remove_failed = []
                self.sats_transfer_aborted = []
                self.sats_activate_aborted = []
                self.sats_update_aborted = []
                self.sats_deactivate_aborted = []
                self.sats_remove_aborted = []
                self.sats_no_operation = []
                self.sats_completed = []
                self._segment_path = lambda: "install-op-status" + "[operation-id='" + str(self.operation_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/install-op-statuses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.InstallOpStatuses.InstallOpStatus, ['operation_id', 'operation_id_xr', 'satellite_range', 'sats_not_initiated', 'sats_transferring', 'sats_activating', 'sats_updating', 'sats_deactivating', 'sats_removing', 'sats_transfer_failed', 'sats_activate_failed', 'sats_update_failed', 'sats_deactivate_failed', 'sats_remove_failed', 'sats_transfer_aborted', 'sats_activate_aborted', 'sats_update_aborted', 'sats_deactivate_aborted', 'sats_remove_aborted', 'sats_no_operation', 'sats_completed'], name, value)


    class SatelliteProperties(Entity):
        """
        ICPE GCO operational information
        
        .. attribute:: id_ranges
        
        	Satellite ID range table
        	**type**\:  :py:class:`IdRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteProperties.IdRanges>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SatelliteProperties, self).__init__()

            self.yang_name = "satellite-properties"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("id-ranges", ("id_ranges", NvSatellite.SatelliteProperties.IdRanges))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.id_ranges = NvSatellite.SatelliteProperties.IdRanges()
            self.id_ranges.parent = self
            self._children_name_map["id_ranges"] = "id-ranges"
            self._children_yang_names.add("id-ranges")
            self._segment_path = lambda: "satellite-properties"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()


        class IdRanges(Entity):
            """
            Satellite ID range table
            
            .. attribute:: id_range
            
            	Satellite ID range
            	**type**\: list of  		 :py:class:`IdRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteProperties.IdRanges.IdRange>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SatelliteProperties.IdRanges, self).__init__()

                self.yang_name = "id-ranges"
                self.yang_parent_name = "satellite-properties"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("id-range", ("id_range", NvSatellite.SatelliteProperties.IdRanges.IdRange))])
                self._leafs = OrderedDict()

                self.id_range = YList(self)
                self._segment_path = lambda: "id-ranges"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-properties/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SatelliteProperties.IdRanges, [], name, value)


            class IdRange(Entity):
                """
                Satellite ID range
                
                .. attribute:: sat_id_range  (key)
                
                	Sat ID range
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: min
                
                	Min
                	**type**\: int
                
                	**range:** 0..2147483647
                
                .. attribute:: max
                
                	Max
                	**type**\: int
                
                	**range:** 0..2147483647
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SatelliteProperties.IdRanges.IdRange, self).__init__()

                    self.yang_name = "id-range"
                    self.yang_parent_name = "id-ranges"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['sat_id_range']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('sat_id_range', YLeaf(YType.str, 'sat-id-range')),
                        ('min', YLeaf(YType.uint32, 'min')),
                        ('max', YLeaf(YType.uint32, 'max')),
                    ])
                    self.sat_id_range = None
                    self.min = None
                    self.max = None
                    self._segment_path = lambda: "id-range" + "[sat-id-range='" + str(self.sat_id_range) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/satellite-properties/id-ranges/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SatelliteProperties.IdRanges.IdRange, ['sat_id_range', 'min', 'max'], name, value)


    class SdacpDiscovery2S(Entity):
        """
        ICPE Configured interface state information
        table
        
        .. attribute:: sdacp_discovery2
        
        	ICPE Configured interface state information
        	**type**\: list of  		 :py:class:`SdacpDiscovery2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2>`
        
        

        """

        _prefix = 'icpe-sdacp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SdacpDiscovery2S, self).__init__()

            self.yang_name = "sdacp-discovery2s"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sdacp-discovery2", ("sdacp_discovery2", NvSatellite.SdacpDiscovery2S.SdacpDiscovery2))])
            self._leafs = OrderedDict()

            self.sdacp_discovery2 = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SdacpDiscovery2S, [], name, value)


        class SdacpDiscovery2(Entity):
            """
            ICPE Configured interface state information
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\: str
            
            .. attribute:: interface
            
            	ICPE Discovery interface state information table
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface>`
            
            .. attribute:: satellite
            
            	ICPE Satellite state information table
            	**type**\: list of  		 :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite>`
            
            

            """

            _prefix = 'icpe-sdacp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2, self).__init__()

                self.yang_name = "sdacp-discovery2"
                self.yang_parent_name = "sdacp-discovery2s"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface", ("interface", NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface)), ("satellite", ("satellite", NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite))])
                self._leafs = OrderedDict([
                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                    ('interface_name_xr', YLeaf(YType.str, 'interface-name-xr')),
                ])
                self.interface_name = None
                self.interface_name_xr = None

                self.interface = YList(self)
                self.satellite = YList(self)
                self._segment_path = lambda: "sdacp-discovery2" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-sdacp-oper:sdacp-discovery2s/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2, ['interface_name', 'interface_name_xr'], name, value)


            class Interface(Entity):
                """
                ICPE Discovery interface state information table
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\: str
                
                .. attribute:: interface_status
                
                	Interface status
                	**type**\:  :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "sdacp-discovery2"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('interface_status', YLeaf(YType.enumeration, 'interface-status')),
                    ])
                    self.interface_name = None
                    self.interface_status = None
                    self._segment_path = lambda: "interface"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface, ['interface_name', 'interface_status'], name, value)


            class Satellite(Entity):
                """
                ICPE Satellite state information table
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: satellite_status
                
                	Satellite status
                	**type**\:  :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: satellite_ip_address
                
                	Satellite IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: host_ip_address
                
                	Host IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface
                
                	ICPE Discovered satellite state information table
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface>`
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "sdacp-discovery2"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("interface", ("interface", NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface))])
                    self._leafs = OrderedDict([
                        ('satellite_id', YLeaf(YType.uint16, 'satellite-id')),
                        ('satellite_status', YLeaf(YType.enumeration, 'satellite-status')),
                        ('conflict_reason', YLeaf(YType.uint32, 'conflict-reason')),
                        ('satellite_ip_address', YLeaf(YType.str, 'satellite-ip-address')),
                        ('host_ip_address', YLeaf(YType.str, 'host-ip-address')),
                    ])
                    self.satellite_id = None
                    self.satellite_status = None
                    self.conflict_reason = None
                    self.satellite_ip_address = None
                    self.host_ip_address = None

                    self.interface = YList(self)
                    self._segment_path = lambda: "satellite"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite, ['satellite_id', 'satellite_status', 'conflict_reason', 'satellite_ip_address', 'host_ip_address'], name, value)


                class Interface(Entity):
                    """
                    ICPE Discovered satellite state information
                    table
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: satellite_status
                    
                    	Satellite status
                    	**type**\:  :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: satellite_chassis_vendor
                    
                    	Satellite chassis vendor
                    	**type**\: str
                    
                    .. attribute:: satellite_interface_id
                    
                    	Satellite interface ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: satellite_interface_mac
                    
                    	Satellite interface MAC
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: satellite_chassis_mac
                    
                    	Satellite chassis MAC
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: satellite_serial_id
                    
                    	Satellite serial id
                    	**type**\: str
                    
                    .. attribute:: satellite_module_vendor
                    
                    	Satellite module vendor
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "satellite"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_handle', YLeaf(YType.str, 'interface-handle')),
                            ('satellite_status', YLeaf(YType.enumeration, 'satellite-status')),
                            ('conflict_reason', YLeaf(YType.uint32, 'conflict-reason')),
                            ('satellite_chassis_vendor', YLeaf(YType.str, 'satellite-chassis-vendor')),
                            ('satellite_interface_id', YLeaf(YType.uint32, 'satellite-interface-id')),
                            ('satellite_interface_mac', YLeaf(YType.str, 'satellite-interface-mac')),
                            ('satellite_chassis_mac', YLeaf(YType.str, 'satellite-chassis-mac')),
                            ('satellite_serial_id', YLeaf(YType.str, 'satellite-serial-id')),
                            ('satellite_module_vendor', YLeaf(YType.str, 'satellite-module-vendor')),
                        ])
                        self.interface_handle = None
                        self.satellite_status = None
                        self.conflict_reason = None
                        self.satellite_chassis_vendor = None
                        self.satellite_interface_id = None
                        self.satellite_interface_mac = None
                        self.satellite_chassis_mac = None
                        self.satellite_serial_id = None
                        self.satellite_module_vendor = None
                        self._segment_path = lambda: "interface"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface, ['interface_handle', 'satellite_status', 'conflict_reason', 'satellite_chassis_vendor', 'satellite_interface_id', 'satellite_interface_mac', 'satellite_chassis_mac', 'satellite_serial_id', 'satellite_module_vendor'], name, value)


    class IcpeDpms(Entity):
        """
        ICPE DPM operational information table
        
        .. attribute:: icpe_dpm
        
        	ICPE DPM operational information
        	**type**\: list of  		 :py:class:`IcpeDpm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms.IcpeDpm>`
        
        

        """

        _prefix = 'icpe-sdacp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.IcpeDpms, self).__init__()

            self.yang_name = "icpe-dpms"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("icpe-dpm", ("icpe_dpm", NvSatellite.IcpeDpms.IcpeDpm))])
            self._leafs = OrderedDict()

            self.icpe_dpm = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.IcpeDpms, [], name, value)


        class IcpeDpm(Entity):
            """
            ICPE DPM operational information
            
            .. attribute:: discovery_interface  (key)
            
            	Discovery interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: discovery_interface_xr
            
            	Discovery interface
            	**type**\: str
            
            .. attribute:: discovery_interface_handle
            
            	Discovery interface handle
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: discovery_interface_status
            
            	Discovery interface status
            	**type**\:  :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
            
            .. attribute:: ident_packets_received
            
            	Ident packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ready_packets_received
            
            	Ready packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: los_packets_received
            
            	Los packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: invalid_packets_received
            
            	Invalid packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: configuration_packets_sent
            
            	Configuration packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ack_packets_sent
            
            	Ack packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: reject_packets_sent
            
            	Reject packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: probe_packets_sent
            
            	Probe packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: host_ack_packets_received
            
            	Host ack packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: host_ack_packets_sent
            
            	Host ack packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: secs_since_pkts_cleaned
            
            	Secs since pkts cleaned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: satellite
            
            	ICPE DPM satellite operational information table
            	**type**\: list of  		 :py:class:`Satellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms.IcpeDpm.Satellite>`
            
            .. attribute:: remote_host
            
            	ICPE DPM remote host operational information table
            	**type**\: list of  		 :py:class:`RemoteHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.IcpeDpms.IcpeDpm.RemoteHost>`
            
            

            """

            _prefix = 'icpe-sdacp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.IcpeDpms.IcpeDpm, self).__init__()

                self.yang_name = "icpe-dpm"
                self.yang_parent_name = "icpe-dpms"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['discovery_interface']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("satellite", ("satellite", NvSatellite.IcpeDpms.IcpeDpm.Satellite)), ("remote-host", ("remote_host", NvSatellite.IcpeDpms.IcpeDpm.RemoteHost))])
                self._leafs = OrderedDict([
                    ('discovery_interface', YLeaf(YType.str, 'discovery-interface')),
                    ('discovery_interface_xr', YLeaf(YType.str, 'discovery-interface-xr')),
                    ('discovery_interface_handle', YLeaf(YType.str, 'discovery-interface-handle')),
                    ('discovery_interface_status', YLeaf(YType.enumeration, 'discovery-interface-status')),
                    ('ident_packets_received', YLeaf(YType.uint64, 'ident-packets-received')),
                    ('ready_packets_received', YLeaf(YType.uint64, 'ready-packets-received')),
                    ('los_packets_received', YLeaf(YType.uint64, 'los-packets-received')),
                    ('invalid_packets_received', YLeaf(YType.uint64, 'invalid-packets-received')),
                    ('configuration_packets_sent', YLeaf(YType.uint64, 'configuration-packets-sent')),
                    ('ack_packets_sent', YLeaf(YType.uint64, 'ack-packets-sent')),
                    ('reject_packets_sent', YLeaf(YType.uint64, 'reject-packets-sent')),
                    ('probe_packets_sent', YLeaf(YType.uint64, 'probe-packets-sent')),
                    ('host_ack_packets_received', YLeaf(YType.uint64, 'host-ack-packets-received')),
                    ('host_ack_packets_sent', YLeaf(YType.uint64, 'host-ack-packets-sent')),
                    ('secs_since_pkts_cleaned', YLeaf(YType.uint64, 'secs-since-pkts-cleaned')),
                ])
                self.discovery_interface = None
                self.discovery_interface_xr = None
                self.discovery_interface_handle = None
                self.discovery_interface_status = None
                self.ident_packets_received = None
                self.ready_packets_received = None
                self.los_packets_received = None
                self.invalid_packets_received = None
                self.configuration_packets_sent = None
                self.ack_packets_sent = None
                self.reject_packets_sent = None
                self.probe_packets_sent = None
                self.host_ack_packets_received = None
                self.host_ack_packets_sent = None
                self.secs_since_pkts_cleaned = None

                self.satellite = YList(self)
                self.remote_host = YList(self)
                self._segment_path = lambda: "icpe-dpm" + "[discovery-interface='" + str(self.discovery_interface) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-sdacp-oper:icpe-dpms/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.IcpeDpms.IcpeDpm, ['discovery_interface', 'discovery_interface_xr', 'discovery_interface_handle', 'discovery_interface_status', 'ident_packets_received', 'ready_packets_received', 'los_packets_received', 'invalid_packets_received', 'configuration_packets_sent', 'ack_packets_sent', 'reject_packets_sent', 'probe_packets_sent', 'host_ack_packets_received', 'host_ack_packets_sent', 'secs_since_pkts_cleaned'], name, value)


            class Satellite(Entity):
                """
                ICPE DPM satellite operational information table
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: satellite_interface_id
                
                	Satellite interface ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: satellite_interface_mac
                
                	Satellite interface MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: satellite_ip_address
                
                	Satellite IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: host_ip_address
                
                	Host IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: satellite_chassis_type
                
                	Satellite chassis type
                	**type**\: str
                
                .. attribute:: satellite_chassis_vendor
                
                	Satellite chassis vendor
                	**type**\: str
                
                .. attribute:: satellite_chassis_mac
                
                	Satellite chassis MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: satellite_serial_id
                
                	Satellite serial id
                	**type**\: str
                
                .. attribute:: satellite_module_type
                
                	Satellite module type
                	**type**\: str
                
                .. attribute:: satellite_module_vendor
                
                	Satellite module vendor
                	**type**\: str
                
                .. attribute:: satellite_module_mac
                
                	Satellite module MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_sys_mac
                
                	Received sys MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: host_chassis_type
                
                	Host chassis type
                	**type**\: str
                
                .. attribute:: host_chassis_vendor
                
                	Host chassis vendor
                	**type**\: str
                
                .. attribute:: host_chassis_mac
                
                	Host chassis MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: discovery_protocol_state
                
                	Discovery protocol state
                	**type**\:  :py:class:`DpmProtoState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoState>`
                
                .. attribute:: last_imdr_state
                
                	Last IMDR state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_timeout
                
                	Current timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_queued_for_efd
                
                	Is queued for EFD
                	**type**\: bool
                
                .. attribute:: is_queued_for_oc
                
                	Is queued for OC
                	**type**\: bool
                
                .. attribute:: ifmgr_state
                
                	Ifmgr state
                	**type**\: bool
                
                .. attribute:: legacy
                
                	Legacy
                	**type**\: bool
                
                .. attribute:: deleting
                
                	Deleting
                	**type**\: bool
                
                .. attribute:: ident_packets_received
                
                	Ident packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ready_packets_received
                
                	Ready packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: los_packets_received
                
                	Los packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: invalid_packets_received
                
                	Invalid packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: configuration_packets_sent
                
                	Configuration packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ack_packets_sent
                
                	Ack packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reject_packets_sent
                
                	Reject packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: secs_since_pkts_cleaned
                
                	Secs since pkts cleaned
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.IcpeDpms.IcpeDpm.Satellite, self).__init__()

                    self.yang_name = "satellite"
                    self.yang_parent_name = "icpe-dpm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('satellite_id', YLeaf(YType.uint16, 'satellite-id')),
                        ('satellite_interface_id', YLeaf(YType.uint32, 'satellite-interface-id')),
                        ('satellite_interface_mac', YLeaf(YType.str, 'satellite-interface-mac')),
                        ('satellite_ip_address', YLeaf(YType.str, 'satellite-ip-address')),
                        ('host_ip_address', YLeaf(YType.str, 'host-ip-address')),
                        ('satellite_chassis_type', YLeaf(YType.str, 'satellite-chassis-type')),
                        ('satellite_chassis_vendor', YLeaf(YType.str, 'satellite-chassis-vendor')),
                        ('satellite_chassis_mac', YLeaf(YType.str, 'satellite-chassis-mac')),
                        ('satellite_serial_id', YLeaf(YType.str, 'satellite-serial-id')),
                        ('satellite_module_type', YLeaf(YType.str, 'satellite-module-type')),
                        ('satellite_module_vendor', YLeaf(YType.str, 'satellite-module-vendor')),
                        ('satellite_module_mac', YLeaf(YType.str, 'satellite-module-mac')),
                        ('conflict_reason', YLeaf(YType.uint32, 'conflict-reason')),
                        ('received_sys_mac', YLeaf(YType.str, 'received-sys-mac')),
                        ('host_chassis_type', YLeaf(YType.str, 'host-chassis-type')),
                        ('host_chassis_vendor', YLeaf(YType.str, 'host-chassis-vendor')),
                        ('host_chassis_mac', YLeaf(YType.str, 'host-chassis-mac')),
                        ('discovery_protocol_state', YLeaf(YType.enumeration, 'discovery-protocol-state')),
                        ('last_imdr_state', YLeaf(YType.uint32, 'last-imdr-state')),
                        ('current_timeout', YLeaf(YType.uint32, 'current-timeout')),
                        ('is_queued_for_efd', YLeaf(YType.boolean, 'is-queued-for-efd')),
                        ('is_queued_for_oc', YLeaf(YType.boolean, 'is-queued-for-oc')),
                        ('ifmgr_state', YLeaf(YType.boolean, 'ifmgr-state')),
                        ('legacy', YLeaf(YType.boolean, 'legacy')),
                        ('deleting', YLeaf(YType.boolean, 'deleting')),
                        ('ident_packets_received', YLeaf(YType.uint64, 'ident-packets-received')),
                        ('ready_packets_received', YLeaf(YType.uint64, 'ready-packets-received')),
                        ('los_packets_received', YLeaf(YType.uint64, 'los-packets-received')),
                        ('invalid_packets_received', YLeaf(YType.uint64, 'invalid-packets-received')),
                        ('configuration_packets_sent', YLeaf(YType.uint64, 'configuration-packets-sent')),
                        ('ack_packets_sent', YLeaf(YType.uint64, 'ack-packets-sent')),
                        ('reject_packets_sent', YLeaf(YType.uint64, 'reject-packets-sent')),
                        ('secs_since_pkts_cleaned', YLeaf(YType.uint64, 'secs-since-pkts-cleaned')),
                    ])
                    self.satellite_id = None
                    self.satellite_interface_id = None
                    self.satellite_interface_mac = None
                    self.satellite_ip_address = None
                    self.host_ip_address = None
                    self.satellite_chassis_type = None
                    self.satellite_chassis_vendor = None
                    self.satellite_chassis_mac = None
                    self.satellite_serial_id = None
                    self.satellite_module_type = None
                    self.satellite_module_vendor = None
                    self.satellite_module_mac = None
                    self.conflict_reason = None
                    self.received_sys_mac = None
                    self.host_chassis_type = None
                    self.host_chassis_vendor = None
                    self.host_chassis_mac = None
                    self.discovery_protocol_state = None
                    self.last_imdr_state = None
                    self.current_timeout = None
                    self.is_queued_for_efd = None
                    self.is_queued_for_oc = None
                    self.ifmgr_state = None
                    self.legacy = None
                    self.deleting = None
                    self.ident_packets_received = None
                    self.ready_packets_received = None
                    self.los_packets_received = None
                    self.invalid_packets_received = None
                    self.configuration_packets_sent = None
                    self.ack_packets_sent = None
                    self.reject_packets_sent = None
                    self.secs_since_pkts_cleaned = None
                    self._segment_path = lambda: "satellite"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.IcpeDpms.IcpeDpm.Satellite, ['satellite_id', 'satellite_interface_id', 'satellite_interface_mac', 'satellite_ip_address', 'host_ip_address', 'satellite_chassis_type', 'satellite_chassis_vendor', 'satellite_chassis_mac', 'satellite_serial_id', 'satellite_module_type', 'satellite_module_vendor', 'satellite_module_mac', 'conflict_reason', 'received_sys_mac', 'host_chassis_type', 'host_chassis_vendor', 'host_chassis_mac', 'discovery_protocol_state', 'last_imdr_state', 'current_timeout', 'is_queued_for_efd', 'is_queued_for_oc', 'ifmgr_state', 'legacy', 'deleting', 'ident_packets_received', 'ready_packets_received', 'los_packets_received', 'invalid_packets_received', 'configuration_packets_sent', 'ack_packets_sent', 'reject_packets_sent', 'secs_since_pkts_cleaned'], name, value)


            class RemoteHost(Entity):
                """
                ICPE DPM remote host operational information
                table
                
                .. attribute:: host_chassis_mac
                
                	Host chassis MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: host_interface_mac
                
                	Host interface MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: discovery_protocol_state
                
                	Discovery protocol state
                	**type**\:  :py:class:`DpmProtoHostState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.DpmProtoHostState>`
                
                .. attribute:: route_length
                
                	Route length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_timeout
                
                	Current timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: host_ack_packets_received
                
                	Host ack packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: host_ack_packets_sent
                
                	Host ack packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: secs_since_pkts_cleaned
                
                	Secs since pkts cleaned
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.IcpeDpms.IcpeDpm.RemoteHost, self).__init__()

                    self.yang_name = "remote-host"
                    self.yang_parent_name = "icpe-dpm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('host_chassis_mac', YLeaf(YType.str, 'host-chassis-mac')),
                        ('host_interface_mac', YLeaf(YType.str, 'host-interface-mac')),
                        ('discovery_protocol_state', YLeaf(YType.enumeration, 'discovery-protocol-state')),
                        ('route_length', YLeaf(YType.uint32, 'route-length')),
                        ('current_timeout', YLeaf(YType.uint32, 'current-timeout')),
                        ('host_ack_packets_received', YLeaf(YType.uint64, 'host-ack-packets-received')),
                        ('host_ack_packets_sent', YLeaf(YType.uint64, 'host-ack-packets-sent')),
                        ('secs_since_pkts_cleaned', YLeaf(YType.uint64, 'secs-since-pkts-cleaned')),
                    ])
                    self.host_chassis_mac = None
                    self.host_interface_mac = None
                    self.discovery_protocol_state = None
                    self.route_length = None
                    self.current_timeout = None
                    self.host_ack_packets_received = None
                    self.host_ack_packets_sent = None
                    self.secs_since_pkts_cleaned = None
                    self._segment_path = lambda: "remote-host"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.IcpeDpms.IcpeDpm.RemoteHost, ['host_chassis_mac', 'host_interface_mac', 'discovery_protocol_state', 'route_length', 'current_timeout', 'host_ack_packets_received', 'host_ack_packets_sent', 'secs_since_pkts_cleaned'], name, value)


    class SdacpControls(Entity):
        """
        SDAC Protocol Discovery information table
        
        .. attribute:: sdacp_control
        
        	SDAC Protocol Discovery information
        	**type**\: list of  		 :py:class:`SdacpControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl>`
        
        

        """

        _prefix = 'icpe-sdacp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellite.SdacpControls, self).__init__()

            self.yang_name = "sdacp-controls"
            self.yang_parent_name = "nv-satellite"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sdacp-control", ("sdacp_control", NvSatellite.SdacpControls.SdacpControl))])
            self._leafs = OrderedDict()

            self.sdacp_control = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls"
            self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvSatellite.SdacpControls, [], name, value)


        class SdacpControl(Entity):
            """
            SDAC Protocol Discovery information
            
            .. attribute:: satellite_id  (key)
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 100..65534
            
            .. attribute:: protocol_state_timestamp
            
            	Timestamp
            	**type**\:  :py:class:`ProtocolStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp>`
            
            .. attribute:: transport_error_timestamp
            
            	Timestamp
            	**type**\:  :py:class:`TransportErrorTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp>`
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: satellite_ip_address
            
            	Satellite IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ip_address_auto
            
            	IP address auto
            	**type**\: bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: control_protocol_state
            
            	Control protocol state
            	**type**\:  :py:class:`IcpeCpmControlFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.IcpeCpmControlFsmState>`
            
            .. attribute:: transport_error
            
            	Transport error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: channel
            
            	Channels on satellite table
            	**type**\: list of  		 :py:class:`Channel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel>`
            
            

            """

            _prefix = 'icpe-sdacp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellite.SdacpControls.SdacpControl, self).__init__()

                self.yang_name = "sdacp-control"
                self.yang_parent_name = "sdacp-controls"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['satellite_id']
                self._child_container_classes = OrderedDict([("protocol-state-timestamp", ("protocol_state_timestamp", NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp)), ("transport-error-timestamp", ("transport_error_timestamp", NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp))])
                self._child_list_classes = OrderedDict([("channel", ("channel", NvSatellite.SdacpControls.SdacpControl.Channel))])
                self._leafs = OrderedDict([
                    ('satellite_id', YLeaf(YType.uint32, 'satellite-id')),
                    ('satellite_id_xr', YLeaf(YType.uint16, 'satellite-id-xr')),
                    ('satellite_ip_address', YLeaf(YType.str, 'satellite-ip-address')),
                    ('ip_address_auto', YLeaf(YType.boolean, 'ip-address-auto')),
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('control_protocol_state', YLeaf(YType.enumeration, 'control-protocol-state')),
                    ('transport_error', YLeaf(YType.uint32, 'transport-error')),
                ])
                self.satellite_id = None
                self.satellite_id_xr = None
                self.satellite_ip_address = None
                self.ip_address_auto = None
                self.vrf_name = None
                self.control_protocol_state = None
                self.transport_error = None

                self.protocol_state_timestamp = NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp()
                self.protocol_state_timestamp.parent = self
                self._children_name_map["protocol_state_timestamp"] = "protocol-state-timestamp"
                self._children_yang_names.add("protocol-state-timestamp")

                self.transport_error_timestamp = NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp()
                self.transport_error_timestamp.parent = self
                self._children_name_map["transport_error_timestamp"] = "transport-error-timestamp"
                self._children_yang_names.add("transport-error-timestamp")

                self.channel = YList(self)
                self._segment_path = lambda: "sdacp-control" + "[satellite-id='" + str(self.satellite_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-sdacp-oper:sdacp-controls/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NvSatellite.SdacpControls.SdacpControl, ['satellite_id', 'satellite_id_xr', 'satellite_ip_address', 'ip_address_auto', 'vrf_name', 'control_protocol_state', 'transport_error'], name, value)


            class ProtocolStateTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp, self).__init__()

                    self.yang_name = "protocol-state-timestamp"
                    self.yang_parent_name = "sdacp-control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                        ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                    ])
                    self.seconds = None
                    self.nanoseconds = None
                    self._segment_path = lambda: "protocol-state-timestamp"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp, ['seconds', 'nanoseconds'], name, value)


            class TransportErrorTimestamp(Entity):
                """
                Timestamp
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp, self).__init__()

                    self.yang_name = "transport-error-timestamp"
                    self.yang_parent_name = "sdacp-control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                        ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                    ])
                    self.seconds = None
                    self.nanoseconds = None
                    self._segment_path = lambda: "transport-error-timestamp"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp, ['seconds', 'nanoseconds'], name, value)


            class Channel(Entity):
                """
                Channels on satellite table
                
                .. attribute:: capabilities
                
                	Capabilities
                	**type**\:  :py:class:`Capabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities>`
                
                .. attribute:: resync_state_timestamp
                
                	Timestamp
                	**type**\:  :py:class:`ResyncStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp>`
                
                .. attribute:: channel_state_timestamp
                
                	Timestamp
                	**type**\:  :py:class:`ChannelStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp>`
                
                .. attribute:: channel_id
                
                	Channel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: resync_state
                
                	Resync state
                	**type**\:  :py:class:`IcpeCpmChannelResyncState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.IcpeCpmChannelResyncState>`
                
                .. attribute:: channel_state
                
                	Channel state
                	**type**\:  :py:class:`IcpeCpmChanFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper.IcpeCpmChanFsmState>`
                
                .. attribute:: control_messages_sent
                
                	Control messages sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_sent
                
                	Normal messages sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_received
                
                	Control messages received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_received
                
                	Normal messages received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_dropped
                
                	Control messages dropped
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_dropped
                
                	Normal messages dropped
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: secs_since_last_cleared
                
                	Secs since last cleared
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                .. attribute:: version
                
                	Version
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'icpe-sdacp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellite.SdacpControls.SdacpControl.Channel, self).__init__()

                    self.yang_name = "channel"
                    self.yang_parent_name = "sdacp-control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("capabilities", ("capabilities", NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities)), ("resync-state-timestamp", ("resync_state_timestamp", NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp)), ("channel-state-timestamp", ("channel_state_timestamp", NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('channel_id', YLeaf(YType.uint16, 'channel-id')),
                        ('resync_state', YLeaf(YType.enumeration, 'resync-state')),
                        ('channel_state', YLeaf(YType.enumeration, 'channel-state')),
                        ('control_messages_sent', YLeaf(YType.uint64, 'control-messages-sent')),
                        ('normal_messages_sent', YLeaf(YType.uint64, 'normal-messages-sent')),
                        ('control_messages_received', YLeaf(YType.uint64, 'control-messages-received')),
                        ('normal_messages_received', YLeaf(YType.uint64, 'normal-messages-received')),
                        ('control_messages_dropped', YLeaf(YType.uint64, 'control-messages-dropped')),
                        ('normal_messages_dropped', YLeaf(YType.uint64, 'normal-messages-dropped')),
                        ('secs_since_last_cleared', YLeaf(YType.uint64, 'secs-since-last-cleared')),
                        ('version', YLeaf(YType.uint16, 'version')),
                    ])
                    self.channel_id = None
                    self.resync_state = None
                    self.channel_state = None
                    self.control_messages_sent = None
                    self.normal_messages_sent = None
                    self.control_messages_received = None
                    self.normal_messages_received = None
                    self.control_messages_dropped = None
                    self.normal_messages_dropped = None
                    self.secs_since_last_cleared = None
                    self.version = None

                    self.capabilities = NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities()
                    self.capabilities.parent = self
                    self._children_name_map["capabilities"] = "capabilities"
                    self._children_yang_names.add("capabilities")

                    self.resync_state_timestamp = NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp()
                    self.resync_state_timestamp.parent = self
                    self._children_name_map["resync_state_timestamp"] = "resync-state-timestamp"
                    self._children_yang_names.add("resync-state-timestamp")

                    self.channel_state_timestamp = NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp()
                    self.channel_state_timestamp.parent = self
                    self._children_name_map["channel_state_timestamp"] = "channel-state-timestamp"
                    self._children_yang_names.add("channel-state-timestamp")
                    self._segment_path = lambda: "channel"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.Channel, ['channel_id', 'resync_state', 'channel_state', 'control_messages_sent', 'normal_messages_sent', 'control_messages_received', 'normal_messages_received', 'control_messages_dropped', 'normal_messages_dropped', 'secs_since_last_cleared', 'version'], name, value)


                class Capabilities(Entity):
                    """
                    Capabilities
                    
                    .. attribute:: tl_vs
                    
                    	Capability TLVs table
                    	**type**\: list of  		 :py:class:`TlVs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs>`
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities, self).__init__()

                        self.yang_name = "capabilities"
                        self.yang_parent_name = "channel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("tl-vs", ("tl_vs", NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs))])
                        self._leafs = OrderedDict()

                        self.tl_vs = YList(self)
                        self._segment_path = lambda: "capabilities"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities, [], name, value)


                    class TlVs(Entity):
                        """
                        Capability TLVs table
                        
                        .. attribute:: type
                        
                        	Type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: debug
                        
                        	Debug
                        	**type**\: str
                        
                        .. attribute:: value
                        
                        	Value
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'icpe-sdacp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs, self).__init__()

                            self.yang_name = "tl-vs"
                            self.yang_parent_name = "capabilities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.uint32, 'type')),
                                ('debug', YLeaf(YType.str, 'debug')),
                                ('value', YLeafList(YType.uint8, 'value')),
                            ])
                            self.type = None
                            self.debug = None
                            self.value = []
                            self._segment_path = lambda: "tl-vs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs, ['type', 'debug', 'value'], name, value)


                class ResyncStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp, self).__init__()

                        self.yang_name = "resync-state-timestamp"
                        self.yang_parent_name = "channel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', YLeaf(YType.uint32, 'seconds')),
                            ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "resync-state-timestamp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp, ['seconds', 'nanoseconds'], name, value)


                class ChannelStateTimestamp(Entity):
                    """
                    Timestamp
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'icpe-sdacp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp, self).__init__()

                        self.yang_name = "channel-state-timestamp"
                        self.yang_parent_name = "channel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', YLeaf(YType.uint32, 'seconds')),
                            ('nanoseconds', YLeaf(YType.uint32, 'nanoseconds')),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "channel-state-timestamp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp, ['seconds', 'nanoseconds'], name, value)

    def clone_ptr(self):
        self._top_entity = NvSatellite()
        return self._top_entity

