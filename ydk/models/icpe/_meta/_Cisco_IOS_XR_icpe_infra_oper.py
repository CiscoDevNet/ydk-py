


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'IcpeOperSdacpSessStateEnum' : _MetaInfoEnum('IcpeOperSdacpSessStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-sdacp-sess-state-not-created':'ICPE_OPER_SDACP_SESS_STATE_NOT_CREATED',
            'icpe-oper-sdacp-sess-state-created':'ICPE_OPER_SDACP_SESS_STATE_CREATED',
            'icpe-oper-sdacp-sess-state-authentication-not-ok':'ICPE_OPER_SDACP_SESS_STATE_AUTHENTICATION_NOT_OK',
            'icpe-oper-sdacp-sess-state-authentication-ok':'ICPE_OPER_SDACP_SESS_STATE_AUTHENTICATION_OK',
            'icpe-oper-sdacp-sess-state-version-not-ok':'ICPE_OPER_SDACP_SESS_STATE_VERSION_NOT_OK',
            'icpe-oper-sdacp-sess-state-up':'ICPE_OPER_SDACP_SESS_STATE_UP',
            'icpe-oper-sdacp-sess-state-issu':'ICPE_OPER_SDACP_SESS_STATE_ISSU',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeGcoOperControlReasonEnum' : _MetaInfoEnum('IcpeGcoOperControlReasonEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-gco-oper-control-reason-unknown-error':'ICPE_GCO_OPER_CONTROL_REASON_UNKNOWN_ERROR',
            'icpe-gco-oper-control-reason-wrong-chassis-type':'ICPE_GCO_OPER_CONTROL_REASON_WRONG_CHASSIS_TYPE',
            'icpe-gco-oper-control-reason-wrong-chassis-serial':'ICPE_GCO_OPER_CONTROL_REASON_WRONG_CHASSIS_SERIAL',
            'icpe-gco-oper-control-reason-needs-to-upgrade':'ICPE_GCO_OPER_CONTROL_REASON_NEEDS_TO_UPGRADE',
            'icpe-gco-oper-control-reason-none':'ICPE_GCO_OPER_CONTROL_REASON_NONE',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmSyncFsmStateEnum' : _MetaInfoEnum('IcpeOpmSyncFsmStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-sync-fsm-state-split-brain':'ICPE_OPM_SYNC_FSM_STATE_SPLIT_BRAIN',
            'icpe-opm-sync-fsm-state-waiting':'ICPE_OPM_SYNC_FSM_STATE_WAITING',
            'icpe-opm-sync-fsm-state-whole-brain':'ICPE_OPM_SYNC_FSM_STATE_WHOLE_BRAIN',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmArbitrationFsmStateEnum' : _MetaInfoEnum('IcpeOpmArbitrationFsmStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-arbitration-fsm-state-unarbitrated':'ICPE_OPM_ARBITRATION_FSM_STATE_UNARBITRATED',
            'icpe-opm-arbitration-fsm-state-waiting':'ICPE_OPM_ARBITRATION_FSM_STATE_WAITING',
            'icpe-opm-arbitration-fsm-state-arbitrating':'ICPE_OPM_ARBITRATION_FSM_STATE_ARBITRATING',
            'icpe-opm-arbitration-fsm-state-arbitrated':'ICPE_OPM_ARBITRATION_FSM_STATE_ARBITRATED',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperInstallStateEnum' : _MetaInfoEnum('IcpeOperInstallStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-install-state-stable':'ICPE_OPER_INSTALL_STATE_STABLE',
            'icpe-oper-install-state-transferring':'ICPE_OPER_INSTALL_STATE_TRANSFERRING',
            'icpe-oper-install-state-transferred':'ICPE_OPER_INSTALL_STATE_TRANSFERRED',
            'icpe-oper-install-state-installing':'ICPE_OPER_INSTALL_STATE_INSTALLING',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmTransportStateEnum' : _MetaInfoEnum('IcpeOpmTransportStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-transport-state-disconnected':'ICPE_OPM_TRANSPORT_STATE_DISCONNECTED',
            'icpe-opm-transport-state-iccp-unavailable':'ICPE_OPM_TRANSPORT_STATE_ICCP_UNAVAILABLE',
            'icpe-opm-transport-state-no-member-present':'ICPE_OPM_TRANSPORT_STATE_NO_MEMBER_PRESENT',
            'icpe-opm-transport-state-member-down':'ICPE_OPM_TRANSPORT_STATE_MEMBER_DOWN',
            'icpe-opm-transport-state-member-not-reachable':'ICPE_OPM_TRANSPORT_STATE_MEMBER_NOT_REACHABLE',
            'icpe-opm-transport-state-waiting-for-app-connect':'ICPE_OPM_TRANSPORT_STATE_WAITING_FOR_APP_CONNECT',
            'icpe-opm-transport-state-waiting-for-app-connect-response':'ICPE_OPM_TRANSPORT_STATE_WAITING_FOR_APP_CONNECT_RESPONSE',
            'icpe-opm-transport-state-connected':'ICPE_OPM_TRANSPORT_STATE_CONNECTED',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperDiscdLinkStateEnum' : _MetaInfoEnum('IcpeOperDiscdLinkStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-discd-link-state-stopped':'ICPE_OPER_DISCD_LINK_STATE_STOPPED',
            'icpe-oper-discd-link-state-probing':'ICPE_OPER_DISCD_LINK_STATE_PROBING',
            'icpe-oper-discd-link-state-configuring':'ICPE_OPER_DISCD_LINK_STATE_CONFIGURING',
            'icpe-oper-discd-link-state-ready':'ICPE_OPER_DISCD_LINK_STATE_READY',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperConflictEnum' : _MetaInfoEnum('IcpeOperConflictEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-conflict-not-calculated':'ICPE_OPER_CONFLICT_NOT_CALCULATED',
            'icpe-oper-conflict-no-conflict':'ICPE_OPER_CONFLICT_NO_CONFLICT',
            'icpe-oper-conflict-satellite-not-configured':'ICPE_OPER_CONFLICT_SATELLITE_NOT_CONFIGURED',
            'icpe-oper-conflict-satellite-no-type':'ICPE_OPER_CONFLICT_SATELLITE_NO_TYPE',
            'icpe-oper-conflict-satellite-id-invalid':'ICPE_OPER_CONFLICT_SATELLITE_ID_INVALID',
            'icpe-oper-conflict-satellite-no-ipv4-addr':'ICPE_OPER_CONFLICT_SATELLITE_NO_IPV4_ADDR',
            'icpe-oper-conflict-satellite-conflicting-ipv4-addr':'ICPE_OPER_CONFLICT_SATELLITE_CONFLICTING_IPV4_ADDR',
            'icpe-oper-conflict-no-configured-links':'ICPE_OPER_CONFLICT_NO_CONFIGURED_LINKS',
            'icpe-oper-conflict-no-discovered-links':'ICPE_OPER_CONFLICT_NO_DISCOVERED_LINKS',
            'icpe-oper-conflict-invalid-ports':'ICPE_OPER_CONFLICT_INVALID_PORTS',
            'icpe-oper-conflict-ports-overlap':'ICPE_OPER_CONFLICT_PORTS_OVERLAP',
            'icpe-oper-conflict-waiting-for-ipv4-addr':'ICPE_OPER_CONFLICT_WAITING_FOR_IPV4_ADDR',
            'icpe-oper-conflict-waiting-for-vrf':'ICPE_OPER_CONFLICT_WAITING_FOR_VRF',
            'icpe-oper-conflict-different-ipv4-addr':'ICPE_OPER_CONFLICT_DIFFERENT_IPV4_ADDR',
            'icpe-oper-conflict-different-vrf':'ICPE_OPER_CONFLICT_DIFFERENT_VRF',
            'icpe-oper-conflict-satellite-link-ipv4-overlap':'ICPE_OPER_CONFLICT_SATELLITE_LINK_IPV4_OVERLAP',
            'icpe-oper-conflict-waiting-for-ident':'ICPE_OPER_CONFLICT_WAITING_FOR_IDENT',
            'icpe-oper-conflict-multiple-ids':'ICPE_OPER_CONFLICT_MULTIPLE_IDS',
            'icpe-oper-conflict-multiple-satellites':'ICPE_OPER_CONFLICT_MULTIPLE_SATELLITES',
            'icpe-oper-conflict-ident-rejected':'ICPE_OPER_CONFLICT_IDENT_REJECTED',
            'icpe-oper-conflict-interface-down':'ICPE_OPER_CONFLICT_INTERFACE_DOWN',
            'icpe-oper-conflict-auto-ip-unavailable':'ICPE_OPER_CONFLICT_AUTO_IP_UNAVAILABLE',
            'icpe-oper-conflict-satellite-auto-ip-link-manual-ip':'ICPE_OPER_CONFLICT_SATELLITE_AUTO_IP_LINK_MANUAL_IP',
            'icpe-oper-conflict-link-auto-ip-satellite-manual-ip':'ICPE_OPER_CONFLICT_LINK_AUTO_IP_SATELLITE_MANUAL_IP',
            'icpe-oper-conflict-serial-num-mismatch':'ICPE_OPER_CONFLICT_SERIAL_NUM_MISMATCH',
            'icpe-oper-conflict-satellite-not-identified':'ICPE_OPER_CONFLICT_SATELLITE_NOT_IDENTIFIED',
            'icpe-oper-conflict-satellite-unsupported-type':'ICPE_OPER_CONFLICT_SATELLITE_UNSUPPORTED_TYPE',
            'icpe-oper-conflict-satellite-partition-unsupported':'ICPE_OPER_CONFLICT_SATELLITE_PARTITION_UNSUPPORTED',
            'icpe-oper-conflict-satellite-no-serial-number':'ICPE_OPER_CONFLICT_SATELLITE_NO_SERIAL_NUMBER',
            'icpe-oper-conflict-satellite-conflicting-serial-number':'ICPE_OPER_CONFLICT_SATELLITE_CONFLICTING_SERIAL_NUMBER',
            'icpe-oper-conflict-satellite-link-waiting-for-arp':'ICPE_OPER_CONFLICT_SATELLITE_LINK_WAITING_FOR_ARP',
            'icpe-oper-conflict-host-pe-isolated-split-brain':'ICPE_OPER_CONFLICT_HOST_PE_ISOLATED_SPLIT_BRAIN',
            'icpe-oper-conflict-fabric-iccp-group-inconsistent':'ICPE_OPER_CONFLICT_FABRIC_ICCP_GROUP_INCONSISTENT',
            'icpe-oper-conflict-invalid-iccp-group':'ICPE_OPER_CONFLICT_INVALID_ICCP_GROUP',
            'icpe-oper-conflict-port-rejected':'ICPE_OPER_CONFLICT_PORT_REJECTED',
            'icpe-oper-conflict-satellite-icl-not-supported':'ICPE_OPER_CONFLICT_SATELLITE_ICL_NOT_SUPPORTED',
            'icpe-oper-conflict-multiple-serial-number':'ICPE_OPER_CONFLICT_MULTIPLE_SERIAL_NUMBER',
            'icpe-oper-conflict-multiple-mac-address':'ICPE_OPER_CONFLICT_MULTIPLE_MAC_ADDRESS',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmResyncFsmStateEnum' : _MetaInfoEnum('IcpeOpmResyncFsmStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-resync-fsm-state-not-open':'ICPE_OPM_RESYNC_FSM_STATE_NOT_OPEN',
            'icpe-opm-resync-fsm-state-stable':'ICPE_OPM_RESYNC_FSM_STATE_STABLE',
            'icpe-opm-resync-fsm-state-in-resync':'ICPE_OPM_RESYNC_FSM_STATE_IN_RESYNC',
            'icpe-opm-resync-fsm-state-queued':'ICPE_OPM_RESYNC_FSM_STATE_QUEUED',
            'icpe-opm-resync-fsm-state-resync-req':'ICPE_OPM_RESYNC_FSM_STATE_RESYNC_REQ',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperPortEnum' : _MetaInfoEnum('IcpeOperPortEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-port-unknown':'ICPE_OPER_PORT_UNKNOWN',
            'icpe-oper-port-gigabit-ethernet':'ICPE_OPER_PORT_GIGABIT_ETHERNET',
            'icpe-oper-port-ten-gig-e':'ICPE_OPER_PORT_TEN_GIG_E',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmAuthFsmStateEnum' : _MetaInfoEnum('IcpeOpmAuthFsmStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-auth-fsm-state-unauth':'ICPE_OPM_AUTH_FSM_STATE_UNAUTH',
            'icpe-opm-auth-fsm-state-waiting':'ICPE_OPM_AUTH_FSM_STATE_WAITING',
            'icpe-opm-auth-fsm-state-waiting-for-auth':'ICPE_OPM_AUTH_FSM_STATE_WAITING_FOR_AUTH',
            'icpe-opm-auth-fsm-state-waiting-for-reply':'ICPE_OPM_AUTH_FSM_STATE_WAITING_FOR_REPLY',
            'icpe-opm-auth-fsm-state-authed':'ICPE_OPM_AUTH_FSM_STATE_AUTHED',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmControllerEnum' : _MetaInfoEnum('IcpeOpmControllerEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-controller-unknown':'ICPE_OPM_CONTROLLER_UNKNOWN',
            'icpe-opm-controller-primary':'ICPE_OPM_CONTROLLER_PRIMARY',
            'icpe-opm-controller-secondary':'ICPE_OPM_CONTROLLER_SECONDARY',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperFabricPortEnum' : _MetaInfoEnum('IcpeOperFabricPortEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-fabric-port-unknown':'ICPE_OPER_FABRIC_PORT_UNKNOWN',
            'icpe-oper-fabric-port-n-v-fabric-gig-e':'ICPE_OPER_FABRIC_PORT_N_V_FABRIC_GIG_E',
            'icpe-oper-fabric-port-n-v-fabric-ten-gig-e':'ICPE_OPER_FABRIC_PORT_N_V_FABRIC_TEN_GIG_E',
            'icpe-oper-fabric-port-n-v-fabric-hundred-gig-e':'ICPE_OPER_FABRIC_PORT_N_V_FABRIC_HUNDRED_GIG_E',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOperVerCheckStateEnum' : _MetaInfoEnum('IcpeOperVerCheckStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-oper-ver-check-state-unknown':'ICPE_OPER_VER_CHECK_STATE_UNKNOWN',
            'icpe-oper-ver-check-state-not-compatible':'ICPE_OPER_VER_CHECK_STATE_NOT_COMPATIBLE',
            'icpe-oper-ver-check-state-current-version':'ICPE_OPER_VER_CHECK_STATE_CURRENT_VERSION',
            'icpe-oper-ver-check-state-compatible-older':'ICPE_OPER_VER_CHECK_STATE_COMPATIBLE_OLDER',
            'icpe-oper-ver-check-state-compatible-newer':'ICPE_OPER_VER_CHECK_STATE_COMPATIBLE_NEWER',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpticalSyncStateEnum' : _MetaInfoEnum('IcpeOpticalSyncStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-optical-sync-state-unknown':'ICPE_OPTICAL_SYNC_STATE_UNKNOWN',
            'icpe-optical-sync-state-syncing':'ICPE_OPTICAL_SYNC_STATE_SYNCING',
            'icpe-optical-sync-state-synced':'ICPE_OPTICAL_SYNC_STATE_SYNCED',
            'icpe-optical-sync-state-not-connected':'ICPE_OPTICAL_SYNC_STATE_NOT_CONNECTED',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmChanFsmStateEnum' : _MetaInfoEnum('IcpeOpmChanFsmStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-chan-fsm-state-down':'ICPE_OPM_CHAN_FSM_STATE_DOWN',
            'icpe-opm-chan-fsm-state-closed':'ICPE_OPM_CHAN_FSM_STATE_CLOSED',
            'icpe-opm-chan-fsm-state-opening':'ICPE_OPM_CHAN_FSM_STATE_OPENING',
            'icpe-opm-chan-fsm-state-opened':'ICPE_OPM_CHAN_FSM_STATE_OPENED',
            'icpe-opm-chan-fsm-state-open':'ICPE_OPM_CHAN_FSM_STATE_OPEN',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'IcpeOpmSessStateEnum' : _MetaInfoEnum('IcpeOpmSessStateEnum', 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper',
        {
            'icpe-opm-sess-state-disconnected':'ICPE_OPM_SESS_STATE_DISCONNECTED',
            'icpe-opm-sess-state-connecting':'ICPE_OPM_SESS_STATE_CONNECTING',
            'icpe-opm-sess-state-authenticating':'ICPE_OPM_SESS_STATE_AUTHENTICATING',
            'icpe-opm-sess-state-arbitrating':'ICPE_OPM_SESS_STATE_ARBITRATING',
            'icpe-opm-sess-state-waiting-for-resyncs':'ICPE_OPM_SESS_STATE_WAITING_FOR_RESYNCS',
            'icpe-opm-sess-state-connected':'ICPE_OPM_SESS_STATE_CONNECTED',
        }, 'Cisco-IOS-XR-icpe-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper']),
    'NvSatellite.InstallStatuses.InstallStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallStatuses.InstallStatus',
            False, 
            [
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Satellite range
                ''',
                'satellite_range',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                Sats activate aborted
                ''',
                'sats_activate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats activate failed
                ''',
                'sats_activate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats activating
                ''',
                'sats_activating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-completed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats completed
                ''',
                'sats_completed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-no-operation', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats no operation
                ''',
                'sats_no_operation',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats transfer aborted
                ''',
                'sats_transfer_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats transfer failed
                ''',
                'sats_transfer_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transferring', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats transferring
                ''',
                'sats_transferring',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallStatuses',
            False, 
            [
            _MetaInfoClassMember('install-status', REFERENCE_LIST, 'InstallStatus' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallStatuses.InstallStatus', 
                [], [], 
                '''                Detailed breakdown of install status
                ''',
                'install_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'protocol-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'channel-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'resync-state-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel',
            False, 
            [
            _MetaInfoClassMember('chan-state', REFERENCE_ENUM_CLASS, 'IcpeOpmChanFsmStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmChanFsmStateEnum', 
                [], [], 
                '''                Chan state
                ''',
                'chan_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('channel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Channel ID
                ''',
                'channel_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('channel-state-timestamp', REFERENCE_CLASS, 'ChannelStateTimestamp' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'channel_state_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('control-messages-received', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Control messages received
                ''',
                'control_messages_received',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('control-messages-sent', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Control messages sent
                ''',
                'control_messages_sent',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('normal-messages-received', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Normal messages received
                ''',
                'normal_messages_received',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('normal-messages-sent', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Normal messages sent
                ''',
                'normal_messages_sent',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('resync-state', REFERENCE_ENUM_CLASS, 'IcpeOpmResyncFsmStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmResyncFsmStateEnum', 
                [], [], 
                '''                Resync state
                ''',
                'resync_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('resync-state-timestamp', REFERENCE_CLASS, 'ResyncStateTimestamp' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'resync_state_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'channel',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies.SdacpRedundancy' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies.SdacpRedundancy',
            False, 
            [
            _MetaInfoClassMember('iccp-group', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ICCP group
                ''',
                'iccp_group',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('arbitration-state', REFERENCE_ENUM_CLASS, 'IcpeOpmArbitrationFsmStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmArbitrationFsmStateEnum', 
                [], [], 
                '''                Arbitration state
                ''',
                'arbitration_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('authentication-state', REFERENCE_ENUM_CLASS, 'IcpeOpmAuthFsmStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmAuthFsmStateEnum', 
                [], [], 
                '''                Authentication state
                ''',
                'authentication_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel', 
                [], [], 
                '''                Channels on this session table
                ''',
                'channel',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('iccp-group-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('primacy', REFERENCE_ENUM_CLASS, 'IcpeOpmControllerEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmControllerEnum', 
                [], [], 
                '''                Primacy
                ''',
                'primacy',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('protocol-state', REFERENCE_ENUM_CLASS, 'IcpeOpmSessStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmSessStateEnum', 
                [], [], 
                '''                Protocol state
                ''',
                'protocol_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('protocol-state-timestamp', REFERENCE_CLASS, 'ProtocolStateTimestamp' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp', 
                [], [], 
                '''                Timestamp
                ''',
                'protocol_state_timestamp',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('synchronization-state', REFERENCE_ENUM_CLASS, 'IcpeOpmSyncFsmStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmSyncFsmStateEnum', 
                [], [], 
                '''                Synchronization state
                ''',
                'synchronization_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                System MAC
                ''',
                'system_mac',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('transport-state', REFERENCE_ENUM_CLASS, 'IcpeOpmTransportStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpmTransportStateEnum', 
                [], [], 
                '''                Transport state
                ''',
                'transport_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'sdacp-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SdacpRedundancies' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SdacpRedundancies',
            False, 
            [
            _MetaInfoClassMember('sdacp-redundancy', REFERENCE_LIST, 'SdacpRedundancy' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies.SdacpRedundancy', 
                [], [], 
                '''                nV Satellite Redundancy Protocol Information
                ''',
                'sdacp_redundancy',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'sdacp-redundancies',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'IcpeOperFabricPortEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperFabricPortEnum', 
                [], [], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
                [(0, 65535)], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'IcpeOperFabricPortEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperFabricPortEnum', 
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
                [(0, 65535)], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Subslot
                ''',
                'subslot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'current-port',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
            _MetaInfoClassMember('configured-port', REFERENCE_LIST, 'ConfiguredPort' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort', 
                [], [], 
                '''                Configured Candidate Fabric Ports table
                ''',
                'configured_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('current-port', REFERENCE_LIST, 'CurrentPort' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort', 
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
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
            _MetaInfoClassMember('sync-state', REFERENCE_ENUM_CLASS, 'IcpeOpticalSyncStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpticalSyncStateEnum', 
                [], [], 
                '''                Sync state
                ''',
                'sync_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'application',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus',
            False, 
            [
            _MetaInfoClassMember('application', REFERENCE_LIST, 'Application' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application', 
                [], [], 
                '''                Application State table
                ''',
                'application',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('chassis-sync-state', REFERENCE_ENUM_CLASS, 'IcpeOpticalSyncStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOpticalSyncStateEnum', 
                [], [], 
                '''                Chassis sync state
                ''',
                'chassis_sync_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'optical-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'redundancy-out-of-sync-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('high-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                High port
                ''',
                'high_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('low-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Low port
                ''',
                'low_port',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'IcpeOperPortEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperPortEnum', 
                [], [], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Subslot
                ''',
                'subslot',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'port-range',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IcpeOperDiscdLinkStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperDiscdLinkStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'discovered-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
                [], [], 
                '''                Conflict reason
                ''',
                'conflict_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('discovered-link', REFERENCE_LIST, 'DiscoveredLink' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink', 
                [], [], 
                '''                Discovered Links table
                ''',
                'discovered_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
                [(0, 4294967295)], [], 
                '''                Minimum preferred links
                ''',
                'minimum_preferred_links',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('number-active-links', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number active links
                ''',
                'number_active_links',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange', 
                [], [], 
                '''                Port ranges table
                ''',
                'port_range',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses.SatelliteStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses.SatelliteStatus',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('candidate-fabric-ports', REFERENCE_CLASS, 'CandidateFabricPorts' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts', 
                [], [], 
                '''                Candidate Fabric Ports on this Satellite
                ''',
                'candidate_fabric_ports',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('cfgd-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Cfgd timeout
                ''',
                'cfgd_timeout',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('configured-link', REFERENCE_LIST, 'ConfiguredLink' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink', 
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
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
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
            _MetaInfoClassMember('install-state', REFERENCE_ENUM_CLASS, 'IcpeOperInstallStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperInstallStateEnum', 
                [], [], 
                '''                Install state
                ''',
                'install_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
            _MetaInfoClassMember('optical-status', REFERENCE_CLASS, 'OpticalStatus' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus', 
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
            _MetaInfoClassMember('redundancy-iccp-group', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Redundancy ICCP group
                ''',
                'redundancy_iccp_group',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('redundancy-out-of-sync-timestamp', REFERENCE_CLASS, 'RedundancyOutOfSyncTimestamp' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp', 
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
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('sdacp-session-failure-reason', REFERENCE_ENUM_CLASS, 'IcpeGcoOperControlReasonEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeGcoOperControlReasonEnum', 
                [], [], 
                '''                SDACP session failure reason
                ''',
                'sdacp_session_failure_reason',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sdacp-session-state', REFERENCE_ENUM_CLASS, 'IcpeOperSdacpSessStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperSdacpSessStateEnum', 
                [], [], 
                '''                SDACP session state
                ''',
                'sdacp_session_state',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('version-check-state', REFERENCE_ENUM_CLASS, 'IcpeOperVerCheckStateEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperVerCheckStateEnum', 
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
                [(0, 4294967295)], [], 
                '''                VRFID
                ''',
                'vrfid',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteStatuses',
            False, 
            [
            _MetaInfoClassMember('satellite-status', REFERENCE_LIST, 'SatelliteStatus' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses.SatelliteStatus', 
                [], [], 
                '''                Satellite status information
                ''',
                'satellite_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice',
            False, 
            [
            _MetaInfoClassMember('icl-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ICL ID
                ''',
                'icl_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'remote-device',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('remote-device', REFERENCE_LIST, 'RemoteDevice' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice', 
                [], [], 
                '''                Remote Device table
                ''',
                'remote_device',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'fabric-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
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
            _MetaInfoClassMember('conflict-reason', REFERENCE_ENUM_CLASS, 'IcpeOperConflictEnum' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'IcpeOperConflictEnum', 
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
            _MetaInfoClassMember('fabric-link', REFERENCE_LIST, 'FabricLink' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink', 
                [], [], 
                '''                Local Satellite Fabric Link table
                ''',
                'fabric_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('num-hops', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                VLAN ID
                ''',
                'vlan_id',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies.SatelliteTopology' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies.SatelliteTopology',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('discovered-link', REFERENCE_LIST, 'DiscoveredLink' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink', 
                [], [], 
                '''                Discovered Links table
                ''',
                'discovered_link',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('satellite', REFERENCE_LIST, 'Satellite' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite', 
                [], [], 
                '''                Satellite table
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-topology',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.SatelliteTopologies' : {
        'meta_info' : _MetaInfoClass('NvSatellite.SatelliteTopologies',
            False, 
            [
            _MetaInfoClassMember('satellite-topology', REFERENCE_LIST, 'SatelliteTopology' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies.SatelliteTopology', 
                [], [], 
                '''                Satellite Topology Information
                ''',
                'satellite_topology',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'satellite-topologies',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallProgresses.InstallProgress' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallProgresses.InstallProgress',
            False, 
            [
            _MetaInfoClassMember('progress-percentage', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Progress percentage
                ''',
                'progress_percentage',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('progress-percentage-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Progress percentage
                ''',
                'progress_percentage_xr',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Satellite count
                ''',
                'satellite_count',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-progress',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallProgresses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallProgresses',
            False, 
            [
            _MetaInfoClassMember('install-progress', REFERENCE_LIST, 'InstallProgress' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallProgresses.InstallProgress', 
                [], [], 
                '''                Current percentage of install
                ''',
                'install_progress',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-progresses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.ReloadStatuses.ReloadStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.ReloadStatuses.ReloadStatus',
            False, 
            [
            _MetaInfoClassMember('satellite-range', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
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
                [(0, 65535)], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reload-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats reload failed
                ''',
                'sats_reload_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reloaded', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats reloaded
                ''',
                'sats_reloaded',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-reloading', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats reloading
                ''',
                'sats_reloading',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'reload-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.ReloadStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.ReloadStatuses',
            False, 
            [
            _MetaInfoClassMember('reload-status', REFERENCE_LIST, 'ReloadStatus' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.ReloadStatuses.ReloadStatus', 
                [], [], 
                '''                Detailed breakdown of reload status
                ''',
                'reload_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'reload-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallOpStatuses.InstallOpStatus' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallOpStatuses.InstallOpStatus',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-icpe-infra-oper', True),
            _MetaInfoClassMember('operation-id-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                Sats activate aborted
                ''',
                'sats_activate_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activate-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats activate failed
                ''',
                'sats_activate_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-activating', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats activating
                ''',
                'sats_activating',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-completed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats completed
                ''',
                'sats_completed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-no-operation', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats no operation
                ''',
                'sats_no_operation',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-not-initiated', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats not initiated
                ''',
                'sats_not_initiated',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-aborted', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats transfer aborted
                ''',
                'sats_transfer_aborted',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transfer-failed', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats transfer failed
                ''',
                'sats_transfer_failed',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sats-transferring', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Sats transferring
                ''',
                'sats_transferring',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-op-status',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite.InstallOpStatuses' : {
        'meta_info' : _MetaInfoClass('NvSatellite.InstallOpStatuses',
            False, 
            [
            _MetaInfoClassMember('install-op-status', REFERENCE_LIST, 'InstallOpStatus' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallOpStatuses.InstallOpStatus', 
                [], [], 
                '''                Detailed breakdown of install status
                ''',
                'install_op_status',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            ],
            'Cisco-IOS-XR-icpe-infra-oper',
            'install-op-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-oper'],
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
    'NvSatellite' : {
        'meta_info' : _MetaInfoClass('NvSatellite',
            False, 
            [
            _MetaInfoClassMember('install-op-statuses', REFERENCE_CLASS, 'InstallOpStatuses' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallOpStatuses', 
                [], [], 
                '''                Detailed breakdown of install status table
                ''',
                'install_op_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-progresses', REFERENCE_CLASS, 'InstallProgresses' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallProgresses', 
                [], [], 
                '''                Current percentage of install table
                ''',
                'install_progresses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('install-statuses', REFERENCE_CLASS, 'InstallStatuses' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.InstallStatuses', 
                [], [], 
                '''                Detailed breakdown of install status table
                ''',
                'install_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('reload-statuses', REFERENCE_CLASS, 'ReloadStatuses' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.ReloadStatuses', 
                [], [], 
                '''                Detailed breakdown of reload status table
                ''',
                'reload_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-statuses', REFERENCE_CLASS, 'SatelliteStatuses' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteStatuses', 
                [], [], 
                '''                Satellite status information table
                ''',
                'satellite_statuses',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('satellite-topologies', REFERENCE_CLASS, 'SatelliteTopologies' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SatelliteTopologies', 
                [], [], 
                '''                Satellite Topology Information table
                ''',
                'satellite_topologies',
                'Cisco-IOS-XR-icpe-infra-oper', False),
            _MetaInfoClassMember('sdacp-redundancies', REFERENCE_CLASS, 'SdacpRedundancies' , 'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper', 'NvSatellite.SdacpRedundancies', 
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
        'ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper'
        ),
    },
}
_meta_table['NvSatellite.InstallStatuses.InstallStatus']['meta_info'].parent =_meta_table['NvSatellite.InstallStatuses']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info'].parent =_meta_table['NvSatellite.SdacpRedundancies']['meta_info']
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
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info'].parent =_meta_table['NvSatellite.SatelliteTopologies']['meta_info']
_meta_table['NvSatellite.InstallProgresses.InstallProgress']['meta_info'].parent =_meta_table['NvSatellite.InstallProgresses']['meta_info']
_meta_table['NvSatellite.ReloadStatuses.ReloadStatus']['meta_info'].parent =_meta_table['NvSatellite.ReloadStatuses']['meta_info']
_meta_table['NvSatellite.InstallOpStatuses.InstallOpStatus']['meta_info'].parent =_meta_table['NvSatellite.InstallOpStatuses']['meta_info']
_meta_table['NvSatellite.InstallStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SdacpRedundancies']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatelliteStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.SatelliteTopologies']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.InstallProgresses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.ReloadStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
_meta_table['NvSatellite.InstallOpStatuses']['meta_info'].parent =_meta_table['NvSatellite']['meta_info']
