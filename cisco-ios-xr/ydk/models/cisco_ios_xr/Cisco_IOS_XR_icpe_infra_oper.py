""" Cisco_IOS_XR_icpe_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package operational data.

This module contains definitions
for the following management objects\:
  nv\-satellite\: Satellite operational information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IcpeGcoOperControlReasonEnum(Enum):
    """
    IcpeGcoOperControlReasonEnum

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

    icpe_gco_oper_control_reason_unknown_error = 0

    icpe_gco_oper_control_reason_wrong_chassis_type = 1

    icpe_gco_oper_control_reason_wrong_chassis_serial = 2

    icpe_gco_oper_control_reason_needs_to_upgrade = 3

    icpe_gco_oper_control_reason_none = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeGcoOperControlReasonEnum']


class IcpeOperConflictEnum(Enum):
    """
    IcpeOperConflictEnum

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

    icpe_oper_conflict_not_calculated = 0

    icpe_oper_conflict_no_conflict = 1

    icpe_oper_conflict_satellite_not_configured = 2

    icpe_oper_conflict_satellite_no_type = 3

    icpe_oper_conflict_satellite_id_invalid = 4

    icpe_oper_conflict_satellite_no_ipv4_addr = 5

    icpe_oper_conflict_satellite_conflicting_ipv4_addr = 6

    icpe_oper_conflict_no_configured_links = 7

    icpe_oper_conflict_no_discovered_links = 8

    icpe_oper_conflict_invalid_ports = 9

    icpe_oper_conflict_ports_overlap = 10

    icpe_oper_conflict_waiting_for_ipv4_addr = 11

    icpe_oper_conflict_waiting_for_vrf = 12

    icpe_oper_conflict_different_ipv4_addr = 13

    icpe_oper_conflict_different_vrf = 14

    icpe_oper_conflict_satellite_link_ipv4_overlap = 15

    icpe_oper_conflict_waiting_for_ident = 16

    icpe_oper_conflict_multiple_ids = 17

    icpe_oper_conflict_multiple_satellites = 18

    icpe_oper_conflict_ident_rejected = 19

    icpe_oper_conflict_interface_down = 20

    icpe_oper_conflict_auto_ip_unavailable = 21

    icpe_oper_conflict_satellite_auto_ip_link_manual_ip = 22

    icpe_oper_conflict_link_auto_ip_satellite_manual_ip = 23

    icpe_oper_conflict_serial_num_mismatch = 24

    icpe_oper_conflict_satellite_not_identified = 25

    icpe_oper_conflict_satellite_unsupported_type = 26

    icpe_oper_conflict_satellite_partition_unsupported = 27

    icpe_oper_conflict_satellite_no_serial_number = 28

    icpe_oper_conflict_satellite_conflicting_serial_number = 29

    icpe_oper_conflict_satellite_link_waiting_for_arp = 30

    icpe_oper_conflict_host_pe_isolated_split_brain = 31

    icpe_oper_conflict_fabric_iccp_group_inconsistent = 32

    icpe_oper_conflict_invalid_iccp_group = 33

    icpe_oper_conflict_port_rejected = 34

    icpe_oper_conflict_satellite_icl_not_supported = 35

    icpe_oper_conflict_multiple_serial_number = 36

    icpe_oper_conflict_multiple_mac_address = 37


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperConflictEnum']


class IcpeOperDiscdLinkStateEnum(Enum):
    """
    IcpeOperDiscdLinkStateEnum

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

    icpe_oper_discd_link_state_stopped = 0

    icpe_oper_discd_link_state_probing = 1

    icpe_oper_discd_link_state_configuring = 2

    icpe_oper_discd_link_state_ready = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperDiscdLinkStateEnum']


class IcpeOperFabricPortEnum(Enum):
    """
    IcpeOperFabricPortEnum

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

    icpe_oper_fabric_port_unknown = 0

    icpe_oper_fabric_port_n_v_fabric_gig_e = 1

    icpe_oper_fabric_port_n_v_fabric_ten_gig_e = 2

    icpe_oper_fabric_port_n_v_fabric_hundred_gig_e = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperFabricPortEnum']


class IcpeOperInstallStateEnum(Enum):
    """
    IcpeOperInstallStateEnum

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

    icpe_oper_install_state_stable = 0

    icpe_oper_install_state_transferring = 1

    icpe_oper_install_state_transferred = 2

    icpe_oper_install_state_installing = 3

    icpe_oper_install_state_in_progress = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperInstallStateEnum']


class IcpeOperPortEnum(Enum):
    """
    IcpeOperPortEnum

    Icpe oper port

    .. data:: icpe_oper_port_unknown = 0

    	Unknown

    .. data:: icpe_oper_port_gigabit_ethernet = 1

    	Gigabit ethernet

    .. data:: icpe_oper_port_ten_gig_e = 2

    	Ten gig e

    """

    icpe_oper_port_unknown = 0

    icpe_oper_port_gigabit_ethernet = 1

    icpe_oper_port_ten_gig_e = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperPortEnum']


class IcpeOperSdacpSessStateEnum(Enum):
    """
    IcpeOperSdacpSessStateEnum

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

    icpe_oper_sdacp_sess_state_not_created = 0

    icpe_oper_sdacp_sess_state_created = 1

    icpe_oper_sdacp_sess_state_authentication_not_ok = 2

    icpe_oper_sdacp_sess_state_authentication_ok = 3

    icpe_oper_sdacp_sess_state_version_not_ok = 4

    icpe_oper_sdacp_sess_state_up = 5

    icpe_oper_sdacp_sess_state_issu = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperSdacpSessStateEnum']


class IcpeOperTopoRemoteSourceEnum(Enum):
    """
    IcpeOperTopoRemoteSourceEnum

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

    icpe_oper_topo_remote_source_unknown = 0

    icpe_oper_topo_remote_source_remote_icl_id = 1

    icpe_oper_topo_remote_source_remote_satellite_mac = 2

    icpe_oper_topo_remote_source_remote_host_mac = 3

    icpe_oper_topo_remote_source_direct_satellite = 4

    icpe_oper_topo_remote_source_direct_host = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperTopoRemoteSourceEnum']


