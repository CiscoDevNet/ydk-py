


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IcpeOperVerCheckStateEnum' : _MetaInfoEnum('IcpeOperVerCheckStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-ver-check-state-unknown':'icpe_oper_ver_check_state_unknown',
            'icpe-oper-ver-check-state-not-compatible':'icpe_oper_ver_check_state_not_compatible',
            'icpe-oper-ver-check-state-current-version':'icpe_oper_ver_check_state_current_version',
            'icpe-oper-ver-check-state-compatible-older':'icpe_oper_ver_check_state_compatible_older',
            'icpe-oper-ver-check-state-compatible-newer':'icpe_oper_ver_check_state_compatible_newer',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmAuthFsmStateEnum' : _MetaInfoEnum('IcpeOpmAuthFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-auth-fsm-state-unauth':'icpe_opm_auth_fsm_state_unauth',
            'icpe-opm-auth-fsm-state-waiting':'icpe_opm_auth_fsm_state_waiting',
            'icpe-opm-auth-fsm-state-waiting-for-auth':'icpe_opm_auth_fsm_state_waiting_for_auth',
            'icpe-opm-auth-fsm-state-waiting-for-reply':'icpe_opm_auth_fsm_state_waiting_for_reply',
            'icpe-opm-auth-fsm-state-authed':'icpe_opm_auth_fsm_state_authed',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperInstallStateEnum' : _MetaInfoEnum('IcpeOperInstallStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-install-state-stable':'icpe_oper_install_state_stable',
            'icpe-oper-install-state-transferring':'icpe_oper_install_state_transferring',
            'icpe-oper-install-state-transferred':'icpe_oper_install_state_transferred',
            'icpe-oper-install-state-installing':'icpe_oper_install_state_installing',
            'icpe-oper-install-state-in-progress':'icpe_oper_install_state_in_progress',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperFabricPortEnum' : _MetaInfoEnum('IcpeOperFabricPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-fabric-port-unknown':'icpe_oper_fabric_port_unknown',
            'icpe-oper-fabric-port-n-v-fabric-gig-e':'icpe_oper_fabric_port_n_v_fabric_gig_e',
            'icpe-oper-fabric-port-n-v-fabric-ten-gig-e':'icpe_oper_fabric_port_n_v_fabric_ten_gig_e',
            'icpe-oper-fabric-port-n-v-fabric-hundred-gig-e':'icpe_oper_fabric_port_n_v_fabric_hundred_gig_e',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmArbitrationFsmStateEnum' : _MetaInfoEnum('IcpeOpmArbitrationFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-arbitration-fsm-state-unarbitrated':'icpe_opm_arbitration_fsm_state_unarbitrated',
            'icpe-opm-arbitration-fsm-state-waiting':'icpe_opm_arbitration_fsm_state_waiting',
            'icpe-opm-arbitration-fsm-state-arbitrating':'icpe_opm_arbitration_fsm_state_arbitrating',
            'icpe-opm-arbitration-fsm-state-arbitrated':'icpe_opm_arbitration_fsm_state_arbitrated',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeInstallPkgSuppEnum' : _MetaInfoEnum('IcpeInstallPkgSuppEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-install-pkg-supp-unknown':'icpe_install_pkg_supp_unknown',
            'icpe-install-pkg-supp-not-supported':'icpe_install_pkg_supp_not_supported',
            'icpe-install-pkg-supp-supported':'icpe_install_pkg_supp_supported',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperDiscdLinkStateEnum' : _MetaInfoEnum('IcpeOperDiscdLinkStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-discd-link-state-stopped':'icpe_oper_discd_link_state_stopped',
            'icpe-oper-discd-link-state-probing':'icpe_oper_discd_link_state_probing',
            'icpe-oper-discd-link-state-configuring':'icpe_oper_discd_link_state_configuring',
            'icpe-oper-discd-link-state-ready':'icpe_oper_discd_link_state_ready',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmControllerEnum' : _MetaInfoEnum('IcpeOpmControllerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-controller-unknown':'icpe_opm_controller_unknown',
            'icpe-opm-controller-primary':'icpe_opm_controller_primary',
            'icpe-opm-controller-secondary':'icpe_opm_controller_secondary',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperConflictEnum' : _MetaInfoEnum('IcpeOperConflictEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-conflict-not-calculated':'icpe_oper_conflict_not_calculated',
            'icpe-oper-conflict-no-conflict':'icpe_oper_conflict_no_conflict',
            'icpe-oper-conflict-satellite-not-configured':'icpe_oper_conflict_satellite_not_configured',
            'icpe-oper-conflict-satellite-no-type':'icpe_oper_conflict_satellite_no_type',
            'icpe-oper-conflict-satellite-id-invalid':'icpe_oper_conflict_satellite_id_invalid',
            'icpe-oper-conflict-satellite-no-ipv4-addr':'icpe_oper_conflict_satellite_no_ipv4_addr',
            'icpe-oper-conflict-satellite-conflicting-ipv4-addr':'icpe_oper_conflict_satellite_conflicting_ipv4_addr',
            'icpe-oper-conflict-no-configured-links':'icpe_oper_conflict_no_configured_links',
            'icpe-oper-conflict-no-discovered-links':'icpe_oper_conflict_no_discovered_links',
            'icpe-oper-conflict-invalid-ports':'icpe_oper_conflict_invalid_ports',
            'icpe-oper-conflict-ports-overlap':'icpe_oper_conflict_ports_overlap',
            'icpe-oper-conflict-waiting-for-ipv4-addr':'icpe_oper_conflict_waiting_for_ipv4_addr',
            'icpe-oper-conflict-waiting-for-vrf':'icpe_oper_conflict_waiting_for_vrf',
            'icpe-oper-conflict-different-ipv4-addr':'icpe_oper_conflict_different_ipv4_addr',
            'icpe-oper-conflict-different-vrf':'icpe_oper_conflict_different_vrf',
            'icpe-oper-conflict-satellite-link-ipv4-overlap':'icpe_oper_conflict_satellite_link_ipv4_overlap',
            'icpe-oper-conflict-waiting-for-ident':'icpe_oper_conflict_waiting_for_ident',
            'icpe-oper-conflict-multiple-ids':'icpe_oper_conflict_multiple_ids',
            'icpe-oper-conflict-multiple-satellites':'icpe_oper_conflict_multiple_satellites',
            'icpe-oper-conflict-ident-rejected':'icpe_oper_conflict_ident_rejected',
            'icpe-oper-conflict-interface-down':'icpe_oper_conflict_interface_down',
            'icpe-oper-conflict-auto-ip-unavailable':'icpe_oper_conflict_auto_ip_unavailable',
            'icpe-oper-conflict-satellite-auto-ip-link-manual-ip':'icpe_oper_conflict_satellite_auto_ip_link_manual_ip',
            'icpe-oper-conflict-link-auto-ip-satellite-manual-ip':'icpe_oper_conflict_link_auto_ip_satellite_manual_ip',
            'icpe-oper-conflict-serial-num-mismatch':'icpe_oper_conflict_serial_num_mismatch',
            'icpe-oper-conflict-satellite-not-identified':'icpe_oper_conflict_satellite_not_identified',
            'icpe-oper-conflict-satellite-unsupported-type':'icpe_oper_conflict_satellite_unsupported_type',
            'icpe-oper-conflict-satellite-partition-unsupported':'icpe_oper_conflict_satellite_partition_unsupported',
            'icpe-oper-conflict-satellite-no-serial-number':'icpe_oper_conflict_satellite_no_serial_number',
            'icpe-oper-conflict-satellite-conflicting-serial-number':'icpe_oper_conflict_satellite_conflicting_serial_number',
            'icpe-oper-conflict-satellite-link-waiting-for-arp':'icpe_oper_conflict_satellite_link_waiting_for_arp',
            'icpe-oper-conflict-host-pe-isolated-split-brain':'icpe_oper_conflict_host_pe_isolated_split_brain',
            'icpe-oper-conflict-fabric-iccp-group-inconsistent':'icpe_oper_conflict_fabric_iccp_group_inconsistent',
            'icpe-oper-conflict-invalid-iccp-group':'icpe_oper_conflict_invalid_iccp_group',
            'icpe-oper-conflict-port-rejected':'icpe_oper_conflict_port_rejected',
            'icpe-oper-conflict-satellite-icl-not-supported':'icpe_oper_conflict_satellite_icl_not_supported',
            'icpe-oper-conflict-multiple-serial-number':'icpe_oper_conflict_multiple_serial_number',
            'icpe-oper-conflict-multiple-mac-address':'icpe_oper_conflict_multiple_mac_address',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeGcoOperControlReasonEnum' : _MetaInfoEnum('IcpeGcoOperControlReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-gco-oper-control-reason-unknown-error':'icpe_gco_oper_control_reason_unknown_error',
            'icpe-gco-oper-control-reason-wrong-chassis-type':'icpe_gco_oper_control_reason_wrong_chassis_type',
            'icpe-gco-oper-control-reason-wrong-chassis-serial':'icpe_gco_oper_control_reason_wrong_chassis_serial',
            'icpe-gco-oper-control-reason-needs-to-upgrade':'icpe_gco_oper_control_reason_needs_to_upgrade',
            'icpe-gco-oper-control-reason-none':'icpe_gco_oper_control_reason_none',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmSessStateEnum' : _MetaInfoEnum('IcpeOpmSessStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-sess-state-disconnected':'icpe_opm_sess_state_disconnected',
            'icpe-opm-sess-state-connecting':'icpe_opm_sess_state_connecting',
            'icpe-opm-sess-state-authenticating':'icpe_opm_sess_state_authenticating',
            'icpe-opm-sess-state-arbitrating':'icpe_opm_sess_state_arbitrating',
            'icpe-opm-sess-state-waiting-for-resyncs':'icpe_opm_sess_state_waiting_for_resyncs',
            'icpe-opm-sess-state-connected':'icpe_opm_sess_state_connected',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmSyncFsmStateEnum' : _MetaInfoEnum('IcpeOpmSyncFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-sync-fsm-state-split-brain':'icpe_opm_sync_fsm_state_split_brain',
            'icpe-opm-sync-fsm-state-waiting':'icpe_opm_sync_fsm_state_waiting',
            'icpe-opm-sync-fsm-state-whole-brain':'icpe_opm_sync_fsm_state_whole_brain',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmChanFsmStateEnum' : _MetaInfoEnum('IcpeOpmChanFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-chan-fsm-state-down':'icpe_opm_chan_fsm_state_down',
            'icpe-opm-chan-fsm-state-closed':'icpe_opm_chan_fsm_state_closed',
            'icpe-opm-chan-fsm-state-opening':'icpe_opm_chan_fsm_state_opening',
            'icpe-opm-chan-fsm-state-opened':'icpe_opm_chan_fsm_state_opened',
            'icpe-opm-chan-fsm-state-open':'icpe_opm_chan_fsm_state_open',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperPortEnum' : _MetaInfoEnum('IcpeOperPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-port-unknown':'icpe_oper_port_unknown',
            'icpe-oper-port-gigabit-ethernet':'icpe_oper_port_gigabit_ethernet',
            'icpe-oper-port-ten-gig-e':'icpe_oper_port_ten_gig_e',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperSdacpSessStateEnum' : _MetaInfoEnum('IcpeOperSdacpSessStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-sdacp-sess-state-not-created':'icpe_oper_sdacp_sess_state_not_created',
            'icpe-oper-sdacp-sess-state-created':'icpe_oper_sdacp_sess_state_created',
            'icpe-oper-sdacp-sess-state-authentication-not-ok':'icpe_oper_sdacp_sess_state_authentication_not_ok',
            'icpe-oper-sdacp-sess-state-authentication-ok':'icpe_oper_sdacp_sess_state_authentication_ok',
            'icpe-oper-sdacp-sess-state-version-not-ok':'icpe_oper_sdacp_sess_state_version_not_ok',
            'icpe-oper-sdacp-sess-state-up':'icpe_oper_sdacp_sess_state_up',
            'icpe-oper-sdacp-sess-state-issu':'icpe_oper_sdacp_sess_state_issu',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpticalSyncStateEnum' : _MetaInfoEnum('IcpeOpticalSyncStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-optical-sync-state-unknown':'icpe_optical_sync_state_unknown',
            'icpe-optical-sync-state-syncing':'icpe_optical_sync_state_syncing',
            'icpe-optical-sync-state-synced':'icpe_optical_sync_state_synced',
            'icpe-optical-sync-state-not-connected':'icpe_optical_sync_state_not_connected',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperTopoRemoteSourceEnum' : _MetaInfoEnum('IcpeOperTopoRemoteSourceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-topo-remote-source-unknown':'icpe_oper_topo_remote_source_unknown',
            'icpe-oper-topo-remote-source-remote-icl-id':'icpe_oper_topo_remote_source_remote_icl_id',
            'icpe-oper-topo-remote-source-remote-satellite-mac':'icpe_oper_topo_remote_source_remote_satellite_mac',
            'icpe-oper-topo-remote-source-remote-host-mac':'icpe_oper_topo_remote_source_remote_host_mac',
            'icpe-oper-topo-remote-source-direct-satellite':'icpe_oper_topo_remote_source_direct_satellite',
            'icpe-oper-topo-remote-source-direct-host':'icpe_oper_topo_remote_source_direct_host',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmResyncFsmStateEnum' : _MetaInfoEnum('IcpeOpmResyncFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-resync-fsm-state-not-open':'icpe_opm_resync_fsm_state_not_open',
            'icpe-opm-resync-fsm-state-stable':'icpe_opm_resync_fsm_state_stable',
            'icpe-opm-resync-fsm-state-in-resync':'icpe_opm_resync_fsm_state_in_resync',
            'icpe-opm-resync-fsm-state-queued':'icpe_opm_resync_fsm_state_queued',
            'icpe-opm-resync-fsm-state-resync-req':'icpe_opm_resync_fsm_state_resync_req',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmTransportStateEnum' : _MetaInfoEnum('IcpeOpmTransportStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-transport-state-disconnected':'icpe_opm_transport_state_disconnected',
            'icpe-opm-transport-state-iccp-unavailable':'icpe_opm_transport_state_iccp_unavailable',
            'icpe-opm-transport-state-no-member-present':'icpe_opm_transport_state_no_member_present',
            'icpe-opm-transport-state-member-down':'icpe_opm_transport_state_member_down',
            'icpe-opm-transport-state-member-not-reachable':'icpe_opm_transport_state_member_not_reachable',
            'icpe-opm-transport-state-waiting-for-app-connect':'icpe_opm_transport_state_waiting_for_app_connect',
            'icpe-opm-transport-state-waiting-for-app-connect-response':'icpe_opm_transport_state_waiting_for_app_connect_response',
            'icpe-opm-transport-state-connected':'icpe_opm_transport_state_connected',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperMultichassisRedundancyEnum' : _MetaInfoEnum('IcpeOperMultichassisRedundancyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-multi-chassis-redundancy-not-redundant':'icpe_oper_multi_chassis_redundancy_not_redundant',
            'icpe-oper-multi-chassis-redundancy-active':'icpe_oper_multi_chassis_redundancy_active',
            'icpe-oper-multi-chassis-redundancy-standby':'icpe_oper_multi_chassis_redundancy_standby',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeInstallSatStateEnum' : _MetaInfoEnum('IcpeInstallSatStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-install-sat-state-unknown':'icpe_install_sat_state_unknown',
            'icpe-install-sat-state-not-initiat-ed':'icpe_install_sat_state_not_initiat_ed',
            'icpe-install-sat-state-transferring':'icpe_install_sat_state_transferring',
            'icpe-install-sat-state-activating':'icpe_install_sat_state_activating',
            'icpe-install-sat-state-updating':'icpe_install_sat_state_updating',
            'icpe-install-sat-state-deactivating':'icpe_install_sat_state_deactivating',
            'icpe-install-sat-state-removing':'icpe_install_sat_state_removing',
            'icpe-install-sat-state-success':'icpe_install_sat_state_success',
            'icpe-install-sat-state-failure':'icpe_install_sat_state_failure',
            'icpe-install-sat-state-multiple-ops':'icpe_install_sat_state_multiple_ops',
            'icpe-install-sat-state-aborted':'icpe_install_sat_state_aborted',
            'icpe-install-sat-state-protocol-version':'icpe_install_sat_state_protocol_version',
            'icpe-install-sat-state-pkg-not-present':'icpe_install_sat_state_pkg_not_present',
            'icpe-install-sat-state-no-image':'icpe_install_sat_state_no_image',
            'icpe-install-sat-state-no-such-file':'icpe_install_sat_state_no_such_file',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'NvSatellite.ReloadOpStatuses.ReloadOpStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.ReloadOpStatuses.ReloadOpStatus',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('operation-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite range
                ''',
                'satellite_range',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reload-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats reload failed
                ''',
                'sats_reload_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reloaded', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats reloaded
                ''',
                'sats_reloaded',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reloading', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats reloading
                ''',
                'sats_reloading',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'reload-op-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.ReloadOpStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.ReloadOpStatuses',
            False, 
            [
            _MetaInfoClassMember('reload-op-status', REFERENCE_LIST, 'ReloadOpStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.ReloadOpStatuses.ReloadOpStatus', 
                [], [], 
                '''                Detailed breakdown of reload status
                ''',
                'reload_op_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'reload-op-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallStatuses.InstallStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallStatuses.InstallStatus',
            False, 
            [
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Satellite range
                ''',
                'satellite_range',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-range-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite range
                ''',
                'satellite_range_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activate aborted
                ''',
                'sats_activate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activate failed
                ''',
                'sats_activate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activating
                ''',
                'sats_activating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-completed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats completed
                ''',
                'sats_completed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivate-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivate aborted
                ''',
                'sats_deactivate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivate failed
                ''',
                'sats_deactivate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivating
                ''',
                'sats_deactivating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-no-operation', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats no operation
                ''',
                'sats_no_operation',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-remove-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats remove aborted
                ''',
                'sats_remove_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-remove-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats remove failed
                ''',
                'sats_remove_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-removing', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats removing
                ''',
                'sats_removing',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transfer aborted
                ''',
                'sats_transfer_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transfer failed
                ''',
                'sats_transfer_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transferring', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transferring
                ''',
                'sats_transferring',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-update-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats update aborted
                ''',
                'sats_update_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-update-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats update failed
                ''',
                'sats_update_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-updating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats updating
                ''',
                'sats_updating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallStatuses',
            False, 
            [
            _MetaInfoClassMember('install-status', REFERENCE_LIST, 'InstallStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallStatuses.InstallStatus', 
                [], [], 
                '''                Detailed breakdown of install status
                ''',
                'install_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'protocol-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'channel-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'resync-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel',
            False, 
            [
            _MetaInfoClassMember('chan-state', REFERENCE_ENUM_CLASS, 'IcpeOpmChanFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmChanFsmStateEnum', 
                [], [], 
                '''                Chan state
                ''',
                'chan_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Channel ID
                ''',
                'channel_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('channel-state-timestamp', REFERENCE_CLASS, 'ChannelStateTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'channel_state_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('control-messages-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control messages received
                ''',
                'control_messages_received',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('control-messages-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control messages sent
                ''',
                'control_messages_sent',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('normal-messages-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Normal messages received
                ''',
                'normal_messages_received',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('normal-messages-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Normal messages sent
                ''',
                'normal_messages_sent',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('resync-state', REFERENCE_ENUM_CLASS, 'IcpeOpmResyncFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmResyncFsmStateEnum', 
                [], [], 
                '''                Resync state
                ''',
                'resync_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('resync-state-timestamp', REFERENCE_CLASS, 'ResyncStateTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'resync_state_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'channel',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy',
            False, 
            [
            _MetaInfoClassMember('iccp-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP group
                ''',
                'iccp_group',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('arbitration-state', REFERENCE_ENUM_CLASS, 'IcpeOpmArbitrationFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmArbitrationFsmStateEnum', 
                [], [], 
                '''                Arbitration state
                ''',
                'arbitration_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('authentication-state', REFERENCE_ENUM_CLASS, 'IcpeOpmAuthFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmAuthFsmStateEnum', 
                [], [], 
                '''                Authentication state
                ''',
                'authentication_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel', 
                [], [], 
                '''                Channels on this session table
                ''',
                'channel',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('iccp-group-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICCP group
                ''',
                'iccp_group_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('isolated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Isolated
                ''',
                'isolated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('primacy', REFERENCE_ENUM_CLASS, 'IcpeOpmControllerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmControllerEnum', 
                [], [], 
                '''                Primacy
                ''',
                'primacy',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('protocol-state', REFERENCE_ENUM_CLASS, 'IcpeOpmSessStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmSessStateEnum', 
                [], [], 
                '''                Protocol state
                ''',
                'protocol_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('protocol-state-timestamp', REFERENCE_CLASS, 'ProtocolStateTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'protocol_state_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('synchronization-state', REFERENCE_ENUM_CLASS, 'IcpeOpmSyncFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmSyncFsmStateEnum', 
                [], [], 
                '''                Synchronization state
                ''',
                'synchronization_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                System MAC
                ''',
                'system_mac',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('transport-state', REFERENCE_ENUM_CLASS, 'IcpeOpmTransportStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmTransportStateEnum', 
                [], [], 
                '''                Transport state
                ''',
                'transport_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'sdacp-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies',
            False, 
            [
            _MetaInfoClassMember('sdacp-redundancy', REFERENCE_LIST, 'SdacpRedundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy', 
                [], [], 
                '''                nV Satellite Redundancy Protocol Information
                ''',
                'sdacp_redundancy',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'sdacp-redundancies',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallShows.InstallShow.Satellite' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallShows.InstallShow.Satellite',
            False, 
            [
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                End time
                ''',
                'end_time',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Info
                ''',
                'info',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Percentage
                ''',
                'percentage',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Retries
                ''',
                'retries',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Start time
                ''',
                'start_time',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IcpeInstallSatStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeInstallSatStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallShows.InstallShow' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallShows.InstallShow',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                End time
                ''',
                'end_time',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('name-string', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Name strings
                ''',
                'name_string',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('operation-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('operation-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Operation type
                ''',
                'operation_type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('progress-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Progress percentage
                ''',
                'progress_percentage',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ref-state', REFERENCE_ENUM_CLASS, 'IcpeInstallSatStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeInstallSatStateEnum', 
                [], [], 
                '''                Ref state
                ''',
                'ref_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite', REFERENCE_LIST, 'Satellite' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallShows.InstallShow.Satellite', 
                [], [], 
                '''                Breakdown per satellite table
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite range
                ''',
                'satellite_range',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activate aborted
                ''',
                'sats_activate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activate failed
                ''',
                'sats_activate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activating
                ''',
                'sats_activating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-completed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats completed
                ''',
                'sats_completed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivate-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivate aborted
                ''',
                'sats_deactivate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivate failed
                ''',
                'sats_deactivate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivating
                ''',
                'sats_deactivating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-no-operation', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats no operation
                ''',
                'sats_no_operation',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-remove-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats remove aborted
                ''',
                'sats_remove_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-remove-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats remove failed
                ''',
                'sats_remove_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-removing', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats removing
                ''',
                'sats_removing',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transfer aborted
                ''',
                'sats_transfer_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transfer failed
                ''',
                'sats_transfer_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transferring', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transferring
                ''',
                'sats_transferring',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-update-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats update aborted
                ''',
                'sats_update_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-update-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats update failed
                ''',
                'sats_update_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-updating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats updating
                ''',
                'sats_updating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Start time
                ''',
                'start_time',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-show',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallShows' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallShows',
            False, 
            [
            _MetaInfoClassMember('install-show', REFERENCE_LIST, 'InstallShow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallShows.InstallShow', 
                [], [], 
                '''                Detailed breakdown of install status
                ''',
                'install_show',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-shows',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'IcpeOperFabricPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperFabricPortEnum', 
                [], [], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Subslot
                ''',
                'subslot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Valid
                ''',
                'valid',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'configured-port',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort',
            False, 
            [
            _MetaInfoClassMember('permanent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Permanent
                ''',
                'permanent',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'IcpeOperFabricPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperFabricPortEnum', 
                [], [], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('requested', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Requested
                ''',
                'requested',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Subslot
                ''',
                'subslot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'current-port',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts',
            False, 
            [
            _MetaInfoClassMember('channel-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Channel up
                ''',
                'channel_up',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('configured-port', REFERENCE_LIST, 'ConfiguredPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort', 
                [], [], 
                '''                Configured Candidate Fabric Ports table
                ''',
                'configured_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('current-port', REFERENCE_LIST, 'CurrentPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort', 
                [], [], 
                '''                Current Candidate Fabric Ports on this Satellite
                table
                ''',
                'current_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('error-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error string
                ''',
                'error_string',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('out-of-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Out of sync
                ''',
                'out_of_sync',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'candidate-fabric-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sync-state', REFERENCE_ENUM_CLASS, 'IcpeOpticalSyncStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpticalSyncStateEnum', 
                [], [], 
                '''                Sync state
                ''',
                'sync_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'application',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus',
            False, 
            [
            _MetaInfoClassMember('application', REFERENCE_LIST, 'Application' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application', 
                [], [], 
                '''                Application State table
                ''',
                'application',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('chassis-sync-state', REFERENCE_ENUM_CLASS, 'IcpeOpticalSyncStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpticalSyncStateEnum', 
                [], [], 
                '''                Chassis sync state
                ''',
                'chassis_sync_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'optical-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'redundancy-out-of-sync-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange',
            False, 
            [
            _MetaInfoClassMember('conflict-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Conflict context
                ''',
                'conflict_context',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('high-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High port
                ''',
                'high_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('low-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Low port
                ''',
                'low_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'IcpeOperPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperPortEnum', 
                [], [], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Subslot
                ''',
                'subslot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'port-range',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink',
            False, 
            [
            _MetaInfoClassMember('conflict-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Conflict context
                ''',
                'conflict_context',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IcpeOperDiscdLinkStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperDiscdLinkStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'discovered-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink',
            False, 
            [
            _MetaInfoClassMember('conflict-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Conflict context
                ''',
                'conflict_context',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('discovered-link', REFERENCE_LIST, 'DiscoveredLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink', 
                [], [], 
                '''                Discovered Links table
                ''',
                'discovered_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP address auto
                ''',
                'ip_address_auto',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('min-links-satisfied', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Min links satisfied
                ''',
                'min_links_satisfied',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('minimum-preferred-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum preferred links
                ''',
                'minimum_preferred_links',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('minimum-required-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum required links
                ''',
                'minimum_required_links',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('number-active-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number active links
                ''',
                'number_active_links',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange', 
                [], [], 
                '''                Port ranges table
                ''',
                'port_range',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('required-min-links-satisfied', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Required min links satisfied
                ''',
                'required_min_links_satisfied',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('vrf-id-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF ID present
                ''',
                'vrf_id_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'configured-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('candidate-fabric-ports', REFERENCE_CLASS, 'CandidateFabricPorts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts', 
                [], [], 
                '''                Candidate Fabric Ports on this Satellite
                ''',
                'candidate_fabric_ports',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('cfgd-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cfgd timeout
                ''',
                'cfgd_timeout',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('configured-link', REFERENCE_LIST, 'ConfiguredLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink', 
                [], [], 
                '''                Configured Links on this Satellite table
                ''',
                'configured_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('configured-serial-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configured serial number
                ''',
                'configured_serial_number',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('configured-serial-number-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configured serial number present
                ''',
                'configured_serial_number_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Conflict context
                ''',
                'conflict_context',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description
                ''',
                'description',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('description-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Description present
                ''',
                'description_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ethernet-fabric-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet fabric supported
                ''',
                'ethernet_fabric_supported',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('host-treating-as-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Host treating as active
                ''',
                'host_treating_as_active',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-state', REFERENCE_ENUM_CLASS, 'IcpeOperInstallStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperInstallStateEnum', 
                [], [], 
                '''                Install state
                ''',
                'install_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP address auto
                ''',
                'ip_address_auto',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP address present
                ''',
                'ip_address_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ipv6-address-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IPV6 address present
                ''',
                'ipv6_address_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('mac-address-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAC address present
                ''',
                'mac_address_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('optical-status', REFERENCE_CLASS, 'OpticalStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus', 
                [], [], 
                '''                Optical Satellite Status
                ''',
                'optical_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('optical-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Optical supported
                ''',
                'optical_supported',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('password-error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Password error
                ''',
                'password_error',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('received-host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Received hostname
                ''',
                'received_host_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('received-serial-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Received serial number
                ''',
                'received_serial_number',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('received-serial-number-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Received serial number present
                ''',
                'received_serial_number_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('recovery-delay-time-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Recovery delay time left
                ''',
                'recovery_delay_time_left',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('redundancy-iccp-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Redundancy ICCP group
                ''',
                'redundancy_iccp_group',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('redundancy-out-of-sync-timestamp', REFERENCE_CLASS, 'RedundancyOutOfSyncTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'redundancy_out_of_sync_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Remote version
                ''',
                'remote_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote version present
                ''',
                'remote_version_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-treating-as-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Satellite treating as active
                ''',
                'satellite_treating_as_active',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sdacp-session-failure-reason', REFERENCE_ENUM_CLASS, 'IcpeGcoOperControlReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeGcoOperControlReasonEnum', 
                [], [], 
                '''                SDACP session failure reason
                ''',
                'sdacp_session_failure_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sdacp-session-state', REFERENCE_ENUM_CLASS, 'IcpeOperSdacpSessStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperSdacpSessStateEnum', 
                [], [], 
                '''                SDACP session state
                ''',
                'sdacp_session_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('timeout-warning', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timeout warning
                ''',
                'timeout_warning',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version-check-state', REFERENCE_ENUM_CLASS, 'IcpeOperVerCheckStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperVerCheckStateEnum', 
                [], [], 
                '''                Version check state
                ''',
                'version_check_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('vrfid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRFID
                ''',
                'vrfid',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses',
            False, 
            [
            _MetaInfoClassMember('satellite-status', REFERENCE_LIST, 'SatelliteStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus', 
                [], [], 
                '''                Satellite status information
                ''',
                'satellite_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatellitePriorities.SatellitePriority' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatellitePriorities.SatellitePriority',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('best-path-hops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Best path hops
                ''',
                'best_path_hops',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('configured-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured priority
                ''',
                'configured_priority',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('host-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Host priority
                ''',
                'host_priority',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('multichassis-redundancy', REFERENCE_ENUM_CLASS, 'IcpeOperMultichassisRedundancyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperMultichassisRedundancyEnum', 
                [], [], 
                '''                Multichassis redundancy
                ''',
                'multichassis_redundancy',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('partner-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Partner priority
                ''',
                'partner_priority',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('rgid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RG ID
                ''',
                'rgid',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-priority',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatellitePriorities' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatellitePriorities',
            False, 
            [
            _MetaInfoClassMember('satellite-priority', REFERENCE_LIST, 'SatellitePriority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatellitePriorities.SatellitePriority', 
                [], [], 
                '''                Satellite priority information
                ''',
                'satellite_priority',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-priorities',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion',
            False, 
            [
            _MetaInfoClassMember('remote-version', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Remote version
                ''',
                'remote_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote version present
                ''',
                'remote_version_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version-check-state', REFERENCE_ENUM_CLASS, 'IcpeOperVerCheckStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperVerCheckStateEnum', 
                [], [], 
                '''                Version check state
                ''',
                'version_check_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'active-version',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion',
            False, 
            [
            _MetaInfoClassMember('remote-version', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Remote version
                ''',
                'remote_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote version present
                ''',
                'remote_version_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version-check-state', REFERENCE_ENUM_CLASS, 'IcpeOperVerCheckStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperVerCheckStateEnum', 
                [], [], 
                '''                Version check state
                ''',
                'version_check_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'transferred-version',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion',
            False, 
            [
            _MetaInfoClassMember('remote-version', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Remote version
                ''',
                'remote_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote version present
                ''',
                'remote_version_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version-check-state', REFERENCE_ENUM_CLASS, 'IcpeOperVerCheckStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperVerCheckStateEnum', 
                [], [], 
                '''                Version check state
                ''',
                'version_check_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'committed-version',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteVersions.SatelliteVersion' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteVersions.SatelliteVersion',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('active-version', REFERENCE_CLASS, 'ActiveVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion', 
                [], [], 
                '''                Satellite active version information
                ''',
                'active_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('committed-version', REFERENCE_CLASS, 'CommittedVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion', 
                [], [], 
                '''                Satellite committed version information
                ''',
                'committed_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Remote version
                ''',
                'remote_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-version-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote version present
                ''',
                'remote_version_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('transferred-version', REFERENCE_CLASS, 'TransferredVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion', 
                [], [], 
                '''                Satellite transferred version information
                ''',
                'transferred_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version-check-state', REFERENCE_ENUM_CLASS, 'IcpeOperVerCheckStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperVerCheckStateEnum', 
                [], [], 
                '''                Version check state
                ''',
                'version_check_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-version',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteVersions' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteVersions',
            False, 
            [
            _MetaInfoClassMember('satellite-version', REFERENCE_LIST, 'SatelliteVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteVersions.SatelliteVersion', 
                [], [], 
                '''                Satellite remote version information
                ''',
                'satellite_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-versions',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink',
            False, 
            [
            _MetaInfoClassMember('discovery-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discovery running
                ''',
                'discovery_running',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'discovered-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice',
            False, 
            [
            _MetaInfoClassMember('icl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICL ID
                ''',
                'icl_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-is-local-host', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote is local host
                ''',
                'remote_is_local_host',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-is-satellite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote is satellite
                ''',
                'remote_is_satellite',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'IcpeOperTopoRemoteSourceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperTopoRemoteSourceEnum', 
                [], [], 
                '''                Source
                ''',
                'source',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'remote-device',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Active
                ''',
                'active',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('display-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Display name
                ''',
                'display_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('icl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICL ID
                ''',
                'icl_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('obsolete', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Obsolete
                ''',
                'obsolete',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('redundant', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redundant
                ''',
                'redundant',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('remote-device', REFERENCE_LIST, 'RemoteDevice' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice', 
                [], [], 
                '''                Remote Device table
                ''',
                'remote_device',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'fabric-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite',
            False, 
            [
            _MetaInfoClassMember('configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configured
                ''',
                'configured',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Conflict context
                ''',
                'conflict_context',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('display-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Display name
                ''',
                'display_name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('fabric-link', REFERENCE_LIST, 'FabricLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink', 
                [], [], 
                '''                Local Satellite Fabric Link table
                ''',
                'fabric_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('num-hops', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Num hops
                ''',
                'num_hops',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('received-serial-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Received serial number
                ''',
                'received_serial_number',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('received-serial-number-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Received serial number present
                ''',
                'received_serial_number_present',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID
                ''',
                'vlan_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('discovered-link', REFERENCE_LIST, 'DiscoveredLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink', 
                [], [], 
                '''                Discovered Links table
                ''',
                'discovered_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('is-physical', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is physical
                ''',
                'is_physical',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('redundancy-iccp-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Redundancy ICCP group
                ''',
                'redundancy_iccp_group',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ring-whole', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ring whole
                ''',
                'ring_whole',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite', REFERENCE_LIST, 'Satellite' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite', 
                [], [], 
                '''                Satellite table
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-topology',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies',
            False, 
            [
            _MetaInfoClassMember('satellite-topology', REFERENCE_LIST, 'SatelliteTopology' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology', 
                [], [], 
                '''                Satellite Topology Information
                ''',
                'satellite_topology',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-topologies',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallProgresses.InstallProgress' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallProgresses.InstallProgress',
            False, 
            [
            _MetaInfoClassMember('progress-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Progress percentage
                ''',
                'progress_percentage',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('progress-percentage-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Progress percentage
                ''',
                'progress_percentage_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite count
                ''',
                'satellite_count',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-progress',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallProgresses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallProgresses',
            False, 
            [
            _MetaInfoClassMember('install-progress', REFERENCE_LIST, 'InstallProgress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallProgresses.InstallProgress', 
                [], [], 
                '''                Current percentage of install
                ''',
                'install_progress',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-progresses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.ReloadStatuses.ReloadStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.ReloadStatuses.ReloadStatus',
            False, 
            [
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Satellite range
                ''',
                'satellite_range',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('satellite-range-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite range
                ''',
                'satellite_range_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reload-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats reload failed
                ''',
                'sats_reload_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reloaded', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats reloaded
                ''',
                'sats_reloaded',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reloading', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats reloading
                ''',
                'sats_reloading',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'reload-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.ReloadStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.ReloadStatuses',
            False, 
            [
            _MetaInfoClassMember('reload-status', REFERENCE_LIST, 'ReloadStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.ReloadStatuses.ReloadStatus', 
                [], [], 
                '''                Detailed breakdown of reload status
                ''',
                'reload_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'reload-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package',
            False, 
            [
            _MetaInfoClassMember('is-base-image', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is base image
                ''',
                'is_base_image',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package', 
                [], [], 
                '''                A package on this Satellite table
                ''',
                'package',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'active-packages',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package',
            False, 
            [
            _MetaInfoClassMember('is-base-image', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is base image
                ''',
                'is_base_image',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package', 
                [], [], 
                '''                A package on this Satellite table
                ''',
                'package',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'inactive-packages',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package',
            False, 
            [
            _MetaInfoClassMember('is-base-image', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is base image
                ''',
                'is_base_image',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package', 
                [], [], 
                '''                A package on this Satellite table
                ''',
                'package',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'committed-packages',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo',
            False, 
            [
            _MetaInfoClassMember('active-packages', REFERENCE_CLASS, 'ActivePackages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages', 
                [], [], 
                '''                Active Packages running on this Satellite
                ''',
                'active_packages',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('committed-packages', REFERENCE_CLASS, 'CommittedPackages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages', 
                [], [], 
                '''                Committed Packages running on this Satellite
                ''',
                'committed_packages',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('inactive-packages', REFERENCE_CLASS, 'InactivePackages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages', 
                [], [], 
                '''                Inactive Packages on this Satellite
                ''',
                'inactive_packages',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-package-info',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('install-package-info', REFERENCE_CLASS, 'InstallPackageInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo', 
                [], [], 
                '''                Package Data on this Satellite
                ''',
                'install_package_info',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('package-support', REFERENCE_ENUM_CLASS, 'IcpeInstallPkgSuppEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'IcpeInstallPkgSuppEnum', 
                [], [], 
                '''                Package support
                ''',
                'package_support',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-software-version',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install.SatelliteSoftwareVersions' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install.SatelliteSoftwareVersions',
            False, 
            [
            _MetaInfoClassMember('satellite-software-version', REFERENCE_LIST, 'SatelliteSoftwareVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion', 
                [], [], 
                '''                Satellite Software Package Information
                ''',
                'satellite_software_version',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-software-versions',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.Install' : {
        'meta_info' : _MetaInfoClass('NvSatellite.Install',
            False, 
            [
            _MetaInfoClassMember('satellite-software-versions', REFERENCE_CLASS, 'SatelliteSoftwareVersions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install.SatelliteSoftwareVersions', 
                [], [], 
                '''                Satellite Software Package Information table
                ''',
                'satellite_software_versions',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallOpStatuses.InstallOpStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallOpStatuses.InstallOpStatus',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('operation-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operation ID
                ''',
                'operation_id_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite range
                ''',
                'satellite_range',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activate aborted
                ''',
                'sats_activate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activate failed
                ''',
                'sats_activate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats activating
                ''',
                'sats_activating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-completed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats completed
                ''',
                'sats_completed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivate-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivate aborted
                ''',
                'sats_deactivate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivate failed
                ''',
                'sats_deactivate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-deactivating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats deactivating
                ''',
                'sats_deactivating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-no-operation', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats no operation
                ''',
                'sats_no_operation',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-remove-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats remove aborted
                ''',
                'sats_remove_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-remove-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats remove failed
                ''',
                'sats_remove_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-removing', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats removing
                ''',
                'sats_removing',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transfer aborted
                ''',
                'sats_transfer_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transfer failed
                ''',
                'sats_transfer_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transferring', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats transferring
                ''',
                'sats_transferring',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-update-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats update aborted
                ''',
                'sats_update_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-update-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats update failed
                ''',
                'sats_update_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-updating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sats updating
                ''',
                'sats_updating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-op-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallOpStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallOpStatuses',
            False, 
            [
            _MetaInfoClassMember('install-op-status', REFERENCE_LIST, 'InstallOpStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallOpStatuses.InstallOpStatus', 
                [], [], 
                '''                Detailed breakdown of install status
                ''',
                'install_op_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-op-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteProperties.IdRanges.IdRange' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteProperties.IdRanges.IdRange',
            False, 
            [
            _MetaInfoClassMember('sat-id-range', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sat ID range
                ''',
                'sat_id_range',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('max', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Max
                ''',
                'max',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Min
                ''',
                'min',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'id-range',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteProperties.IdRanges' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteProperties.IdRanges',
            False, 
            [
            _MetaInfoClassMember('id-range', REFERENCE_LIST, 'IdRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteProperties.IdRanges.IdRange', 
                [], [], 
                '''                Satellite ID range
                ''',
                'id_range',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'id-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteProperties' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteProperties',
            False, 
            [
            _MetaInfoClassMember('id-ranges', REFERENCE_CLASS, 'IdRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteProperties.IdRanges', 
                [], [], 
                '''                Satellite ID range table
                ''',
                'id_ranges',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-properties',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'DpmProtoStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'DpmProtoStateEnum', 
                [], [], 
                '''                Interface status
                ''',
                'interface_status',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface',
            False, 
            [
            _MetaInfoClassMember('conflict-reason', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-chassis-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Satellite chassis MAC
                ''',
                'satellite_chassis_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-chassis-vendor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite chassis vendor
                ''',
                'satellite_chassis_vendor',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite interface ID
                ''',
                'satellite_interface_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-interface-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Satellite interface MAC
                ''',
                'satellite_interface_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-module-vendor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite module vendor
                ''',
                'satellite_module_vendor',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-serial-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite serial id
                ''',
                'satellite_serial_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-status', REFERENCE_ENUM_CLASS, 'DpmProtoStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'DpmProtoStateEnum', 
                [], [], 
                '''                Satellite status
                ''',
                'satellite_status',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite',
            False, 
            [
            _MetaInfoClassMember('conflict-reason', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Host IP address
                ''',
                'host_ip_address',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface', 
                [], [], 
                '''                ICPE Discovered satellite state information
                table
                ''',
                'interface',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Satellite IP address
                ''',
                'satellite_ip_address',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-status', REFERENCE_ENUM_CLASS, 'DpmProtoStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'DpmProtoStateEnum', 
                [], [], 
                '''                Satellite status
                ''',
                'satellite_status',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpDiscovery2S.SdacpDiscovery2',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-sdacp-oper', True),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface', 
                [], [], 
                '''                ICPE Discovery interface state information table
                ''',
                'interface',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite', REFERENCE_LIST, 'Satellite' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite', 
                [], [], 
                '''                ICPE Satellite state information table
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'sdacp-discovery2',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpDiscovery2S' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpDiscovery2S',
            False, 
            [
            _MetaInfoClassMember('sdacp-discovery2', REFERENCE_LIST, 'SdacpDiscovery2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpDiscovery2S.SdacpDiscovery2', 
                [], [], 
                '''                ICPE Configured interface state information
                ''',
                'sdacp_discovery2',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'sdacp-discovery2s',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.IcpeDpms.IcpeDpm.Satellite' : {
        'meta_info' : _MetaInfoClass('NvSatellite.IcpeDpms.IcpeDpm.Satellite',
            False, 
            [
            _MetaInfoClassMember('ack-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Ack packets sent
                ''',
                'ack_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('configuration-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Configuration packets sent
                ''',
                'configuration_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('conflict-reason', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('current-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current timeout
                ''',
                'current_timeout',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('deleting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Deleting
                ''',
                'deleting',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('discovery-protocol-state', REFERENCE_ENUM_CLASS, 'DpmProtoStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'DpmProtoStateEnum', 
                [], [], 
                '''                Discovery protocol state
                ''',
                'discovery_protocol_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-chassis-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Host chassis MAC
                ''',
                'host_chassis_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-chassis-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host chassis type
                ''',
                'host_chassis_type',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-chassis-vendor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host chassis vendor
                ''',
                'host_chassis_vendor',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Host IP address
                ''',
                'host_ip_address',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('ident-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Ident packets received
                ''',
                'ident_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('ifmgr-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ifmgr state
                ''',
                'ifmgr_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('invalid-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Invalid packets received
                ''',
                'invalid_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('is-queued-for-efd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is queued for EFD
                ''',
                'is_queued_for_efd',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('is-queued-for-oc', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is queued for OC
                ''',
                'is_queued_for_oc',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('last-imdr-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last IMDR state
                ''',
                'last_imdr_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('legacy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Legacy
                ''',
                'legacy',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('los-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Los packets received
                ''',
                'los_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('ready-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Ready packets received
                ''',
                'ready_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('received-sys-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Received sys MAC
                ''',
                'received_sys_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('reject-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Reject packets sent
                ''',
                'reject_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-chassis-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Satellite chassis MAC
                ''',
                'satellite_chassis_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-chassis-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite chassis type
                ''',
                'satellite_chassis_type',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-chassis-vendor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite chassis vendor
                ''',
                'satellite_chassis_vendor',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite interface ID
                ''',
                'satellite_interface_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-interface-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Satellite interface MAC
                ''',
                'satellite_interface_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Satellite IP address
                ''',
                'satellite_ip_address',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-module-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Satellite module MAC
                ''',
                'satellite_module_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-module-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite module type
                ''',
                'satellite_module_type',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-module-vendor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite module vendor
                ''',
                'satellite_module_vendor',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-serial-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite serial id
                ''',
                'satellite_serial_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('secs-since-pkts-cleaned', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secs since pkts cleaned
                ''',
                'secs_since_pkts_cleaned',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.IcpeDpms.IcpeDpm.RemoteHost' : {
        'meta_info' : _MetaInfoClass('NvSatellite.IcpeDpms.IcpeDpm.RemoteHost',
            False, 
            [
            _MetaInfoClassMember('current-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current timeout
                ''',
                'current_timeout',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('discovery-protocol-state', REFERENCE_ENUM_CLASS, 'DpmProtoHostStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'DpmProtoHostStateEnum', 
                [], [], 
                '''                Discovery protocol state
                ''',
                'discovery_protocol_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-ack-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Host ack packets received
                ''',
                'host_ack_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-ack-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Host ack packets sent
                ''',
                'host_ack_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-chassis-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Host chassis MAC
                ''',
                'host_chassis_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-interface-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Host interface MAC
                ''',
                'host_interface_mac',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('route-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route length
                ''',
                'route_length',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('secs-since-pkts-cleaned', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secs since pkts cleaned
                ''',
                'secs_since_pkts_cleaned',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'remote-host',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.IcpeDpms.IcpeDpm' : {
        'meta_info' : _MetaInfoClass('NvSatellite.IcpeDpms.IcpeDpm',
            False, 
            [
            _MetaInfoClassMember('discovery-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Discovery interface
                ''',
                'discovery_interface',
                'Cisco-IOS-XR-icpe-sdacp-oper', True),
            _MetaInfoClassMember('ack-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Ack packets sent
                ''',
                'ack_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('configuration-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Configuration packets sent
                ''',
                'configuration_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('discovery-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Discovery interface handle
                ''',
                'discovery_interface_handle',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('discovery-interface-status', REFERENCE_ENUM_CLASS, 'DpmProtoStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'DpmProtoStateEnum', 
                [], [], 
                '''                Discovery interface status
                ''',
                'discovery_interface_status',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('discovery-interface-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Discovery interface
                ''',
                'discovery_interface_xr',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-ack-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Host ack packets received
                ''',
                'host_ack_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('host-ack-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Host ack packets sent
                ''',
                'host_ack_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('ident-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Ident packets received
                ''',
                'ident_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('invalid-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Invalid packets received
                ''',
                'invalid_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('los-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Los packets received
                ''',
                'los_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('probe-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Probe packets sent
                ''',
                'probe_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('ready-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Ready packets received
                ''',
                'ready_packets_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('reject-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Reject packets sent
                ''',
                'reject_packets_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('remote-host', REFERENCE_LIST, 'RemoteHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.IcpeDpms.IcpeDpm.RemoteHost', 
                [], [], 
                '''                ICPE DPM remote host operational information
                table
                ''',
                'remote_host',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite', REFERENCE_LIST, 'Satellite' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.IcpeDpms.IcpeDpm.Satellite', 
                [], [], 
                '''                ICPE DPM satellite operational information table
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('secs-since-pkts-cleaned', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secs since pkts cleaned
                ''',
                'secs_since_pkts_cleaned',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'icpe-dpm',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.IcpeDpms' : {
        'meta_info' : _MetaInfoClass('NvSatellite.IcpeDpms',
            False, 
            [
            _MetaInfoClassMember('icpe-dpm', REFERENCE_LIST, 'IcpeDpm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.IcpeDpms.IcpeDpm', 
                [], [], 
                '''                ICPE DPM operational information
                ''',
                'icpe_dpm',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'icpe-dpms',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'protocol-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'transport-error-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Debug
                ''',
                'debug',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('value', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Value
                ''',
                'value',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'tl-vs',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities',
            False, 
            [
            _MetaInfoClassMember('tl-vs', REFERENCE_LIST, 'TlVs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs', 
                [], [], 
                '''                Capability TLVs table
                ''',
                'tl_vs',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'capabilities',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'resync-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'channel-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl.Channel' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl.Channel',
            False, 
            [
            _MetaInfoClassMember('capabilities', REFERENCE_CLASS, 'Capabilities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities', 
                [], [], 
                '''                Capabilities
                ''',
                'capabilities',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Channel ID
                ''',
                'channel_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('channel-state', REFERENCE_ENUM_CLASS, 'IcpeCpmChanFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'IcpeCpmChanFsmStateEnum', 
                [], [], 
                '''                Channel state
                ''',
                'channel_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('channel-state-timestamp', REFERENCE_CLASS, 'ChannelStateTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'channel_state_timestamp',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('control-messages-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control messages dropped
                ''',
                'control_messages_dropped',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('control-messages-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control messages received
                ''',
                'control_messages_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('control-messages-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control messages sent
                ''',
                'control_messages_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('normal-messages-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Normal messages dropped
                ''',
                'normal_messages_dropped',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('normal-messages-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Normal messages received
                ''',
                'normal_messages_received',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('normal-messages-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Normal messages sent
                ''',
                'normal_messages_sent',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('resync-state', REFERENCE_ENUM_CLASS, 'IcpeCpmChannelResyncStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'IcpeCpmChannelResyncStateEnum', 
                [], [], 
                '''                Resync state
                ''',
                'resync_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('resync-state-timestamp', REFERENCE_CLASS, 'ResyncStateTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'resync_state_timestamp',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('secs-since-last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secs since last cleared
                ''',
                'secs_since_last_cleared',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'channel',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls.SdacpControl' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls.SdacpControl',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-sdacp-oper', True),
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.Channel', 
                [], [], 
                '''                Channels on satellite table
                ''',
                'channel',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('control-protocol-state', REFERENCE_ENUM_CLASS, 'IcpeCpmControlFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper', 'IcpeCpmControlFsmStateEnum', 
                [], [], 
                '''                Control protocol state
                ''',
                'control_protocol_state',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('ip-address-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP address auto
                ''',
                'ip_address_auto',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('protocol-state-timestamp', REFERENCE_CLASS, 'ProtocolStateTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'protocol_state_timestamp',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Satellite ID
                ''',
                'satellite_id_xr',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('satellite-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Satellite IP address
                ''',
                'satellite_ip_address',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('transport-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transport error
                ''',
                'transport_error',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('transport-error-timestamp', REFERENCE_CLASS, 'TransportErrorTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'transport_error_timestamp',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'sdacp-control',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpControls' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpControls',
            False, 
            [
            _MetaInfoClassMember('sdacp-control', REFERENCE_LIST, 'SdacpControl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls.SdacpControl', 
                [], [], 
                '''                SDAC Protocol Discovery information
                ''',
                'sdacp_control',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            ],
            'Cisco-IOS-XR-icpe-sdacp-oper',
            'sdacp-controls',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite' : {
        'meta_info' : _MetaInfoClass('NvSatellite',
            False, 
            [
            _MetaInfoClassMember('icpe-dpms', REFERENCE_CLASS, 'IcpeDpms' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.IcpeDpms', 
                [], [], 
                '''                ICPE DPM operational information table
                ''',
                'icpe_dpms',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('install', REFERENCE_CLASS, 'Install' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.Install', 
                [], [], 
                '''                Satellite Install Information
                ''',
                'install',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-op-statuses', REFERENCE_CLASS, 'InstallOpStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallOpStatuses', 
                [], [], 
                '''                Detailed breakdown of install status table
                ''',
                'install_op_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-progresses', REFERENCE_CLASS, 'InstallProgresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallProgresses', 
                [], [], 
                '''                Current percentage of install table
                ''',
                'install_progresses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-shows', REFERENCE_CLASS, 'InstallShows' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallShows', 
                [], [], 
                '''                Detailed breakdown of install status table
                ''',
                'install_shows',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-statuses', REFERENCE_CLASS, 'InstallStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallStatuses', 
                [], [], 
                '''                Detailed breakdown of install status table
                ''',
                'install_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('reload-op-statuses', REFERENCE_CLASS, 'ReloadOpStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.ReloadOpStatuses', 
                [], [], 
                '''                Detailed breakdown of reload status table
                ''',
                'reload_op_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('reload-statuses', REFERENCE_CLASS, 'ReloadStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.ReloadStatuses', 
                [], [], 
                '''                Detailed breakdown of reload status table
                ''',
                'reload_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-priorities', REFERENCE_CLASS, 'SatellitePriorities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatellitePriorities', 
                [], [], 
                '''                Satellite priority information table
                ''',
                'satellite_priorities',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-properties', REFERENCE_CLASS, 'SatelliteProperties' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteProperties', 
                [], [], 
                '''                ICPE GCO operational information
                ''',
                'satellite_properties',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-statuses', REFERENCE_CLASS, 'SatelliteStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses', 
                [], [], 
                '''                Satellite status information table
                ''',
                'satellite_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-topologies', REFERENCE_CLASS, 'SatelliteTopologies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies', 
                [], [], 
                '''                Satellite Topology Information table
                ''',
                'satellite_topologies',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-versions', REFERENCE_CLASS, 'SatelliteVersions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteVersions', 
                [], [], 
                '''                Satellite remote version information table
                ''',
                'satellite_versions',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sdacp-controls', REFERENCE_CLASS, 'SdacpControls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpControls', 
                [], [], 
                '''                SDAC Protocol Discovery information table
                ''',
                'sdacp_controls',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('sdacp-discovery2s', REFERENCE_CLASS, 'SdacpDiscovery2S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpDiscovery2S', 
                [], [], 
                '''                ICPE Configured interface state information
                table
                ''',
                'sdacp_discovery2s',
                'Cisco-IOS-XR-icpe-sdacp-oper', False),
            _MetaInfoClassMember('sdacp-redundancies', REFERENCE_CLASS, 'SdacpRedundancies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies', 
                [], [], 
                '''                nV Satellite Redundancy Protocol Information
                table
                ''',
                'sdacp_redundancies',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'nv-satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
}
_meta_table['NvSatellite.ReloadOpStatuses.ReloadOpStatus']['meta_info'].parent =_meta_table['NvSatellite.ReloadOpStatuses']['meta_info']
_meta_table['NvSatellite.InstallStatuses.InstallStatus']['meta_info'].parent =_meta_table['NvSatellite.InstallStatuses']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies']['meta_info']
_meta_table['NvSatellite.InstallShows.InstallShow.Satellite']['meta_info'].parent =_meta_table['NvSatellite.InstallShows.InstallShow']['meta_info']
_meta_table['NvSatellite.InstallShows.InstallShow']['meta_info'].parent =_meta_table['NvSatellite.InstallShows']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info'].parent =_meta_table['NvSatellite.SatelliteStatuses']['meta_info']
_meta_table['NvSatellite.SatellitePriorities.SatellitePriority']['meta_info'].parent =_meta_table['NvSatellite.SatellitePriorities']['meta_info']
_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion.ActiveVersion']['meta_info'].parent =_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion']['meta_info']
_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion.TransferredVersion']['meta_info'].parent =_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion']['meta_info']
_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion.CommittedVersion']['meta_info'].parent =_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion']['meta_info']
_meta_table['NvSatellite.SatelliteVersions.SatelliteVersion']['meta_info'].parent =_meta_table['NvSatellite.SatelliteVersions']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies']['meta_info']
_meta_table['NvSatellite.InstallProgresses.InstallProgress']['meta_info'].parent =_meta_table['NvSatellite.InstallProgresses']['meta_info']
_meta_table['NvSatellite.ReloadStatuses.ReloadStatus']['meta_info'].parent =_meta_table['NvSatellite.ReloadStatuses']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages.Package']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages.Package']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages.Package']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.ActivePackages']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.InactivePackages']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo.CommittedPackages']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion.InstallPackageInfo']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions.SatelliteSoftwareVersion']['meta_info'].parent =_meta_table['NvSatellite.Install.SatelliteSoftwareVersions']['meta_info']
_meta_table['NvSatellite.Install.SatelliteSoftwareVersions']['meta_info'].parent =_meta_table['NvSatellite.Install']['meta_info']
_meta_table['NvSatellite.InstallOpStatuses.InstallOpStatus']['meta_info'].parent =_meta_table['NvSatellite.InstallOpStatuses']['meta_info']
_meta_table['NvSatellite.SatelliteProperties.IdRanges.IdRange']['meta_info'].parent =_meta_table['NvSatellite.SatelliteProperties.IdRanges']['meta_info']
_meta_table['NvSatellite.SatelliteProperties.IdRanges']['meta_info'].parent =_meta_table['NvSatellite.SatelliteProperties']['meta_info']
_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite.Interface']['meta_info'].parent =_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite']['meta_info']
_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Interface']['meta_info'].parent =_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2']['meta_info']
_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2.Satellite']['meta_info'].parent =_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2']['meta_info']
_meta_table['NvSatellite.SdacpDiscovery2S.SdacpDiscovery2']['meta_info'].parent =_meta_table['NvSatellite.SdacpDiscovery2S']['meta_info']
_meta_table['NvSatellite.IcpeDpms.IcpeDpm.Satellite']['meta_info'].parent =_meta_table['NvSatellite.IcpeDpms.IcpeDpm']['meta_info']
_meta_table['NvSatellite.IcpeDpms.IcpeDpm.RemoteHost']['meta_info'].parent =_meta_table['NvSatellite.IcpeDpms.IcpeDpm']['meta_info']
_meta_table['NvSatellite.IcpeDpms.IcpeDpm']['meta_info'].parent =_meta_table['NvSatellite.IcpeDpms']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities.TlVs']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel.Capabilities']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel.ResyncStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel.ChannelStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.ProtocolStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.TransportErrorTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl.Channel']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls.SdacpControl']['meta_info']
_meta_table['NvSatellite.SdacpControls.SdacpControl']['meta_info'].parent =_meta_table['NvSatellite.SdacpControls']['meta_info']
_meta_table['NvSatellite.ReloadOpStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.InstallStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.InstallShows']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatellitePriorities']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatelliteVersions']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.InstallProgresses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.ReloadStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.Install']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.InstallOpStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatelliteProperties']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SdacpDiscovery2S']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.IcpeDpms']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SdacpControls']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