class IcpeOperVerCheckStateEnum(Enum):
    """
    IcpeOperVerCheckStateEnum

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

    icpe_oper_ver_check_state_unknown = 0

    icpe_oper_ver_check_state_not_compatible = 1

    icpe_oper_ver_check_state_current_version = 2

    icpe_oper_ver_check_state_compatible_older = 3

    icpe_oper_ver_check_state_compatible_newer = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperVerCheckStateEnum']


class IcpeOpmArbitrationFsmStateEnum(Enum):
    """
    IcpeOpmArbitrationFsmStateEnum

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

    icpe_opm_arbitration_fsm_state_unarbitrated = 0

    icpe_opm_arbitration_fsm_state_waiting = 1

    icpe_opm_arbitration_fsm_state_arbitrating = 2

    icpe_opm_arbitration_fsm_state_arbitrated = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmArbitrationFsmStateEnum']


class IcpeOpmAuthFsmStateEnum(Enum):
    """
    IcpeOpmAuthFsmStateEnum

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

    icpe_opm_auth_fsm_state_unauth = 0

    icpe_opm_auth_fsm_state_waiting = 1

    icpe_opm_auth_fsm_state_waiting_for_auth = 2

    icpe_opm_auth_fsm_state_waiting_for_reply = 3

    icpe_opm_auth_fsm_state_authed = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmAuthFsmStateEnum']


class IcpeOpmChanFsmStateEnum(Enum):
    """
    IcpeOpmChanFsmStateEnum

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

    icpe_opm_chan_fsm_state_down = 0

    icpe_opm_chan_fsm_state_closed = 1

    icpe_opm_chan_fsm_state_opening = 2

    icpe_opm_chan_fsm_state_opened = 3

    icpe_opm_chan_fsm_state_open = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmChanFsmStateEnum']


class IcpeOpmControllerEnum(Enum):
    """
    IcpeOpmControllerEnum

    Icpe opm controller

    .. data:: icpe_opm_controller_unknown = 0

    	Unknown

    .. data:: icpe_opm_controller_primary = 1

    	Primary

    .. data:: icpe_opm_controller_secondary = 2

    	Secondary

    """

    icpe_opm_controller_unknown = 0

    icpe_opm_controller_primary = 1

    icpe_opm_controller_secondary = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmControllerEnum']


class IcpeOpmResyncFsmStateEnum(Enum):
    """
    IcpeOpmResyncFsmStateEnum

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

    icpe_opm_resync_fsm_state_not_open = 0

    icpe_opm_resync_fsm_state_stable = 1

    icpe_opm_resync_fsm_state_in_resync = 2

    icpe_opm_resync_fsm_state_queued = 3

    icpe_opm_resync_fsm_state_resync_req = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmResyncFsmStateEnum']


class IcpeOpmSessStateEnum(Enum):
    """
    IcpeOpmSessStateEnum

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

    icpe_opm_sess_state_disconnected = 0

    icpe_opm_sess_state_connecting = 1

    icpe_opm_sess_state_authenticating = 2

    icpe_opm_sess_state_arbitrating = 3

    icpe_opm_sess_state_waiting_for_resyncs = 4

    icpe_opm_sess_state_connected = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmSessStateEnum']


class IcpeOpmSyncFsmStateEnum(Enum):
    """
    IcpeOpmSyncFsmStateEnum

    Icpe opm sync fsm state

    .. data:: icpe_opm_sync_fsm_state_split_brain = 0

    	Split brain

    .. data:: icpe_opm_sync_fsm_state_waiting = 1

    	Waiting

    .. data:: icpe_opm_sync_fsm_state_whole_brain = 2

    	Whole brain

    """

    icpe_opm_sync_fsm_state_split_brain = 0

    icpe_opm_sync_fsm_state_waiting = 1

    icpe_opm_sync_fsm_state_whole_brain = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmSyncFsmStateEnum']


class IcpeOpmTransportStateEnum(Enum):
    """
    IcpeOpmTransportStateEnum

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

    icpe_opm_transport_state_disconnected = 0

    icpe_opm_transport_state_iccp_unavailable = 1

    icpe_opm_transport_state_no_member_present = 2

    icpe_opm_transport_state_member_down = 3

    icpe_opm_transport_state_member_not_reachable = 4

    icpe_opm_transport_state_waiting_for_app_connect = 5

    icpe_opm_transport_state_waiting_for_app_connect_response = 6

    icpe_opm_transport_state_connected = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmTransportStateEnum']


class IcpeOpticalSyncStateEnum(Enum):
    """
    IcpeOpticalSyncStateEnum

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

    icpe_optical_sync_state_unknown = 0

    icpe_optical_sync_state_syncing = 1

    icpe_optical_sync_state_synced = 2

    icpe_optical_sync_state_not_connected = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpticalSyncStateEnum']



class NvSatellite(object):
    """
    Satellite operational information
    
    .. attribute:: install_op_statuses
    
    	Detailed breakdown of install status table
    	**type**\:   :py:class:`InstallOpStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses>`
    
    .. attribute:: install_progresses
    
    	Current percentage of install table
    	**type**\:   :py:class:`InstallProgresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallProgresses>`
    
    .. attribute:: install_statuses
    
    	Detailed breakdown of install status table
    	**type**\:   :py:class:`InstallStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallStatuses>`
    
    .. attribute:: reload_op_statuses
    
    	Detailed breakdown of reload status table
    	**type**\:   :py:class:`ReloadOpStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadOpStatuses>`
    
    .. attribute:: reload_statuses
    
    	Detailed breakdown of reload status table
    	**type**\:   :py:class:`ReloadStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses>`
    
    .. attribute:: satellite_statuses
    
    	Satellite status information table
    	**type**\:   :py:class:`SatelliteStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses>`
    
    .. attribute:: satellite_topologies
    
    	Satellite Topology Information table
    	**type**\:   :py:class:`SatelliteTopologies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies>`
    
    .. attribute:: sdacp_redundancies
    
    	nV Satellite Redundancy Protocol Information table
    	**type**\:   :py:class:`SdacpRedundancies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies>`
    
    

    """

    _prefix = 'icpe-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.install_op_statuses = NvSatellite.InstallOpStatuses()
        self.install_op_statuses.parent = self
        self.install_progresses = NvSatellite.InstallProgresses()
        self.install_progresses.parent = self
        self.install_statuses = NvSatellite.InstallStatuses()
        self.install_statuses.parent = self
        self.reload_op_statuses = NvSatellite.ReloadOpStatuses()
        self.reload_op_statuses.parent = self
        self.reload_statuses = NvSatellite.ReloadStatuses()
        self.reload_statuses.parent = self
        self.satellite_statuses = NvSatellite.SatelliteStatuses()
        self.satellite_statuses.parent = self
        self.satellite_topologies = NvSatellite.SatelliteTopologies()
        self.satellite_topologies.parent = self
        self.sdacp_redundancies = NvSatellite.SdacpRedundancies()
        self.sdacp_redundancies.parent = self


    class ReloadOpStatuses(object):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_op_status
        
        	Detailed breakdown of reload status
        	**type**\: list of    :py:class:`ReloadOpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadOpStatuses.ReloadOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.reload_op_status = YList()
            self.reload_op_status.parent = self
            self.reload_op_status.name = 'reload_op_status'


        class ReloadOpStatus(object):
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
                self.parent = None
                self.operation_id = None
                self.operation_id_xr = None
                self.satellite_range = None
                self.sats_not_initiated = YLeafList()
                self.sats_not_initiated.parent = self
                self.sats_not_initiated.name = 'sats_not_initiated'
                self.sats_reload_failed = YLeafList()
                self.sats_reload_failed.parent = self
                self.sats_reload_failed.name = 'sats_reload_failed'
                self.sats_reloaded = YLeafList()
                self.sats_reloaded.parent = self
                self.sats_reloaded.name = 'sats_reloaded'
                self.sats_reloading = YLeafList()
                self.sats_reloading.parent = self
                self.sats_reloading.name = 'sats_reloading'

            @property
            def _common_path(self):
                if self.operation_id is None:
                    raise YPYModelError('Key property operation_id is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:reload-op-statuses/Cisco-IOS-XR-icpe-infra-oper:reload-op-status[Cisco-IOS-XR-icpe-infra-oper:operation-id = ' + str(self.operation_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.operation_id is not None:
                    return True

                if self.operation_id_xr is not None:
                    return True

                if self.satellite_range is not None:
                    return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_reload_failed is not None:
                    for child in self.sats_reload_failed:
                        if child is not None:
                            return True

                if self.sats_reloaded is not None:
                    for child in self.sats_reloaded:
                        if child is not None:
                            return True

                if self.sats_reloading is not None:
                    for child in self.sats_reloading:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.ReloadOpStatuses.ReloadOpStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:reload-op-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.reload_op_status is not None:
                for child_ref in self.reload_op_status:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.ReloadOpStatuses']['meta_info']


    class InstallStatuses(object):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_status
        
        	Detailed breakdown of install status
        	**type**\: list of    :py:class:`InstallStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallStatuses.InstallStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.install_status = YList()
            self.install_status.parent = self
            self.install_status.name = 'install_status'


        class InstallStatus(object):
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
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.satellite_range = None
                self.operation_id = None
                self.satellite_range_xr = None
                self.sats_activate_aborted = YLeafList()
                self.sats_activate_aborted.parent = self
                self.sats_activate_aborted.name = 'sats_activate_aborted'
                self.sats_activate_failed = YLeafList()
                self.sats_activate_failed.parent = self
                self.sats_activate_failed.name = 'sats_activate_failed'
                self.sats_activating = YLeafList()
                self.sats_activating.parent = self
                self.sats_activating.name = 'sats_activating'
                self.sats_completed = YLeafList()
                self.sats_completed.parent = self
                self.sats_completed.name = 'sats_completed'
                self.sats_deactivate_aborted = YLeafList()
                self.sats_deactivate_aborted.parent = self
                self.sats_deactivate_aborted.name = 'sats_deactivate_aborted'
                self.sats_deactivate_failed = YLeafList()
                self.sats_deactivate_failed.parent = self
                self.sats_deactivate_failed.name = 'sats_deactivate_failed'
                self.sats_deactivating = YLeafList()
                self.sats_deactivating.parent = self
                self.sats_deactivating.name = 'sats_deactivating'
                self.sats_no_operation = YLeafList()
                self.sats_no_operation.parent = self
                self.sats_no_operation.name = 'sats_no_operation'
                self.sats_not_initiated = YLeafList()
                self.sats_not_initiated.parent = self
                self.sats_not_initiated.name = 'sats_not_initiated'
                self.sats_remove_aborted = YLeafList()
                self.sats_remove_aborted.parent = self
                self.sats_remove_aborted.name = 'sats_remove_aborted'
                self.sats_remove_failed = YLeafList()
                self.sats_remove_failed.parent = self
                self.sats_remove_failed.name = 'sats_remove_failed'
                self.sats_removing = YLeafList()
                self.sats_removing.parent = self
                self.sats_removing.name = 'sats_removing'
                self.sats_transfer_aborted = YLeafList()
                self.sats_transfer_aborted.parent = self
                self.sats_transfer_aborted.name = 'sats_transfer_aborted'
                self.sats_transfer_failed = YLeafList()
                self.sats_transfer_failed.parent = self
                self.sats_transfer_failed.name = 'sats_transfer_failed'
                self.sats_transferring = YLeafList()
                self.sats_transferring.parent = self
                self.sats_transferring.name = 'sats_transferring'

            @property
            def _common_path(self):
                if self.satellite_range is None:
                    raise YPYModelError('Key property satellite_range is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-statuses/Cisco-IOS-XR-icpe-infra-oper:install-status[Cisco-IOS-XR-icpe-infra-oper:satellite-range = ' + str(self.satellite_range) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.satellite_range is not None:
                    return True

                if self.operation_id is not None:
                    return True

                if self.satellite_range_xr is not None:
                    return True

                if self.sats_activate_aborted is not None:
                    for child in self.sats_activate_aborted:
                        if child is not None:
                            return True

                if self.sats_activate_failed is not None:
                    for child in self.sats_activate_failed:
                        if child is not None:
                            return True

                if self.sats_activating is not None:
                    for child in self.sats_activating:
                        if child is not None:
                            return True

                if self.sats_completed is not None:
                    for child in self.sats_completed:
                        if child is not None:
                            return True

                if self.sats_deactivate_aborted is not None:
                    for child in self.sats_deactivate_aborted:
                        if child is not None:
                            return True

                if self.sats_deactivate_failed is not None:
                    for child in self.sats_deactivate_failed:
                        if child is not None:
                            return True

                if self.sats_deactivating is not None:
                    for child in self.sats_deactivating:
                        if child is not None:
                            return True

                if self.sats_no_operation is not None:
                    for child in self.sats_no_operation:
                        if child is not None:
                            return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_remove_aborted is not None:
                    for child in self.sats_remove_aborted:
                        if child is not None:
                            return True

                if self.sats_remove_failed is not None:
                    for child in self.sats_remove_failed:
                        if child is not None:
                            return True

                if self.sats_removing is not None:
                    for child in self.sats_removing:
                        if child is not None:
                            return True

                if self.sats_transfer_aborted is not None:
                    for child in self.sats_transfer_aborted:
                        if child is not None:
                            return True

                if self.sats_transfer_failed is not None:
                    for child in self.sats_transfer_failed:
                        if child is not None:
                            return True

                if self.sats_transferring is not None:
                    for child in self.sats_transferring:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.InstallStatuses.InstallStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.install_status is not None:
                for child_ref in self.install_status:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.InstallStatuses']['meta_info']


    class SdacpRedundancies(object):
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
            self.parent = None
            self.sdacp_redundancy = YList()
            self.sdacp_redundancy.parent = self
            self.sdacp_redundancy.name = 'sdacp_redundancy'


        class SdacpRedundancy(object):
            """
            nV Satellite Redundancy Protocol Information
            
            .. attribute:: iccp_group  <key>
            
            	ICCP group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: arbitration_state
            
            	Arbitration state
            	**type**\:   :py:class:`IcpeOpmArbitrationFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmArbitrationFsmStateEnum>`
            
            .. attribute:: authentication_state
            
            	Authentication state
            	**type**\:   :py:class:`IcpeOpmAuthFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmAuthFsmStateEnum>`
            
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
            	**type**\:   :py:class:`IcpeOpmControllerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmControllerEnum>`
            
            .. attribute:: protocol_state
            
            	Protocol state
            	**type**\:   :py:class:`IcpeOpmSessStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSessStateEnum>`
            
            .. attribute:: protocol_state_timestamp
            
            	Timestamp
            	**type**\:   :py:class:`ProtocolStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp>`
            
            .. attribute:: synchronization_state
            
            	Synchronization state
            	**type**\:   :py:class:`IcpeOpmSyncFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSyncFsmStateEnum>`
            
            .. attribute:: system_mac
            
            	System MAC
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: transport_state
            
            	Transport state
            	**type**\:   :py:class:`IcpeOpmTransportStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmTransportStateEnum>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.iccp_group = None
                self.arbitration_state = None
                self.authentication_state = None
                self.channel = YList()
                self.channel.parent = self
                self.channel.name = 'channel'
                self.iccp_group_xr = None
                self.isolated = None
                self.primacy = None
                self.protocol_state = None
                self.protocol_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp()
                self.protocol_state_timestamp.parent = self
                self.synchronization_state = None
                self.system_mac = None
                self.transport_state = None


            class ProtocolStateTimestamp(object):
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
                    self.parent = None
                    self.nanoseconds = None
                    self.seconds = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:protocol-state-timestamp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.nanoseconds is not None:
                        return True

                    if self.seconds is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp']['meta_info']


            class Channel(object):
                """
                Channels on this session table
                
                .. attribute:: chan_state
                
                	Chan state
                	**type**\:   :py:class:`IcpeOpmChanFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmChanFsmStateEnum>`
                
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
                	**type**\:   :py:class:`IcpeOpmResyncFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmResyncFsmStateEnum>`
                
                .. attribute:: resync_state_timestamp
                
                	Timestamp
                	**type**\:   :py:class:`ResyncStateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.chan_state = None
                    self.channel_id = None
                    self.channel_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp()
                    self.channel_state_timestamp.parent = self
                    self.control_messages_received = None
                    self.control_messages_sent = None
                    self.normal_messages_received = None
                    self.normal_messages_sent = None
                    self.resync_state = None
                    self.resync_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp()
                    self.resync_state_timestamp.parent = self


                class ChannelStateTimestamp(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:channel-state-timestamp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp']['meta_info']


                class ResyncStateTimestamp(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:resync-state-timestamp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:channel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.chan_state is not None:
                        return True

                    if self.channel_id is not None:
                        return True

                    if self.channel_state_timestamp is not None and self.channel_state_timestamp._has_data():
                        return True

                    if self.control_messages_received is not None:
                        return True

                    if self.control_messages_sent is not None:
                        return True

                    if self.normal_messages_received is not None:
                        return True

                    if self.normal_messages_sent is not None:
                        return True

                    if self.resync_state is not None:
                        return True

                    if self.resync_state_timestamp is not None and self.resync_state_timestamp._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info']

            @property
            def _common_path(self):
                if self.iccp_group is None:
                    raise YPYModelError('Key property iccp_group is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:sdacp-redundancies/Cisco-IOS-XR-icpe-infra-oper:sdacp-redundancy[Cisco-IOS-XR-icpe-infra-oper:iccp-group = ' + str(self.iccp_group) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.iccp_group is not None:
                    return True

                if self.arbitration_state is not None:
                    return True

                if self.authentication_state is not None:
                    return True

                if self.channel is not None:
                    for child_ref in self.channel:
                        if child_ref._has_data():
                            return True

                if self.iccp_group_xr is not None:
                    return True

                if self.isolated is not None:
                    return True

                if self.primacy is not None:
                    return True

                if self.protocol_state is not None:
                    return True

                if self.protocol_state_timestamp is not None and self.protocol_state_timestamp._has_data():
                    return True

                if self.synchronization_state is not None:
                    return True

                if self.system_mac is not None:
                    return True

                if self.transport_state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:sdacp-redundancies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.sdacp_redundancy is not None:
                for child_ref in self.sdacp_redundancy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.SdacpRedundancies']['meta_info']


    class SatelliteStatuses(object):
        """
        Satellite status information table
        
        .. attribute:: satellite_status
        
        	Satellite status information
        	**type**\: list of    :py:class:`SatelliteStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.satellite_status = YList()
            self.satellite_status.parent = self
            self.satellite_status.name = 'satellite_status'


        class SatelliteStatus(object):
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
            	**type**\:   :py:class:`IcpeOperConflictEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflictEnum>`
            
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
            	**type**\:   :py:class:`IcpeOperInstallStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperInstallStateEnum>`
            
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
            	**type**\:   :py:class:`IcpeGcoOperControlReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeGcoOperControlReasonEnum>`
            
            .. attribute:: sdacp_session_state
            
            	SDACP session state
            	**type**\:   :py:class:`IcpeOperSdacpSessStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperSdacpSessStateEnum>`
            
            .. attribute:: timeout_warning
            
            	Timeout warning
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: type
            
            	Type
            	**type**\:  str
            
            .. attribute:: version_check_state
            
            	Version check state
            	**type**\:   :py:class:`IcpeOperVerCheckStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckStateEnum>`
            
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
                self.parent = None
                self.satellite_id = None
                self.candidate_fabric_ports = NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts()
                self.candidate_fabric_ports.parent = self
                self.cfgd_timeout = None
                self.configured_link = YList()
                self.configured_link.parent = self
                self.configured_link.name = 'configured_link'
                self.configured_serial_number = None
                self.configured_serial_number_present = None
                self.conflict_context = None
                self.conflict_reason = None
                self.description = None
                self.description_present = None
                self.ethernet_fabric_supported = None
                self.host_treating_as_active = None
                self.install_state = None
                self.ip_address = None
                self.ip_address_auto = None
                self.ip_address_present = None
                self.ipv6_address = None
                self.ipv6_address_present = None
                self.mac_address = None
                self.mac_address_present = None
                self.optical_status = NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus()
                self.optical_status.parent = self
                self.optical_supported = None
                self.password = None
                self.password_error = None
                self.received_host_name = None
                self.received_serial_number = None
                self.received_serial_number_present = None
                self.recovery_delay_time_left = None
                self.redundancy_iccp_group = None
                self.redundancy_out_of_sync_timestamp = NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp()
                self.redundancy_out_of_sync_timestamp.parent = self
                self.remote_version = YLeafList()
                self.remote_version.parent = self
                self.remote_version.name = 'remote_version'
                self.remote_version_present = None
                self.satellite_id_xr = None
                self.satellite_treating_as_active = None
                self.sdacp_session_failure_reason = None
                self.sdacp_session_state = None
                self.timeout_warning = None
                self.type = None
                self.version_check_state = None
                self.vrf_name = None
                self.vrfid = None


            class CandidateFabricPorts(object):
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
                    self.parent = None
                    self.channel_up = None
                    self.configured_port = YList()
                    self.configured_port.parent = self
                    self.configured_port.name = 'configured_port'
                    self.current_port = YList()
                    self.current_port.parent = self
                    self.current_port.name = 'current_port'
                    self.error_string = None
                    self.out_of_sync = None


                class ConfiguredPort(object):
                    """
                    Configured Candidate Fabric Ports table
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\:   :py:class:`IcpeOperFabricPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPortEnum>`
                    
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
                        self.parent = None
                        self.port = None
                        self.port_type = None
                        self.slot = None
                        self.subslot = None
                        self.valid = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:configured-port'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.port is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.slot is not None:
                            return True

                        if self.subslot is not None:
                            return True

                        if self.valid is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort']['meta_info']


                class CurrentPort(object):
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
                    	**type**\:   :py:class:`IcpeOperFabricPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPortEnum>`
                    
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
                        self.parent = None
                        self.permanent = None
                        self.port = None
                        self.port_type = None
                        self.requested = None
                        self.slot = None
                        self.subslot = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:current-port'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.permanent is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.requested is not None:
                            return True

                        if self.slot is not None:
                            return True

                        if self.subslot is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:candidate-fabric-ports'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.channel_up is not None:
                        return True

                    if self.configured_port is not None:
                        for child_ref in self.configured_port:
                            if child_ref._has_data():
                                return True

                    if self.current_port is not None:
                        for child_ref in self.current_port:
                            if child_ref._has_data():
                                return True

                    if self.error_string is not None:
                        return True

                    if self.out_of_sync is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts']['meta_info']


            class OpticalStatus(object):
                """
                Optical Satellite Status
                
                .. attribute:: application
                
                	Application State table
                	**type**\: list of    :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application>`
                
                .. attribute:: chassis_sync_state
                
                	Chassis sync state
                	**type**\:   :py:class:`IcpeOpticalSyncStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncStateEnum>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.application = YList()
                    self.application.parent = self
                    self.application.name = 'application'
                    self.chassis_sync_state = None


                class Application(object):
                    """
                    Application State table
                    
                    .. attribute:: name
                    
                    	Name
                    	**type**\:  str
                    
                    .. attribute:: sync_state
                    
                    	Sync state
                    	**type**\:   :py:class:`IcpeOpticalSyncStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncStateEnum>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.sync_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:application'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.sync_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:optical-status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.application is not None:
                        for child_ref in self.application:
                            if child_ref._has_data():
                                return True

                    if self.chassis_sync_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus']['meta_info']


            class RedundancyOutOfSyncTimestamp(object):
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
                    self.parent = None
                    self.nanoseconds = None
                    self.seconds = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:redundancy-out-of-sync-timestamp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.nanoseconds is not None:
                        return True

                    if self.seconds is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp']['meta_info']


            class ConfiguredLink(object):
                """
                Configured Links on this Satellite table
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\:  str
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\:   :py:class:`IcpeOperConflictEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflictEnum>`
                
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
                
                .. attribute:: number_active_links
                
                	Number active links
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_range
                
                	Port ranges table
                	**type**\: list of    :py:class:`PortRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange>`
                
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
                    self.parent = None
                    self.conflict_context = None
                    self.conflict_reason = None
                    self.discovered_link = YList()
                    self.discovered_link.parent = self
                    self.discovered_link.name = 'discovered_link'
                    self.interface_handle = None
                    self.ip_address = None
                    self.ip_address_auto = None
                    self.min_links_satisfied = None
                    self.minimum_preferred_links = None
                    self.number_active_links = None
                    self.port_range = YList()
                    self.port_range.parent = self
                    self.port_range.name = 'port_range'
                    self.vrf_id = None
                    self.vrf_id_present = None


                class PortRange(object):
                    """
                    Port ranges table
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\:  str
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:   :py:class:`IcpeOperConflictEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflictEnum>`
                    
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
                    	**type**\:   :py:class:`IcpeOperPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperPortEnum>`
                    
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
                        self.parent = None
                        self.conflict_context = None
                        self.conflict_reason = None
                        self.high_port = None
                        self.low_port = None
                        self.port_type = None
                        self.slot = None
                        self.subslot = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:port-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.conflict_context is not None:
                            return True

                        if self.conflict_reason is not None:
                            return True

                        if self.high_port is not None:
                            return True

                        if self.low_port is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.slot is not None:
                            return True

                        if self.subslot is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange']['meta_info']


                class DiscoveredLink(object):
                    """
                    Discovered Links table
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\:  str
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\:   :py:class:`IcpeOperConflictEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflictEnum>`
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:   :py:class:`IcpeOperDiscdLinkStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperDiscdLinkStateEnum>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.conflict_context = None
                        self.conflict_reason = None
                        self.interface_handle = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:discovered-link'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.conflict_context is not None:
                            return True

                        if self.conflict_reason is not None:
                            return True

                        if self.interface_handle is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:configured-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.conflict_context is not None:
                        return True

                    if self.conflict_reason is not None:
                        return True

                    if self.discovered_link is not None:
                        for child_ref in self.discovered_link:
                            if child_ref._has_data():
                                return True

                    if self.interface_handle is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    if self.ip_address_auto is not None:
                        return True

                    if self.min_links_satisfied is not None:
                        return True

                    if self.minimum_preferred_links is not None:
                        return True

                    if self.number_active_links is not None:
                        return True

                    if self.port_range is not None:
                        for child_ref in self.port_range:
                            if child_ref._has_data():
                                return True

                    if self.vrf_id is not None:
                        return True

                    if self.vrf_id_present is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink']['meta_info']

            @property
            def _common_path(self):
                if self.satellite_id is None:
                    raise YPYModelError('Key property satellite_id is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-statuses/Cisco-IOS-XR-icpe-infra-oper:satellite-status[Cisco-IOS-XR-icpe-infra-oper:satellite-id = ' + str(self.satellite_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.satellite_id is not None:
                    return True

                if self.candidate_fabric_ports is not None and self.candidate_fabric_ports._has_data():
                    return True

                if self.cfgd_timeout is not None:
                    return True

                if self.configured_link is not None:
                    for child_ref in self.configured_link:
                        if child_ref._has_data():
                            return True

                if self.configured_serial_number is not None:
                    return True

                if self.configured_serial_number_present is not None:
                    return True

                if self.conflict_context is not None:
                    return True

                if self.conflict_reason is not None:
                    return True

                if self.description is not None:
                    return True

                if self.description_present is not None:
                    return True

                if self.ethernet_fabric_supported is not None:
                    return True

                if self.host_treating_as_active is not None:
                    return True

                if self.install_state is not None:
                    return True

                if self.ip_address is not None:
                    return True

                if self.ip_address_auto is not None:
                    return True

                if self.ip_address_present is not None:
                    return True

                if self.ipv6_address is not None:
                    return True

                if self.ipv6_address_present is not None:
                    return True

                if self.mac_address is not None:
                    return True

                if self.mac_address_present is not None:
                    return True

                if self.optical_status is not None and self.optical_status._has_data():
                    return True

                if self.optical_supported is not None:
                    return True

                if self.password is not None:
                    return True

                if self.password_error is not None:
                    return True

                if self.received_host_name is not None:
                    return True

                if self.received_serial_number is not None:
                    return True

                if self.received_serial_number_present is not None:
                    return True

                if self.recovery_delay_time_left is not None:
                    return True

                if self.redundancy_iccp_group is not None:
                    return True

                if self.redundancy_out_of_sync_timestamp is not None and self.redundancy_out_of_sync_timestamp._has_data():
                    return True

                if self.remote_version is not None:
                    for child in self.remote_version:
                        if child is not None:
                            return True

                if self.remote_version_present is not None:
                    return True

                if self.satellite_id_xr is not None:
                    return True

                if self.satellite_treating_as_active is not None:
                    return True

                if self.sdacp_session_failure_reason is not None:
                    return True

                if self.sdacp_session_state is not None:
                    return True

                if self.timeout_warning is not None:
                    return True

                if self.type is not None:
                    return True

                if self.version_check_state is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vrfid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.satellite_status is not None:
                for child_ref in self.satellite_status:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.SatelliteStatuses']['meta_info']


    class SatelliteTopologies(object):
        """
        Satellite Topology Information table
        
        .. attribute:: satellite_topology
        
        	Satellite Topology Information
        	**type**\: list of    :py:class:`SatelliteTopology <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.satellite_topology = YList()
            self.satellite_topology.parent = self
            self.satellite_topology.name = 'satellite_topology'


        class SatelliteTopology(object):
            """
            Satellite Topology Information
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
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
                self.parent = None
                self.interface_name = None
                self.discovered_link = YList()
                self.discovered_link.parent = self
                self.discovered_link.name = 'discovered_link'
                self.interface_handle = None
                self.interface_name_xr = None
                self.is_physical = None
                self.redundancy_iccp_group = None
                self.ring_whole = None
                self.satellite = YList()
                self.satellite.parent = self
                self.satellite.name = 'satellite'


            class DiscoveredLink(object):
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
                    self.parent = None
                    self.discovery_running = None
                    self.interface_handle = None
                    self.interface_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:discovered-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.discovery_running is not None:
                        return True

                    if self.interface_handle is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink']['meta_info']


            class Satellite(object):
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
                	**type**\:   :py:class:`IcpeOperConflictEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflictEnum>`
                
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
                    self.parent = None
                    self.configured = None
                    self.conflict_context = None
                    self.conflict_reason = None
                    self.display_name = None
                    self.fabric_link = YList()
                    self.fabric_link.parent = self
                    self.fabric_link.name = 'fabric_link'
                    self.mac_address = None
                    self.num_hops = None
                    self.received_serial_number = None
                    self.received_serial_number_present = None
                    self.satellite_id = None
                    self.type = None
                    self.vlan_id = None


                class FabricLink(object):
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
                        self.parent = None
                        self.active = None
                        self.display_name = None
                        self.icl_id = None
                        self.interface_name = None
                        self.obsolete = None
                        self.redundant = None
                        self.remote_device = YList()
                        self.remote_device.parent = self
                        self.remote_device.name = 'remote_device'


                    class RemoteDevice(object):
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
                        	**type**\:   :py:class:`IcpeOperTopoRemoteSourceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.IcpeOperTopoRemoteSourceEnum>`
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.icl_id = None
                            self.interface_handle = None
                            self.interface_name = None
                            self.mac_address = None
                            self.remote_is_local_host = None
                            self.remote_is_satellite = None
                            self.source = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:remote-device'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.icl_id is not None:
                                return True

                            if self.interface_handle is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.remote_is_local_host is not None:
                                return True

                            if self.remote_is_satellite is not None:
                                return True

                            if self.source is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                            return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:fabric-link'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.active is not None:
                            return True

                        if self.display_name is not None:
                            return True

                        if self.icl_id is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.obsolete is not None:
                            return True

                        if self.redundant is not None:
                            return True

                        if self.remote_device is not None:
                            for child_ref in self.remote_device:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:satellite'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.configured is not None:
                        return True

                    if self.conflict_context is not None:
                        return True

                    if self.conflict_reason is not None:
                        return True

                    if self.display_name is not None:
                        return True

                    if self.fabric_link is not None:
                        for child_ref in self.fabric_link:
                            if child_ref._has_data():
                                return True

                    if self.mac_address is not None:
                        return True

                    if self.num_hops is not None:
                        return True

                    if self.received_serial_number is not None:
                        return True

                    if self.received_serial_number_present is not None:
                        return True

                    if self.satellite_id is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.vlan_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-topologies/Cisco-IOS-XR-icpe-infra-oper:satellite-topology[Cisco-IOS-XR-icpe-infra-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                if self.discovered_link is not None:
                    for child_ref in self.discovered_link:
                        if child_ref._has_data():
                            return True

                if self.interface_handle is not None:
                    return True

                if self.interface_name_xr is not None:
                    return True

                if self.is_physical is not None:
                    return True

                if self.redundancy_iccp_group is not None:
                    return True

                if self.ring_whole is not None:
                    return True

                if self.satellite is not None:
                    for child_ref in self.satellite:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-topologies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.satellite_topology is not None:
                for child_ref in self.satellite_topology:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.SatelliteTopologies']['meta_info']


    class InstallProgresses(object):
        """
        Current percentage of install table
        
        .. attribute:: install_progress
        
        	Current percentage of install
        	**type**\: list of    :py:class:`InstallProgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallProgresses.InstallProgress>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.install_progress = YList()
            self.install_progress.parent = self
            self.install_progress.name = 'install_progress'


        class InstallProgress(object):
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
                self.parent = None
                self.progress_percentage = None
                self.progress_percentage_xr = None
                self.satellite_count = None

            @property
            def _common_path(self):
                if self.progress_percentage is None:
                    raise YPYModelError('Key property progress_percentage is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-progresses/Cisco-IOS-XR-icpe-infra-oper:install-progress[Cisco-IOS-XR-icpe-infra-oper:progress-percentage = ' + str(self.progress_percentage) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.progress_percentage is not None:
                    return True

                if self.progress_percentage_xr is not None:
                    return True

                if self.satellite_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.InstallProgresses.InstallProgress']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-progresses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.install_progress is not None:
                for child_ref in self.install_progress:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.InstallProgresses']['meta_info']


    class ReloadStatuses(object):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_status
        
        	Detailed breakdown of reload status
        	**type**\: list of    :py:class:`ReloadStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses.ReloadStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.reload_status = YList()
            self.reload_status.parent = self
            self.reload_status.name = 'reload_status'


        class ReloadStatus(object):
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
                self.parent = None
                self.satellite_range = None
                self.satellite_range_xr = None
                self.sats_not_initiated = YLeafList()
                self.sats_not_initiated.parent = self
                self.sats_not_initiated.name = 'sats_not_initiated'
                self.sats_reload_failed = YLeafList()
                self.sats_reload_failed.parent = self
                self.sats_reload_failed.name = 'sats_reload_failed'
                self.sats_reloaded = YLeafList()
                self.sats_reloaded.parent = self
                self.sats_reloaded.name = 'sats_reloaded'
                self.sats_reloading = YLeafList()
                self.sats_reloading.parent = self
                self.sats_reloading.name = 'sats_reloading'

            @property
            def _common_path(self):
                if self.satellite_range is None:
                    raise YPYModelError('Key property satellite_range is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:reload-statuses/Cisco-IOS-XR-icpe-infra-oper:reload-status[Cisco-IOS-XR-icpe-infra-oper:satellite-range = ' + str(self.satellite_range) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.satellite_range is not None:
                    return True

                if self.satellite_range_xr is not None:
                    return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_reload_failed is not None:
                    for child in self.sats_reload_failed:
                        if child is not None:
                            return True

                if self.sats_reloaded is not None:
                    for child in self.sats_reloaded:
                        if child is not None:
                            return True

                if self.sats_reloading is not None:
                    for child in self.sats_reloading:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.ReloadStatuses.ReloadStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:reload-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.reload_status is not None:
                for child_ref in self.reload_status:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.ReloadStatuses']['meta_info']


    class InstallOpStatuses(object):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_op_status
        
        	Detailed breakdown of install status
        	**type**\: list of    :py:class:`InstallOpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses.InstallOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.install_op_status = YList()
            self.install_op_status.parent = self
            self.install_op_status.name = 'install_op_status'


        class InstallOpStatus(object):
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
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.operation_id = None
                self.operation_id_xr = None
                self.satellite_range = None
                self.sats_activate_aborted = YLeafList()
                self.sats_activate_aborted.parent = self
                self.sats_activate_aborted.name = 'sats_activate_aborted'
                self.sats_activate_failed = YLeafList()
                self.sats_activate_failed.parent = self
                self.sats_activate_failed.name = 'sats_activate_failed'
                self.sats_activating = YLeafList()
                self.sats_activating.parent = self
                self.sats_activating.name = 'sats_activating'
                self.sats_completed = YLeafList()
                self.sats_completed.parent = self
                self.sats_completed.name = 'sats_completed'
                self.sats_deactivate_aborted = YLeafList()
                self.sats_deactivate_aborted.parent = self
                self.sats_deactivate_aborted.name = 'sats_deactivate_aborted'
                self.sats_deactivate_failed = YLeafList()
                self.sats_deactivate_failed.parent = self
                self.sats_deactivate_failed.name = 'sats_deactivate_failed'
                self.sats_deactivating = YLeafList()
                self.sats_deactivating.parent = self
                self.sats_deactivating.name = 'sats_deactivating'
                self.sats_no_operation = YLeafList()
                self.sats_no_operation.parent = self
                self.sats_no_operation.name = 'sats_no_operation'
                self.sats_not_initiated = YLeafList()
                self.sats_not_initiated.parent = self
                self.sats_not_initiated.name = 'sats_not_initiated'
                self.sats_remove_aborted = YLeafList()
                self.sats_remove_aborted.parent = self
                self.sats_remove_aborted.name = 'sats_remove_aborted'
                self.sats_remove_failed = YLeafList()
                self.sats_remove_failed.parent = self
                self.sats_remove_failed.name = 'sats_remove_failed'
                self.sats_removing = YLeafList()
                self.sats_removing.parent = self
                self.sats_removing.name = 'sats_removing'
                self.sats_transfer_aborted = YLeafList()
                self.sats_transfer_aborted.parent = self
                self.sats_transfer_aborted.name = 'sats_transfer_aborted'
                self.sats_transfer_failed = YLeafList()
                self.sats_transfer_failed.parent = self
                self.sats_transfer_failed.name = 'sats_transfer_failed'
                self.sats_transferring = YLeafList()
                self.sats_transferring.parent = self
                self.sats_transferring.name = 'sats_transferring'

            @property
            def _common_path(self):
                if self.operation_id is None:
                    raise YPYModelError('Key property operation_id is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-op-statuses/Cisco-IOS-XR-icpe-infra-oper:install-op-status[Cisco-IOS-XR-icpe-infra-oper:operation-id = ' + str(self.operation_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.operation_id is not None:
                    return True

                if self.operation_id_xr is not None:
                    return True

                if self.satellite_range is not None:
                    return True

                if self.sats_activate_aborted is not None:
                    for child in self.sats_activate_aborted:
                        if child is not None:
                            return True

                if self.sats_activate_failed is not None:
                    for child in self.sats_activate_failed:
                        if child is not None:
                            return True

                if self.sats_activating is not None:
                    for child in self.sats_activating:
                        if child is not None:
                            return True

                if self.sats_completed is not None:
                    for child in self.sats_completed:
                        if child is not None:
                            return True

                if self.sats_deactivate_aborted is not None:
                    for child in self.sats_deactivate_aborted:
                        if child is not None:
                            return True

                if self.sats_deactivate_failed is not None:
                    for child in self.sats_deactivate_failed:
                        if child is not None:
                            return True

                if self.sats_deactivating is not None:
                    for child in self.sats_deactivating:
                        if child is not None:
                            return True

                if self.sats_no_operation is not None:
                    for child in self.sats_no_operation:
                        if child is not None:
                            return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_remove_aborted is not None:
                    for child in self.sats_remove_aborted:
                        if child is not None:
                            return True

                if self.sats_remove_failed is not None:
                    for child in self.sats_remove_failed:
                        if child is not None:
                            return True

                if self.sats_removing is not None:
                    for child in self.sats_removing:
                        if child is not None:
                            return True

                if self.sats_transfer_aborted is not None:
                    for child in self.sats_transfer_aborted:
                        if child is not None:
                            return True

                if self.sats_transfer_failed is not None:
                    for child in self.sats_transfer_failed:
                        if child is not None:
                            return True

                if self.sats_transferring is not None:
                    for child in self.sats_transferring:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.InstallOpStatuses.InstallOpStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-op-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.install_op_status is not None:
                for child_ref in self.install_op_status:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.InstallOpStatuses']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.install_op_statuses is not None and self.install_op_statuses._has_data():
            return True

        if self.install_progresses is not None and self.install_progresses._has_data():
            return True

        if self.install_statuses is not None and self.install_statuses._has_data():
            return True

        if self.reload_op_statuses is not None and self.reload_op_statuses._has_data():
            return True

        if self.reload_statuses is not None and self.reload_statuses._has_data():
            return True

        if self.satellite_statuses is not None and self.satellite_statuses._has_data():
            return True

        if self.satellite_topologies is not None and self.satellite_topologies._has_data():
            return True

        if self.sdacp_redundancies is not None and self.sdacp_redundancies._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['NvSatellite']['meta_info']


